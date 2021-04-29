import os
import PIL
import cv2
from PIL import ImageFont, ImageDraw, Image
import numpy as np
SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
import_img1 = cv2.imread("import_pic/1.jpg")
import_img2 = cv2.imread("import_pic/2.jpg")

def run1st(import_img1,college,grade,major,class_t,name,number,sex,nation,applydate,phone,type,behalf,begin,end,days):
    #fontpath=ImageFont.load("STHeiti-Medium.ttf")
    import_img=import_img1
    font = ImageFont.truetype("fonts/STHeiti-Medium.ttf", 29)
    #fontpath = "font/simsun.ttc"
    #font = ImageFont.truetype(fontpath, 32)

    img_pil = Image.fromarray(import_img)
    draw = ImageDraw.Draw(img_pil)
    #draw.text((100, 300),  "Hello World", font = font, fill = (255, 255, 255))
    draw.text((267, 395),  college, font = font, fill = (60, 60, 60))
    draw.text((267, 481),  grade, font = font, fill = (60, 60, 60))
    draw.text((267, 561),  major, font = font, fill = (60, 60, 60))
    draw.text((267, 643),  class_t, font = font, fill = (60, 60, 60))
    draw.text((267, 723),  name, font = font, fill = (60, 60, 60))
    draw.text((267, 808),  number, font = font, fill = (60, 60, 60))
    draw.text((267, 887),  sex, font = font, fill = (60, 60, 60))
    draw.text((267, 970),  nation, font = font, fill = (60, 60, 60))
    draw.text((267, 1055),  applydate, font = font, fill = (60, 60, 60))
    draw.text((267, 1136),  phone, font = font, fill = (60, 60, 60))
    draw.text((267, 1214),  type, font = font, fill = (60, 60, 60))
    draw.text((267, 1297),  behalf, font = font, fill = (60, 60, 60))
    draw.text((267, 1406),  begin, font = font, fill = (60, 60, 60))
    draw.text((267, 1536),  end, font = font, fill = (60, 60, 60))
    draw.text((267, 1644),  days, font = font, fill = (60, 60, 60))
    import_img = np.array(img_pil)
    cv2.imshow("export",import_img)
    cv2.waitKey()
    cv2.imwrite("export_pic/export1.jpg",import_img)
    print("success1")
def run2nd(import_img2,college,grade,major,class_t,name,number,sex,nation,applydate,phone,type,behalf,begin,end,days,year,mouth,day,hour,minute,parents_know,parents_name,parents_phone,where,why,counselor,counselor_name):
    #fontpath=ImageFont.load("STHeiti-Medium.ttf")
    passtime=year+"年"+mouth+"月"+day+"日"+"\t"+"14"+"时"+"51"+"分"
    font = ImageFont.truetype("fonts/STHeiti-Medium.ttf", 29)
    #fontpath = "font/simsun.ttc"
    #font = ImageFont.truetype(fontpath, 32)
    import_img=import_img2
    img_pil = Image.fromarray(import_img)
    draw = ImageDraw.Draw(img_pil)
    #draw.text((100, 300),  "Hello World", font = font, fill = (255, 255, 255))
    '''
    draw.text((267, 395),  college, font = font, fill = (60, 60, 60))
    draw.text((267, 481),  grade, font = font, fill = (60, 60, 60))
    draw.text((267, 561),  major, font = font, fill = (60, 60, 60))
    draw.text((267, 643),  class_t, font = font, fill = (60, 60, 60))
    draw.text((267, 723),  name, font = font, fill = (60, 60, 60))
    draw.text((267, 808),  number, font = font, fill = (60, 60, 60))
    draw.text((267, 887),  sex, font = font, fill = (60, 60, 60))
    draw.text((267, 970),  nation, font = font, fill = (60, 60, 60))
    draw.text((267, 1055),  applydate, font = font, fill = (60, 60, 60))
    draw.text((267, 1136),  phone, font = font, fill = (60, 60, 60))
    '''

    draw.text((267, 339),  type, font = font, fill = (60, 60, 60))
    draw.text((267, 423),  behalf, font = font, fill = (60, 60, 60))
    draw.text((267, 532),  begin, font = font, fill = (60, 60, 60))
    draw.text((267, 662),  end, font = font, fill = (60, 60, 60))
    draw.text((267, 769),  days, font = font, fill = (60, 60, 60))
    draw.text((267, 872),  parents_know, font = font, fill = (60, 60, 60))
    draw.text((267, 978),  parents_name, font = font, fill = (60, 60, 60))
    draw.text((267, 1087),  parents_phone, font = font, fill = (60, 60, 60))
    draw.text((267, 1213),  where, font = font, fill = (60, 60, 60))
    draw.text((267, 1319),  why, font = font, fill = (60, 60, 60))
    draw.text((267, 1396),  counselor, font = font, fill = (60, 60, 60))
    draw.text((267, 1446),  counselor_name, font = font, fill = (135, 154, 127))
    draw.text((267, 1498),  passtime, font = font, fill = (60, 60, 60))
    import_img = np.array(img_pil)
    cv2.imshow("export",import_img)
    cv2.waitKey()
    cv2.imwrite("export_pic/export2.jpg",import_img)
    print("success2")


