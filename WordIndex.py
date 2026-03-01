#WordIndex.py
#Name:Gavin Grow
#Date:3/1/26
#Assignment:word index

def main():
    # initialize data structures
    words = {}             
    lineNum = 0

    # open file and iterate lines
    with open("fish.txt", 'r') as textFile:
        for line in textFile:
            lineNum += 1
            # split into words and clean punctuation
            wordList = line.split()
            for w in wordList:
                cleaned = w.lower()
                # remove common punctuation characters
                for ch in ",.!?;\"'":
                    cleaned = cleaned.replace(ch, "")
                if cleaned == "":
                    continue

                if cleaned in words:
                    if lineNum not in words[cleaned]:
                        words[cleaned].append(lineNum)
                else:
                    words[cleaned] = [lineNum]

    # print the index
    for word in sorted(words):
        print(word, words[word])


if __name__ == '__main__':
    main()
