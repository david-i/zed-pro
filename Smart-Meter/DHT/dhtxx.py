#!/usr/bin/python

import json
import requests
import sys

import Adafruit_DHT
 
url_h = "https://io.adafruit.com/api/v2/david_i/feeds/humidity/data"
url_t = "https://io.adafruit.com/api/v2/david_i/feeds/temperature/data"
aio_key = "9b120dce69f5cfed06a983259008eb689fd9046e"

headers = {
           'x-aio-key': aio_key,
           'Cache-Control': "no-cache",
           'Content-Type': "application/x-www-form-urlencoded"
           }

humidity, temperature = Adafruit_DHT.read_retry(22, 4)

# Convert degrees Celsius to Fahrenheit
temperature = temperature * 9/5.0 + 32

payload_h = "value=" + str(humidity)
payload_t = "value=" + str(temperature)

try: 
    response_h = requests.post(url_h, headers=headers, data=payload_h) 
    print(response_h.text)
    response_t = requests.post(url_t, headers=headers, data=payload_t) 
    print(response_t.text)

except:
    print("POST error to adafruit.io\n")
