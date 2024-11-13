from polygon import RESTClient

api_key = "YOUR_API_KEY"
client = RESTClient(api_key)

# Example API call to fetch a snapshot for a single stock
snapshot = client.get_snapshot("stocks", "AAPL")
print(snapshot)

