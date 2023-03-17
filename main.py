import requests, smtplib
from bs4 import BeautifulSoup

my_email = 'baiastansa@gmail.com'
password = 'rhmeghghrqbvqvmy'



URL = "https://www.amazon.com/dp/B07J2Q4N2G?tag=camelproducts-20&linkCode=ogi&th=1&psc=1&language=en_US"


headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
  'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
  'upgrade-insecure-requests':'1',
  'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
  'sec-fetch-site':'cross-site',
  'sec-fetch-mode':'navigate',
  'sec-fetch-user':'?1',
  'sec-fetch-dest':'document',
  'sec-ch-ua':'"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
  'sec-ch-ua-mobile':'?0',
  'sec-ch-ua-platform':'"Windows"',
  'Accept-Encoding':'gzip, deflate, br',
  'x-forwarded-proto':'https',
  'x-https':'on',
  'X-Forwarded-For': '50.201.92.222',
}
response = requests.get(URL, headers = headers)


soup = BeautifulSoup(response.text, 'html.parser')
price = soup.find_all(name = 'span', class_='a-price a-text-price a-size-medium apexPriceToPay')[0].find(class_='a-offscreen').getText().replace('$','')


name = soup.find_all(name = 'h1', id = 'title', class_='a-size-large a-spacing-none')[0].getText().strip()


if int(price.split('.')[0]) < 451:
  with smtplib.SMTP('smtp.gmail.com') as connection:
      connection.starttls()
      connection.login(user = my_email, password = password)
      connection.sendmail(
        from_addr = my_email,
        to_addrs = 'bayastankydyrov@gmail.com',
        msg = f'{name} is now ${price}'
      )