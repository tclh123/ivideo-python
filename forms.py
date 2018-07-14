import requests
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired


def make_choice(api_name):
    api = requests.get('https://iodefog.github.io/text/viplist.json').json()
    return [(a['url'], a['name']) for a in api[api_name]]


class VipListForm(FlaskForm):
    parser = SelectField('解析线路', validators=[DataRequired()], choices=make_choice('list'), coerce=str)
    url = StringField('视频地址', validators=[DataRequired()])
    submit = SubmitField('解析')