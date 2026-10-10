import quantcraft.process.runtime as rt

def plot_line(symbol, name, values, pane=None, style="solid"):
    points = [
        {
            "time": t,
            "value": v
        } for t, v in values if t is not None and v is not None
    ]
    rt.chart_indicators.add(points, pane="separate" if pane else "main", render="line",
                           line_style=style, id=f"{name}_{symbol}", name=name,
                           symbol=symbol, pane_id=pane)
    