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
    return render_template('character.html', hero=gen_hero)


@app.route('/magicweapon')
def magicweapon():
    gen_hero = create_hero()
    return render_template('magicweapon.html', hero=gen_hero)
