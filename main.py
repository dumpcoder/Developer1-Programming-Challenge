delimiters = {' ','.',',','\n', ':', ';', '"', '(' ')', '{', '}', '[', ']', '?', '!'}

inputFile = open('input.txt', 'r')
paragraph = inputFile.read() + ' '
inputFile.close()

#Gets words
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


histogram = {}
justify = 0
for word in words:
    if word in histogram:
        histogram[word] += 1
    else:
        histogram[word] = 1
        wordLength = len(word)
        if wordLength > justify:
            justify = wordLength

histogram = sorted(histogram.items(), key=lambda x: x[1], reverse=True)
outputFile = open('output.txt', 'w')
for item in histogram:
    word = item[0]
    count = item[1]
    outputFile.write(f'{word.rjust(justify)} | {chr(35) * count} ({count})\n')
outputFile.close()
