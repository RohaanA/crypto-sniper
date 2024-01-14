import yaml

def fetch_details(exchange="binance"):
    # Fetches the details of the exchange from config.yaml
    # Returns a dictionary of the details
    with open("config.yaml", "r") as f:
        details = yaml.safe_load(f)
    return details[exchange]