from flask import Flask, render_template
from monitoring.test_monitoring import *

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/monitorings')
def monitorings():
    return render_template('monitorings.html')


@app.route('/monitorings/new_draft', methods=['GET', 'POST'])
def new_monitoring():
    monitoring_info = Monitoring.draft_monitoring()
    print(type(monitoring_info))
    return monitoring_info

if __name__ == '__main__':
    app.run(debug=True)
