from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import xlsxwriter
#!/usr/bin/env python2
# -*- coding: utf-8 -*-

workbook = xlsxwriter.Workbook('Nur.xlsx')
worksheet = workbook.add_worksheet()

driver = webdriver.Chrome()
driver.implicitly_wait(10)
path = "http://vesti.kz"
driver.get(path)

news = [i.text for i in driver.find_elements_by_xpath('//div[@class="top-news subblock"]/div[@class="jspContainer"]/div[@class="jspPane"]/div[@class="single-item"]/div[@class="news_date"]//span[@class="showed"]')] #[3, 4, 0] #comments
news_link = [j.get_attribute("href") for j in driver.find_elements_by_xpath('//div[@class="top-news subblock"]/div[@class="jspContainer"]/div[@class="jspPane"]/div[@class="single-item"]/a')] #[https://tengrinews.kz, https://tengrinews.kz]

for j in range(0, 5):
	if j==0:
		worksheet.write(0, j, "News Title")
	elif j==1:
		worksheet.write(0, j, "Comments")
	elif j==2:
		worksheet.write(0, j, "Authors")
	elif j==3:
		worksheet.write(0, j, "Likes")
	elif j==4:
		worksheet.write(0, j, "Dates")

comments_count=1
for i in range(0, len(news)):
	if news[i]>=0:
		driver.get(news_link[i])
		title = driver.find_elements_by_xpath('//div[@class="subblock"]/h1[@class="inner-header"]')
		worksheet.write(comments_count, 0, title[0].text)	#comments_count=1,
		driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
		
		authors = 	driver.find_elements_by_xpath('//div[@class="comment-area-header"]/a[@class="comment-user"]')
		comments = 	driver.find_elements_by_xpath('//div[contains(@class, "comment-text")]') 
		ratings = 	driver.find_elements_by_xpath('//span[@class="comment_rating_count"]')
		dates = 	driver.find_elements_by_xpath('//span[@class="comment-date"]')
		for j in range(0, 10): #number of comments
			for k in range(1, 5):
					if k==1:
						worksheet.write(comments_count, k, comments[j].text)
					elif k==2:
						worksheet.write(comments_count, k, authors[j].text)
					elif k==3:	
						worksheet.write(comments_count, k, ratings[j].text)
					elif k==4:	
						worksheet.write(comments_count, k, dates[j].text)
			comments_count=comments_count+1	
	else:
		print("next")
		
workbook.close()