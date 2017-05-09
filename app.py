from flask import Flask, request, render_template
import psycopg2
import json
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

# conn = psycopg2.connect(user='hawkol01', host='knuth.luther.edu')
# db = conn.cursor()


@app.route('/')
def index():
    # when the page loads, display the list of events

    return render_template('index.html')

@app.route('/create_event', methods=['GET', 'POST'])
def create_event():
    form = EventForm()
    if request.method == 'POST':
        if form.validate() == False:
            flash('All fields are required.')
            return render_template('create_event.html', form=form)
        else:
            return render_template('index.html', form=form)
    elif request.method == 'GET':
        return render_template('create_event.html', form = form)

    # allow user to enter information about the event,
    # then take them to the create_location view

@app.route('/create_location', methods=['POST'])
def create_location():
    conn = psycopg2.connect(user='hawkol01', dbname='world', host='knuth.luther.edu')
    data = conn.cursor()
    res = data.execute("""SELECT * FROM city;""")
    return render_template('create_location.html')

@app.route('/create_category', methods=['POST'])
def create_category():
    form = CatForm()
    if request.method == 'POST':
        if form.validate() == False:
            flash('All fields are required.')
            return render_template('create_category.html', form = form)
        else:
            return render_template('index.html', form = form)
    elif request.method == 'GET':
        return render_template('create_category.html', form = form)


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
