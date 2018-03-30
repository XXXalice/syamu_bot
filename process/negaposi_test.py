from janome.tokenizer import Tokenizer
import pandas as pd


negaposi_dict = 'pn.dic.csv'
text = 'こんにちは。'

def tokenize(text):
    """
    形態素解析するだけ
    :param text: 解析対象の文章
    :return: 品詞毎に分けられた文章の配列
    """
    t = Tokenizer()
    result = []

    tokens = t.tokenize(text)
    for token in tokens:
        result.append(token.base_form)

    return result


def make_pndict(csv):
    """
    極性辞書を読み込んで扱いやすい形式にして返す関数
    :param csv: 極性辞書
    :return: '文':pn値の辞書
    """
    pn_df = pd.read_csv('../src/' + csv, sep=':', encoding='utf-8', names=('word', 'read', 'POS', 'PN'))
    word_list = list(pn_df['word'])
    pn_list = list(pn_df['PN'])
    pn_dict = dict(zip(word_list, pn_list))

    return pn_dict


def calc_pn(tokenize_result, pn_dict):
    """
    ネガポジの計算をする
    :param tokenize_result:
    :param pn_dict:
    :return:
    """
    pn_value = 0
    positive = True

    for token in tokenize_result:
        if token in pn_dict:
            pn_value += pn_dict[token]

    if pn_value < 0:
        positive = False
    return (pn_value, positive)

def main():
    pn_dict = make_pndict(negaposi_dict)
    tokenize_result = tokenize(text)
    result = calc_pn(tokenize_result, pn_dict)
    if result[1] == False:
        print('result:Negative', result[0])
    else:
        print('result:Positive', result[0])

if __name__ == '__main__':
    main()