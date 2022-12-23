import json
import pandas as pd
import requests


def consumer_spending():
    url = 'https://kosis.kr/openapi/Param/statisticsParameterData.do?method=getList&apiKey=MTc0MDVmNDdhNTYyOWQ1MWU0NTYzYmNhOWQ3ODEyMGQ=&itmId=T1+T2+T3+T4+&objL1=ALL&objL2=&objL3=&objL4=&objL5=&objL6=&objL7=&objL8=&format=json&jsonVD=Y&prdSe=Y&newEstPrdCnt=10&orgId=101&tblId=DT_1C86'

    response = requests.get(url)
    result = json.loads(response.text)

    df = pd.DataFrame(result)

    df.drop(
        ['TBL_NM', 'TBL_ID', 'ITM_NM_ENG', 'ORG_ID', 'ITM_ID', 'ORG_ID', 'UNIT_NM_ENG', 'C1_OBJ_NM', 'C1_OBJ_NM_ENG',
         'PRD_SE', 'C1_NM_ENG', 'UNIT_NM', 'C1'], axis=1, inplace=True)

    df['DT'] = df['DT'] + '000'
    df = df[df['ITM_NM'] == '1인당 민간소비']
    df.drop('ITM_NM', axis=1, inplace=True)
    df.reset_index(inplace=True)
    df.drop('index', axis=1, inplace=True)
    return df
