import numpy as np
import plotly.graph_objects as go
import plotly.io as pio

from pyroll.core import Unit, RollPass
from pyroll.report import hookimpl


@hookimpl(specname="unit_plot")
def roll_pass_pillars_flow_stress_(unit: Unit):
    if isinstance(unit, RollPass) and unit.disk_elements:
        rp: RollPass = unit
        x = np.array([np.ones_like(de.out_profile.pillars) * de.out_profile.x for de in rp.disk_elements])
        y = np.array([de.out_profile.pillars for de in rp.disk_elements])
        z = np.array([de.out_profile.pillars_flow_stress for de in rp.disk_elements])

        fig = go.Figure(data=[go.Surface(z=z, x=x, y=y)])
        fig.update_layout(title='Workpiece Flow Stress Profile')
        fig.update_layout(
            scene=dict(
                xaxis=dict(title='Contact Length', gridcolor='rgb(200, 200, 200)', showgrid=True),
                yaxis=dict(title='Profile Width', gridcolor='rgb(200, 200, 200)', showgrid=True),
                zaxis=dict(title='Flow Stress', gridcolor='rgb(200, 200, 200)', showgrid=True),
            ),
            title='Workpiece Flow Stress Profile',
            width=1200,
            height=800,
            template='simple_white'
        )

        html_string = pio.to_html(fig, full_html=False, include_plotlyjs='cdn')

        return html_string
