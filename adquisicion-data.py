import requests
import json
import pandas as pd
import datetime
import time as t
import codecs
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')




URL = 'https://url-api'
resp = requests.get(URL)
resptext = resp.text

print(resptext)
respuesta = json.loads(resptext)
df = pd.read_json(respuesta)
log = str(resp.status_code)
fichero = 'fichero.csv'
df.to_csv(fichero, sep='|', index=False)

