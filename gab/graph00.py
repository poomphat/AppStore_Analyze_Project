import numpy as np
import matplotlib.pyplot as plt
y = np.arange(1,24)
x = [463,64,66,24,29,21,6,33,31,4,0,13,47,33,10,15,6,11,11,4,15,3,5]
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



