#!/usr/bin/python
#-*-coding:utf-8 -*-

import jieba
import sys
import os
import re
reload(sys)
sys.setdefaultencoding('utf8')

words = []

def loading():
    stopwords = {}
    fstop = open('stop_word.txt', 'r')
    for eachWord in fstop:
        stopwords[eachWord.strip().decode('utf-8', 'ignore')] = eachWord.strip().decode('utf-8', 'ignore')
    fstop.close()
    with open('10train.txt', 'r') as fin:
        for line in fin:
            line1 = line.strip().decode('utf-8', 'ignore')
            line1 = re.sub("[0-9\s+\.\!\/_,$%^*()?;；:-【】+\"\']+|[+——！，;:。？、~@#￥%……&*（）]+".decode("utf8"), "".decode("utf8"),line1)
            wordList = list(jieba.cut(line1))                        #用结巴分词，对每行内容进行分词  
            outStr = [] 
            for word in wordList:
                if word not in stopwords:  
                    outStr.append(word)  
            words.append(' '.join(outStr))
            '''             
            segs = list(jieba.cut(line, cut_all = False))
            segs = [word for word in list(segs) if word not in stopwords] 
            words.append(' '.join(segs))
            print ' '.join(segs).encode('utf-8')
            '''

def saving(name):
    with open(name, 'wb') as fout:
        for i in xrange(len(words)):
            fout.write(words[i].encode('utf-8'))
            fout.write("\n")

if __name__ == '__main__':
    corpus = 'segment.txt'
    if not os.path.exists(corpus):
        loading()
        saving(corpus)
    import word2vec
    bin_name = 'corpusWord2Vec.bin'
    word2vec.word2vec(corpus, bin_name , size=300, verbose=True)
    model = word2vec.load(bin_name)
    print (model.vectors)
