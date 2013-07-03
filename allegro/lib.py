from bs4 import BeautifulSoup
import mechanize


class AllegroError(Exception):
    pass


def downolad_data(product):
    browser = mechanize.Browser()
    try:
        browser.open("http://allegro.pl")
    except (mechanize.HTTPError, mechanize.URLError):
        raise AllegroError('No connection with allegro.pl')

    browser.select_form(nr=0)
    browser.form['string'] = product
    browser.submit()

    try:
        browser.select_form(name='display-form')
    except mechanize._mechanize.FormNotFoundError:
        raise AllegroError('Allegro takes exactly 1 argument!')

    browser.find_control('offerTypeBuyNow').items[0].selected = True
    browser.find_control('standard_allegro').items[0].selected = True
    browser.find_control('startingTime').items[7].selected = False
    browser.find_control('shippingTime').items[0].selected = False
    browser.submit()
    html = browser.response().read()
    soup = BeautifulSoup(html)
    offers = soup.find('section', class_='offers')

    if not offers:
        raise AllegroError('No result!!')

    url = 'http://allegro.pl' + offers.find('a').get('href')

    price = offers.div.find('span', class_='buy-now dist')
    price = price.contents[2]
    price = ''.join(price.split())
    price = price.replace(',', '.')
    price = float(price)
    return url, price
