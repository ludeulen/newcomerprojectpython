import numpy as np
import pandas as pd


def Food_CSI_proprocessing(df, df1):
    df = df.astype(str)

    df['disMonth'] = df['disMonth'].str.zfill(2)
    df['disDate'] = df['disDate'].str.zfill(2)

    df = df.drop('Unnamed: 0', axis=1)
    df['ID'] = df['disYear'] + df['disMonth'] + df['citySidoName']

    df_m = pd.merge(df, df1, how='left', on='ID')
    df_m.drop(['TIME', 'AREA', 'ID'], axis=1, inplace=True)
    df_m['disQuantity'] = df_m['disQuantity'].astype(int)
    df_m['disMonth'] = df_m['disMonth'].astype(int)

    list_disDay = []
    for i in df_m['disDay']:
        if i == '1':
            list_disDay.append('일')
        elif i == '2':
            list_disDay.append('월')
        elif i == '3':
            list_disDay.append('화')
        elif i == '4':
            list_disDay.append('수')
        elif i == '5':
            list_disDay.append('목')
        elif i == '6':
            list_disDay.append('금')
        elif i == '7':
            list_disDay.append('토')
    df_m['disDay'] = list_disDay
    df_m['sin_Month'] = np.sin(2 * np.pi * df_m['disMonth'] / 12)

    return df_m

def fw_region(df):
    df_seoul = df[df['citySidoName'] == '서울특별시']
    df_gyeonggi = df[(df['citySidoName'] == '경기도') | (df['citySidoName'] == '인천광역시')]
    df_gyeongsangnamdo = df[
        (df['citySidoName'] == '경상남도') | (df['citySidoName'] == '부산광역시') | (df['citySidoName'] == '울산광역시')]
    df_gyeongsangbukdo = df[(df['citySidoName'] == '경상북도') | (df['citySidoName'] == '대구광역시')]
    df_gangwondo = df[df['citySidoName'] == '강원도']
    df_chungcheongdo = df[
        (df['citySidoName'] == '충청북도') | (df['citySidoName'] == '충청남도') | (df['citySidoName'] == '대전광역시')]
    df_jeollado = df[
        (df['citySidoName'] == '전라북도') | (df['citySidoName'] == '전라남도') | (df['citySidoName'] == '광주광역시')]
    df_jeju = df[df['citySidoName'] == '제주특별자치도']


