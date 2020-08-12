from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import re
import random
# import pyautogui

class RandomWordGenerator:

	def __init__(self):
		self.__driver = webdriver.Chrome("/Users/khushidesai/Desktop/csprojects/pythonwebscraping/chromedriver")
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
		i = random.randint(0, len(all_websites))

		selected_website = all_websites[i]
		nested_rc_r = selected_website.find_element_by_class_name('rc').find_element_by_class_name('r')

		self.__driver.get(website_link)
		return website_link
		# search_box.submit()
		# self.__driver.quit()

	def __get_random_word_from_web(self):
		website = __get_random_website()

	def get_random_word(self):
		self.__get_random_website()

    # def get_random_words(number_of_words="-1"):

    # def get_random_words_within_range(min_word_length="0", max_word_length="-1"):

    # def get_random_words_start_with(start_letter):

    # def get_random_words_contains(substring):

if __name__ == '__main__':
	random_word_gen = RandomWordGenerator()
	print(random_word_gen.get_random_word())