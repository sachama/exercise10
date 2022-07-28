from flask import Flask
from prometheus_flask_exporter import PrometheusMetrics


app = Flask(__name__)
counter = 1
# group by endpoint rather than path
metrics = PrometheusMetrics(app, group_by='endpoint')

@app.route('/collection/:collection_id/item/:item_id')
@metrics.counter(
    'cnt_collection', 'Number of invocations per collection', labels={
        'collection': lambda: request.view_args['collection_id'],
        'status': lambda resp: resp.status_code
    })
def get_item_from_collection(collection_id, item_id):
    pass

metrics.start_http_server(8099)

@app.route("/")
def test():
    global counter
    counter += 1
    return (f"CONGRATULATIONS. You visit this page {counter}-times")


@app.route("/grafanadashboard")
def test4():
    return ("Grafana Dashboard")

if __name__=="__main__":
    app.run(host="0.0.0.0", port=8088)