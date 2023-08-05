import plotly.express as px
import solara

df = px.data.iris()


@solara.component
def PlotGroup(grps):
    plot_data = df[df.species.isin(grps)].copy()
    with solara.Columns([1, 1, 1, 1]):
        solara.FigurePlotly(px.scatter(plot_data, x="sepal_width", y="sepal_length", color="species"))
        solara.FigurePlotly(px.scatter(plot_data, x="sepal_width", y="sepal_length", color="species"))
        solara.FigurePlotly(px.scatter(plot_data, x="sepal_width", y="sepal_length", color="species"))


@solara.component
def PlotGroup1(grps):
    solara.Markdown("## A Few Plots I would like to render immediately so the user gets immediate feedback:")
    solara.Markdown(f"selected_groups 1: {grps}")
    with solara.Row():
        with solara.Columns([1, 1, 1, 1]):
            PlotGroup(grps)


@solara.component
def PlotGroup2(grps):
    solara.Markdown("## Lots More Plots that can render while the user is distracted with the above")
    solara.Markdown(f"selected_groups 1: {grps}")
    for i in range(30):
        with solara.Row():
            with solara.Columns([1, 1, 1, 1]):
                PlotGroup(grps)


@solara.component
def Page():

    all_grps = ["setosa", "versicolor", "virginica"]
    selected_groups = solara.use_reactive(all_grps)

    with solara.Div(style={"margin": "20px"}):
        with solara.Column(margin=20):
            solara.Markdown("## Groups to Include")
            solara.SelectMultiple(
                label="Groups to Include",
                values=selected_groups,
                all_values=all_grps,
                style={"max-width": "400px"},
            )
        ## I want to render these immediately
        PlotGroup1(selected_groups.value)

        ## no rush on these
        PlotGroup2(selected_groups.value)
