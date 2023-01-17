from flask import Flask
import usefulcode.code as uc
import openapi.Food_waste as of
import openapi.living_waste as ol
import openapi.CSI as oc
import usefulcode.mysql as um

app = Flask(__name__)


@app.route('/')
def home():
    return 'Hello, World!'


@app.route('/update')
def sql_update():
    fw = of.df_food_waste()
    lw = ol.df_living_waste()
    CSI = oc.df_CSI()
    um.update(fw, 'food_waste')
    um.update(lw, 'living_waste')
    um.update(CSI, 'CSI')
    return '전송완료'


@app.route('/api_ol')
def openapi_living_waste():
    ol.living_waste_2014_2018()
    ol.living_waste2019()
    ol.living_waste2020()
    return '저장 완료'


@app.route('/api_csi')
def openapi_CSI():
    oc.CSI()
    return '저장완료'


if __name__ == '__main__':
    app.run(port=8000)
