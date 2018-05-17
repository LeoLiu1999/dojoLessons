from flask import Flask, render_template

app = Flask (__name__)  

@app.route("/")
def hello_world():
  return "HAIIIII!"

@app.route("/template1")
def temp1():
  return render_template("example_template.html", content = "Hi, this is a template")

@app.route("/template2")
def temp2():
  return render_template("example_template.html", content = "Hi, this is another template")

if __name__ == "__main__":
  app.debug = True
  app.run() 
