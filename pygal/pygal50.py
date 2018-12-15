import os
import uuid
from pygal import *
bar_chart = HorizontalBar()
bar_chart.title = "Rate 5"

bar_chart.add("Games",937)
bar_chart.add("Entertainment",111)
bar_chart.add("Education",65)
bar_chart.add("Photo & Video",52)
bar_chart.add("Utilities",45)
bar_chart.add("Health & Fitness",38)
bar_chart.add("Productivity",23)
bar_chart.add("Social Networking",35)
bar_chart.add("Lifestyle",30)
bar_chart.add("Music",16)
bar_chart.add("Shoping",0)
bar_chart.add("Sports",17)
bar_chart.add("Book",38)
bar_chart.add("Finance",20)
bar_chart.add("Travel",12)
bar_chart.add("News",11)
bar_chart.add("Weather",8)
bar_chart.add("Reference",16)
bar_chart.add("Food & Drink",13)
bar_chart.add("Business",11)
bar_chart.add("Navigation",5)
bar_chart.add("Medical",4)
bar_chart.add("Catalogs",2)

bar_chart.render_to_file('50.svg')
