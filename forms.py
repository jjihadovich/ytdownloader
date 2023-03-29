from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired


class YtSearch(FlaskForm):
    link = StringField('', [InputRequired()], render_kw={"placeholder": "Вставьте ссылку на видео:"})
    submit = SubmitField("Скачать")
