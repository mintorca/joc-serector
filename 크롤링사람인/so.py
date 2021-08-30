import requests
from bs4 import BeautifulSoup

URL = "https://bme.konyang.ac.kr/cop/bbs/BBSMSTR_000000000273/selectBoardList.do?bbsId=BBSMSTR_000000000273&pageIndex=1&kind=&searchCnd=&searchWrd="


def get_last_page():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")
    pages = soup.find('ul', {'class': 'paginate'}).find_all('a')
    last_pages = pages[-3].string
    return int(last_pages)


def ex_job(html):
    ky='https://bme.konyang.ac.kr/'
    k='건양'
    s='의공'
    title = html.find('span', {'class': 'link'}).string
    adr = html.find('a')['href']
    
    return {'title': title,'학교':k,'학과':s,'adress':f'{ky}{adr}'}


def extract_job(last_page):
    jobs = []
    for page in range(last_page):
      
        pages = page + 1
        print(f'건양파일:{pages}')
        result = requests.get(
            f'https://bme.konyang.ac.kr/cop/bbs/BBSMSTR_000000000273/selectBoardList.do?bbsId=BBSMSTR_000000000273&pageIndex={pages}&kind=&searchCnd=&searchWrd='
        )
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all('div', {'class': 'list_subject'})
        for result in results:
            job = ex_job(result)
            jobs.append(job)
        return jobs


def get_jobs():
    last_page = get_last_page()
    jobs = extract_job(last_page)
    return jobs
