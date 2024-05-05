This folder contain a backend flask app.

To run, follow this guide:
1. create a virtual environment (python3 -m venv .venv) and activate it (source .venv/bin/activate)
2. install all required python library (pip install -r requirements.txt)
3. Download all model from Huggingface (https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGUF/blob/main/llama-2-7b-chat.Q3_K_S.gguf and https://huggingface.co/Amalq/mental_classification)
4. create .env file and add "FLASK_APP=app.py" in the first line.
5. run the back end using (flask run)
