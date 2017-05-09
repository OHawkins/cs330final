from flask import Flask, request, render_template
import psycopg2
import json
from flask_boostrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

# conn = psycopg2.connect(user='hawkol01', host='knuth.luther.edu')
# db = conn.cursor()


@app.route('/')
def index():
    # when the page loads, display the list of events
    
    return render_template('create_event.html')

# @app.route('/create_event', methods=['POST'])
# def create_event():
#     # allow user to enter information about the event,
#     # then take them to the create_location view
#     return render_template('create')
#     pass
#
# @app.route('/create_location', methods=['POST'])
# def create_location():
#     # allow user to enter information about the location
#     return render_template('location.html')


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
