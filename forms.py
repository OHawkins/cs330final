from flask_wtf import Form
from wtforms import SubmitField, TextField, IntegerField, TextAreaField, DateField, RadioField, SelectField
from wtforms import validators

class EventForm(Form):
	name=TextField("Event Name",[validators.Required("Please enter the name of the event.")])
	category=TextField("Event Category",[validators.Required("Please enter the category of the event.")])
	date=DateField("Event Date",[validators.Required("Please enter the date of the event.")])
	start=TextField("Event Start",[validators.Required("Please enter the start time of the event.")])
	end=TextField("Event End",[validators.Required("Please enter the end time of the event.")])
	location=TextField("Event Location",[validators.Required("Please enter the location (city) of the event.")])
	submit = SubmitField("Create Event")

class CatForm(Form):
	name = TextField("Category Name", [validators.Required("Please enter the title of the category.")])
	submit = SubmitField("Create Category")
	
