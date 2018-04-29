from django.db import models
from PIL import Image, ImageDraw, ImageFont
import textwrap
import urllib.request
import requests
from bs4 import BeautifulSoup

# Create your models here.
class Raw_data(models.Model):
	title = models.TextField()
	bg_img = models.TextField()
	link = models.TextField()

	def parse(self, slug1, slug2):
		url = "https://crimemoldova.com/rss/"
		resp = requests.get(url)
		soup = BeautifulSoup(resp.content, features='xml')

		items = soup.findAll('item')
		news_url = "https://crimemoldova.com/news/" + slug1 + "/" + slug2 + "/"
		print(news_url)
		news_items = []

		for item in items:
		    if item.link.text == news_url:
		        news_item = {}
		        news_item['link'] = item.link.text
		        news_item['title'] = item.title.text
		        news_item['image'] = item.enclosure['url']
		        news_items.append(news_item)
		        break
		self.row_title = news_items[0]['title']
		self.row_link = news_items[0]['link']
		self.row_image = news_items[0]['image']

	def __str__(self):
		return self.title

	 

class Imag(models.Model):
	full_img = models.ImageField(upload_to='uploads/')
	title = models.TextField()
	link = models.TextField()

	def create(self, bg, title_text):
		URL = bg


		with urllib.request.urlopen(URL) as url:
		    with open('back.jpg', 'wb') as f:
		        f.write(url.read())

		ironman = Image.open('image_maker/static/image_maker/images/Crime_Moldova_trans.png', 'r')
		bg = Image.open('back.jpg', 'r')
		pb = bg.resize((1368, 627))
		pp = pb.point(lambda x: x*0.38)
		text_img = Image.new('RGBA', (1200, 627), (0, 0, 0, 0))
		text_img.paste(pp, (-84, 0))
		text_img.paste(ironman, (0, 0), mask=ironman)
		text_img.save("result.png", format="png")


		title = title_text
		img = Image.open("result.png")
		draw = ImageDraw.Draw(img)
		font = ImageFont.truetype("image_maker/static/image_maker/fonts/Uni Sans Heavy.otf", 48)

		text = textwrap.fill(title, width=40)

		draw.multiline_text((100, 357),text, (255,255,255),font=font, align="left", spacing= 20)
		img.save('image_maker/static/image_maker/images/final_result.png')




		



