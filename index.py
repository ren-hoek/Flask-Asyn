from flask import Flask, render_template, request, jsonify
app = Flask(__name__,
        static_url_path="/static")

@app.route("/")
def home():
    return render_template('home.html')


@app.route("/data", methods=['GET', 'POST'])
def data():
    print(request.get_json())
    return(jsonify(request.get_json()))



if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
