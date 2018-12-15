import os
import uuid
from pygal import *
bar_chart = HorizontalBar()
bar_chart.title = "Rate 3.5"

bar_chart.add("Games",301)
bar_chart.add("Entertainment",68)
bar_chart.add("Education",70)
bar_chart.add("Photo & Video",29)
bar_chart.add("Utilities",33)
bar_chart.add("Health & Fitness",12)
bar_chart.add("Productivity",16)
bar_chart.add("Social Networking",26)
bar_chart.add("Lifestyle",10)
bar_chart.add("Music",17)
bar_chart.add("Shoping",0)
bar_chart.add("Sports",22)
bar_chart.add("Book",4)
bar_chart.add("Finance",14)
bar_chart.add("Travel",9)
bar_chart.add("News",14)
bar_chart.add("Weather",11)
bar_chart.add("Reference",7)
bar_chart.add("Food & Drink",9)
bar_chart.add("Business",4)
bar_chart.add("Navigation",8)
bar_chart.add("Medical",3)
bar_chart.add("Catalogs",1)

bar_chart.render_to_file('35.svg')
