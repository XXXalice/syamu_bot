import bot as b

phase = 0
limit = 3
first_word = '今日'

def dialogue(w):
    global phase, limit
    try:
        phase += 1
        print('phase' + str(phase))
        word1 = b.load_w2v(w)
        sentence1 = b.make_sentence(word1)
        print('syamu1:' + sentence1)
        word2 = b.tokenize(sentence1)
        sentence2 = b.make_sentence(word2)
        print('syamu2:' + sentence2)
        next_word_base = b.tokenize(sentence2)
        if not phase >= limit:
            dialogue(next_word_base)
        else:
            return
    except Exception as e:
        print('occur an error.' + e)
        exit(0)
def main():
    dialogue(first_word)


if __name__ == '__main__':
    main()