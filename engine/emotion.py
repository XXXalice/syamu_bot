import bot as b
import pandas as pd

pn_csv = 'pn.dic.csv'
emo_param_file = 'emo_param.dat'
syamu_emo = [1,2,3,4,5]#数字が若いほど明るい


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


def emotion(say):
    """
    感情を数値で算出する関数
    パラメータはsrcフォルダ下のdatファイルで管理
    :param say: こっちの発言
    :return: syamuの気分
    """
    pn_dict = make_pndict(pn_csv)
    tokenize_result = b.tokenize_all(say)
    feel_dict = {
        1:'絶好調',
        2:'好調',
        3:'普通',
        4:'不快',
        5:'最悪'
    }

    with open('../src/' + emo_param_file, "r") as f:
        param = float(f.read())
        for token in tokenize_result:
            if token in pn_dict:
                param += pn_dict[token]
    with open('../src/' + emo_param_file, "w") as f:
        f.write(str(param))
    #ここ汚いから直したい
    if -1 < param < 1:
        return feel_dict[syamu_emo[2]]
    elif 1 <= param < 2:
        return feel_dict[syamu_emo[1]]
    elif 2 <= param:
        return feel_dict[syamu_emo[0]]
    elif -2 < param <= -1:
        return feel_dict[syamu_emo[3]]
    elif param <= -2:
        return feel_dict[syamu_emo[4]]
