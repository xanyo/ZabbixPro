#!/usr/bin/env python3
'''
Script for extracting the price of item's on the Zwilling website
'''
import requests
from bs4 import BeautifulSoup
import sys
import json
# 'https://uk.zwilling-shop.com/Kitchen-World/Kitchen-Knives/Knife-accessories/Knife-blocks-empty/Knife-block-bamboo-magnet-Zwilling-35046-110-0.html'


def obtain_price(url):
	''' Returns the price of the item without currency symbols '''
	try:
		response = requests.get(url)
	except:
		exit('Failed to perform GET of URL: ' + url)
	soup = BeautifulSoup(response.text, 'lxml')
	price = soup.h1.find(attrs={'itemprop':'price'}).text.strip().lstrip().replace('£','')
	return print(price)

def obtain_availability(url):
	''' Returns 1 if item is available or 0 if not '''
	try:
		response = requests.get(url)
	except:
		exit('Failed to perform GET of URL: ' + url)
	soup = BeautifulSoup(response.text, 'lxml')
	results = soup.h1
	content = results.find('meta', attrs={'itemprop':'availability'})['content']
	if content == 'InStock':
		availability = 1
	else:
		availability = 0
	return print(availability)

def main():
	URL = sys.argv[1]
	if sys.argv[2] == 'price':
		obtain_price(URL)
	elif sys.argv[2] == 'availability':
		obtain_availability(URL)
	return

if __name__ == '__main__':
	main()
