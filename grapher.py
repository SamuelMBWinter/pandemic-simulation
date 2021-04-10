import SirPy
import numpy as np
import plotly.graph_objects as go

def get_graph(N=1000, days=100):

    pop = SirPy.Population(N) 
    data = pop.update_n_days(days)

    days = range(1, len(data)+1)

    Sus = np.array([day[0] for day in data])
    Inf = np.array([day[1] for day in data])
    Rec = np.array([day[2] for day in data])
    Dea = np.array([day[3] for day in data])

    fig = go.Figure(data=go.Bar(y=Rec))
    
    return fig
