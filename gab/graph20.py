import numpy as np
import matplotlib.pyplot as plt
y = np.arange(1,24)
x = [10,6,3,4,6,3,2,3,7,0,0,1,0,6,1,1,1,1,0,0,0,1,0]
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



