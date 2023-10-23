## Flask App Routing

from flask import Flask,render_template,request,redirect,url_for

## Create a simple flask application
app = Flask(__name__)

@app.route('/', methods=['GET'])
def welcome():
    return '<h1>Welcome To My Page</h1>'

@app.route('/index', methods=['GET'])
def index():
    return '<h2>Welcome To The Index Page</h2>'

## Variable Rule 
@app.route('/success/<int:score>')
def success(score):
    return 'The Person Has Passed And the Score Is: '+ str(score)

@app.route('/fail/<int:score>', methods=['GET'])
def fail(score):
    return 'The Person Has Failed With Marks: '+ str(score)

@app.route('/form', methods=['GET','POST'])
def form():
    if request.method == 'GET':
        return render_template('form.html')

    else:
        maths=float(request.form['maths'])
        science=float(request.form['science'])
        history=float(request.form['history'])

        avg_marks = (maths+science+history)/3
        res= ""

        # if avg_marks >= 50:
        #     res='success'

        # else:
        #     res='fail'

        # return redirect(url_for(res, score = avg_marks))
        return render_template('form.html', score = avg_marks)

if __name__ == '__main__':
    app.run(debug=True)
