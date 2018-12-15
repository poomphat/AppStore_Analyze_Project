import numpy as np
import matplotlib.pyplot as plt
y = np.arange(1,24)
x = [1007,188,139,98,81,47,48,61,36,48,0,40,20,35,20,28,28,14,19,18,15,7,3]
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

