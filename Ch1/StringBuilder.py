import random
import string
import time
from xml.etree.ElementTree import tostring

#Adding words without append
def strbuild(w):
    sentence = ""
    for l in w:
        sentence = sentence + l
    return sentence

#With append
def strbuildap(w):
    sentence = []
    for l in w:
        sentence.append(l)
    return "".join(sentence)

def main():
    N = 10000000
    longstring = list(random.choices(string.ascii_uppercase + string.digits, k=N))
    start_time = time.time()
    a = strbuild(longstring)
    print("--- %s seconds without append ---" % (time.time() - start_time))
    start_time = time.time()
    b = strbuildap(longstring)
    print("--- %s seconds with append ---" % (time.time() - start_time))
    return

if __name__ == "__main__":
    main()