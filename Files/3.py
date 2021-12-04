from collections import Counter
def word_count(fname):
    with open(fname) as f:
        return Counter(f.read().split())
print("number of words:",word_count("demo1.txt"))