import numpy as np
import matplotlib.pyplot as plt
y = np.arange(1,24)
x = [458,93,102,80,48,50,46,31,30,28,0,40,12,30,24,16,24,13,15,10,12,10,1]
gen = ["Games","Entertainment","Education","Photo & Video","Utilities","Health & Fitness"\
       ,"Productivity","Social Networking","Lifestyle","Music","Shoping","Sports"\
       ,"Book","Finance","Travel","News","Weather","Reference","Food & Drink"\
       ,"Business","Navigation","Medical","Catalogs"]
gen.reverse()
x.reverse()
ay = plt.gca(yticks=y)
ay.set_yticklabels(gen,rotation=0)
plt.barh(y,x)
plt.show()

