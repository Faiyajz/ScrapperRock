import time
from requests_html import HTMLSession

session = HTMLSession()

t1 = time.perf_counter()


r = session.get('https://httpbin.org/delay/1')
response = r.html.url
print(response)

r = session.get('https://httpbin.org/delay/2')
response = r.html.url
print(response)

r = session.get('https://httpbin.org/delay/3')
response = r.html.url
print(response)


t2 = time.perf_counter()

print(f'Synchronous: {t2-t1} seconds')
