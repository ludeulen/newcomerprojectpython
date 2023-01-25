import dash
from dash import dcc
from dash import html
import plotly.express as px
import openapi.Food_waste as of
import graph.food_graph as gf

app = dash.Dash(__name__)

df = of.df_food_waste()
data = gf.food_data_preprocessing(df)

fig = px.line(data, title="배출량 : 월/톤")

app.layout = html.Div(
    children=[
        html.H1(children='음식물 폐기물'),
        html.Div(
            children='''
        지역마다 다른선을 사용
    '''
        ),
        dcc.Graph(id='example-graph', figure=fig),
    ]
)

if __name__ == '__main__':
    app.run_server(debug=True, port=8010)
