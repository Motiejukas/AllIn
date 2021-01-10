import requests

def belekiek_kaciuku(kiekis):
    for i in range(kiekis):
        r = requests.get('https://cataas.com/cat')
        with open(f'cat{i+1}.jpg', 'wb') as file:
            file.write(r.content)


belekiek_kaciuku(3)



def sites_headers_data(*args):
    print('URL\t\t\tServer')
    print('-------------------------------------')
    for site in args:
        r = requests.get(site)
        result = r.headers
        print(f'{r.url}\t{result["Server"]}')

sites_headers_data('http://delfi.lt', 'http://alfa.lt', 'http://15min.lt', 'http://lrytas.lt', 'http://google.com')

import requests

r = requests.get('https://orai.15min.lt/prognozes')
html = r.text
split_by_vilnius = html.split('Vilnius')
split_by_hot = split_by_vilnius[-1].split('hot">')
res = split_by_hot[1].split()[0]

print(res)

