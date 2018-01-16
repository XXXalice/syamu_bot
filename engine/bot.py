from gensim.models import word2vec
from janome.tokenizer import Tokenizer
import json, random

model_file = 'syamu_w2v_model.model'
markov_file = 'syamu_markov.json'

def tokenize(s):
    t = Tokenizer()
    tokens = t.tokenize(s)
    for token in tokens:
        base_form = token.base_form
        pos = token.part_of_speech
        pos = pos.split(',')[0]
        if pos in ['名詞','動詞','形容詞']:
            return base_form
    return '@'

def load_w2v(word):
    model = word2vec.Word2Vec.load('../src/' + model_file)
    try:
        similar_words = model.most_similar(positive=[word])
        return random.choice([w[0] for w in similar_words])
    except:
        return word

def make_sentence(reply):
    markov_dic = json.load(open('../src/' + markov_file))
    if not reply == '':
        ret = []
        if not '@' in markov_dic:
            return 'no dict'

        top = markov_dic['@']
        word1 = word_choice(top)
        word2 = word_choice(top[word1])
        ret.append(word1)
        ret.append(word2)
        while True:
            word3 = word_choice(markov_dic[word1][word2])
            ret.append(word3)
            if word3 == '。':
                break
            if len(ret) >= 10:
                ret.append('。')
                break
            word1, word2 = word2, word3
        return ''.join(ret)
    else:
        return ''

def word_choice(sel):
    keys = sel.keys()
    ran = random.choice(list(keys))
    return ran


def main():
    while True:
        s = input('you  :')
        if s == 'quit':
            break
            exit(0)
        word = tokenize(s)
        if not word == '@':
            reply = load_w2v(word)
        else:
            reply = ''
        sentence = make_sentence(reply)
        print('syamu:' + sentence)

if __name__ == '__main__':
    main()