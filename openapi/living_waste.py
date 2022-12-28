import requests
import pandas as pd
import json
import usefulcode


# 칼럼 값은 아래 링크 참고
# https://www.recycling-info.or.kr/statDoc/%ED%8F%90%EA%B8%B0%EB%AC%BC%ED%86%B5%EA%B3%84_OpenAPI%ED%99%9C%EC%9A%A9%EA%B0%80%EC%9D%B4%EB%93%9C.pdf

def living_waste_2014_2018():

    usefulcode.make_dirs('./Data/living_waste')

    year = ['2014', '2015', '2016', '2017', '2018']
    for y in year:
        url = "http://www.recycling-info.or.kr/sds/JsonApi.do?PID=NTN003&YEAR=" + y + "&USRID=kriem546&KEY=OIZF6LPJKYIUCWX2CEKO05O1RX1N46OX8VL95HHDO5ABE"
        response = requests.get(url)
        result = json.loads(response.text)

        data = result['data']
        df = pd.DataFrame(data)
        df['처리년도'] = y
        df.to_csv('./Data/living_waste/living_waste_' + y + '.csv', encoding='cp949')

    return '저장 완료'


def living_waste2019():

    usefulcode.make_dirs('./Data/living_waste')

    url = "http://www.recycling-info.or.kr/sds/JsonApi.do?PID=NTN006&YEAR=2019&USRID=kriem546&KEY=OIZF6LPJKYIUCWX2CEKO05O1RX1N46OX8VL95HHDO5ABE"
    response = requests.get(url)
    result = json.loads(response.text)

    data = result['data']
    df = pd.DataFrame(data)
    df['처리년도'] = '2019'

    df['WT_TYPE_GB_NM'] = df['WT_TYPE_GB_NM'] + '/' + df['WSTE_M_CODE_NM'] + '/' + df['WSTE_CODE_NM']
    df.drop(['WSTE_M_CODE_NM', 'WSTE_CODE_NM'], axis=1, inplace=True)

    df.replace(['\r', 'EMPTY'], '', inplace=True, regex=True)
    df.replace('//', '', inplace=True, regex=True)

    df.to_csv('./Data/living_waste/living_waste_2019.csv', encoding='cp949')

    return '저장 완료'


def living_waste2020():

    usefulcode.make_dirs('./Data/living_waste')

    url = "http://www.recycling-info.or.kr/sds/JsonApi.do?PID=NTN007&YEAR=2020&USRID=kriem546&KEY=OIZF6LPJKYIUCWX2CEKO05O1RX1N46OX8VL95HHDO5ABE"
    response = requests.get(url)
    result = json.loads(response.text)

    data = result['data']
    df = pd.DataFrame(data)
    df['처리년도'] = '2020'

    df['WT_TYPE_GB_NM'] = df['WT_TYPE_GB_NM'] + '/' + df['WSTE_M_CODE_NM'] + '/' + df['WSTE_CODE_NM']
    df.drop(['WSTE_M_CODE_NM', 'WSTE_CODE_NM'], axis=1, inplace=True)

    df.replace(['\r', 'EMPTY'], '', inplace=True, regex=True)
    df.replace('//', '', inplace=True, regex=True)

    df.to_csv('./Data/living_waste/living_waste_2020.csv', encoding='cp949')

    return '저장 완료'
