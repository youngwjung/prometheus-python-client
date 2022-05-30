from prometheus_client import start_http_server, Summary, Counter
import random
import time

# Create a metric to track time spent and requests made.
request_summary = Summary('request_processing_seconds',
                          'Time spent processing request')

# Create a metric to count requests made.
request_counter = Counter('request', 'Number of request')

# Decorate function with metric.
@request_summary.time()
def process_request(t):
    # Simulate request processing
    time.sleep(t)

    # Increment request count
    request_counter.inc()


if __name__ == '__main__':
    # Start up the server to expose the metrics.
    start_http_server(8000)
    # Generate some requests.
    while True:
        process_request(random.random())
