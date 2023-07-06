from flask import Flask, render_template, url_for, redirect, request, flash
from flask import session as login_session
import pyrebase



config = {
  'apiKey': "AIzaSyDHjKFzbJ8whSyZxLPzRm1xTYFZ79NH_co",
  'authDomain': "journal-f2d0f.firebaseapp.com",
  'projectId': "journal-f2d0f",
  'storageBucket': "journal-f2d0f.appspot.com",
  'messagingSenderId': "410488329960",
  'appId': "1:410488329960:web:ac5277738a4e5c1c815b5d",
  'measurementId': "G-C6LVP92MQ2",
  'databaseURL': ""
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

app = Flask(__name__)
app.config['SECRET_KEY'] = "FAFGDSA_FADSAFDSA"



@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['login_email']
        password = request.form['password']

        if len(email) < 4:
            flash('Email must be greater than 4 characters.', category='error')
        elif len(password) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            pass


        try:
            user = auth.sign_in_with_email_and_password(email, password)

            return redirect(url_for('journal'))
        except:
            return render_template('login.html', error='Invalid credentials')

    return render_template('login.html')


@app.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form['signup_email']
        firstName = request.form['firstName']
        password1 = request.form['password1']
        password2 = request.form['password2']

        if len(email) < 4:
            flash('Email must be greater than 4 characters.', category='error')
        elif len(firstName) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            flash('Account created!', category='success')

        try:
            user = auth.create_user_with_email_and_password(email, password1)
            return redirect(url_for('journal'))
        except:
            return render_template('sign_up.html')

    return render_template('sign_up.html')





@app.route('/home', methods=["GET"])
def home():
    return render_template("home.html")



@app.route('/journal', methods=['GET', 'POST'])
def journal():
    if request.method == 'POST':
        pass

    else:

        return render_template("journal.html")



if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)