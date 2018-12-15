import os
import uuid
from pygal import *
bar_chart = HorizontalBar()
bar_chart.title = "Rate 3"

bar_chart.add("Games",1007)
bar_chart.add("Entertainment",188)
bar_chart.add("Education",139)
bar_chart.add("Photo & Video",98)
bar_chart.add("Utilities",81)
bar_chart.add("Health & Fitness",47)
bar_chart.add("Productivity",48)
bar_chart.add("Social Networking",61)
bar_chart.add("Lifestyle",36)
bar_chart.add("Music",48)
bar_chart.add("Shoping",0)
bar_chart.add("Sports",40)
bar_chart.add("Book",20)
bar_chart.add("Finance",35)
bar_chart.add("Travel",20)
bar_chart.add("News",28)
bar_chart.add("Weather",28)
bar_chart.add("Reference",14)
bar_chart.add("Food & Drink",19)
bar_chart.add("Business",18)
bar_chart.add("Navigation",15)
bar_chart.add("Medical",7)
bar_chart.add("Catalogs",3)

bar_chart.render_to_file('30.svg')
