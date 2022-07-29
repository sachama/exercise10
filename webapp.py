from flask import Flask
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
counter = 1

metrics = PrometheusMetrics(app)

@app.route("/")
def test():
    global counter
    counter += 1
    return (f"You visit this page {counter}-times")

if __name__=="__main__":
    app.run(host="0.0.0.0", port=8088)