import os
import ast
import keen
from app import app
from flask import url_for, json, redirect, render_template, request

keen.project_id = app.config['KEEN_PROJECT_ID']
keen.write_key = app.config['KEEN_WRITE_KEY']
keen.read_key = app.config['KEEN_READ_KEY']
master_key = app.config['KEEN_MASTER_KEY']

static_directory = os.path.dirname(os.path.abspath(__file__)) + "/static/"
uploads_path = "uploads/"
uploads_directory = static_directory + uploads_path

def read_contents(uploaded):
  upload_url = url_for('static', filename=uploads_path + uploaded) 
  try:
    with open(uploads_directory + uploaded, 'r') as myfile:
      file_content = json.load(myfile)
  except IOError:
    abort(404)
  return file_content

@app.route("/", methods=['GET', 'POST'])
def hello():
  if request.method == 'POST':
    new_file = request.files['file']
    if new_file:
      filename = new_file.filename
      new_file.save(os.path.join(uploads_directory, filename))
      send_data_to_keen(filename)
    return(redirect(url_for('dashboard', dashboard_name=filename)))
  return render_template('index.html') 

@app.route("/upload", )
def upload():
  if request.method == 'POST':
    new_file = request.files['file']
    if new_file:
      filename = new_file.filename
      new_file.save(os.path.join(uploads_directory, filename))
      send_data_to_keen(filename)
    return(redirect(url_for('dashboard', dashboard_name=filename)))
  return(render_template('upload.html'))

@app.route("/dashboard/<dashboard_name>", methods=['GET'])
def dashboard(dashboard_name):
  return render_template('dashboard.html')

def send_data_to_keen(keen_json):
  contents = read_contents(keen_json)
  for key in contents.keys():
    events = contents.get(key)
    for event in events:
      keen.add_events({str(key): [event]})

