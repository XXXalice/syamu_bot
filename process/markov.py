from janome.tokenizer import Tokenizer
import json,os

from markov_test import test


text_file = 'hatsugen.txt'
json_file = 'syamu_markov.json'

def tokenize(text):
    t = Tokenizer()
    lines = text.split('\n')
    words = ' '.join(lines)
    tokens = t.tokenize(words)
    markov_dic = make_markov_dic(tokens)

    return markov_dic

def make_markov_dic(tokens):
    tmp = ['@']
    dic = {}
    for token in tokens:
        word = token.base_form
        if word == '　' or word == ' ' or word == '「' or word == '」' or word == '\n':
            continue
        tmp.append(word)
        if len(tmp) < 3:
            continue
        if len(tmp) > 3:
            tmp = tmp[1:]
        word1, word2, word3 = tmp
        if not word1 in dic:
            dic[word1] = {}
        if not word2 in dic[word1]:
            dic[word1][word2] = {}
        if not word3 in dic[word1][word2]:
            dic[word1][word2][word3] = 0
        dic[word1][word2][word3] += 1
        if word == '。':
            tmp = ['@']
            continue

    return dic

def main():
    if not os.path.exists('../src/' + json_file):
        try:
            bindata = open('../src/' + text_file, 'rb').read()
            text = bindata.decode('utf-8')
        except Exception as e:
            print('error!',e)
            exit(0)

        markov_dic = tokenize(text)
        json.dump(markov_dic, open('../src/' + json_file, 'w', encoding='utf-8'))
    else:
        markov_dic = json.load(open('../src/' + json_file, 'r'))

    print(test(markov_dic))

if __name__ == '__main__':
    main()