from flask import Flask
import usefulcode.code as uc
import openapi.Food_waste as of
import openapi.CSI as oc

app = Flask(__name__)


@app.route('/')
def home():
    return 'Hello, World!'


@app.route('/update')
def update():
    uc.waiting_time()
    return 'null'

@app.route('/of20182021')
def openapi_food_2018_2021():
    of.food_waste_2018_2021()
    return '저장 완료'

@app.route('/of2022')
def openapi_food_2022():
    of.food_waste_2022()
    return '저장 완료'

@app.route('/CSI')
def openapi_CSI():
    oc.CSI()
    return '저장완료'

if __name__ == '__main__':
    app.run(port=8000)
