from flask import Flask, redirect, url_for, render_template
app = Flask(__name__)

@app.route("/")
def root():
  return render_template("main.html")

@app.route("/display/")
@app.route("/display/<page>")
def display(page=None):
  if page == None:
    return redirect(url_for("root"))
  else:
    return "This is a page about %s" % page


if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
