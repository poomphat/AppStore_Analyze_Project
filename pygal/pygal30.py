import os
import uuid
from pygal import *
bar_chart = HorizontalBar()
bar_chart.title = "Rate 3.0"

bar_chart.add("Games",201)
bar_chart.add("Entertainment",32)
bar_chart.add("Education",26)
bar_chart.add("Photo & Video",19)
bar_chart.add("Utilities",12)
bar_chart.add("Health & Fitness",13)
bar_chart.add("Productivity",11)
bar_chart.add("Social Networking",9)
bar_chart.add("Lifestyle",6)
bar_chart.add("Music",5)
bar_chart.add("Shoping",0)
bar_chart.add("Sports",1)
bar_chart.add("Book",2)
bar_chart.add("Finance",4)
bar_chart.add("Travel",5)
bar_chart.add("News",2)
bar_chart.add("Weather",7)
bar_chart.add("Reference",2)
bar_chart.add("Food & Drink",2)
bar_chart.add("Business",1)
bar_chart.add("Navigation",3)
bar_chart.add("Medical",3)
bar_chart.add("Catalogs",2)

bar_chart.render_to_file('30.svg')
