# APAI4011 Project - Group 3

This repository is for APAI4011 project. You can find our finding while creating a mental health chatbot inside this repository.

## Project Structure

```
📦apai-nlp-project
 ┣ 📂GUI
 ┃ ┣ 📂Flask
 ┃ ┃ ┣ 📜app.py
 ┃ ┃ ┣ 📜messages.csv                           # stores the user input messages
 ┃ ┃ ┣ 📜readme.txt                             # instructions on running the backend flask app
 ┃ ┃ ┗ 📜requirements.txt
 ┃ ┣ 📂chatbot
 ┃ ┗ 📜readme.txt                               # instructions on running the chatbot application
 ┣ 📂classifier                                 # mental health topics classifier
 ┃ ┣ 📜sample_output.csv                        # sample classifier output
 ┃ ┣ 📜topic_classification.py
 ┃ ┣ 📜training_data.json
 ┃ ┗ 📜vocabs.txt
 ┣ 📂data
 ┃ ┣ 📂processed                                # pre-processed data
 ┃ ┃ ┣ 📂split                                  # training and testing data
 ┃ ┃ ┃ ┗ ...
 ┃ ┃ ┗ ...
 ┃ ┗ 📂raw
 ┃ ┃ ┗ 📜counsel-chat.pkl                       # raw data
 ┣ 📂notebooks
 ┃ ┣ 📂classification
 ┃ ┃ ┣ 📜bag-of-words-naive-bayes.ipynb         # for mental health topics classification
 ┃ ┃ ┗ 📜mental-classification.ipynb            # for binary classification
 ┃ ┣ 📂data
 ┃ ┃ ┣ 📜data-preprocessing.ipynb               # notebook for data pre-processing
 ┃ ┃ ┣ 📜data-retrieval.ipynb                   # notebook for data retrieval from huggingface
 ┃ ┃ ┗ 📜eda-wordclouds.ipynb                   # notebook for word clouds generation
 ┃ ┗ 📂modelling
 ┃ ┃ ┣ 📜Llama2-7B-RAG.ipynb                    # notebook for RAG approach
 ┃ ┃ ┣ 📜eval-bleu-and-bertscore.ipynb          # notebook for model evaluation
 ┃ ┃ ┣ 📜model-finetuning-llama2-test.ipynb     # notebook for fine-tuned model inferencing
 ┃ ┃ ┗ 📜model-finetuning-llama2-train.ipynb    # notebook for fine-tuning Llama2-7B-chat model
 ┣ 📂response
 ┃ ┣ 📜test-response-llama2-7B-RAG.csv          # response generated with RAG
 ┃ ┗ 📜test-response-llama2-7B-finetuned.csv    # response generated with fine-tuned model
 ┣ 📜Demo Chatbot.mp4                           # demo video
 ┗ 📜README.md
```

## Guide to Run the Chatbot

Inside the `GUI` folder, you can find a `readme.txt` file. Make sure to read it carefully and follow the instruction accordingly.

## Guide to perform Mental Health Topics Classification

To perform mental health topics classification, run the following codes
```bash
pip install nltk pandas scikit-learn
pip install gensim scipy==1.12
python classifier/topic_classification.py <input.csv> <output.csv>
```
where `<input.csv>` is the file that stores users' input texts of the chatbot while `<output.csv>` is will store the classification results.
