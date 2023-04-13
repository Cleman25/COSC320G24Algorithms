from time import time
import json, csv, random

with open ('./contractions.json') as f:
    contradict = json.load(f)

with open ('./abbreviations.json') as f:
    abbredict = json.load(f)

sentences = []

def algo1(S: str, contraction_dict: dict[str, str], abbreviation_dict: dict[str, str]) -> str:
    E = ""
    for word in S.split():
        # if word is a contraction
        if "'" in word:
            for contraction, full_phrase in contraction_dict.items(): # for each contraction in the dictionary
                if word.lower() == contraction.lower():
                    index = random.randrange(len(contraction_dict[contraction]))
                    E += contraction_dict[contraction][index] + " "
        # if word is an abbreviation
        elif word.lower() in abbreviation_dict:
            index = random.randrange(len(abbreviation_dict[word]))
            E += abbreviation_dict[word][index] + " " # add the full phrase
        else:
            E += word + " " # add the word
    return E

def loadData():
    with open('./datasets/training.1600000.processed.noemoticon.csv') as f2, open('./datasets/testdata.manual.2009.06.14.csv') as f3:
        reader = None
        if largeData:
            reader = csv.reader(f2)
        else:
            reader = csv.reader(f3)
        for line in reader:
            sentences.append(line[5])

if __name__ == "__main__":
    global largeData
    useLarge = bool(input("Use large data? (y/n): ") == "y")
    largeData = useLarge
    loadData()
    start = time()
    for sentence in sentences:
        print(algo1(sentence, contradict, abbredict))
    print(time() - start)