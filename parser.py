import requests
import re
from bs4 import BeautifulSoup
from selenium import webdriver
import os.path
import pandas as pd
import math
import csv

def find_page_number(url):
    html = requests.get(url, headers={'User-Agent': 'Custom'})
    soup = BeautifulSoup(html.text, 'html.parser')
    header = soup.find('h1', attrs={'class': 'bloko-header-1'}).text
    header = re.sub('[^0-9]', '', header)
    return math.ceil(int(header)/100)


def create(basic_url, file_name):
    page_number = find_page_number(basic_url)
    print('Number of pages: %d' % page_number)

    def xstr(s):
        if s is None:
            return ''
        return s.text

    pages = list(range(0, page_number))
    titles = []
    salaries = []
    companies = []
    locations = []
    dates = []
    for page in pages:
        url = basic_url + ('&page=%d' % (page))
        html = requests.get(url, headers={'User-Agent': 'Custom'})
        soup = BeautifulSoup(html.text, 'html.parser')
        print (file_name + ' - processing page: %s' % (page + 1))
        for block in soup.findAll('div', attrs={'class': 'vacancy-serp-item'}):
            title_str = block.find(
                'div', attrs={'class': 'vacancy-serp-item__info'}).text
            titles.append(title_str)
            salary_str = block.find(
                'div', attrs={'class': 'vacancy-serp-item__sidebar'}).text
            salaries.append(salary_str.replace('\u202f', ' '))
            company_str = xstr(block.find(
                'a', attrs={'data-qa': 'vacancy-serp__vacancy-employer'}))
            companies.append(company_str.replace('\u202f', ' '))
            location_str = block.find(
                'span', attrs={'data-qa': 'vacancy-serp__vacancy-address'}).text
            locations.append(location_str.replace('\u202f', ' '))
            date_str = block.find(
                'span', attrs={'data-qa': 'vacancy-serp__vacancy-date'}).text
            dates.append(date_str.replace('\u202f', ' '))

    df = pd.DataFrame(list(zip(titles, salaries, companies, locations, dates)),
                      columns=['Title', 'Salary', 'Company', 'Location', 'Date'])

    df.to_csv(file_name, index=False, sep=';', encoding='utf-8')
    print('Successfully finished')
    
def read_csv(file_path):
    data = []
    if os.path.exists(file_path):
        f = open(file_path, 'r', encoding='utf-8')
        with f:
            next(f)
            reader = csv.reader(f, delimiter=';')
            for row in reader:
                data.append(row)
    return data