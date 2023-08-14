from flask import Flask,render_template,request
from flask_wtf import FlaskForm 
from wtforms import StringField,SubmitField,validators

app = Flask(__name__)
app.config['SECRET_KEY'] = 'nishu'

class MyForm(FlaskForm): 
    name = StringField('Name: ')
    email = StringField('Email: ')
    submit = SubmitField('Sign Up')

@app.route("/", methods=['GET','POST'])
def nush():
        form = MyForm()
        if request.method == 'POST':
            return "Form submitted!"
        else:
           return render_template('index.html', form=form)

if __name__ == "__main__":
    app.run(debug=True)