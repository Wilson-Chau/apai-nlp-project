import gensim
import json
import nltk
import pandas as pd
import sys
from nltk.corpus import stopwords
from sklearn.naive_bayes import GaussianNB

def main():
    if len(sys.argv) != 3:
        print("Usage: python classifier/topic_classification.py <input.csv> <output.csv>")
        sys.exit(1)

    input_path = sys.argv[1]
    output_path = sys.argv[2]

    topics = [
        'anxiety',
        'depression',
        'family-conflict',
        'intimacy',
        'parenting',
        'relationships',
        'self-esteem',
    ]
        
    # load input texts
    input_texts = pd.read_csv(input_path).rename(columns={" message": "message"})
    
    # 1. Pre-processing
    nltk.download("stopwords")
    input_texts["words"] = input_texts["message"].apply(lambda x: list(filter(
        lambda word: word not in stopwords.words("english"), gensim.utils.simple_preprocess(x)
    )))
    
    # 2. Bag of Words Representation
    with open("classifier/vocabs.txt") as f:
        vocabs = [line.rstrip() for line in f]
    def get_bow(ws):
        words = [word if word in vocabs else vocabs[0] for word in ws]
        return [words.count(v) for v in vocabs]
    input_texts["bow"] = input_texts["words"].apply(get_bow)
    
    # 3. Classification
    with open("classifier/training_data.json") as f:
        data = json.load(f)
    for t in topics:
        gnb = GaussianNB()
        gnb.fit(data[t]["X"], data[t]["y"])
        input_texts[t] = gnb.predict(list(input_texts["bow"]))
    
    # save classification results
    input_texts.drop(columns=["words", "bow"]).to_csv(output_path, index=False)

if __name__ == "__main__":
    main()