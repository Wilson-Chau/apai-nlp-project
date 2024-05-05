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