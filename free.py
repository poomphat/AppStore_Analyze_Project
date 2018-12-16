import os
import uuid
from pygal import *
bar_chart = Bar()
bar_chart.title = "Free & Not free"

bar_chart.add("Free",4056)
bar_chart.add("Not free",3141)


bar_chart.render_to_file('free.svg')
