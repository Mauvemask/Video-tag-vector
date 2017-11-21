#coding:utf8
import codecs
import re
import os
class preProccess:
	"""
	对文件的读写处理
	"""
	def __init__(self):
		# super(wordSample, self).__init__()
		# self.arg = arg
		pass
		

	# convert file to list
	def rTxTtoList(self, file_name):
		'''
		文本中的每一行转换为list中的一个元素
		将标签库导入进程序作为list
		'''
		fin = open(file_name,'r')
		tagger = []
		for line in fin.readlines():
			line = line.lstrip('\ufeff')
			# print line,
			tagger.append(line.decode('utf-8').replace('\n',''))
		fin.close()
		
		return tagger

	# read txt, find key word and write it to txt
	def rwAllTxTbyP(self,file_name,taggers):
		'''
		1. 读入文本
		2. 按照\n\n切割，并存入list
		3. 对于list中的每段文本寻找关键词
		4. 若存在，将文本写入文件，并删除list中的文本片段（list中元素）
		5. 若不存在跳转到list中下一个元素，直到list最后一个元素
		'''
		# 1
		fin = codecs.open(file_name, 'r','utf-8')

		# 2
		text = fin.read()
		try:
			text = text.lstrip('\ufeff')
			# print 'text'
			# print text
		except UnicodeError:
			raise ValueError('without BOM')
		paraList = re.split('\r\n\r\n', text)
		# print 'paraList'
		# print paraList

		# 3 4 5
		
		for keyword in taggers:
			file_name = keyword + '.txt'
			while os.path.exists(file_name):
				os.remove(file_name)
			# print 'keyword'
			# print keyword
			i=1
			for p in paraList:
				estimate = self.matchTagger(p,keyword)
				if estimate == True:
					self.writeToTXT_continue(p,file_name)
				else:
					pass
	def readbyP(self, file_name_in,file_name_out, tagger):
		'''
		1. 读入文本
		2. 按照n\n切割得到文本源序列
		3. 按照关键词排序写文件
		'''
		fin = codecs.open(file_name_in, 'r', 'utf-8')
		text = fin.read()
		try:
			text = text.lstrip('\ufeff')
		except UnicodeError:
			raise ValueError('without BOM')
		finally:
			paraList = re.split('\r\n\r\n', text)

		while os.path.exists(file_name_out):
			os.remove(file_name_out)
		for keyword in tagger:
			for p in paraList:
				estimate = self.matchTagger(p,keyword)
				if estimate == True:
					p = re.sub('\r\n', ' ', p)
					# print p
					self.writeToTXT_continue(p, file_name_out)
					
				else:
					continue
			self.writeToTXT_continue('\r\n', file_name_out)


	def writeToTXT_continue(self, p, file_name):
		'''
		从尾部继续写入txt文件
		'''
		fout = codecs.open(file_name,'a',encoding='utf-8')
		print >> fout,p
		fout.close()

	def writeToTXT(self,p,file_name):
		'''
		以覆盖的方式写入文件
		'''
		fout = codecs.open(file_name,'w',encoding='utf-8')
		print >> fout,p
		fout.close()

	def matchTagger(self,paragraph,keyword):
		'''
		判断段落的标题中是否包含关键字：
		包括，返回Ture
		不包括，返回FALSE
		'''
		p = paragraph

		# 表达式
		expression = '> (.*)\r\n'
		pattern = re.compile(expression)
		match = re.search(pattern, p)
		keyword = keyword.lstrip('\ufeff')

		# 判断返回值
		try:
			# print match.group(1)
			title = match.group(1).split(' ')
			b= keyword.encode('utf-8').decode('utf-8-sig')
			if b in title:
				return True
			else:
				return False
		except:
			return False

	def pre_Proccess(self, tag_file_name):
		'''
		建立标签
		'''
		pre = preProccess()
		tagger = pre.rTxTtoList(tag_file_name)
		return tagger
	







