import numpy as np
import pickle
import csv
from imp import reload
from ipynb.fs.defs.POS_tagging import viterbi_decode

label_vocab = dict()

# check viterbi with test inputs
def check_viterbi():

    with open("test.pickle","rb") as f:
        examples = pickle.load(f)
    test_input = examples[0]["tensor"]

    try:
        results = [viterbi_decode(example["tensor"]) == example["predictions"] for example in examples]
        if len(set(results)) == 1 and results[0]:
            print("Check Successful")
        else:
            print("Error!")
    except Exception as e:
        print("Error!")
        print(e.args)

if __name__ == "__main__":
    check_viterbi()
