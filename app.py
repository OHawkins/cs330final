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
    #create_orm.clearTable()
    # when the page loads, display the list of events
    print("SHOW EVENTS")
    res = create_orm.show_events()
    return render_template('index.html', res=res)
print("AFTER INDEX")

@app.route('/create_event', methods=['GET', 'POST'])
def create_event():
    form = EventForm(request.form)
    form.category.choices = create_orm.getCat()
    if request.method == 'POST':
        if form.validate() == False:
            #flash('All fields are required.')
            return render_template('create_event.html', form = form)
        else:
            print("ELSE")
            create_orm.crevnt(request.form["name"], request.form["category"], request.form["start"], request.form["end"], request.form["location"])
            res = create_orm.show_events()
            return render_template('index.html', res=res)
    elif request.method == 'GET':
        return render_template('create_event.html', form = form)
print("AFTER CREATE_EVENT")
    # allow user to enter information about the event,
    # then take them to the create_location view

# @app.route('/create_location', methods=['GET', 'POST'])
# def create_location():
#     res = data.execute("""SELECT * FROM city;""")
#     return render_template('create_location.html', res = res)

@app.route('/create_category', methods=['GET','POST'])
def create_category():
    form = CatForm(request.form)
    if request.method == 'POST':
        if form.validate() == False:
            return render_template('category.html', form = form)
        else:
            create_orm.crt_ctgry(request.form["name"])
            return render_template('index.html', form = form, res = create_orm.show_events())
    elif request.method == 'GET':
        return render_template('category.html', form = form)


if __name__ == '__main__':
    print("NAME == MAIN")
    app.run(debug=True, port=5000)
