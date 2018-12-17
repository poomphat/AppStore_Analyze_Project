import os
import uuid
from pygal import *
bar_chart = Bar()
bar_chart.title = "Better or Worse"


bar_chart.add("Better",1411)
bar_chart.add("Worse",1685)
bar_chart.add("Same",4101)

bar_chart.render_to_file('good or bad.svg')
