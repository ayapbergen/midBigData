from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import xlwt
#!/usr/bin/env python2
# -*- coding: utf-8 -*-

workbook = xlwt.Workbook()
worksheet = workbook.add_sheet('Vesti', cell_overwrite_ok=True)

driver = webdriver.Chrome()
driver.implicitly_wait(10)
path = "http://vesti.kz"
driver.get(path)

news = [i.text for i in driver.find_elements_by_xpath('//div[@class="single-item"]/div[@class="news_date"]//span[@class="showed"]')]
news_link = [j.get_attribute("href") for j in driver.find_elements_by_xpath('//div[@class="single-item"]/a')]

worksheet.write(0, 0, "Title")
worksheet.write(0, 1, "Comments")
worksheet.write(0, 2, "Authors")
worksheet.write(0, 3, "Likes")
worksheet.write(0, 4, "Dates")

comments_count=1
for i in range(0, len(news)):
	if news[i]>=0:
		driver.get(news_link[i])
		driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
		
		title = driver.find_elements_by_xpath('//div[@class="subblock"]/h1[@class="inner-header"]')
		authors = 	driver.find_elements_by_xpath('//div[@class="comment-area-header"]/a[@class="comment-user"]')
		comments = 	driver.find_elements_by_xpath('//div[contains(@class, "comment-text")]') 
		ratings = 	driver.find_elements_by_xpath('//span[@class="comment_rating_count"]')
		dates = 	driver.find_elements_by_xpath('//span[@class="comment-date"]')
        
        worksheet.write(comments_count, 0, title[0].text)
        for j in range(len(comments)):
            worksheet.write(comments_count, 1, comments[j].text)
            worksheet.write(comments_count, 2, authors[j].text)
            worksheet.write(comments_count, 3, ratings[j].text)
            worksheet.write(comments_count, 4, dates[j].text)
            comments_count+=1

workbook.save('vesti.xls')