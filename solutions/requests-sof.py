import requests
import pandas as pd
import matplotlib.pyplot as plt


base_url = "https://api.stackexchange.com"
query = '/2.2/tags?page=1&pagesize=1&order=desc&sort=popular&inname={0}&site=stackoverflow'

df = pd.DataFrame()
for name in ('matlab', 'numpy', 'scipy', 'matplotlib'):
    r = requests.get(base_url + query.format(name))
    assert r.ok
    df = pd.concat((df, pd.DataFrame(r.json()['items'])))
df = df.sort_values('count')
df.plot.barh('name', 'count', color='k')
plt.show()