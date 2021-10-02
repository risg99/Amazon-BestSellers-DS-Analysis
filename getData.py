import pandas as pd
from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests

maxPages = 2

def get_data(pageNo):
	'''
	Get data of Amazon's Best Book Sellers
	'''

	headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}
	r = requests.get('https://www.amazon.in/gp/bestsellers/books/ref=zg_bs_pg_'+str(pageNo)+'?ie=UTF8&pg='+str(pageNo), headers=headers)#, proxies=proxies)
	content = r.content
	soup = BeautifulSoup(content,features="html.parser")

	bookResults = []
	for data in soup.findAll('div', attrs={'class':'a-section a-spacing-none aok-relative'}):
		bookNameDiv = data.find('span', attrs={'class':'zg-text-center-align'})
		bookName = bookNameDiv.find_all('img',alt=True)
		bookAuthor = data.find('a', attrs={'class':'a-size-small a-link-child'})
		bookRating = data.find('span',attrs={'class':'a-icon-alt'})
		bookUsersRated = data.find('a', attrs={'class':'a-size-small a-link-normal'})
		bookPrice = data.find('span', attrs={'class':'p13n-sc-price'})
		
		bookResult = []

		if bookName is not None:
			bookResult.append(bookName[0]['alt'])
		else:
			bookResult.append('Unknown-Book')

		if bookAuthor is not None:
			bookResult.append(bookAuthor.text)
		else:
			author = data.find('span', attrs={'class':'a-size-small a-color-base'})
			if author is not None:
				bookResult.append(author.text)
			else:
				bookResult.append('Unknown-Author')

		if bookRating is not None:
			bookResult.append(bookRating.text)
		else:
			bookResult.append('-1')

		if bookUsersRated is not None:
			bookResult.append(bookUsersRated.text)
		else:
			bookResult.append('0')

		if bookPrice is not None:
			bookResult.append(bookPrice.text)
		else:
			bookResult.append('0')
		bookResults.append(bookResult)
	return bookResults

amazonBestSellers = []
for i in range(1,maxPages+1):
	amazonBestSellers.append(get_data(i))

flattenData = lambda lis : [item for sublist in lis for item in sublist]
cols = ["Book Name", "Book Author", "Book Rating", "Users Rated", "Book Price"]
df = pd.DataFrame(flattenData(amazonBestSellers),columns = cols)
df.to_csv('amazon_bestsellers.csv',index=False, encoding='utf-8')