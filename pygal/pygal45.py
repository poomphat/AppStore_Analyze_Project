import os
import uuid
from pygal import *
bar_chart = HorizontalBar()
bar_chart.title = "Rate 4.5"

bar_chart.add("Games",1385)
bar_chart.add("Entertainment",193)
bar_chart.add("Education",184)
bar_chart.add("Photo & Video",151)
bar_chart.add("Utilities",101)
bar_chart.add("Health & Fitness",66)
bar_chart.add("Productivity",69)
bar_chart.add("Social Networking",54)
bar_chart.add("Lifestyle",51)
bar_chart.add("Music",48)
bar_chart.add("Shoping",0)
bar_chart.add("Sports",43)
bar_chart.add("Book",39)
bar_chart.add("Finance",42)
bar_chart.add("Travel",33)
bar_chart.add("News",28)
bar_chart.add("Weather",23)
bar_chart.add("Reference",22)
bar_chart.add("Food & Drink",30)
bar_chart.add("Business",16)
bar_chart.add("Navigation",19)
bar_chart.add("Medical",9)
bar_chart.add("Catalogs",5)

bar_chart.render_to_file('45.svg')
