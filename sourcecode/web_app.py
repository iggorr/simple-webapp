from flask import Flask, redirect, url_for, render_template, abort
import json
app = Flask(__name__)

# Opening the JSON file that stores all the data for the web app and loading it
# into a python list
with open('static/data.json') as infile:
  data = json.load(infile)
  infile.close()

# Main route of the application that displays the html template with data
@app.route('/')
def root():
  return render_template('main.html', data=data)

# Route to a particular maker or type of makers that is passed as a URL variable
@app.route('/<mtype>')
@app.route('/<mtype>/<maker>')
def display(mtype, maker=None):
  # Iterating through each maker type in the data
  for item in data:
    # If a maker type with a matching URL has been found
    if item['url'] == mtype:
      # If a particular maker hasn't been passed as a URL variable, 
      # display the html template with the maker type's details
      if maker == None:
        return render_template('results.html', result=item) 
      # If a particular maker has been specified
      else:
        # Iterate through each make of the specified type
        for machine in item['makers']:
          # If a maker with a matching URL has been found
          if machine['url'] == maker:
            return "Item found!"
  # Otherwise, throw a 404 error
  abort(404)

# Custom defined error for code 404
@app.errorhandler(404)
def page_not_found(error):
  return "The page you have requested wasn't found!", 404





@app.route('/display/')
@app.route('/display/<page>')
def dispglay(page=None):
  if page == None:
    return redirect(url_for('root'))
  else:
    return "This is a page about %s" % page





if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
