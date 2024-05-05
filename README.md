# APAI4011 Project - Group 3

This repository is for APAI4011 project. You can find our finding while creating a mental health chatbot inside this repository.

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

## File tree

```
📦apai-nlp-project
 ┣ 📂GUI
 ┃ ┣ 📂Flask
 ┃ ┃ ┣ 📜app.py
 ┃ ┃ ┣ 📜messages.csv
 ┃ ┃ ┣ 📜readme.txt
 ┃ ┃ ┗ 📜requirements.txt
 ┃ ┣ 📂chatbot
 ┃ ┃ ┣ 📂public
 ┃ ┃ ┃ ┣ 📜favicon.ico
 ┃ ┃ ┃ ┣ 📜index.html
 ┃ ┃ ┃ ┣ 📜logo192.png
 ┃ ┃ ┃ ┣ 📜logo512.png
 ┃ ┃ ┃ ┣ 📜manifest.json
 ┃ ┃ ┃ ┗ 📜robots.txt
 ┃ ┃ ┣ 📂src
 ┃ ┃ ┃ ┣ 📂components
 ┃ ┃ ┃ ┃ ┣ 📜BotMessage.jsx
 ┃ ┃ ┃ ┃ ┣ 📜Dictaphone.jsx
 ┃ ┃ ┃ ┃ ┣ 📜Header.jsx
 ┃ ┃ ┃ ┃ ┣ 📜Input.jsx
 ┃ ┃ ┃ ┃ ┣ 📜Loader.jsx
 ┃ ┃ ┃ ┃ ┣ 📜Messages.jsx
 ┃ ┃ ┃ ┃ ┗ 📜UserMessage.jsx
 ┃ ┃ ┃ ┣ 📜ChatbotAPI.js
 ┃ ┃ ┃ ┣ 📜index.js
 ┃ ┃ ┃ ┗ 📜styles.css
 ┃ ┃ ┣ 📜.gitignore
 ┃ ┃ ┣ 📜README.md
 ┃ ┃ ┣ 📜package-lock.json
 ┃ ┃ ┗ 📜package.json
 ┃ ┗ 📜readme.txt
 ┣ 📂classifier
 ┃ ┣ 📜sample_output.csv
 ┃ ┣ 📜topic_classification.py
 ┃ ┣ 📜training_data.json
 ┃ ┗ 📜vocabs.txt
 ┣ 📂data
 ┃ ┣ 📂processed
 ┃ ┃ ┣ 📂split
 ┃ ┃ ┃ ┣ 📜counsel-chat-best-answer-test.csv
 ┃ ┃ ┃ ┣ 📜counsel-chat-best-answer-train.csv
 ┃ ┃ ┃ ┗ 📜train_test_split.txt
 ┃ ┃ ┣ 📜counsel-chat-best-answer.csv
 ┃ ┃ ┗ 📜counsel-chat-multiple-answers.csv
 ┃ ┗ 📂raw
 ┃ ┃ ┗ 📜counsel-chat.pkl
 ┣ 📂models
 ┃ ┗ 📂model_240411_0952
 ┃ ┃ ┣ 📜README.md
 ┃ ┃ ┣ 📜adapter_config.json
 ┃ ┃ ┣ 📜adapter_model.safetensors
 ┃ ┃ ┣ 📜special_tokens_map.json
 ┃ ┃ ┣ 📜tokenizer.json
 ┃ ┃ ┣ 📜tokenizer.model
 ┃ ┃ ┗ 📜tokenizer_config.json
 ┣ 📂notebooks
 ┃ ┣ 📂classification
 ┃ ┃ ┣ 📜bag-of-words-naive-bayes.ipynb
 ┃ ┃ ┗ 📜mental-classification.ipynb
 ┃ ┣ 📂data
 ┃ ┃ ┣ 📜data-preprocessing.ipynb
 ┃ ┃ ┣ 📜data-retrieval.ipynb
 ┃ ┃ ┗ 📜eda-wordclouds.ipynb
 ┃ ┗ 📂modelling
 ┃ ┃ ┣ 📜Llama2-7B-RAG.ipynb
 ┃ ┃ ┣ 📜eval-bleu-and-bertscore.ipynb
 ┃ ┃ ┣ 📜model-finetuning-llama2-test.ipynb
 ┃ ┃ ┗ 📜model-finetuning-llama2-train.ipynb
 ┣ 📂response
 ┃ ┣ 📜test-response-llama2-7B-RAG.csv
 ┃ ┗ 📜test-response-llama2-7B-finetuned.csv
 ┣ 📜.gitattributes
 ┣ 📜.gitignore
 ┣ 📜Demo Chatbot.mp4
 ┗ 📜README.md
```
