from flask import Flask,render_template,request

app=Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/more",methods=["GET","POST"])
def more():
    if request.method=="GET":
        return "Please submit the form instead"
    else:
        name=request.form.get("name")
        return render_template("more.html",name=name)
