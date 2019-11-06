import re
import collections
import nltk
import pandas



path = r"enter the path of your json file"

def word_counts(file):
    with open(file, encoding = 'utf-8') as f:
        words_box = []
        for line in f:
            if re.match(r'[a-zA-Z0-9]*', line, flags=re.IGNORECASE):#avoid other languges
                line = re.sub(r'[^\w\s]','',line) #avoid any symbols
                words_box.extend(line.strip().split())
    return collections.Counter(words_box) #returns a dictionary



def word_classification(dict):
    word = []
    tag = []
    word_count = []
    for key, value in dict.items():
        tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
        text = tokenizer.tokenize(key)
        key_class_pair = nltk.pos_tag(text)
        word.append(key_class_pair[0][0])
        tag.append(key_class_pair[0][1])
        word_count.append(str(value))
    for i in range(len(word)):
        print(word[i], tag[i], word_count[i])

    #export the list to csv file
    df = pandas.DataFrame(data={"word": word, "tag": tag, "word_count": word_count})
    df.to_csv("word_counts_class.csv", sep=',', index=False)



def main():
    word_classification(word_counts(path))


if __name__ == '__main__':
    main()






