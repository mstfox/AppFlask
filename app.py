from flask import Flask , render_template , jsonify

app = Flask(__name__)
JOBS = [
    {'id': 1,
     'title' : 'Data Analyst',
     'location' : 'Tehran',
     'salary': '$120,000'},
    {'id': 2,
     'title' : 'Data Scientist',
     'location' : 'Yazd',
     'salary': '$130,000'},    
    {'id': 3,
     'title' : 'Financial Analyst',
     'location' : 'Tabriz',
     'salary': '$140,000'},
    {'id': 4,
     'title' : 'Administrator',
     'location' : 'Remote',
     'salary': '$150,000'},
]
@app.route('/')
def hello_world():
    return render_template('home.html' , jobs =JOBS)

@app.route('/jobs')
def Jason_():
    return jsonify(JOBS)

if __name__ == '__main__':
    app.run(host= '0.0.0.0', debug=True)
