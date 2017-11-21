#coding:utf8
import gensim.models.word2vec as w2v 
from wordSegment import wordSegment
from word_preProcess import preProccess
import csv
import codecs
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class wordModel():
	'''
	1. 建立模型
	2. 储存模型
	3. 读取模型
	4. 计算关键词之间的距离
	'''
	def __init__(self):
		# super(wordModel, self).__init__()
		# self.arg = arg
		pass

	def createModel(self,file_name,model_name):
		'''
		输入关键字文段，得出关键字对应的模型
		'''
		
		# print file_name
		# f = codecs.open(file_name,'r',encoding='utf-8')
		sentences = w2v.LineSentence(file_name)
		# print sentences[0]
		word_model = w2v.Word2Vec(sentences, size=90, window=5, min_count=1, workers=4, hs=0, negative=3)
		word_model.save(model_name)

	def countDistance(self, tag1, tag2, model_name):
		'''
		1. 读取模型
		2. 计算两个标签在该模型中的距离
		3. 若标签在模型中存在，计算两个关键词之间的距离
		5. 若标签在模型中不存在，设置两个关键词之间的距离为零
		'''
		# print 'tag1:',tag1,' ','tag2:',tag2
		tag_others_distances=[]
		word_model = w2v.Word2Vec.load(model_name)
		if tag1==' ' or tag2==' ' or tag1=='\r' or tag2=='\r' or tag1=='\n' or tag2=='\n' or len(tag1)==0 or len(tag2)==0 or tag1.strip()=='' or tag2.strip()=='':
			return False
		else:
			try:
				tag_tag_distance = (unicode(tag1),unicode(tag2),word_model.similarity(tag1,tag2))
			except:
				print tag1,tag2
				print 'Distance count error!'
				tag_tag_distance = (unicode(tag1),unicode(tag2),0)
			finally:
				return tag_tag_distance

	def unicodeCovert(self,x):
		x = x.lstrip('\ufeff')
		try: 
			model.similar_by_word(x)
		except:
			x = x.encode('utf-8').decode('utf-8-sig')
		return x

	def fileBatch(self, model_name_suff, tagger):
		'''
		分标签建立model并储存
		'''
		for tag in tagger:
			file_name_in = tag+'.txt'
			model_name = tag + model_name_suff
			self.createModel(file_name_in, tag+'.model')

	def batchCount(model_name, tagger):
		result_distance=[]
		for tag in tagger:
			distance=[]
			model_name= tag + model_name_suff
			others = [items for items in tagger if items!=tag]
			for keyword in others:
				tag1 = self.unicodeCovert(tag)
				tag2 = self.unicodeCovert(keyword)
				distance.append(countDistance(tag1,tag2,model_name))
			result_distance.append(distances)
		return result_distance

	def singleCount(self, model_name, tagger):
		result_distance=[]
		for i in range(len(tagger)):
			distance=[]
			tag = tagger[i]
			others = [items for items in tagger if items != tag]
			for keyword in others:
				tag1 = self.unicodeCovert(tag)
				tag2 = self.unicodeCovert(keyword)
				temp = self.countDistance(tag1, tag2, model_name)
				if temp==False:
					continue
				else:
					distance.append(temp)
			result_distance.append(distance)
		return result_distance

	def tag_keywords_estblish(self,model_name,video_name,keywords):
		result_distance=[]
		for video in range(len(video_name)):
			distance=[]
			word = video_name[video]
			for keyword in keywords:
				# print 'enter'
				word1 = self.unicodeCovert(word)
				# print word1
				word2 = self.unicodeCovert(keyword)
				# print word2
				distance_between_words = self.countDistance(word1, word2, model_name)
				if distance_between_words==False:
					continue
				else:
					# record = (word1,word2,distance)
					distance.append(distance_between_words)
			# distance = sorted(distance,key=lambda distances:distances[2])
			result_distance.append(distance)
			# print len(distance)
			# for num in range(len(distance)):
			# 	print distance[num][1]
			# # # distance.sort(key, reverse)
		return result_distance

	def writeToCSV(self, list_name, file_name_out):
		f = open(file_name_out,'wb')
		f.write(codecs.BOM_UTF8)
		writer = csv.writer(f, delimiter=',')
		# lenth = len(list_name)
		for i in range(len(list_name)):
			# lenth2 = len(list_name[i])
			for j in range(len(list_name[i])):
				writer.writerow(list_name[i][j])
		f.close()


if __name__ =='__main__':
	video_file = '../data/video_name.txt'
	keywords_file = '../data/keywords.txt'
	model_name ='../model/text.model'
	pre_proccess=preProccess()
	video_name = pre_proccess.rTxTtoList(video_file)
	keywords = pre_proccess.rTxTtoList(keywords_file)
	output_name = '../result/video_words_distance.csv'
	# print video_name
	# print keywords
	word_model=wordModel()
	distance_list = []
	distance_list = word_model.tag_keywords_estblish(model_name, video_name[:30], keywords)
	word_model.writeToCSV(distance_list, output_name)
