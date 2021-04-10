import sirpy
import plotly.graph_objects as go

fig = sirpy.get_graph(
        days=1000,
        size=1000, 
        initial_infections=3, 
        contact_mean=0.267, 
        transmission_chance=0.015, 
        transmission_window=14, 
        recovery_period=30, 
        death_rate=0.02
        )

fig.write_html('first_figure.html', auto_open=True)
