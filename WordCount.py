#WordCount.py
#Name:Gavin Grow
#Date:3/1/26
#Assignment:word count

def main():
    # open the file using a context manager so it gets closed automatically
    with open("gettysberg.txt", 'r') as textFile:
        lineCount = 0
        wordCount = 0
        letterCount = 0

        for line in textFile:
            lineCount += 1
            words = line.split()
            wordCount += len(words)

            # count letters in each word (ignore non-alpha characters)
            for w in words:
                for ch in w:
                    if ch.isalpha():
                        letterCount += 1

    # print results after processing the file
    print("Words:", wordCount)
    print("Lines:", lineCount)
    print("Letters:", letterCount)


if __name__ == '__main__':
    main()
