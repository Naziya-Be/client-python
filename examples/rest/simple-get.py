from polygon import RESTClient
from polygon.rest import models

client = RESTClient("90YFsduHTdpZdo8xQueZvu5EcSh0pcqI")

aggs = client.get_aggs(
    "AAPL",
    1,
    "day",
    "2022-04-04",
    "2022-04-04",
)
print(aggs)
