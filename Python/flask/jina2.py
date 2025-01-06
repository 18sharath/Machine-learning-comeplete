# it helps to any information from the form it will take into any html template
# building URL dynamically
# variable Rule
# jinja 2 template engine

'''
{{...}} is used to print output in htmml

{%...%} used to for conditions , for loops

{#...#} used to commenting
'''

from flask import Flask,render_template,request
'''
It create a instance of class flask ,
which will be our WSGI application
'''

app=Flask(__name__)
'''
___name__ is the entry for python and  it will run from that (entry point )
'''
@app.route("/")
def welcome():
    return "<html><h1>Welcome to this course flask123</h1></html>"

@app.route("/index",methods=['GET'])
def index():
    return render_template("index.html")


@app.route('/submit',methods=['GET','POST'])
def submit():
    if request.method=='POST':
        name=request.form['lname']
        return f'hello {name}'
    return render_template('form.html')

# variable rule
# @app.route('/success/<int:score>')
# def success(score):
#     return f" the score is {score}" # this score can be string hence we are using <int:score> or u can use str(score)


@app.route('/success/<int:score>')
def success(score):
    res=""
    if score>35:
        res="PASSED"
    else :
        res="Failed"
    return render_template('results.html',results=res)


@app.route('/successres/<int:score>')
def success1(score):
    res=""
    if score>35:
        res="PASSED"
    else :
        res="Failed"
    exp={'score':score,'res':res}
    return render_template('results1.html',results=exp)


if __name__=="__main__":
    app.run(debug=True) # debug=True is helpfull to make like nodemon no need to no need to run again again file 





