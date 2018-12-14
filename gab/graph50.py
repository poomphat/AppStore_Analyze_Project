import numpy as np
import matplotlib.pyplot as plt
y = np.arange(1,24)
x = [1664,118,314,154,62,81,78,36,29,58,0,15,30,20,24,12,24,21,15,22,13,11,1]
gen = ["Games","Entertainment","Education","Photo & Video","Utilities","Health & Fitness"\
       ,"Productivity","Social Networking","Lifestyle","Music","Shoping","Sports"\
       ,"Book","Finance","Travel","News","Weather","Reference","Food & Drink"\
       ,"Business","Navigation","Medical","Catalogs"]
gen.reverse()
x.reverse()
ay = plt.gca(yticks=y) # กำหนดให้ขีดวางตรงทุกค่าตำแน่งที่ป้อนเข้าไป 
ay.set_yticklabels(gen,rotation=0) # ใส่ชื่อจังหวัดลงไปแทนตัวเลข 
plt.barh(y,x)
plt.show()
