import glob
import re


words_by_file = {}

def findWordInLine(line, word):
    return len(re.findall(word, line, re.IGNORECASE))


def findWordInFile(file, word):
    with open(file) as f:
        line = f.readline()
        line_num = 1
        while (line):
            num_occurances = findWordInLine(line , word)
            if num_occurances:
                if file not in words_by_file:
                    words_by_file[file] = [[], 0, file]
                words_by_file[file][0].append(line_num)
                words_by_file[file][1] += num_occurances
            line = f.readline()
            line_num += 1


def iterateOverFiles(path, word):
    # Itearate over the files in the path
    for file_path in glob.glob(path):
        findWordInFile(file_path, word)



def outPutSortedFileList():
    # sorting
    matches = words_by_file.values()

    matches_sorted = sorted(matches, key=lambda x: x[1], reverse=True)
    print matches_sorted





if __name__ == "__main__":
    iterateOverFiles('./data/*.txt', 'juliet')
    outPutSortedFileList()











