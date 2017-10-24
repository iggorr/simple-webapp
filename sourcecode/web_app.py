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
@app.route('/<category>')
@app.route('/<category>/<maker>')
def display(category, maker=None):
  # Iterating through each maker type in the data
  for item in data:
    # If a maker type with a matching URL has been found
    if item['url'] == category:
      # If a particular maker hasn't been passed as a URL variable, 
      # display the html template with the maker type's details
      if maker == None:
        return render_template('makers.html', result=item)
      # If a particular maker has been specified
      else:
        # Iterate through each make of the specified type
        for machine in item['makers']:
          # If a maker with a matching URL has been found
          if machine['url'] == maker:
            # Display the html template with the details of the maker
            return render_template('maker.html', result=machine, cat=item)
        # If the maker wasn't found in the type's details, return the page
        # of the maker type instead
        return redirect(url_for('display', category=category))
  # If a maker type wasn't found, throw a 404 error
  abort(404)

# Custom defined error for code 404
@app.errorhandler(404)
def page_not_found(error):
  # Displaying the appropriate template and returning the error code
  return render_template('404.html'), 404

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
