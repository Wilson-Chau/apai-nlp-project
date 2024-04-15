from flask import Flask, request, jsonify
from flask_cors import CORS

from llama_index.llms.llama_cpp import LlamaCPP
from llama_index.vector_stores.elasticsearch import ElasticsearchStore
from llama_index.core.query_engine import RetrieverQueryEngine
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core import QueryBundle
from llama_index.core.retrievers import BaseRetriever
from typing import Any, List
from llama_index.core.vector_stores import VectorStoreQuery
from llama_index.core.schema import NodeWithScore
from typing import Optional

app = Flask(__name__)
CORS(app)

@app.route("/")
def hello_world():
    return "Hello, World!"

@app.route("/ask", methods=["POST"])
def get_llm_response():
    data = request.get_json().get("message")

    embed_model = HuggingFaceEmbedding(model_name="mixedbread-ai/mxbai-embed-large-v1")

    vector_store = ElasticsearchStore(
        index_name="qna_mental_health",
        es_url="http://localhost:9200",
    )

    # model_url = "https://huggingface.co/TheBloke/Llama-2-13B-chat-GGML/resolve/main/llama-2-13b-chat.ggmlv3.q4_0.bin"
    model_path = "llama-2-7b-chat.Q3_K_S.gguf"

    llm = LlamaCPP(
        # You can pass in the URL to a GGML model to download it automatically
        # model_url=model_url,
        # optionally, you can set the path to a pre-downloaded model instead of model_url
        model_path=model_path,
        temperature=0.1,
        max_new_tokens=512,
        # llama2 has a context window of 4096 tokens, but we set it lower to allow for some wiggle room
        context_window=4000,
        # kwargs to pass to __call__()
        generate_kwargs={},
        # kwargs to pass to __init__()
        # set to at least 1 to use GPU
        model_kwargs={"n_gpu_layers": 0},
        verbose=True,
    )

    class VectorDBRetriever(BaseRetriever):
        """Retriever over a postgres vector store."""

        def __init__(
            self,
            vector_store: ElasticsearchStore,
            embed_model: Any,
            query_mode: str = "default",
            similarity_top_k: int = 2,
        ) -> None:
            """Init params."""
            self._vector_store = vector_store
            self._embed_model = embed_model
            self._query_mode = query_mode
            self._similarity_top_k = similarity_top_k
            super().__init__()

        def _retrieve(self, query_bundle: QueryBundle) -> List[NodeWithScore]:
            """Retrieve."""
            query_embedding = embed_model.get_query_embedding(
                query_bundle.query_str
            )
            vector_store_query = VectorStoreQuery(
                query_embedding=query_embedding,
                similarity_top_k=self._similarity_top_k,
                mode=self._query_mode,
            )
            query_result = vector_store.query(vector_store_query)

            nodes_with_scores = []
            for index, node in enumerate(query_result.nodes):
                score: Optional[float] = None
                if query_result.similarities is not None:
                    score = query_result.similarities[index]
                nodes_with_scores.append(NodeWithScore(node=node, score=score))

            return nodes_with_scores

    retriever = VectorDBRetriever(
        vector_store, embed_model, query_mode="default", similarity_top_k=2
    )
    query_engine = RetrieverQueryEngine.from_args(retriever, llm=llm)

    print(data)
    llm_response = query_engine.query(data)
    response = {
        'query': data,
        'response': str(llm_response)
        }
    
    return jsonify(response)
    

if __name__ == "__main__":
    app.run(debug=True)