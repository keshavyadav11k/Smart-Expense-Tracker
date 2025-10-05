from flask import Flask,render_template,request


app = Flask(__name__)



@app.route('/')
def index():
    return render_template('login.html')

@app.route('/register')
def register():


    return render_template('register.html')

@app.route('/perform_registration')
def perform_registration():

    return 'registration successfull'

if __name__ == '__main__':
    app.run(debug=True)

