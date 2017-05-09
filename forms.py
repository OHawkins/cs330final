from flask_wtf import Form
from wtforms import TextField, IntegerField, TextAreaField, DateField, RadioField, SelectField
from wtforms import validators

class EventForm(Form):
	name=TextField("Event Name",[validators.Required("Please enter the name of the event.")])
	category=TextField("Event Category",[validators.Required("Please enter the category of the event.")])
	date=DateField("Event Date",[validators.Required("Please enter the date of the event.")])
	start=TextField("Event Start",[validators.Required("Please enter the start time of the event.")])
	end=TextField("Event End",[validators.Required("Please enter the end time of the event.")])
	location=SelectField("Event Location")
	submit = SubmitField("Create Event")
