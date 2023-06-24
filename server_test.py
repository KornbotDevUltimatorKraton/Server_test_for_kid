#Flask synchronous server 
from flask import Flask,render_template,request,jsonify 

app = Flask(__name__) 

#end point  / 
@app.route("/")
def index():

     return "Hello world wide web"

#end point /main_page
@app.route("/main_page")
def main_page_data():

     return render_template("index.html") 


if __name__ == "__main__":

           app.run(debug=True,threaded=True,host="0.0.0.0",port=5789)
