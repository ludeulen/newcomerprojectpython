import plotly.express as px
import pandas as pd


def food_data_preprocessing(df):
    df_graph = df.drop(
        ['cityCode', 'disQuantityRate', 'disCount', 'disCountRate'],
        axis=1)
    df_graph = df_graph.astype(str)
    df_graph['disQuantity'] = df_graph['disQuantity'].astype(float)
    df_graph['disQuantity'] = df_graph['disQuantity'] / 1000000
    df_graph['disMonth'] = df_graph['disMonth'].str.zfill(2)
    df_graph['disDate'] = df_graph['disDate'].str.zfill(2)
    df_graph['disDate'] = df_graph['disYear'] + '-' + df_graph['disMonth'] + '-' + df_graph['disDate']
    df_graph.drop(['disYear', 'disMonth'], axis=1, inplace=True)
    df_graph['disDate'] = pd.to_datetime(df_graph['disDate'])
    df_graph['disDate'] = df_graph['disDate'].dt.strftime('%Y-%m')
    data = pd.pivot_table(df_graph, index='disDate', columns='citySidoName', values='disQuantity', aggfunc='sum')

    return data