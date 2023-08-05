import logging
import plotly.express as px
import solara

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s.%(msecs)03d %(levelname)s:\t%(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    force=True,
)

df = px.data.iris()

@solara.component
def Plot(grps):
    plot_data = df[df.species.isin(grps)].copy()
    fig = px.scatter(plot_data, x="sepal_width", y="sepal_length", color="species")
    logging.info(f"-")
    return solara.FigurePlotly(fig)

@solara.component
def Page():

    all_grps = ["setosa", "veriscolor", "virginica"]
    selected_groups = solara.use_reactive(all_grps)

    with solara.Column(margin=20):
        solara.Markdown("## Groups to Include")
        solara.SelectMultiple(
            label="Groups to Include",
            values=selected_groups,
            all_values=all_grps,
            style={"max-width": "400px"},
        )

    solara.Markdown("## A Few I would like to render immediately so user gets immediate feedback")
    with solara.Column(margin=20):
        with solara.Row():
            with solara.Columns([1, 1, 1, 1]):
                Plot(selected_groups.value)
                Plot(selected_groups.value)
                Plot(selected_groups.value)

        solara.Markdown("## Lots More Graphs that can render while the user is distracted with the above")
        for i in range(50):
            with solara.Row():
                with solara.Columns([1, 1, 1, 1]):
                    Plot(selected_groups.value)
                    Plot(selected_groups.value)
                    Plot(selected_groups.value)

