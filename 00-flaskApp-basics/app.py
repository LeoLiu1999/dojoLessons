from flask import Flask  

app = Flask (__name__)  

#Will appear at localhost:5000
@app.route("/")
def hello_world():
  return "HAIIIII!"  

#Will appear at localhost:5000/pageTwo
@app.route("/pageTwo")
def another_page():
  return "HAIIIII! I'm another page!"

if __name__ == "__main__":
  app.run() 
