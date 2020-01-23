#!/usr/bin/python3

import argparse
import re

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('infile',help="Input Filename")
    parser.add_argument('outfile', nargs='?',help="Output Filename")
    args = parser.parse_args()

    inputFilename = args.infile
    outputFilename = args.outfile if args.outfile else "output.txt"

    words = getWordsFromFile(inputFilename)
    histogram, justLength = createHistogramAndGetJustification(words)
    printAndWriteHistogramToFile(outputFilename, histogram, justLength)


def getWordsFromFile(filename):
    inputFile = open(filename, 'r')
    paragraph = inputFile.read()
    inputFile.close()
    return list(re.findall(re.compile('\w+'), paragraph.lower()))

def createHistogramAndGetJustification(words):
    histogram = {}
    # JustLength equals to the max word length in words (for output styling)
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


def printAndWriteHistogramToFile(filname, histogram, justLength):
    outputFile = open(filname, 'w')
    for item in histogram:
        word = item[0]
        count = item[1]
        line = f'{word.rjust(justLength)} | {chr(35) * count} ({count})\n'
        outputFile.write(line)
        print(line, end='')
    outputFile.close()


if __name__ == '__main__':
    main()