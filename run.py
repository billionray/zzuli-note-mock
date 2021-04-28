import os
from main import run1st,run2nd
import cv2
import time
import datetime as dt
datetime = time.strftime("%Y-%m-%d", time.localtime())
year=time.strftime("%Y", time.localtime())
mouth=time.strftime("%m", time.localtime())
day=time.strftime("%d", time.localtime())
#hour=time.strftime("%hour", time.localtime())
#minute=time.strftime("%min", time.localtime())
#print(hour)
#print(minute)
year=str(float(year)-2000)
mouth=str(int(str(mouth)))
day=str(int(str(day)))
#hour=int(str(hour))
#minute=int(str(minute))
hour=0
minute=0
college=""
grade=""
major=""
class_t=""
name=""
number=""
sex=""
nation=""
applydate=""
phone=""
type=""
behalf=""
begin=""
end=""
parents_know=""
parents_name=""
parents_phone=""
where=""
why=""
counselor=""
counselor_name=""

begin_date = dt.datetime.strptime(begin, "%Y-%m-%d").date()  ##datetime.date(2018, 1, 6)
end_date = dt.datetime.strptime(end, "%Y-%m-%d").date()  ##datetime.date(2018, 1, 9)
days = (end_date - begin_date).days+1
days=str(days)






print(days)
import_img1 = cv2.imread("import_pic/1.jpg")
import_img2 = cv2.imread("import_pic/2.jpg")
run1st(import_img1,college,grade,major,class_t,name,number,sex,nation,applydate,phone,type,behalf,begin,end,days)
run2nd(import_img2,college,grade,major,class_t,name,number,sex,nation,applydate,phone,type,behalf,begin,end,days,year,mouth,day,hour,minute,parents_know,parents_name,parents_phone,where,why,counselor,counselor_name)