import SirPy
import numpy as np

#import plotly.graph_objects as go

import plotly.graph_objects as go

pop = SirPy.Population(10000) 
data = pop.update_n_days(365)

days = range(1, len(data)+1)

Sus = np.array([day[0] for day in data])
Inf = np.array([day[1] for day in data])
Rec = np.array([day[2] for day in data])
Dea = np.array([day[3] for day in data])

fig = go.Figure(data=go.Bar(y=Rec))
fig.write_html('first_figure.html', auto_open=True)
