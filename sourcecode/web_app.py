from flask import Flask, redirect, url_for, render_template
import json
app = Flask(__name__)

with open('static/data.json') as infile:
  data = json.load(infile)
  infile.close()

@app.route('/')
def root():
  return render_template('main.html', data=data)

@app.route('/<category>')
def display(category):
  for item in data:
    if item['url'] == category:
      return "Yass"
  return "Item not found babe"



@app.route('/test')
def test():
  print data[1]
  return "Okie"

@app.route('/display/')
@app.route('/display/<page>')
def dispglay(page=None):
  if page == None:
    return redirect(url_for('root'))
  else:
    return "This is a page about %s" % page


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
