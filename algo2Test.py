from collections import defaultdict
from time import time
import json, csv, random

with open ('./contractions.json') as f:
    contradict = json.load(f)

with open ('./abbreviations.json') as f:
    abbredict = json.load(f)

# sentences = ["I'll be there ASAP", "They won't come to the party", "He's got a big car", "Can't wait to see you", "It's a beautiful day today", "what is this lol", "When she laughed at my joke she said LMFAO"]
sentences = []
# contradict = {"'s": "is", "'re": "are", "'ve": "have", "'ll": "will", "'d": "would", "'m": "am", "n't": "not", "'t": "not"}
# abbredict = {"ASAP": "as soon as possible", "LMFAO": "laughing my ass off", "LOL": "laughing out loud", "lol": "laughing out loud"}

largeData = False

def loadData():
    with open('./datasets/training.1600000.processed.noemoticon.csv') as f2, open('./datasets/testdata.manual.2009.06.14.csv') as f3:
        reader = None
        if largeData:
            reader = csv.reader(f2)
        else:
            reader = csv.reader(f3)
        for line in reader:
            sentences.append(line[5])
        
# optimized version
def algo2(sentence, contractions_map, entities=[]):
    words = sentence.split()
    expanded_sentence = []
    
    # create a hash table for contractions_map for fast lookup
    contractions_hash = defaultdict(str)
    for key, value in contractions_map.items():
        index = rng(len(value))
        contractions_hash[key] = value[index]

    # for each word in the sentence
    for word in words:
        # if "'" in word:
        #     expanded_word = word[:word.index("'")] + " " + contractions_hash[word[word.index("'"):]]
        if word.lower() in contractions_hash:
            expanded_word = contractions_hash[word]
        elif word.lower() in entities:
            expanded_sentence.append(entities[word])
            continue
        else:
            expanded_word = word
        expanded_sentence.append(expanded_word)
    expanded_sentence = [item if isinstance(item, str) else ' '.join(item) for item in expanded_sentence]
    # print(f'Expanded sentence: {expanded_sentence}')
    return " ".join(expanded_sentence)

def rng(end):
    return random.randrange(end)

def start():
    global largeData
    start = time()
    useLarge = bool(input("Use large data? (y/n): ") == "y")
    largeData = useLarge
    loadData()
    for sentence in sentences:
        print(algo2(sentence, contradict, abbredict))
    print(time() - start)

if __name__ == "__main__":
    start()