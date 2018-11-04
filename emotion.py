import os
import csv
import sys
sys.path.insert(0, './DeepMoji/examples')
import score_texts_emojis

def get(text):
    # return the list of emoji using Deepmoji
    return score_texts_emojis.predict(text)
#    with open('./test_sentences.csv', 'rb') as f:
#        reader = list(csv.reader(f))
#	print("hey")
#	print(reader[2:7])
#        return reader[2:7]

def process(emotions):
    # arg: [[1, 2, 3], [4, 5, 6], [4, 5, 6], []]
    # increase count in array
    # -1 the null one
    # return max
    print(emotions)
    buckets = [0] * 63
    for x in emotions:
        for y in x:
            buckets[int(y) - 1] += 1
    emotion = ["happy", "sad", "angry", "frustated", "neutral", "surprise", "calm"]
    values = [[0, 7, 15, 16, 53], [2, 3, 5, 22, 27, 29, 34, 35, 52, 25, 45], [1, 19, 37, 55, 32], [37, 52], [25], [4, 23], [36, 54, 44], [12], [14, 35]]
    emoji = "neutral"
    val = 0
    for e in range(7):
        temp = 0;
        for x in values[e]:
            temp += x
        if temp > val:
            val = temp
            emoji = emotion[e]
    return emoji
