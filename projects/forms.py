from flask_wtf import FlaskForm
from wtforms import StringField,RadioField,SubmitField,IntegerField,DateField
from wtforms.fields.html5 import DateField

class fillup(FlaskForm):
    crimeid=StringField('Crime-Id')
    location=StringField('Location')
    policestn=StringField('Police Station')
    date = DateField('Date')
    criminalname=StringField('Criminal Name')
    criminaladhr=IntegerField('Criminal Aadhar Number')
    victimname=StringField('Victim Name')
    victimadhr=IntegerField('Victim Aadhar Number')
    crimetype = RadioField('Crime type', choices = [('Murder','Murder'),('Abuse','Abuse'),('Theft','Theft')]) 
    submit=SubmitField('Submit')