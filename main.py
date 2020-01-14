def main():
    inputFilename = 'input.txt'
    words = getWordsFromFile(inputFilename)
    histogram, justLength = createHistogramAndGetJustification(words)
    outputFilename = 'output.txt'
    writeHistogramToFile(outputFilename, histogram, justLength)


def getWordsFromFile(filename):
    inputFile = open(filename, 'r')
    paragraph = inputFile.read() + ' '
    inputFile.close()
    return parseParagraphForWords(paragraph)


def parseParagraphForWords(paragraph):
    # Set of common delimiters
    delimiters = {' ','.',',','\n', ':', ';', '"', '(' ')', '{', '}', '[', ']', '?', '!'}

    words = []
    curWord = ""
    write = False
    for char in paragraph:
        if char in delimiters and not write:
            continue
        if char in delimiters:
            write = False
            words.append(curWord)
            curWord = ""
        else:
            write = True
            curWord += char.lower()
    return words


def createHistogramAndGetJustification(words):
    histogram = {}
    # JustLength equals to the max word length in words
    justLength = 0
    for word in words:
        if word in histogram:
            histogram[word] += 1
        else:
            histogram[word] = 1
            wordLength = len(word)
            if wordLength > justLength:
                justLength = wordLength

    # Sorts histogram by value, and returns a list of key/value tuples. 
    histogram = sorted(histogram.items(), key=lambda x: x[1], reverse=True)

    return (histogram, justLength)


def writeHistogramToFile(filname, histogram, justLength):
    outputFile = open(filname, 'w')
    for item in histogram:
        word = item[0]
        count = item[1]
        outputFile.write(f'{word.rjust(justLength)} | {chr(35) * count} ({count})\n')
    outputFile.close()


if __name__ == '__main__':
    main()