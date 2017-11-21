#coding:utf8
import codecs
import jieba
import jieba.posseg as pseg
jieba.load_userdict('../dict/userDic.txt')
import os
from word_preProcess import preProccess

class wordSegment(preProccess):
	"""对文本进行切割
		1. 读取文件
		2. 文档清洗：去除符号，英文，数字
		3. 文档切割

	"""
	def __init__(self):
		# super(preProccess, self).__init__()
		#self.arg = arg
		pass

	def cutWords(self,file_name_in,file_name_out,psg=False):
		'''
		去除非中文之后分词
		'''
		symbos = ['\n','\r','\t','\f','\v','\\','.',';',':','!','@','#','$','%','^','&','*','(',')','+','-','_','，','。','！','、','/','（','）','[',']','《','》','‘','’','；','【','】','：','“','”','？','　','<','>']
		fin = codecs.open(file_name_in,'r','utf-8')
		# delete exsiting file
		while os.path.exists(file_name_out):
			os.remove(file_name_out)
		
		line = fin.readline()
		while line:
			if psg==False:
			# delete string which not include in Chinese string set

				# Segment_tool = jieba.posseg.dt

				newline = jieba.cut(line,cut_all=True)
				# print 'newline',newline
				str_out = ' '.join(newline).encode('utf-8')\
				.replace('，',' ').replace('！',' ').replace('？',' ').replace('。',' ')\
				.replace('（',' ').replace('）',' ').replace('《',' ').replace('》',' ')\
				.replace('“',' ').replace('”',' ').replace('；',' ').replace('：',' ')\
				.replace('~',' ').replace('-',' ').replace('——',' ').replace('+',' ')\
				.replace('=',' ').replace('*',' ').replace('&',' ').replace('%',' ')\
				.replace('、',' ').replace('、',' ').replace('.',' ').replace('_',' ').replace('\n',' ')
				self.writeToTXT_continue(str_out, file_name_out)
				line = fin.readline()
			elif psg:
				print 'enter psg success'
				# Segment_tool = pseg.dt
				newline = pseg.cut(line)
				for n in newline:
					print 'n.word:',n.word
					read_word = n.word
					read_word = read_word.strip
					print 'strip success'
					print type(read_word)
					print n.word
					if n.word in symbos:
						continue
					elif len(n.word)==0 or len(n.word)==1:
						continue
					else:
						n.strip()
						self.writeToTXT_continue(n.word, file_name_out)
				'psg end'
				os.exit()
			else:
				print 'word cut error! Please check whether file exist.'

		fin.close()
			# fout.close()
	
	def writeToTXT_continue(self, p, file_name):
		'''
		从尾部继续写入txt文件
		'''
		fout = open(file_name,'a')
		print >> fout,p
		fout.close()

	def unicodeCovert(self,x):
		try: 
			model.similar_by_word(x)
		except:
			x = x.encode('utf-8').decode('utf-8-sig')
		return x

	def fileBatch(self,tagger):
		for tag in tagger:
			file_name_in = tag+'.txt'
			self.cutWords(file_name_in, tag+'Segment.txt')




