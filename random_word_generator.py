from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import re
import random
from string import capwords 
# import pyautogui

class RandomWordGenerator:

	def __init__(self):
		#REMINDER: change this link with your personal info !! 
		self.__driver = webdriver.Chrome("./chromedriver")
		self.__dictionary_path = 'words.txt'
		self.__common_words_path = 'common_words.txt'
		self.__special_char_pattern = '/[^a-zA-Z ]/g'
		self.__dictionary_words = self.__load_dictionary()
		self.__common_words = self.__load_common_words()
		# pyautogui.hotkey('command', 'shift', 'w', interval=0.25)

	def __special_char_filter(self, word):
		if (re.match(self.__special_char_pattern, word)):
			return False
		else:
			return True

	def __common_words_filter(self, word):
		if (word.lower() in self.__common_words):
			return False
		else:
			return True

	def __load_dictionary(self):
		with open(self.__dictionary_path) as word_file:
			all_words = set(word_file.read().split())
		valid_words = [word for word in all_words if self.__special_char_filter(word)]
		return valid_words

	def __load_common_words(self):
		with open(self.__common_words_path) as word_file:
			all_words = set(word_file.read().split())
		return all_words

	def __get_dictionary_word(self):
		i = random.randint(0, len(self.__dictionary_words))
		return self.__dictionary_words[i]

	def __get_random_website(self):
		search_word = self.__get_dictionary_word()
		self.__driver.get('http://www.google.com/')
		search_box = self.__driver.find_element_by_name('q')
		search_box.send_keys(search_word)
		search_box.submit()

		all_websites = self.__driver.find_elements_by_class_name('g')
		i = random.randint(0, len(all_websites) - 1)

		selected_website = all_websites[i]
		nested_rc_r = selected_website.find_element_by_class_name('rc').find_element_by_class_name('r')
		website_link = nested_rc_r.find_element_by_tag_name('a').get_attribute('href')
		return website_link
		# search_box.submit()
		# self.__driver.quit()

	def __get_random_word_from_web(self):
		website = self.__get_random_website()
		self.__driver.get(website)
		all_website_text = self.__driver.find_element_by_tag_name("body").text
		website_words = all_website_text.split()
		filtered_website_words = [word for word in website_words if self.__common_words_filter(word)]
		i = random.randint(0, len(filtered_website_words) - 1)
		return filtered_website_words[i];

	def get_random_word(self):
		s = self.__get_random_word_from_web()
		s = re.sub(r'[^\w\s]','',s).lower()
		s = s.replace(" ", "")
		return s

	#BELOW HERE: METHODS PK HAS WORKED ON
	def get_random_words(self, number_of_words=1000):
		words = []
		while number_of_words != 0: 
			words.append(random_word_gen.get_random_word())
			number_of_words -=1
		return words

	#DISCLAIMER: THIS METHOD FOR TESTING PURPOSES ONLY
	def get_rw_test(self): 
		return ['test', 'words', 'generator', 'deletion', 'hi', 'there', 'preamble', 'precursor']

	def get_random_words_within_range(self, min_word_length=0, max_word_length=-1, num_of_words = 1000):
		#raw_words = random_word_gen.get_random_words(num_of_words)
		#DISCLAIMER: LINE BELOW FOR TESTING PURPOSES ONLY
		raw_words = random_word_gen.get_rw_test()

		if min_word_length == 0 and max_word_length == -1:
			return raw_words
		elif min_word_length != 0 and max_word_length == -1: 
			valid_words = [word for word in raw_words if len(word) >= min_word_length]
		elif min_word_length == 0 and max_word_length != -1:
			valid_words = [word for word in raw_words if len(word) <= max_word_length]
		else: 
			valid_words = [word for word in raw_words if len(word) >= min_word_length and len(word) <= max_word_length]
		return valid_words

	def get_random_words_start_with(self, start_letter=None, num_of_words=1000):
		#raw_words = random_word_gen.get_random_words()
		#DISCLAIMER: LINE BELOW FOR TESTING PURPOSES ONLY
		raw_words = random_word_gen.get_rw_test()
		if start_letter == None: 
			return raw_words
		else: 
			valid_words = [word for word in raw_words if word[0] == start_letter]
		return valid_words

	def get_random_words_order(self, order='alpha',num_of_words=1000): 
		#aw_words = random_word_gen.get_random_words()
		#DISCLAIMER: LINE BELOW FOR TESTING PURPOSES ONLY
		raw_words = random_word_gen.get_rw_test()
		if order == 'alpha': 
			raw_words.sort(key = lambda l: l.lower())
			return raw_words
		elif order == 'rev alpha': 
			raw_words.sort(reverse=True, key = lambda l: l.lower())
			return raw_words
		elif order == 'len': 
			raw_words.sort(key = len)
			return raw_words
		elif order == 'rev len':
			raw_words.sort(reverse=True, key = len)
			return raw_words

	def get_random_words_contains(self, substr=''):
		#aw_words = random_word_gen.get_random_words()
		#DISCLAIMER: LINE BELOW FOR TESTING PURPOSES ONLY
		raw_words = random_word_gen.get_rw_test()
		return [word for word in raw_words if substr in word]

	#def include_pos(self, pos)
	#TO BE IMPLEMENTED WHEN WE FIGURE OUT HOW WE'RE USING CSV

	#def language(self, lang='en')
	#TO BE IMPLEMENTED LATER WHEN WEBSCRAPING IS FINISHED

if __name__ == '__main__':
	random_word_gen = RandomWordGenerator()
	print(random_word_gen.get_random_word())

	#DISCLAIMER: METHODS BELOW FOR TESTING ONLY
	"""
	print("original list ")
	print(random_word_gen.get_rw_test())
	print("range with a min ") 
	print(random_word_gen.get_random_words_within_range(min_word_length = 4))
	print("range with a max ")
	print(random_word_gen.get_random_words_within_range(max_word_length = 5))
	print("range with a min and max") 
	print(random_word_gen.get_random_words_within_range(min_word_length = 2, max_word_length = 5))
	print("with a start letter ") 
	print(random_word_gen.get_random_words_start_with(start_letter = 't'))
	print("alphabet order ") 
	print(random_word_gen.get_random_words_order())
	print("rev alpha ") 
	print(random_word_gen.get_random_words_order(order='rev alpha'))
	print("len ") 
	print(random_word_gen.get_random_words_order(order='len'))
	print("rev len ") 
	print(random_word_gen.get_random_words_order(order='rev len'))
	print("contains")
	print(random_word_gen.get_random_words_contains('pre'))
	"""

