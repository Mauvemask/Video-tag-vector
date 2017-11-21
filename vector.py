#coding:utf8
import gensim.models.word2vec as w2v
import codecs
import csv
from wordOutput import wordOutput

model_name='../model/text.model'
model = w2v.Word2Vec.load(model_name)
wo = wordOutput()
model_sorted = sorted(model.wv.vocab.items(),key=lambda d:d[0],reverse=False)


def wTOcsv(model, model_sorted):
	f = open('wordVectors.csv','wb')
	f.write(codecs.BOM_UTF8)
	writer = csv.writer(f,delimiter=',')
	i=0
	words_list=[]
	for key,value in model_sorted:
		word_list=[]
		word_list.append(key)
		for j in range(len(model.wv[key])):
			word_list.append(model.wv[key][j])
		words_list.append(word_list)
		i += 1
		writer.writerow(word_list)
	f.close()

def wTOtxt(model, model_sorted):
	word_list=[]
	f = codecs.open('wordVectors.txt','w',encoding='utf-8')
	for key,value in model_sorted:
		print >> f,key,model.wv[key],'\n'
	f.close()

wTOcsv(model,model_sorted)
