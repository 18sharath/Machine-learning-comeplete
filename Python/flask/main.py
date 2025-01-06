from flask import Flask,render_template
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

@app.route("/index")
def index():
    return render_template("index.html")

if __name__=="__main__":
    app.run(debug=True) # debug=True is helpfull to make like nodemon no need to no need to run again again file 
