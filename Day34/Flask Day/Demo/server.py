from flask import Flask, render_template, request, url_for

app = Flask(__name__)


@app.route("/home")
def home_page():
  return "<h1>Welcome to Forsk</h1>"

@app.route("/view")
def view_template():
    return render_template("index.html")

@app.route("/data/<name>/<age>")
def get_data(name,age):
    output = {"Name":name,"Age":age}
    return render_template("user_info.html", info=output)

@app.route("/data2")
def argument_data():
    name = request.args.get("name")
    age = request.args.get("age")
    output = {"Name":name,"Age":age}
    return render_template("user_info.html", info=output)

@app.route("/data3", methods=["POST"])
def json_data():
    name = request.json.get("name")
    age = request.json.get("age")
    output = {"Name":name,"Age":age}
    return render_template("user_info.html", info=output)

@app.route("/data4", methods=["GET","POST"])
def form_data():
    if request.method == "GET":
        return "<h1>Hello People, Have Fun</h1>"
    else:
        user_data = request.form
        name = user_data["name"]
        age = user_data["age"]
        output = {"Name":name,"Age":age}
        return render_template("user_info.html", info=output)



if __name__ == "__main__":
  app.run(debug=True)
