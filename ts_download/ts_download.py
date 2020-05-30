import requests

base_url = 'https://hogehoge/file_{}.ts'

for i in range(1, 100, 1):
    url = base_url.format(i)
    r = requests.get(url)
    with open('file_{:04d}.ts'.format(i), 'wb') as f:
        f.write(r.content)
