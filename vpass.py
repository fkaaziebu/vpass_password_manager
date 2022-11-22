from flask import Flask, render_template, url_for, redirect, flash
from forms import PasswordForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '953c22c4e0af991dc9b7baf2b9ec6d7f'

passwords = [
    {
        'user': 'Frederick Aziebu',
        'content': {
            'password_description': 'Microsoft Account',
            'password': '27d4cbd275d204c2614bba4e74a90289' 
        }
    },
    {
        'user': 'Frederick Aziebu',
        'content': {
            'password_description': 'Amazon Account',
            'password': 'ef0cd4d1fbc30a15a3ab9088e894db80' 
        }
    },
    {
        'user': 'Frederick Aziebu',
        'content': {
            'password_description': 'Facebook Account',
            'password': '4f0f1f3a9c41cc38a93291f291f8cc8c' 
        }
    },
    {
        'user': 'Samuel Ameyaw',
        'content': {
            'password_description': 'Twitter Account',
            'password': 'ae57a1a326004f8ad42cbe2c086eeccf'
        }
    }
]

@app.route('/')
@app.route('/home', methods=["GET", "POST"])
def home():
    form = PasswordForm()
    if form.validate_on_submit():
        flash(f'Password with a description of {form.description.data} has been created successfully!', 'success')
        return redirect(url_for('dashboard'))
    return render_template('home.html', form=form)

@app.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    login = 'login'
    if form.validate_on_submit():
        flash(f'Password with a description of {form.description.data} has been created successfully!', 'success')
        return redirect(url_for('dashboard'))
    return render_template('login.html', form=form, page=login)

@app.route('/register', methods=["GET", "POST"])
def register():
    form = PasswordForm()
    if form.validate_on_submit():
        flash(f'Password with a description of {form.description.data} has been created successfully!', 'success')
        return redirect(url_for('dashboard'))
    return render_template('register.html', form=form)

@app.route('/dashboard', methods=["GET", "POST"])
def dashboard():
    form = PasswordForm()
    if form.validate_on_submit():
        flash(f'Password with a description of {form.description.data} has been created successfully!', 'success')
        return redirect(url_for('dashboard'))
    return render_template('dashboard.html', title='User Dashboard', passwords=passwords, form=form)

@app.route('/create_password', methods=['GET', 'POST'])
def create_password():
    form = PasswordForm()
    login='not'
    if form.validate_on_submit():
        flash(f'Password with a description of {form.description.data} has been created successfully!', 'success')
        return redirect(url_for('dashboard'))
    return render_template('create_password.html', title='Create Password', form=form, page=login)

if __name__ == '__main__':
    app.run(debug=True)