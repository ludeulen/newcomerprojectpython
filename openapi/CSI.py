import requests
import json
import pandas as pd
import usefulcode.code as uc


def CSI():
    uc.make_dirs('./Data/CSI')
    # 서울을 뺀 나머지 지역
    url = "https://ecos.bok.or.kr/api/StatisticSearch/KIPUD3Q933N1288BVJZ8/json/kr/1/99999/511Y004/M/201501/202209/FMCA"
    response = requests.get(url)
    result = json.loads(response.text)

    df = pd.DataFrame(result['StatisticSearch']['row'])
    df.dropna(axis=1, inplace=True)
    df['ID'] = df['TIME'] + df['ITEM_NAME2']

    url = "https://ecos.bok.or.kr/api/StatisticSearch/KIPUD3Q933N1288BVJZ8/json/kr/1/99999/511Y004/M/201501/202209/FMCB"
    response = requests.get(url)

    result = json.loads(response.text)
    df1 = pd.DataFrame(result['StatisticSearch']['row'])

    # 칼럼 정리
    df1.dropna(axis=1, inplace=True)
    df1['ID'] = df1['TIME'] + df1['ITEM_NAME2']
    df1.drop(['STAT_CODE', 'STAT_NAME', 'ITEM_CODE2', 'ITEM_NAME2', 'TIME'], axis=1, inplace=True)
    df1.columns = ['ITEM_CODE3', 'ITEM_NAME3', 'DATA_VALUE2', 'ID']
    df_csi = pd.merge(df, df1, how='left', on='ID')

    # 지역 서울
    url = "https://ecos.bok.or.kr/api/StatisticSearch/KIPUD3Q933N1288BVJZ8/json/kr/1/99999/511Y002/M/201501/202209/FMCA/F0001"
    response = requests.get(url)
    result = json.loads(response.text)

    df2 = pd.DataFrame(result['StatisticSearch']['row'])
    df2.dropna(axis=1, inplace=True)
    df2['ID'] = df2['TIME'] + df2['ITEM_NAME2']

    url = "https://ecos.bok.or.kr/api/StatisticSearch/KIPUD3Q933N1288BVJZ8/json/kr/1/99999/511Y002/M/201501/202209/FMCB/F0001"
    response = requests.get(url)

    result = json.loads(response.text)
    df3 = pd.DataFrame(result['StatisticSearch']['row'])

    # 칼럼정리
    df3.dropna(axis=1, inplace=True)
    df3['ID'] = df3['TIME'] + df3['ITEM_NAME2']
    df3.drop(['STAT_CODE', 'STAT_NAME', 'ITEM_CODE2', 'ITEM_NAME2', 'TIME'], axis=1, inplace=True)
    df3.columns = ['ITEM_CODE3', 'ITEM_NAME3', 'DATA_VALUE2', 'ID']

    # 두 df 합치기
    df_csi_seoul = pd.merge(df2, df3, how='left', on='ID')
    df_csi_total = pd.concat([df_csi, df_csi_seoul])

    df_csi_total.drop(
        ['STAT_CODE', 'STAT_NAME', 'ITEM_NAME1', 'ITEM_CODE1', 'ITEM_CODE2', 'ITEM_NAME3', 'ITEM_CODE3', 'ID'], axis=1,
        inplace=True)

    # 칼럼 이름 바꾸기(Household_Income_Outlook_CSI : 가계수입전망CSI, Consumer_Spending_Outlook_CSI : 소비지출전망CSI
    df_csi_total = df_csi_total[['TIME', 'ITEM_NAME2', 'DATA_VALUE', 'DATA_VALUE2']]
    df_csi_total.columns = ['TIME', 'AREA', 'Household_Income_Outlook_CSI', 'Consumer_Spending_Outlook_CSI']

    df1 = df_csi_total[df_csi_total['AREA'] == '대구경북']
    df2 = df_csi_total[df_csi_total['AREA'] == '광주전남']
    df3 = df_csi_total[df_csi_total['AREA'] == '대전충남']

    area = {'AREA': {'부산': '부산광역시', '대구경북': '경상북도', '인천': '인천광역시', '광주전남': '전라남도', '대전충남': '충청남도',
                     '울산': '울산광역시', '경기': '경기도', '강원': '강원도', '충북': '충청북도', '전북': '전라북도', '경남': '경상남도',
                     '제주': '제주특별자치도', '서울': '서울특별시'}}

    df_csi_total.replace(area, inplace=True)
    df1.replace({'대구경북': '대구광역시'}, inplace=True)
    df2.replace({'광주전남': '광주광역시'}, inplace=True)
    df3.replace({'대전충남': '대전광역시'}, inplace=True)
    df_csi_total = pd.concat([df_csi_total, df1, df2, df3])

    df_csi_total.reset_index(inplace=True)
    df_csi_total.drop('index', axis=1, inplace=True)

    df_csi_total.to_csv('./Data/CSI/CSI.csv', encoding='cp949')

    return "저장 완료"


def df_CSI():

    df = pd.read_csv('./Data/CSI/CSI.csv', encoding='cp949')
    return df
