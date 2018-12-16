import os
import uuid
from pygal import *
bar_chart = HorizontalBar()
bar_chart.title = "Rate 3.5"

bar_chart.add("Games",368)
bar_chart.add("Entertainment",48)
bar_chart.add("Education",52)
bar_chart.add("Photo & Video",36)
bar_chart.add("Utilities",18)
bar_chart.add("Health & Fitness",19)
bar_chart.add("Productivity",15)
bar_chart.add("Social Networking",18)
bar_chart.add("Lifestyle",19)
bar_chart.add("Music",16)
bar_chart.add("Shoping",0)
bar_chart.add("Sports",11)
bar_chart.add("Book",12)
bar_chart.add("Finance",7)
bar_chart.add("Travel",9)
bar_chart.add("News",9)
bar_chart.add("Weather",10)
bar_chart.add("Reference",3)
bar_chart.add("Food & Drink",5)
bar_chart.add("Business",4)
bar_chart.add("Navigation",7)
bar_chart.add("Medical",1)
bar_chart.add("Catalogs",0)

bar_chart.render_to_file('35.svg')
