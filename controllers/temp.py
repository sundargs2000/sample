from fastai import *
from fastai.text import *
from fastai.core import *
import re
import sentencepiece as spm
import codecs
import re

import warnings
warnings.filterwarnings("ignore")

path1 = Path('./kannada-work/kannada-chatbot/')
path2 = Path('./kannada-work/kannada-chatbot/models')


class KannadaTokenizer(BaseTokenizer):
    def __init__(self, lang:str):
        self.lang = lang
        self.sp = spm.SentencePieceProcessor()
        self.sp.Load(str(path1/"kannada_lm.model"))
        
    def tokenizer(self, t:str) -> List[str]:
        return self.sp.EncodeAsPieces(t)


learn_clas = load_learner(path2,'kn-final-export.pkl')

learn_clas.predict('ಸುಂದರ')

# data = 'ವಯಸ್ಸು 18 ಕ್ಕಿಂತ ಹೆಚ್ಚಿದ್ದರೆ, ಅವರು ಮತ ಚಲಾಯಿಸಬಹುದು, ಇಲ್ಲದಿದ್ದರೆ, ಅವರು ಮತ ಚಲಾಯಿಸಲು ಸಾಧ್ಯವಿಲ್'
data = input()
print(data)

with open("in.txt", "w", encoding = 'utf-8') as fd:
    fd.write(data)
fd.close()


# -*- coding: utf-8 -*-

class Tokenizer():
	'''class for tokenizer'''

	def __init__(self,text=None):
		if text is  not None:
			self.text=text
			self.clean_text()
		else:
			self.text=None
		self.sentences=[]
		self.tokens=[]
		self.stemmed_word=[]
		self.final_list=[]
		#self.final_tokens=[]
	

	def read_from_file(self,filename):
		f=codecs.open(filename,encoding='utf-8')
		self.text=f.read()
		self.clean_text()



	def generate_sentences(self):
		'''generates a list of sentences'''
		text=self.text
		self.sentences=text.split(u"।")

	def print_sentences(self,sentences=None):
		if sentences:
			for i in sentences:
				print(end='')
		else:
			for i in self.sentences:
				print(end='')


	def clean_text(self):
		'''not working'''
		text=self.text
		text=re.sub(r'(\d+)',r'',text)
		text=text.replace(u',','')
		text=text.replace(u'"','')
		text=text.replace(u'(','')
		text=text.replace(u')','')
		text=text.replace(u'"','')
		text=text.replace(u':','')
		text=text.replace(u"'",'')
		text=text.replace(u"‘‘",'')
		text=text.replace(u"’’",'')
		text=text.replace(u"''",'')
		text=text.replace(u".",'')
		self.text=text

	def remove_only_space_words(self):

		tokens=filter(lambda tok: tok.strip(),self.tokens)
		self.tokens=list(tokens)
		
	def hyphenated_tokens(self):

		for each in self.tokens:
			if '-' in each:
				tok=each.split('-')
				self.tokens.remove(each)
				self.tokens.append(tok[0])
				self.tokens.append(tok[1])



	def tokenize(self):
		'''done'''
		if not self.sentences:
			self.generate_sentences()

		sentences_list=self.sentences
		tokens=[]
		for each in sentences_list:
			word_list=each.split(' ')
			tokens=tokens+word_list
		self.tokens=tokens
		#remove words containing spaces
		self.remove_only_space_words()
		#remove hyphenated words
		self.hyphenated_tokens()

	def print_tokens(self,print_list=None):
		'''done'''
		if print_list is None:
			for i in self.tokens:
			    print(end='')
				



	def tokens_count(self):
		'''done'''
		return len(self.tokens)

	def sentence_count(self):
		'''done'''
		return len(self.sentences)

	def len_text(self):
		'''done'''
		return len(self.text)

	def concordance(self,word):
		'''done'''
		if not self.sentences:
			self.generate_sentences()
		sentence=self.sentences
		concordance_sent=[]
		for each in sentence:
			each=each
			if word in each:
				concordance_sent.append(each)
		return concordance_sent

	def generate_freq_dict(self):
		'''done'''
		freq={}
		if not self.tokens:
			self.tokenize()

		temp_tokens=self.tokens
		#doubt whether set can be used here or not
		for each in self.tokens:
			freq[each]=temp_tokens.count(each)

		return freq

	def print_freq_dict(self,freq):
		'''done'''
		for i in freq.keys():
			print(end='')
        
			# print( i,',',freq[i])

	def remove_stop_words(self):
		f=codecs.open("stopwords.txt",encoding='utf-8')
		if not self.stemmed_word:
			self.generate_stem_dict()
		stopwords=[x.strip() for x in f.readlines()]
		tokens=[i for i in self.stemmed_word if i not in stopwords]
		self.final_tokens=tokens
		return tokens

complex_suffixes = {

#PAST TENSE simple past tense 1st person singular
1 : ["ಳಿದ್ದೆ","ಳಲಿಲ್ಲ","ಳಿದ್ದೆನ","ಳಿದೆನ"], #---> append ಳು

#simple past tense 1st person plural
2 : ["ದಿದೆವು","ದಲಿಲ್ಲ","ದಿದೆವ"],# ---> append ದು

#simple past tense 2nd person
3 : ["ಯಲಿಲ್ಲ"],

#simple past tense 3rd person plural
4 : ["ಯಾಗಿದ್ದರು","ವಾಗಿದ್ದರು","ತಾಗಿದ್ದರು","ದಾಗಿದ್ದರು","ದಿದ್ದರು","ಲಿಲ್ಲ","ದ್ದರಾ"],

#simple past tense 3rd person singular
5 : ["ಯಲಿಲ್ಲ","ಲಿಲ್ಲ","ದನ","ದನಾ"],


#past perfect tense 1st person singular
6 : ["ದಿದ್ದೆ","ಡಿದ್ದೆ","ರಲಿಲ್ಲ","ದ್ದೆನ","ದ್ದೆನಾ"],

#past perfect tennse 1st person plural
7 : ["ದಿದ್ವಿ","ರಲಿಲ್ಲ","ದಿದ್ವಾ"],

#past perfect, 2nd 
8 : ["ದಿದ್ದೆ","ಯುತ್ತಿದ್ದೆ","ತ್ತಿದ್ದವರು","ತ್ತಿದ್ದೆ","ತಿದ್ದೆ","ಯುತ್ತದೆ","ತ್ತದೆ","ಯುತ್ತಿರಲಿಲ್ಲ","ತ್ತಿರಲಿಲ್ಲ","ತಿರಲಿಲ್ಲ","ದಿರಲಿಲ್ಲ","ದ್ದಿದ್ದಾ","ಯುತ್ತಿದ್ದಾ","ತ್ತಿದ್ದಾ"],

#past perfect 3rd plural
9 : ["ದಿದ್ದರು"],

#past perfect 3rd singular
10 : ["ದಿದ್ದ","ದಿದ್ದನು","ದಿದ್ದಳು"],

#PAST CONTINUOUS simple tense 1st singular
11 : ["ತ್ತಿದ್ದೆನೆ"],

#past continuous 1st plural
12 : ["ಯುತ್ತಿದ್ದೆವು","ತ್ತಿದ್ದೆವು","ಯುತ್ತಿದ್ದೆವ","ತ್ತಿದ್ದೆವ"],

#past continuous 2nd 
13 : ["ತ್ತಿದ್ದೆ","ತಿರಲಿಲ್ಲ","ತ್ತಿದ್ದ","ತ್ತಿದ್ದಾ"],

#past continuous 3rd plural
14 : ["ತ್ತಿದ್ದರು","ತ್ತಿರಲಿಲ್ಲ","ತ್ತಿದ್ದರ","ತ್ತಿದ್ದಾರಾ"],

#past continuous 3rd singular
15 : ["ಯುತ್ತಿದ್ದನ","ಯುತ್ತಿದ್ದನಾ","ಯುತ್ತಿದ್ದಳು","ಯುತ್ತಿದ್ದನು","ಯುತ್ತಿದ್ದಳ","ಯುತ್ತಿದ್ದನ","ಯುತ್ತಿದ್ದಳೆ","ಯುತ್ತಿದ್ದನೆ","ತ್ತಿದ್ದನ","ತ್ತಿದ್ದನಾ","ತ್ತಿದ್ದಳು","ತ್ತಿದ್ದನು","ತ್ತಿದ್ದಳ","ತ್ತಿದ್ದನ","ತ್ತಿದ್ದಳೆ","ತ್ತಿದ್ದನೆ"],

#PAST PERFECT continuous 1st singular
16 : ["ತ್ತಿದ್ದೆ","ತ್ತಿರಲಿಲ್ಲ","ತ್ತಿದ್ದೆನ","ತ್ತಿದ್ದೆನಾ"],

#past perfect continuous 1st plural
17 : ["ಯುತ್ತಿದ್ದೆವೆ","ತ್ತಿದ್ದೆವೆ","ಯುತ್ತಿದ್ದೆವು","ತ್ತಿದ್ದೆವು"],

#past p continous 2nd
18 : ["ತ್ತಿದ್ದೆ","ತ್ತಿದ್ದೆವು","ತ್ತಿರಲಿಲ್ಲ","ತ್ತಿದ್ದಾ"], #----- not needed

#past p continuous 3rd plural
19 : ["ತ್ತಿದ್ದರು","ತ್ತಿದ್ದರು"],# -------- not needed

#past p continuous 3rd singular
20 : ["ತ್ತಿಲ್ಲ","ತ್ತಿದ್ದಳ","ತ್ತಿದ್ದಳು","ತ್ತಿದ್ದನ","ತ್ತಿದ್ದನು","ತ್ತಿದ್ದಾರೆ"],

#PRESENT TENSE 
#simple 1st singular
21 : ["ರುತ್ತೆನೆ","ತ್ತೆನೆ","ದಿಲ್ಲ","ಯಲ್ವಾ"],

#simple 1st plural
22 : ["ರುತ್ತೆವೆ","ರುತ್ತೇವೆ","ರುವುದಿಲ್ಲ","ರುತ್ತೇವ","ರುತ್ತೆವ","ತ್ತೆವೆ","ತ್ತೇವೆ","ವುದಿಲ್ಲ","ತ್ತೇವ","ತ್ತೆವ"],

#simple 2nd
23 : ["ತ್ತೀಯ","ವುದಿಲ್ಲ","ತ್ತಿಯ"],

#simple 3rd plural
24 : ["ತ್ತಾರೆ","ತ್ತಾರ"],

#simple 3rd singular
25 : ["ತ್ತಾನೆ","ತ್ತಾಳೆ","ವುದಿಲ್ಲ"],

#Present perfect 1st singular
26 : ["ದ್ದಿನಿ","ದ್ದೆನೆ","ದಿಲ್ಲ","ತ್ತಿದ್ದೆ","ಲ್ಲವ","ದೆನ"],

#present perfect 1st plural
27 : ["ದ್ದೆವೆ","ದ್ದೆವ"],

#present perfect 2nd
28 : ["ಡಿದ್ದೀಯ"],

#present perfect 3rd plural
29 : ["ತ್ತಿದ್ದಾರ","ತ್ತಿದ್ದಾರೆ"],

#present perfect 3rd singular
30 : ["ಯಾಗಿದೆ","ಯಾಗಿಲ್ಲ"],

#present continuous 1st singluar
31 : ["ತ್ತಿದ್ದೆನೆ","ತ್ತೆನೆ","ತ್ತೇನೆ","ತ್ತಿದ್ದೇನೆ","ತ್ತಿಲ್ಲ","ತ್ತಿದ್ದೆನ"],

#present cntinouus 1st plural
32 : ["ತ್ತಿದ್ದೇವೆ","ತ್ತೇವೆ","ತ್ತಿಲ್ಲ","ತ್ತಿದ್ದೇವೆ","ತ್ತಿದ್ದೇವ"],

#present continous 2nd
33 : ["ಯುತ್ತಿದ್ದೀಯ","ಯುತ್ತೀಯ","ಯುತ್ತಿರುವೆ","ಯುತ್ತಿಲ್ಲ","ಯುವುದಿಲ್ಲ","ತ್ತಿದಿಯ"],

#present ocntinuous 3rd plural
34 : ["ಿದರೆ","ತ್ತಿದ್ದಾರೆ","ತ್ತಿಲ್ಲ","ತ್ತಿದ್ದಾರ","ತಿರುವರ"],

#present continuous 3rd singular
35 : ["ತ್ತಿದ್ದಾನೆ","ತ್ತಿದ್ದಾಳೆ","ತ್ತಾನೆ","ತ್ತಾಳೆ","ತ್ತಿದ್ದಾನ","ತ್ತಿದ್ದಾಳ","ತ್ತಿಲ್ಲ"],

#PRESENT PERFECT continuous tense 1st singular 
36 : ["ತ್ತಿದ್ದೀನಿ","ತ್ತಿರುವೆ","ತ್ತಿಲ್ಲ","ತ್ತಿದ್ದೀನಿ","ತ್ತಿಲ್ಲವೆ","ತ್ತಿದ್ದೇನೆ"],

#present perfect continuous tense 1st plural
37 : ["ತ್ತಿದ್ದೇವೆ","ತ್ತಿರುವ","ತ್ತಿರುವೆವು","ತ್ತಿರುವೆವ","ತ್ತಿದ್ದೇವ","ತ್ತಿದೇವ","ತ್ತಿಲ್ಲವ","ತ್ತಿಲ್ಲವಾ"],

#present perfect continuous 2nd
38 : ["ತ್ತಿದೀಯ","ತ್ತಿಲ್ಲ","ತ್ತಿರುವೆಯ","ತ್ತಿದ್ದೆಯ","ತ್ತಿಲ್ಲವ"],

#present perfect continuous 3rd plural
39 : ["ದಲ್ಲಿದೆ","ಯಲ್ಲಿದೆ","ರಲ್ಲಿದೆ"],

#present perfect continuous 3rd singular
40 : ["ತ್ತಿದ್ದಾನೆ","ತ್ತಿದ್ದಾಳೆ","ತ್ತಿದ್ದಾಳ","ತ್ತಿದ್ದಾನೆ"],

41 : ["ಯಾದರೆ","ಗಾದರೆ","ವುದಾದರೆ","ದಾದರೆ"],

42 : ["ಯಾಗಿಯೇ","ಗಾಗಿಯೇ","ದಾಗಿಯೇ","ವಾಗಿಯೇ"],

43 : ["ವಾದರು","ಗಾದರು","ತಾದರು","ದಾದರು","ಯಾದರು","ರಾದರು","ಲಾದರು","ಳಾದರು","ವಾದರೂ","ಗಾದರೂ","ತಾದರೂ","ದಾದರೂ","ಯಾದರೂ","ರಾದರೂ","ಲಾದರರೂ","ಳಾದರೂ"],

44 : ["ತ್ತಿದ್ದರಂತೆ","ದೊಂದಿಗೆ","ಯೊಂದಿಗೆ","ರೊಂದಿಗೆ"],

45 : ["ಗಿದ್ದನು","ಗಿದ್ದಳು","ಗಿದ್ದರು","ಗಿದ್ದರೂ","ತಾದ್ದನು","ತಾದ್ದಳು","ತಾದ್ದರು","ತಾದ್ದರೂ","ದಾದ್ದನು","ದಾದ್ದಳು","ದಾದ್ದರು","ದಾದ್ದರೂ"],

46 : ["ಯೊಂದೆ","ವೊಂದೆ","ರೊಂದೆ","ವೊಂದ","ಯೊಂದ","ರೊಂದ","ವುದೇ"],

47 : ["ಯುವವರ","ರುವವರ","ಸುವವರ"],

48 : ["ದಲ್ಲೇ","ನಲ್ಲೇ","ನಲ್ಲಿ","ವಲ್ಲಿ","ದಲ್ಲಿ","ದಲ್ಲೂ","ಯಲ್ಲಿ","ರಲ್ಲಿ","ಗಳಲ್ಲಿ","ಳಲ್ಲಿ","ಯಲ್ಲಿನ"],

49 : ["ವವರು","ಯವರು","ನವರು","ರವರು","ದವರು","ವವ","ಯವ","ನವ","ರವ","ದವ"],

50 : ["ಗಾಗಿ","ದಾಗಿ","ವಾಗಿ","ರಾಗಿ","ಯಾಗಿ","ತಾಗಿ","ಕ್ಕಾಗಿ","ವಾಗಿದ್ದು","ವಾಗಿದ್ದ","ಗಾಗಿದ್ದು","ಗಾಗಿದ್ದ","ರಾಗಿದ್ದು","ರಾಗಿದ್ದ","ದಾಗಿದ್ದು","ದಾಗಿದ್ದ","ತಾಗಿದ್ದು","ತಾಗಿದ್ದ"],

51 : ["ರನ್ನ","ನನ್ನ","ಯನ್ನ"],

52 : ["ರನ್ನು","ವನ್ನು","ಯನ್ನು","ಗಳನ್ನೇ","ಗಳನ್ನು","ಳನ್ನು","ದನ್ನು"] ,

53 : ["ವಿರುವ","ರುವ","ದ್ದರೆ","ದ್ದಾರೆ"],

54 : ["ತ್ತಾರಂತೆ","ತ್ತಾಳಂತೆ","ತ್ತಾನಂತೆ","ಗಂತೆ","ದ್ದಂತೆ","ದಂತೆ","ನಂತೆ","ರಂತೆ","ಯಂತೆ","ಗಳಂತೆ","ಳಂತೆ","ವಂತೆ"],

55 : ["ಗಳೆಂದು","ಗಂ","ದ್ದಂ","ದಂ","ಯಂ","ರಂ","ವಂ","ಗಿಂದ","ದಿಂದ","ಯಿಂದ","ರಿಂದ","ನಿಂದ"],

56 : ["ನಿಗೆ","ರಿಗೆ","ಯಿಗೆ","ಕೆಗೆ"],

57: ["ದ್ದೇನೆ","ದ್ದಾನೆ","ದ್ದಾಳೆ","ದ್ದಾರೆ","ದಾಗ"],

58 : ["ವಿದೆ" ,"ದಿದೆ","ತಿದೆ","ಗಿದೆ"],

59 : ["ತ್ತಿರು","ವೆಂದು"],

60 : ["ನನ್ನೂ","ಳನ್ನೂ","ರನ್ನೂ"],

61 : ["ಯಾಯಿತು", "ಗಾಯಿತು","ದಾಯಿತು"],

62 : ["ದ್ದನು","ದ್ದಳು","ಯಿದ್ದರು","ದ್ದರು","ದ್ದರೂ","ಗಳೇ","ಗಳು","ಗಳ","ಗಳಿ","ದಳು","ದಳ","ವೆನು","ವನು","ವೆವು","ವಳು","ವಳ","ವುದು","ಲಾಗು","ಗಳಾದ","ಗಳಿಗೆ"],

63 : ["ವುದಕ್ಕೆ","ಕ್ಕೆ","ಗ್ಗಿ","ದ್ದಿ","ಲ್ಲಿ","ನ್ನು","ತ್ತು"],

64 : ["ವಾಯಿತು","ಗಾಯಿತು","ದಾಯಿತು","ತಾಯಿತು","ಲಾಯಿತು","ನಾಯಿತು"],

65 : ["ವಿದ್ದು","ವೆಂದಾಗ"],

66 : ["ವನ್ನೇ","ವೇಕೆ"],

67 : ["ರಾದ","ವಾದ","ಗಾದ","ಯಾದ","ರಾಗುವ"],

68 : ["ವಾದುದು", "ರಾದುದು","ಗಾದುದು","ಯಾದುದು","ದಾದುದು"],

69 : ["ಯಾರು","ದಾರು","ಗಾರು","ರಾರು","ಲ್ಲದಿ"],

70 : ["ಗಳಿಸಿ","ಗಳಿಸು","ಗಳಿವೆ","ಗಳಿವ","ಗಳಿವು"],

71 :  ["ಯು","ದ","ವಿಕೆ","ದೇ","ರು","ಳ","ಳೆ","ಲಿದೆ","ದೆ","ರೆ","ಗೆ","ವೆ","ತೆ","ಗೂ","ಿಂತ"],

72 :  ["ರದ","ಮದ","ನದ"],

73 :  ["ಡಲು","ಲಾಗುತ್ತದೆ","ಸಲು","ಸಿದ್ದಾಳೆ","ಸಿದಾಗ","ಸಲು","ಸಿದರು","ಸಿದನು","ಸಿದಳು","ಸಿದ್ದೇ","ಕಿದೀನಿ"],

74 : ["ದರೆ"]

}


add_1 = ["ು"]



def kannada_root(word, inde):
    global flag
    if word.endswith("\n"):
        word = word.split("\n")[0]

    #checking for suffixes which needs to be retained
    for L in complex_suffixes[72]:
        if len(word) > len(L)+1:
            if word.strip().endswith(L):
                inde.append("  +  "+ L)
                return(word[:-(len(L)-1)], inde)

    #checking for suffixes which needs to retained and modified 
    for L in complex_suffixes[73]:
        if len(word) > len(L)+1:
            if word.strip().endswith(L):
                flag=1
                word =word[:-(len(L)-1)]
                word = word+add_1[0]
                inde.append("  +  "+ L)
                return(kannada_root(word, inde))   

    #checking for suffixes which must be removed    
    L=1
    while L<=70:
        for suffix in complex_suffixes[L]:
            if len(word) > len(suffix)+1: 
                    if word.strip().endswith(suffix):
                        flag=1
                        inde.append("  +  "+ suffix)
                        return(kannada_root(word[:-(len(suffix))], inde))
        L = L+1

    #at last checking for remaining suffixes
    if flag == 0:
        for L in complex_suffixes[71]:
            if len(word)-len(L) >len(L)+1:
                if word.strip().endswith(L):
                    inde.append("  +  "+ L)
                    return(word[:-(len(L))], inde)
                                                      
    return word, inde

x=[]
with open("in.txt", encoding='utf-8') as file:
    num_lines2 =0
    for l in file:
        t=Tokenizer(l)
        t.tokenize()
        x=x+t.tokens
        num_lines2 =num_lines2 +t.tokens_count()


y = []
for j in range(num_lines2):
    flag = 0
    inde = []
    root = x[j]
    # print("Here is " + x[j])
    if x[j].isdigit():
      y.append(x[j])
    else:
      root, inde = kannada_root(x[j], inde)
    #print(root , inde)
    suff=""
    y.append(root+suff.join(inde))

# print(y)
#Build dictionary of split word and original word
orig_word_dict = {}
for i in range(len(y)):
    orig_word_dict[y[i]] = x[i]
# print(orig_word_dict)
#f =  open('out.txt', 'w', encoding='utf-8') 
#f.write("\n".join(y))
#f.close()

word = ""

input_list = []
with open("in.txt", encoding='utf-8') as file:
    val = file.readlines()
    # print(val)
z = []
for l in val[0].split(" "):
    # print(l)
    input_list.append(l)
    z.append(str(learn_clas.predict(l)[0]))
# print(z)
# print(y)

#Skip the numbered index (18). Then, from a stemmer standpoint, look for the words that have been stemmed. This will be the list of conditional words only.
# Use this to build out your code logic

#Step 1: Gather index of numerals

num_index = []
with open("in.txt", encoding='utf-8') as file:
    val = file.readlines()
    # print(val)
index_count = 0
for l in val[0].split(" "):
  if l.isdigit():
    # print("Found number")
    num_index.append(index_count)
  index_count += 1
# print(num_index)

index_count = 0
new_y = y[:num_index[0]] + [input_list[num_index[0]]] + y[num_index[0]:]
for item in new_y:
  if '+' in item:
    condition_index = index_count
    break
  index_count += 1
# print(condition_index)
# print(new_y)


def similar_to(x=None):
    #Greater than
    gt = ['ಹೆಚ್ಚ','ಹೆಚ್ಚಿ','ಹೆಚ್ಚು','ಹೆಚ್ಚಿಗೆ','ಅತಿ','ಬಹಳ','ವೃದ್ಧಿ','ಅಭಿವೃದ್ಧಿ ','ಹಿರಿಯದು','ಮೇಲೆ','ದೊಡ್ಡದು ']
    #less than
    lt = ['ಕಡಿಮೆಯಿ','ಕಡಿಮೆ','ಕಿರಿಯ','ಚಿಕ್ಕದು','ಸಣ್ಣದು','ಅಲ್ಪ']
    #Equal to
    et = ['ಸಮ','ಸಮಾನ','ಸಾಟಿ','ಒಂದೇ','ಸರಿ']
    # print("Received this: %s" %x)
    outcome = check_opposites(x)
    #Use the root word from the orig_word_dict dictionary
    for k,v in orig_word_dict.items():
        if v == x:
            # print("Replacing x with the root word: %s" %k.split("+")[0])
            x = k.split("+")[0]
            break
    if outcome == False:
        # print("Am i here: %s" %x)
        if x.strip() in gt:
            # print("Greater than")
            return ">"
        if x.strip() in lt:
            # print("Less than")
            return "<"
        if x.strip() in et:
            # print("Equal to")
            return "=="
        else:
            return -1
    else:
        x = outcome
        # print("Inside prefix")
        # print(x)
        if x.strip() in gt:
            return "<"
        if x.strip() in lt:
            return ">"
        if x.strip() in et:
            return "!="
        else:
            return -1



def check_opposites(x=None):
    # print("Got x: %s" %x)
    data = split(x)
    # print("Data is %s" %data)
    #Usually, the last 4 characters constitute the likes of 'illa', 'alla' etc
    start_num = len(data) - 4
    val = ''
    old_val = ''
    j = 0
    while j+4 <= len(data):
        word = ''
        for item in data[j:j+4]:
            word += item
        # print("Word is %s" %word)
        j += 1
        if word == "ಿಲ್ಲ":
            # print("Came here")
            full_word = ''
            for item in data[:j]:
                full_word += item
            # print("Full word is %s" %full_word)
            return full_word
    return False
def split(word): 
    return [char for char in word]  


# ವೇಳೆ == if , ಬೇರೆ == else
# First Noun is variable name, NUM is your condition check, stemmed word root is your check and everything else till (and including) next verb is your action
import re
variable = ""
quantity = ""
action = ""
hit_verb = 0
else_condition_exists = 0
else_action = ""
verb_count = 0
for i in range(len(new_y)):
    if z[i] == 'VM':
        verb_count += 1
# print("Total verb count = %s" %verb_count)
verb_count = 0
for i in range(len(new_y)):
#   print("-"*30)
  if z[i] == 'VM':
      print(end='')

    # print("Looking at a Verb now")
    # print(i)
    # print(new_y[i])
    # print(z[i])
  if i < condition_index:
    if z[i] == 'NN' and variable == "":
      variable = new_y[i]
    # print(variable)
    # Handle possible misclassifications
    if (new_y[i].isnumeric() or (z[i] == 'NUM' or z[i] == "QC")) and quantity == "":
    #   print("In here")
      quantity = int(new_y[i])
  elif i == condition_index:
    # print("Is this a verb: %s" %z[i])
    #Map ಹೆಚ್ಚಿ to greater than. TODO Need a model to find words similar to ಹೆಚ್ಚಿ that leads to "greater than"
    condition = similar_to(orig_word_dict[new_y[i]])
    # print("Got this condition: %s" %condition)
    if condition == -1:
        condition = input("We encountered an error. Plese specify the condition manually : Options ('>','<','==')")
  else:
    #Take the rest as action until the next verb
    if z[i] != 'VM':
      action += new_y[i] + " "
    else:
      verb_count += 1
    #   print("Verb number: %s" %i)
      if hit_verb == 0:
        action += new_y[i]
        try:
          if z[i+1] != "CC":
            action += " " + new_y[i+1]
        except:
          continue
        hit_verb = 1
        break
k = ""
curr_index = i + 1
#So now, the verb is accounted for and we need to account for "illandre"
new_index = curr_index + 2

# print("Current verb count is %s" %verb_count)
# print("Current word is: %s" %(new_y[i]))
# print("Current index is %s" %curr_index)
if len(new_y) - new_index > 0:
    else_condition_exists = 1
    # The next word is possibly the else condition.. so skip that word and the rest is your else condition
    #print(new_y[i:])
    else_action = new_y[new_index:]
# print("ELSE ACTION: %s" %else_action)
if else_action:
    for item in else_action:
        if '+' not in item:
            k += item + " "
        else:
            k += item.split("+")[0].lstrip() + " "

# print(variable,quantity,condition,action,k)

  

  

# print(action) 


print("ವೇಳೆ " + variable + " " + condition + " " + str(quantity) + ":")
print("    " + "ಮುದ್ರಿಸಿ(" + '"' + action + '"' + ")")

if else_condition_exists == 1:
  print("ಬೇರೆ:")
  print("    ಮುದ್ರಿಸಿ("+ '"' + k + '")')
