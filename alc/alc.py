import requests
from bs4 import BeautifulSoup

def get_examples(word):
    url = 'http://eow.alc.co.jp/search'
    query = {}
    query['q'] = word
    query['ref'] = 'sa'
    ret = requests.get(url, params=query)
    text = ''
    soup = BeautifulSoup(ret.content, 'lxml')
    for l in soup.findAll('div', {'id':'resultsList'})[0]:
        try:
            text += l.text
        except:
            pass
    return text

if __name__ == '__main__':
    ret = get_examples('Python')
    print(ret)

