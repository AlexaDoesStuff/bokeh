from bokeh.io import show, output_file
from bokeh.models import ColumnDataSource, Legend
from bokeh.palettes import Category20b_17
from bokeh.plotting import figure
import pandas as pd
import numpy as np

#pageViews = pd.DataFrame(pd.read_csv('./Webscrape/0816CountryView.csv'), names = ['By country', 'Page views per minute'])

colnames = ['Bycountry', 'Pageviewsper']
pageViews = pd.read_csv('./Webscrape/0816CountryView.csv', names=colnames)

country = pageViews.Bycountry.tolist()
ppm = pageViews.Pageviewsper.tolist()
#print(country)
#print(ppm)

source = ColumnDataSource(data=dict(country=country, ppm=ppm, color=Category20b_17))

p = figure(x_range=country, y_range=(0, 0.02), plot_height=350, title="Page views per Minute by Country",
           toolbar_location=None, tools="")

p.vbar(x='country', top='ppm', width=0.8, color='color', source=source)

p.xgrid.grid_line_color = None
#Sorry I'm hard coding everything, last day of internship calls for brute force!!!!!
x = np.linspace(0, 4*np.pi, 100)
y = np.sin(x)

r0 = p.square(x, 3*y, fill_color=Category20b_17[0], line_color=None)
r1 = p.square(x, 3*y, fill_color=Category20b_17[1], line_color=None)
r2 = p.square(x, 3*y, fill_color=Category20b_17[2], line_color=None)
r3 = p.square(x, 3*y, fill_color=Category20b_17[3], line_color=None)
r4 = p.square(x, 3*y, fill_color=Category20b_17[4], line_color=None)
r5 = p.square(x, 3*y, fill_color=Category20b_17[5], line_color=None)
r6 = p.square(x, 3*y, fill_color=Category20b_17[6], line_color=None)
r7 = p.square(x, 3*y, fill_color=Category20b_17[7], line_color=None)
r8 = p.square(x, 3*y, fill_color=Category20b_17[8], line_color=None)
r9 = p.square(x, 3*y, fill_color=Category20b_17[9], line_color=None)
r10 = p.square(x, 3*y, fill_color=Category20b_17[10], line_color=None)
r11 = p.square(x, 3*y, fill_color=Category20b_17[11], line_color=None)
r12 = p.square(x, 3*y, fill_color=Category20b_17[12], line_color=None)
r13 = p.square(x, 3*y, fill_color=Category20b_17[13], line_color=None)
r14 = p.square(x, 3*y, fill_color=Category20b_17[14], line_color=None)
r15 = p.square(x, 3*y, fill_color=Category20b_17[15], line_color=None)
r16 = p.square(x, 3*y, fill_color=Category20b_17[16], line_color=None)

legend = Legend(items=[
    ("Great Britain"   , [r0]),
    ("United States"   , [r1]),
    ("Ireland"   , [r2]),
    ("Denmark"   , [r3]),
    ("Austria"   , [r4]),
    ("Brazil"   , [r5]),
    ("Slovakia"   , [r6]),
    ("Hungary"   , [r7]),
    ("Russia"   , [r8]),
    ("Netherlands"   , [r9]),
    ("Venezuela"   , [r10]),
    ("Chile"   , [r11]),
    ("China"   , [r12]),
    ("Spain"   , [r13]),
    ("Japan"   , [r14]),
    ("Malaysia"   , [r15]),
    ("Sweden"   , [r16]),
], location=(0, -28), label_text_font_size='8pt', spacing=0)

#countryFull = ["Great Britain", "United States", "Ireland", "Denmark", "Austria", "Brazil", "Slovakia", "Hungary"
#              "Hungary", "Russia", "Netherlands", "Chile", "China", "Spain", "Japan", "Malaysia", "Sweden"]

p.add_layout(legend, 'right')

output_file("PageViews.html")
show(p)
