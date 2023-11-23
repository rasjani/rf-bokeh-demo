from robot.api import logger
import numpy as np
from bokeh.plotting import figure, show
import bokeh


def log_figure(fig):
    script, div = bokeh.embed.components(fig)

    # Get Rid of the script tags
    script = script.replace('<script type="text/javascript">','')
    script = script.replace('</script>','')

    # Where to load the bokeh
    url = "https://cdn.bokeh.org/bokeh/release/bokeh-3.3.1.min.js"
    # use jquery getScript to get a callback once bokeh is loaded and then
    # run the script from bokeh.embed.components
    force_load_bokeh = f"$.getScript('{url}', function(){{{script}}});"
    logger.info(f'<script type="text/javascript">{force_load_bokeh}</script>{div}', html=True)


def generate_figure():
    N = 4000
    x = np.random.random(size=N) * 100
    y = np.random.random(size=N) * 100
    radii = np.random.random(size=N) * 1.5
    colors = np.array([(r, g, 150) for r, g in zip(50+2*x, 30+2*y)], dtype="uint8")

    TOOLS="hover,crosshair,pan,wheel_zoom,zoom_in,zoom_out,box_zoom,undo,redo,reset,tap,save,box_select,poly_select,lasso_select,examine,help"

    p = figure(tools=TOOLS)

    p.scatter(x, y, radius=radii,
            fill_color=colors, fill_alpha=0.6,
            line_color=None)
    return p
