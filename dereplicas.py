#!/usr/bin/python
# encoding=utf-8
from __future__ import print_function
from collections import Counter, defaultdict
import sys
import jieba.posseg as pseg

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

seperators=set(['.', ':', '：', '#', '，', ',', '。', ';', '；', '?', '？'])
cluster=defaultdict(list)
for nloop, line in enumerate(sys.stdin):
    if nloop % 100 == 0:
        eprint('.', end='')
    line=line.strip()
    #line='│  YY、六间房、9158这些秀场的服务和用户群有什么差别？.txt'
    #eprint(line)
    words = pseg.cut(line)
    cnt=Counter()
    phra=''
    phras=[]
    for word, flag in words:
        if word==' ':
            word='[SPACE]'
        elif word=='\n':
            word='[NL]'
        #eprint('%s %s' % (word, flag))
        if word.encode('utf-8') in seperators:
            if len(phra) > 5:
                phras.append(phra)
                #print('*%s'%phra)
            phra=''
        if flag=='x':
            continue
        cnt[word] += 1
        phra+=word
    if len(phra) > 5:
        phras.append(phra)
    #eprint('-----------------------------')
    #for word in cnt:
        #eprint('%s %s' % (word, cnt[word]))
    #print('len(phras)=%s'%len(phras))
    for phra in phras:
        #eprint(phra.encode('utf-8'))
        cluster[phra].append(line)
eprint('')
eprint('=============================')
    #sys.stdout.flush()
for phra, lines in cluster.items():
    if len(lines) < 2:
        continue
    print('---------'+phra.encode('utf-8'))
    for line in lines:
        print(line)
