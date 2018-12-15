import numpy as np
import matplotlib.pyplot as plt
y = np.arange(1,24)
x = [301,68,70,29,33,12,16,26,10,17,0,22,4,14,9,14,11,7,9,4,8,3,1]
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

