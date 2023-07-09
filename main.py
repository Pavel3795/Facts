from random import choice
import random
from flask import Flask

app = Flask(__name__)

facts_list = ['Один из способов борьбы с технологической зависимостью - это поиск занятий, которые приносят удовольствие и улучшают настроение.']
['Изучение технологической зависимости является одной из наиболее актуальных областей научных исследований в настоящее время.']

@app.route("/")
def hello_world():
    return f'<p>{random.choice(facts_list)}</p>'


app.run(debug=True)