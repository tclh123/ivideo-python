from flask import Flask, render_template, redirect
from flask_bootstrap import Bootstrap
from forms import VipListForm, make_choice

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = 'gds324g3434'

@app.route('/', methods=['GET', 'POST'])
def index():
    form = VipListForm()
    platforms = make_choice('platformlist')
    if form.validate_on_submit():
        return redirect(f'{form.parser.data}{form.url.data}')
    return render_template('index.html', form=form, platforms=platforms)