import requests
import pandas as pd
import json
import time
import usefulcode
import os


def food_waste_2018_2021():
    year = ['2018', '2019', '2020', '2021']
    month = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
    code = {'W01', 'W02', 'W03', 'W04', 'W05', 'W06', 'W07', 'W08', 'W09', 'W0A', 'W0B', 'W0C', 'W0D', 'W0E', 'W0F',
            'W0G', 'W0H', 'W0I', 'W0J', 'W0K', 'W0L', 'W0M', 'W0N', 'W0P', 'W0Q', 'W0R', 'W0S', 'W0T', 'W0U', 'W0V',
            'W0W', 'W0X', 'W0Y', 'W0Z', 'W10', 'W11', 'W12', 'W13', 'W14', 'W15', 'W16', 'W17', 'W18', 'W19', 'W1A',
            'W1B', 'W1C', 'W1D', 'W1E', 'W1F', 'W1G', 'W1H', 'W1I', 'W1J', 'W1K', 'W1L', 'W1M', 'W1O', 'W1P', 'W1Q',
            'W1R', 'W1S', 'W1T', 'W1U', 'W1V', 'W1W', 'W1X', 'W1Y', 'W1Z', 'W20', 'W21', 'W22', 'W23', 'W24', 'W25',
            'W26', 'W27', 'W28', 'W29', 'W2A', 'W2B', 'W2D', 'W2G', 'W2H', 'W2I', 'W2L', 'W2P', 'W2Q', 'W2R', 'W2S',
            'W2T', 'W2U', 'W2V', 'W2W', 'W2Y', 'W30', 'W31', 'W32', 'W33', 'W34', 'W35', 'W36', 'W37', 'W38', 'W3C',
            'W3D', 'W3E', 'W3F', 'W3G', 'W3H', 'W3I', 'W3J', 'W3K', 'W3L', 'W3N', 'W3O', 'W3Q', 'W3S', 'W3U', 'W42',
            'W44', 'W4C', 'W4H', 'W4N', 'W4O', 'W4Q', 'W4R', 'W4S', 'W4W', 'W4Z', 'W50', 'W51', 'W52', 'W53', 'W54',
            'W55', 'W56', 'W5D', 'W5I', 'W5J', 'W5K', 'W5M', 'W5P', 'W5S', 'W5T', 'W5U', 'W5V', 'W5W', 'W5X', 'W5Z',
            'W61', 'W64', 'W67', 'W68', 'W69', 'W6B', 'W6C', 'W6D', 'W6F', 'W6H', 'W6J', 'W6L', 'W6M', 'W6N', 'W6P',
            'W6Q', 'W6S', 'W6V', 'W6W', 'W6X', 'W6Y', 'W6Z'}

    usefulcode.make_dirs('./Data/Food_waste')

    for y in year:

        for m in month:

            list_df = []
            for c in code:

                try:
                    url = 'http://apis.data.go.kr/B552584/RfidFoodWasteServiceNew/getCityDateList'
                    param = {
                        'serviceKey':
                            'PnDDFfwlwy/ruQHr8wpEN6CJoMvzkuUqorpGhCcvA6a2yajRCSoET2yx4a77oMwDWZ4RtUi1dY55HmVMDle4ig==',
                        'type': 'json', 'disYear': y, 'disMonth': m, 'cityCode': c, 'page': '1', 'rowNum': '1000'}

                    response = requests.get(url, params=param)
                    result = json.loads(response.text)

                except:

                    url = 'http://apis.data.go.kr/B552584/RfidFoodWasteServiceNew/getCityDateList'
                    param = {
                        'serviceKey':
                            'PnDDFfwlwy/ruQHr8wpEN6CJoMvzkuUqorpGhCcvA6a2yajRCSoET2yx4a77oMwDWZ4RtUi1dY55HmVMDle4ig==',
                        'type': 'json', 'disYear': y, 'disMonth': m, 'cityCode': c, 'page': '1', 'rowNum': '1000'}

                    time.sleep(2)
                    response = requests.get(url, params=param)
                    result = json.loads(response.text)

                if result['data']['resultMsg'] == '성공':
                    df = pd.DataFrame(result['data']['list'])

                    list_df.append(df)

            df_month = pd.concat(list_df)
            df_month.to_csv('./Data/Food_waste/Food_waste_' + y + '_' + m + '.csv', encoding='cp949')

    return "저장 성공"


def df_food_waste():
    list_df = []
    file_list = os.listdir('./Data/Food_waste')
    for f in file_list:
        df = pd.read_csv('./Data/Food_waste/' + f, encoding='cp949')
        list_df.append(df)

    df_total = pd.concat(list_df)

    return df_total

