from flask import Flask
from prometheus_flask_exporter import PrometheusMetrics


app = Flask(__name__)
counter = 1
metrics = PrometheusMetrics(app)

@app.route("/")
def test():
    global counter
    counter += 1
    return (f"CONGRATULATIONS. You visit this page {counter}-times")
    
@app.route("/healthweb")
def test2():
    return ("Health Web - Prometheus metric")

@app.route("/grafanaweb")
def test3():
    return ("Grafana Web")

@app.route("/grafanadashboard")
def test4():
    return ("Grafana Dashboard")

if __name__=="__main__":
    app.run(host="0.0.0.0", port=8088)