from django.db import models
from PIL import Image, ImageDraw, ImageFont
import textwrap
import urllib.request
import requests
import re

# Create your models here.
class Raw_data(models.Model):
	title = models.TextField()
	bg_img = models.TextField()
	link = models.TextField()

	def parse(self, slug1, slug2):


		news_url = "https://crimemoldova.com/news/" + slug1 + "/" + slug2 + "/"
		resp = requests.get(news_url)

		pattern1 = r'.*class="article-header-pic-img" src="(.*)" alt='
		pattern2 = r'.*alt="(.*)"'
		pattern3 = r'.*<b>(.*)</b>'


		image_path = re.findall(pattern1, resp.text)
		full_path = "https://crimemoldova.com" + image_path[0]

		title_text = re.findall(pattern2, resp.text)

		desc = re.findall(pattern3, resp.text)

		self.row_title = title_text[2]
		self.row_link = news_url
		self.row_image = full_path
		self.row_desc = desc[0]

	def __str__(self):
		return self.title

	 

class Imag(models.Model):
	full_img = models.ImageField(upload_to='uploads/')
	title = models.TextField()
	link = models.TextField()

	def create(self, bg, title_text):
		URL = bg


		with urllib.request.urlopen(URL) as url:
		    with open('/home/crimemoldova/crime-post/image_maker/static/image_maker/images/back.jpg', 'wb') as f:
		        f.write(url.read())

		ironman = Image.open('/home/crimemoldova/crime-post/image_maker/static/image_maker/images/Crime_Moldova_trans.png', 'r')
		bg = Image.open('/home/crimemoldova/crime-post/image_maker/static/image_maker/images/back.jpg', 'r')
		pb = bg.resize((1368, 627))
		pp = pb.point(lambda x: x*0.38)
		text_img = Image.new('RGBA', (1200, 627), (0, 0, 0, 0))
		text_img.paste(pp, (-84, 0))
		text_img.paste(ironman, (0, 0), mask=ironman)
		text_img.save("/home/crimemoldova/crime-post/image_maker/static/image_maker/images/result.png", format="png")


		title = title_text
		img = Image.open("/home/crimemoldova/crime-post/image_maker/static/image_maker/images/result.png")
		draw = ImageDraw.Draw(img)
		font = ImageFont.truetype("/home/crimemoldova/crime-post/image_maker/static/image_maker/fonts/Uni Sans Heavy.otf", 48)

		text = textwrap.fill(title, width=40)

		draw.multiline_text((100, 357),text, (255,255,255),font=font, align="left", spacing= 20)
		img.save('/home/crimemoldova/crime-post/image_maker/static/image_maker/images/final_result.png')




		



