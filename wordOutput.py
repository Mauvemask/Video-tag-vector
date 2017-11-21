#coding:utf8
import gensim.models.word2vec as w2v 
import word2vec
from wordSegment import wordSegment
from word_preProcess import preProccess
from wordModel import wordModel
import codecs
import csv
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class wordOutput():
	"""docstring for wordOutput"""
	def __init__(self):
		# super(wordOutput, self).__init__()
		# self.arg = arg
		pass
	def writeToCSV(self, list_name, file_name_out):
		f = open(file_name_out,'w')
		f.write(codecs.BOM_UTF8)
		writer = csv.writer(f, delimiter=',')
		# lenth = len(list_name)
		for i in range(len(list_name)):
			# lenth2 = len(list_name[i])
			for j in range(len(list_name[i])):
				writer.writerow(list_name[i][j])
		f.close()

	def writeToTXT(self, list_name, file_name_out):
		f = codecs.open(file_name_out,'w',encoding='utf-8')
		for i in range(len(list_name)):
			for j in range(len(list_name[i])):
				print >> f,list_name[i][j][0]
				print >> f,list_name[i][j][1]
				print >> f,list_name[i][j][2:]
		f.close()

	def unicodeCovert(self,x):
		try: 
			model.similar_by_word(x)
		except:
			x = x.encode('utf-8').decode('utf-8-sig')
		return x


if __name__ == '__main__':
	tagger=[] 
	distance_list=[]

	pre = preProccess()
	tagger = pre.rTxTtoList('50.txt')
	pre.rwAllTxTbyP('bq_150_eng.txt',tagger)

	cutword = wordSegment()
	model = wordModel()
	cutword.fileBatch(tagger)
	model_name='model.txt'
	model.fileBatch(tagger)

	# model.createModel(file_name_in, model_name)
	distance_list = model.countDistance(model_name,tagger)
	# print distance_list
	record = wordOutput()
	record.writeToCSV(distance_list, 'distances.csv')

	# #test
	# cutword.cutWords('bq_150_eng.txt', 'bq_150_segment.txt')
	# word2vec.word2vec('150150.txt', 'bq_150.bin', size=300, verbose=True)
	# test_model = word2vec.load('bq_150.bin')
	# indexes = test_model.cosine(u'出现')
	# for index in indexes[0]:
	# 	print (test_model.vocab[index])
	
