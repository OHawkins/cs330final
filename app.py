from flask import Flask, request, render_template
import psycopg2
import json
from flask_bootstrap import Bootstrap
import create_orm
from forms import EventForm, CatForm

app = Flask(__name__)
Bootstrap(app)
app.secret_key = 'development key'
print("APP CREATED")

@app.route('/admin/database')
def admin():
    create_orm.db_create()
    print("AFTER ADMIN")

@app.route('/', methods=['GET', 'POST'])
def index():
    # when the page loads, display the list of events
    print("SHOW EVENTS")
    res = create_orm.show_events()
    return render_template('index.html', res=res)
print("AFTER INDEX")

@app.route('/create_event', methods=['GET', 'POST'])
def create_event():
    form = EventForm()
    if request.method == 'POST':
        if form.validate() == False:
            flash('All fields are required.')
            return render_template('create_event.html', form = form)
        else:
            print("ELSE")
            create_orm.crevnt(form.name, form.category, form.start, form.end, form.location)
            return render_template('index.html', form=form, res = create_orm.show_events())
    elif request.method == 'GET':
        return render_template('create_event.html', form = form)
print("AFTER CREATE_EVENT")
    # allow user to enter information about the event,
    # then take them to the create_location view

@app.route('/create_location', methods=['GET', 'POST'])
def create_location():
    res = data.execute("""SELECT * FROM city;""")
    return render_template('create_location.html', res = res)

@app.route('/create_category', methods=['GET','POST'])
def create_category():
    form = CatForm()
    if request.method == 'POST':
        if form.validate() == False:
            flash('All fields are required.')
            return render_template('category.html', form = form)
        else:
            create_orm.crt_ctgry(form.name)
            return render_template('index.html', form = form, res = create_orm.show_events())
    elif request.method == 'GET':
        return render_template('category.html', form = form)


if __name__ == '__main__':
    print("NAME == MAIN")
    app.run(debug=True, port=5000)
