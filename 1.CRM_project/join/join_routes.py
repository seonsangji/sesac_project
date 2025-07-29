from flask import Blueprint, render_template, request, redirect, url_for
from . import database as db
from datetime import date
import uuid

join_bp = Blueprint('join', __name__,  template_folder='../templates/join')

@join_bp.route('/', methods=['GET', 'POST'])
def create_account():
    if request.method == 'POST':
        id = str(uuid.uuid4())
        name = request.form['name']
        gender = request.form['gender']
        birthdate = request.form['birthdate']
        age = 2025 - int(birthdate[:4])
        address = "지구어딘가 지구시 지구구"
        db.create_user(id, name, gender, age, birthdate, address)
        return render_template('join/create_order.html')
    else:
        today = date.today().isoformat()
        print(today)
        return render_template('join.html', today=today)
    
def create_order():
    pass
    

