from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import re
import random
# import pyautogui

class RandomWordGenerator:

	def __init__(self):
		#REMINDER: change this link with your personal info !! 
		self.__driver = webdriver.Chrome("/Users/pranatikuppa/Desktop/random_words/chromedriver")
		self.__path = 'words.txt'
		self.__special_char_pattern = '/[^a-zA-Z ]/g'
		self.__dictionary_words = self.__load_dictionary()
		# pyautogui.hotkey('command', 'shift', 'w', interval=0.25)

	def __special_char_filter(self, word):
		if (re.match(self.__special_char_pattern, word)):
			return False
		else:
			return True

	def __load_dictionary(self):
		with open(self.__path) as word_file:
			all_words = set(word_file.read().split())
		valid_words = [word for word in all_words if self.__special_char_filter(word)]
		return valid_words

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
		print(len(all_websites))
		print(i)

		selected_website = all_websites[i]
		nested_rc_r = selected_website.find_element_by_class_name('rc').find_element_by_class_name('r')
		website_link = nested_rc_r.find_element_by_tag_name('a').get_attribute('href')
		return website_link
		# search_box.submit()
		# self.__driver.quit()

	def __get_random_word_from_web(self):
		website = __get_random_website()
		self.__driver.get(website)

	def get_random_word(self):
		return self.__get_random_word_from_web()

    def get_random_words(self, number_of_words="1000"):
    	words = []
    	while number_of_words != 0: 
    		words.append(get_random_word())
    		number_of_words -=1
    	return words


    def get_random_words_within_range(self, min_word_length="0", max_word_length="-1", num_of_words = "1000"):
    	raw_words = get_random_words(num_of_words)
    	if min_word_length == 0 && max_word_length == -1:
    		return raw_words
    	else if min_word_length != 0 and max_word_length == -1: 
    		valid_words = [word for word in raw_words if word.len() > min_word_length]
    	else if min_word_length == 0 && max_word_length != -1:
    		valid_words = [word for word in raw_words if word.len() < max_word_length]
    	else: 
    		valid_words = [word for word in raw_words if word.len() > min_word_length && word.len() < max_word_length]
    	return valid_words

    def get_random_words_start_with(self, start_letter=None, num_of_words="1000"):
    	raw_words = get_random_words()
    	if start_letter == None: 
    		return raw_words
    	else: 
    		valid_words = [word for word in raw_words if word[0] == start_letter]
    	return valid_words

    # def get_random_words_contains(self, substring):

if __name__ == '__main__':
	random_word_gen = RandomWordGenerator()
	print(random_word_gen.get_random_word())