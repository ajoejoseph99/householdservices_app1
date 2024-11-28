from flask import Flask, render_template, redirect, url_for, request, flash
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.secret_key = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///household_services.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Bootstrap(app)

# Import models and forms
from models import User, Service, ServiceRequest
from forms import LoginForm, RegisterForm, ServiceForm, ServiceRequestForm

@app.route('/')
def home():
    return render_template('index.html')

# Admin, Customer, Professional Routes to be added later

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/admin')
def admin_dashboard():
    services = Service.query.all()
    users = User.query.all()
    return render_template('admin_dashboard.html', services=services, users=users)

@app.route('/admin/service/add', methods=['GET', 'POST'])
def add_service():
    form = ServiceForm()
    if form.validate_on_submit():
        service = Service(
            name=form.name.data,
            description=form.description.data,
            base_price=form.base_price.data
        )
        db.session.add(service)
        db.session.commit()
        flash('Service added successfully!', 'success')
        return redirect(url_for('admin_dashboard'))
    return render_template('add_service.html', form=form)
