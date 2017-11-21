#coding:utf8
import gensim.models.word2vec as w2v 
from wordSegment import wordSegment
from word_preProcess import preProccess
from wordModel import wordModel
from wordOutput import wordOutput
import codecs

def main(text_file_name, tag_file_name, output_name, term=0):
	
	"""	
	1. 选择读全文txt or 读标签txt
	2. 读取文件，做分词处理
	3. 建立模型
	4. 读取模型并计算距离
	"""

	if term == 0:
		allTextProcess(text_file_name, tag_file_name, output_name)
		# print 'enter 0'
	elif term == 1:
		taggerTextProcess(text_file_name, tag_file_name, output_name)
		# print 'enter 1'
	else:
		print 'Wrong parametre!'

def allTextProcess(text_file_name, tag_file_name, output_name):
	tagger = []
	distance_list =[]
	
	# 建立标签
	pre = preProccess()
	tagger = pre.pre_Proccess(tag_file_name)
	
	# 文件源分词处理
	segment = wordSegment()
	psg=False
	segment.cutWords(text_file_name, 'temp_text_name.txt',psg)
	print 'cutwords success'
	
	# 成立模型
	model_name ='../model/text.model'
	model = wordModel()
	model.createModel('temp_text_name.txt',model_name)
	print 'createModel success'
	# print model.wv
	
	# 距离计算
	# distance_list = model.singleCount(model_name,tagger)
	# print 'count distance sucess'
	
	# 距离输出至文件
	# record = wordOutput()
	# record.writeToCSV(distance_list, output_name)

def taggerTextProcess(text_file_name, tag_file_name, output_name):
	tagger = []
	distance_list =[]
	
	# 建立标签
	pre = preProccess()
	tagger = pre.pre_Proccess(tag_file_name)
	print "create tag success"

	# 将文件按照标签将段落重写
	file_name_out = 'temp_file.txt'
	pre.readbyP(text_file_name,file_name_out, tagger)
	print "Preprocess file success"

	#文本源分词处理
	segment = wordSegment()
	segment.cutWords(file_name_out, 'temp_text_name.txt')
	print 'cutwords success'

	# # 文本源分词处理并建立模型并计算距离
	# cutword = wordSegment()
	# cutword.fileBatch(tagger)

	# 成立模型
	# model_name ='text_model.txt'
	# model = wordModel()
	# model.createModel('temp_text_name.txt',model_name)
	# print 'createModel success'

	# model_name_suff='model.txt'
	# model = wordModel()
	# model.fileBatch(model_name_suff, tagger)
	# print "file batch success"

	# model.createModel(file_name_in, model_name)
	# distance_list = model.countDistance(model_name_suff,tagger)
	# print distance_list

	# 距离计算
	# distance_list = model.singleCount(model_name,tagger)
	# print 'count distance sucess'
	
	# 距离输出至文件
	# record = wordOutput()
	# record.writeToCSV(distance_list, output_name)
	# print 'write file success'

if __name__ == "__main__":
	main('../data/bq_150.txt', '50.txt', 'distances.csv', 0)
