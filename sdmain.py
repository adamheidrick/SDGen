from flask import Flask, render_template, request, redirect, url_for
from HeroCreator.hero_main import create_hero

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')


@app.route('/hero')
def hero():
    gen_hero = create_hero()
    hero_class = gen_hero['hero_class']
    match hero_class:
        case 'Fighter':
            return render_template('fighter.html', hero=gen_hero)
        case 'Wizard':
            return render_template('wizard.html', hero=gen_hero)
        case 'Priest':
            return render_template('priest.html', hero=gen_hero)
        case 'Thief':
            return render_template('thief.html', hero=gen_hero)
        case _:
            return render_template('error.html', hero=gen_hero)


@app.route('/magicweapon')
def magicweapon():
    gen_hero = create_hero()
    return render_template('magicweapon.html', hero=gen_hero)
