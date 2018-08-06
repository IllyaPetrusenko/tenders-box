from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from monitoring.test_monitoring import *
from flask import request


app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/base')
def base():
    return render_template('base.html')

@app.route('/monitorings')
def monitorings():
    return render_template('monitorings.html')


@app.route('/monitorings/new_draft', methods=['GET', 'POST'])
def new_monitoring():
    tender_id = request.form['input-info-block']
    monitoring_info = Monitoring.draft_monitoring()
    print(type(monitoring_info))
    return monitoring_info

if __name__ == '__main__':
    app.run(debug=True)
