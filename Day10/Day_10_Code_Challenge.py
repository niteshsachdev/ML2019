
"""
Code Challenge 1

Certificate Generator

Develop a Python code that can generate certificates in image format. 
It must take names and other required information from the user and generates 
certificate of participation in a Python Bootcamp conducted by Forsk.

Certificate should have Forsk Seal, Forsk Signature, Different Fonts
"""
name=input("Enter Your Name ")
branch=input("Enter Your Branch ")
from PIL import Image, ImageDraw, ImageFont
border_img=Image.new('RGB',(600,400),'White')
logo=Image.open('Forsk_logo_bw.png')
logo.thumbnail((150, 100))
border_img.paste(logo, (225, 20))
d = ImageDraw.Draw(border_img)
font = ImageFont.truetype("arial.ttf", 35)
font1 = ImageFont.truetype("arial.ttf",20)
d.text((100,100), "Certificate Of Participation", fill=(255,0,0),font=font)
text="  This is Certify that "+name+" "+branch+" Branch, Successfully"+ '\n' +"Completed Python Bootcamp Conducted by Forsk Technologies"+'\n'+"                        on May. 31, 2019."
d.text((20,180), text, fill=(0,0,0),font=font1)
sign = Image.open("sign.png")
#sign.size
#crop_im = sign.crop(box=(0, 45, 337, 140))
#crop_im.save('sign.png')
sign.thumbnail((150, 100))
border_img.paste(sign, (225, 290))
text1="  Dr. Sylvester"+'\n'+"(Founder Forks)"
d.text((225,340), text1, fill=(0,0,255),font=font1)
certificate = Image.new('RGB', (border_img.width+20, border_img.height+20), 'yellow')
certificate.paste(border_img, (10, 10))

certificate.show()



"""
Code Challenge 2

I-Card Generation System

Write a Python code for a system that generates I-card for all studentsof Forsk
Summer Developer Program and store them in image format. 

It must take names and other required information from the user.
"""
name=input("Enter full Name ")
age=input("Enter Age")
mob_no=input("Enter Mobile No.")
photo=input("Enter the path of Photo")
coll=input("Enter College Short Name")
course=input("Enter Course Name")
from PIL import Image, ImageDraw, ImageFont
id_card=Image.new('RGB',(300,400),'White')
d = ImageDraw.Draw(id_card)
font1 = ImageFont.truetype("arial.ttf", 30)
d.text((20,10), "Forsk Technologies", fill=(255,0,0),font=font1)

photo_id=Image.open(photo)
photo_id = photo_id.resize((100, 100), resample=Image.BICUBIC)

#photo_id.thumbnail((100,50))
id_card.paste(photo_id, (100, 70))

font = ImageFont.truetype("arial.ttf", 20)
d.text((32,200), "Name        : "+name, fill=(0,0,0),font=font)
d.text((32,230),"Company   : Forsk Tech", fill=(0,0,0),font=font)
d.text((32,260), "Age            : "+age, fill=(0,0,0),font=font)
d.text((32,290), "Mobile No. : "+mob_no, fill=(0,0,0),font=font)
d.text((32,320), "College     : "+coll, fill=(0,0,0),font=font)
d.text((32,350), "Course     : "+course, fill=(0,0,0),font=font)

border_im = Image.new('RGB', (id_card.width+20, id_card.height+20), 'yellow')
border_im.paste(id_card, (10, 10))
#border_im.save(name=".jpg")
border_im.show()



"""
Code Challenge 3

Watermarking Application

Have some pictures you want copyright protected? Add your own logo or text lightly 
across the background so that no one can simply steal your graphics off your site. 
Make a program that will add this watermark to the picture.
"""

from PIL import Image, ImageDraw, ImageFont
photo_id=Image.open("photo.png").convert("RGBA")
data = ImageDraw.Draw(photo_id)
w,h = list(map(lambda x: x/2,photo_id.size))
font = ImageFont.truetype("arial.ttf", 35)
data.text((w/2,h), "FORSK", fill=(255, 0, 0,9),font=font)
photo_id.show()

"""
Code Challenge 4
GIF Creator

A program that puts together multiple images (PNGs, JPGs, TIFFs) to make a smooth 
GIF that can be exported. Make the program convert small video files to GIFs as 
well.
"""

import imageio
images = []
kargs = { 'duration': 3 }
filenames=['Forsk_logo_bw.png','photo.png','sign.png']
for filename in filenames:
    images.append(imageio.imread(filename))
imageio.mimsave('movie.gif', images,**kargs)


"""another solution, take all file present in a given folder
import imageio
import os
import sys

if len(sys.argv) < 2:
  print("Not enough args - add the full path")

indir = sys.argv[1]

frames = []

# Load each file into a list
for root, dirs, filenames in os.walk(indir):
  for filename in filenames:
    if filename.endswith(".jpg"):
        print(filename)
        frames.append(imageio.imread(indir + "/" + filename))


# Save them as frames into a gif 
exportname = "output.gif"
kargs = { 'duration': 5 }
imageio.mimsave(exportname, frames, 'GIF', **kargs)
"""


"""
Code Challenge 5

Fortune Teller (Horoscope)

A program that checks your horoscope on various astrology sites and puts them 
together for you each day. The code should share the Horoscope on Tweeter account
 of the user.

"""

from bs4 import BeautifulSoup
import requests
sign=input("Enter Your Zodiac Sign")
url="https://www.astrology.com/horoscope/daily/"+sign+".html"
source = requests.get(url).text
soup = BeautifulSoup(source,"lxml")
page = soup.find('p').getText()
print("\n"+sign.upper()+" HOROSCOPE :\n")
print(page)