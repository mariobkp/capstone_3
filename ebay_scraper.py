# TO DO
# 1. make a request to ebay and get a page
# 2. collect data from each detail page
# 3. collect all links to detail pages of each product
# 4. write scraped data to .csv

import requests

import csv

import pandas as pd

from bs4 import BeautifulSoup


def get_page(url):

    response = requests.get(url)

    if not response.ok:
        print('Server responded: ', response.status_code)
    else:
        soup = BeautifulSoup(response.text, 'lxml')
    return soup


def get_detail_data(soup):

    # title
    # price
    # image
    # description

    try:
        # title = soup.find('h1', id='itemTitle').get('span')
        title = soup.find('span', class_='g-hdn').next_sibling
    except:
        title = ''
    
    try:
        p = soup.find('span', id='prcIsum').text.strip()
        currency, price = p.split(' ')
    except:
        price = ''
        currency = ''
    
    try:
        img = soup.find('img', id='icImg').get('src')
    except:
        img = ''
    
    try:
        # desc = [tr.find_all('td') for tr in soup.find('div', id='viTabs_0_is').find('table').find_all('tr')]
        
        table = soup.find('div', id='viTabs_0_is').find('table')
        table_rows = table.find_all('tr')
        
        d = []

        for tr in table_rows:
            td = tr.find_all('td')
            row = [tr.get_text(strip=True) for tr in td]
            d.append(row)

        try:
            cols = [x[0] for x in d] + [x[2] for x in d]
        except:
            cols = [x[0] for x in d]
        try:
            vals = [x[1] for x in d] + [x[3] for x in d]
        except:
            vals = [x[1] for x in d]
        attrs = {k: v for k,v in zip(cols, vals)}

        desc = attrs
        # desc = pd.DataFrame.from_dict(attrs, orient='index').T
    except:
        desc = ''
    
    
    data = {
        'title': title,
        'price': price,
        'currency': currency,
        'image': img,
        'desc': desc
    }

    return data


def get_index_data(soup):

    try:
        links = soup.find_all('a', class_='s-item__link')
    except:
        links = []
    
    urls = [item.get('href') for item in links]

    return urls


def write_csv(data, url):

    with open('sneaker2.csv', 'a') as csvfile:
        writer = csv.writer(csvfile)

        row = [data['title'], data['price'], data['currency'], data['desc'], data['image'], url]

        writer.writerow(row)


def main():
    
    url = 'https://www.ebay.com/b/Mens-Athletic-Shoes/15709/bn_57918?rt=nc&LH_ItemCondition=3000'
    
    page = 1

    # print(get_detail_data(get_page(url)))
    while requests.get(url).ok==True:

        products = get_index_data(get_page(url))

        for link in products:
            data = get_detail_data(get_page(link))
            write_csv(data, link)

        page += 1

        url = url + '&_pgn=' + str(page)


if __name__ == '__main__':

    main()