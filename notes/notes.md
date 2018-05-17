## Wednesday, May 9: Assemble Toolbox!

### pip: python package manager

#### Basic usage:

<pre><code>$ pip install package </code></pre>

We talked about the virtualenv, which is a sandbox for your python environment.
It allows you to:
  1. Maintain a specific python environment without messing with the system version
  2. Install packages without root access to a system

Then, we talked about Flask, which is a "microframework" (as opposed to enterprise frameworks) for developing web apps.
Flask has its own development web server (no more public_html) and includes a few useful modules:
##### Werkzeug:
  1. WSGI(Web Server Gateway Interface) implementation
  2. allows web apps to respond to web requests  
##### jinja2:
  1. HTML template engine (we will get into this later)
  2. easily create multiple pages that share style and content

#### To make and activated a virtualenv:

<pre><code>$ virtualenv leo  #leo can be replaced with any name </code></pre>

<pre><code>$ . leo/bin/activate   # . is equivalent to bash source command: runs a script </code></pre>

<pre><code>(leo) $ pip install flask </code></pre>

<pre><code>  Write and run flask </code></pre>

<pre><code>(leo) $ deactivate  #leaves the virtualenv </code></pre>


#### Running the following python script displayed the message "Hello World" on a local server.

<pre><code>from flask import Flask  

app = Flask (__name__)  

@app.route("/")  
def hello_world():
  return "Hello World"  

if __name__ == "__main__":

  app.run() </code></pre>