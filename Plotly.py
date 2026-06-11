import plotly.graph_objects as go

spectrum = spec[3]

fig = go.Figure()

fig.add_trace(go.Scatter(
    x=spectrum.spectral_axis.value,
    y=spectrum.flux.value,
    mode='lines',
    name='Spectrum'
))

fig.update_layout(
    width=700,
    height=300,
    margin=dict(l=40, r=40, t=40, b=40),
    xaxis_title=f"Spectral Axis ({spectrum.spectral_axis.unit})",
    yaxis_title=f"Flux Axis ({spectrum.flux.unit})",
    xaxis=dict(showgrid=True),
    yaxis=dict(showgrid=True),
)

fig.show()
