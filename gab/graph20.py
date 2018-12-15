import numpy as np
import matplotlib.pyplot as plt
y = np.arange(1,24)
x = [577,120,114,91,72,43,48,30,36,31,0,33,14,21,25,19,14,8,19,15,7,2,2]
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



