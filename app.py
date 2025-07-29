from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    air_data = {
        "location": "Coimbatore",
        "aqi": 87,
        "status": "Moderate",
        "advice": "People with respiratory issues should limit outdoor activities."
    }
    return render_template("index.html", data=air_data)

if __name__ == "__main__":
    app.run(debug=True)
