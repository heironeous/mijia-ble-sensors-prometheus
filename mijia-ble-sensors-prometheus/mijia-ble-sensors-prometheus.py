from prometheus_client import start_http_server, Gauge
import logging

_LOGGER = logging.getLogger(__name__)

# Config file
config = {}

# Prometheus metric variables
temperature = None
humidity = None
battery_percentage = None
last_data_reading = None

# Initialize the metrics
def setup_metrics():
    global temperature
    temperature = Gauge('temperature', 'Temperature reading from the Mijia Sensor', ['mac_address', 'sensor_name'])
    global humidity
    humidity = Gauge('humidity', 'Humidity reading from the Mijia Sensor', ['mac_address', 'sensor_name'])
    global battery_percentage
    battery_percentage= Gauge('battery_percentage', 'Battery Percentage reading from the Mijia Sensor',
                               ['mac_address', 'sensor_name'])
    global last_data_reading
    last_data_reading = Gauge('last_data_reading', 'Last data reading done from this Mijia Sensor',
                              ['mac_address', 'sensor_name'])

#
def setup_metrics_endpoint():
    start_http_server(config['exporter']['port'])

def main():
    _LOGGER.info()



if __name__ == '__main__':
    parse_inputs()
    read_config()
    setup_metrics()
    setup_metrics_endpoint()
    # Start up the server to expose the metrics.

    # Generate some requests.
    while True:
        process_request(random.random())