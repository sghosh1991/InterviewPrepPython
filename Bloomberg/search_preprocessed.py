import glob
import re
import string


words_by_file = {}

index_by_words_by_file = {}


def findWordInLine(line, word):
    return len(re.findall(word, line, re.IGNORECASE))

def cleanseWord(word):

    return  word.strip(string.punctuation).lower()


def index(file):
    with open(file) as f:
        line = f.readline()
        line_num = 1
        while (line):
            words = line.split()
            for word in words:
                word = cleanseWord(word)
                if word not in index_by_words_by_file:
                    index_by_words_by_file[word] = { }
                if file not in index_by_words_by_file[word]:
                    index_by_words_by_file[word][file] = { 'lines' : [], 'num_occurances': 0 }
                index_by_words_by_file[word][file]['lines'].append(line_num)
                index_by_words_by_file[word][file]['num_occurances'] += 1
            line = f.readline()
            line_num += 1
    #print str(index_by_words_by_file)


def iterateOverFiles(path):
    # Itearate over the files in the path
    for file_path in glob.glob(path):
        index(file_path)



def lookupWord(word):
    if word in index_by_words_by_file:
        outPutSortedFileList(index_by_words_by_file[word])
    return "Not found"

def outPutSortedFileList(searchRes):
    # sorting
    matches = []
    for match in searchRes:
        matches.append(match)

    matches_sorted = sorted(matches, key=lambda x: x[1], reverse=True)
    print matches_sorted


if __name__ == "__main__":
    iterateOverFiles('./data/*.txt')
    word = raw_input("Enter word to search: ")
    while word != 'exit':
        print lookupWord(cleanseWord(word))
        word = str(raw_input("Enter word to search: "))
