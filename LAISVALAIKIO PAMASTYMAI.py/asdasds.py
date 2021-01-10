"""import requests
from PIL import Image
"""
"""import pandas as pd
import numpy as np
from sklearn import preprocessing
import matplotlib.pyplot as plt
plt.rc("font", size=14)
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split"""
"""import seaborn as sns
sns.set(style="white")
sns.set(style="whitegrid", color_codes=True)
"""

#data = pd.read_excel (r'C:\Users\gebruiker 1\Desktop\data.xlsx')

"""
df = pd.DataFrame(data, columns= ['Client_number','Request_number'])
eilutes_stulpeliai = data.shape
stulpeliu_pav = list(data.columns)

table=pd.crosstab(data.Client_number,data.y)
table.div(table.sum(1).astype(float), axis=0).plot(kind='bar', stacked=True)
plt.title('Stacked Bar Chart of Marital Status vs Purchase')
plt.xlabel('Marital Status')
plt.ylabel('Proportion of Customers')
plt.savefig('mariral_vs_pur_stack')
"""




"""r = requests.get('https://g4.dcdn.lt/images/pix/kaune-policija-tikrina-vykstancius-i-miesta-86095709.jpg')
with open('logo.jpg', 'wb') as f:
    f.write(r.content)
im = Image.open("logo.jpg")
im.show()"""

import requests
import json


def get_10_ids(num):
    response = requests.get('https://api.coinlore.com/api/tickers/').json()
    response_cleaned = []
    for i in response['data'][:int(num) + 1]:
        if i['symbol'] != 'USDT':
            response_cleaned.append({'coin': i['name'], 'symbol': i['symbol'], 'id': i['id']})
    return response_cleaned
print(get_10_ids(0))