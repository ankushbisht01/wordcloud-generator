# -*- coding: utf-8 -*-

from wordcloud import WordCloud
from matplotlib import pyplot as plt
from PIL import Image , ImageDraw , ImageFont
import numpy as np
import requests
from bs4 import BeautifulSoup as bs
import lxml , io , base64

from decouple import config

class ImageGen():

    def __init__(self):
        pass


    def read_img_from_url(content):
        r=requests.get(url)
        img = Image.open(BytesIO(content))
        img_matrix = np.array(img)
        return img_matrix


    def read_txt_from_url(text, height=15,widht=5):
        
        wc = WordCloud(background_color="white", max_words=100 , max_font_size=500, width=size[1], height=size[0], random_state=42)
        wc.generate(text)
        txt_matrix =  wc.to_array()
        return txt_matrix
        
    def image_mask(self):    
        img_matrix[txt_matrix == 255] = 0
        final = Image.fromarray(img_matrix)
        final.save('new.jpg')
    
        
    def masking_wordcloud(self,text,img_array):
        new_image = Image.new(mode="RGB",size=img_array.size ,color=(255,255,255))
        new_image.paste(img_array,box=img_array)
        rgb_array = np.array(new_image)

        word_cloud = WordCloud(background='white',mask=rgbarray,colormap='heat').generate(text)

    def normal_wordcloud(self,text,colormap='Paste1',bg_color='white'):
        word_cloud = WordCloud(width=1980,height=1080,max_words=500,font_path = 'fonts/font.ttf',background_color=bg_color,colormap=colormap,collocations=False).generate(text)
        return word_cloud.to_image()

    def upload(self, content):
        buf = io.BytesIO()
        content.save(buf, format='JPEG')
        byte_im = buf.getvalue()
        api_key = config('imgbb_api')
        url = "https://api.imgbb.com/1/upload"
        
        payload = {"key": api_key, "image": base64.b64encode(byte_im)}
        while True:
            try:
                result = requests.post(url, payload)
                if result.status_code == 200: break
            except:
                return "Something is wrong....!"
        
        return result.json()['data']['url']
