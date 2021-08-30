import requests
from bs4 import BeautifulSoup

URL="https://www.saramin.co.kr/zf_user/search/recruit?search_area=main&search_done=y&search_optional_item=n&searchType=default_mysearch&searchword=PYTHON&recruitPage=1&recruitSort=relation&recruitPageCount=100&inner_com_type=&company_cd=0%2C1%2C2%2C3%2C4%2C5%2C6%2C7%2C9%2C10&quick_apply=&except_read="

def saram_page():
  saram=requests.get(URL)

  saram_soup=BeautifulSoup(saram.text,"html.parser")

  pagination=saram_soup.find("div",{'class':"pagination"})

  pages=pagination.find_all('a')

  spans=[]
  for page in pages[:-1]:
    spans.append(int(page.string))

  max_page=spans[-1]
  return max_page

def infor_job(html):
  title=html.find('h2',{'class':'job_tit'}).find("a")['title']
  company=html.find('strong',{'class':'corp_name'})
  anchor=company.find("a")
  if anchor is not None:
   com=str(anchor['title'])
  else:
    com=str(company.find['title'])
  location=html.find('div',{'class':'job_condition'}).find('a').string
  job_id=html['value']
  
  return {'title':title,'company':com,'location':location,'link':f"https://www.saramin.co.kr/zf_user/jobs/relay/view?isMypage=no&rec_idx={job_id}&recommend_ids=eJxVzrsBwzAIBNBp0oPgDlRnEO%2B%2FRXCCJaV8fA5cRgSpFyZe8fYvwT%2B6n%2FTAJjNNFnWwCkXvYU07dlNMcLIGFgWaqRdldPKg2HHo4dXZVJM4%2Bg%2B7L6QjOs7mVFjWo9QfrWSbgFg2a9fdfG4qFXNHeSjHelSQAbn5AYMwR6w%3D&view_type=search&searchword=PYTHON&searchType=default_mysearch&gz=1&t_ref_content=generic&t_ref=search&paid_fl=n#seq=0"} 



  

def extract_saram_job(last_page):
  jobs=[]
  for page in range(last_page):
    pages=page+1
    print(f'페이지개수:{pages}')
    sa=requests.get(f"https://www.saramin.co.kr/zf_user/search/recruit?search_area=main&search_done=y&search_optional_item=n&searchType=default_mysearch&searchword=PYTHON&recruitPage={pages}&recruitSort=relation&recruitPageCount=100&inner_com_type=&company_cd=0%2C1%2C2%2C3%2C4%2C5%2C6%2C7%2C9%2C10&quick_apply=&except_read=")
    soup=BeautifulSoup(sa.text,"html.parser")
    results=soup.find_all('div',{'class':'item_recruit'})

  for result in results:
    job=infor_job(result)
    jobs.append(job)

  return jobs
   # print(sa.status_code)

def saram_get_job():
  last_pages=saram_page()

  job=extract_saram_job(last_pages)
  return job
