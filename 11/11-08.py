from urllib.parse import urlparse, parse_qs
 url = "https://yandex.ru/images/search?text=котики&source=images_drawing"
 parsed_url = urlparse(url)
 pq = parse_qs(parsed_url.query)
 pq
{'text': ['котики'], 'source': ['images_drawing']}
 pq['text']
['котики']