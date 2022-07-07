from flask import (Blueprint, render_template)
import json

pets = json.load(open('pets.json'))
print(pets)

bp = Blueprint('pet', __name__, url_prefix="/pet")

@bp.route('/')
def index(): 
    return render_template('index.html', pet=pets)


@bp.route('/petfax')
def show(id):
    pet = pets[id - 1]
    return render_template('show.html', pet=pets) 