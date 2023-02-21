import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# [함수] 브라우저 기다리기  #time.sleep(n)은 다른 방법
def wait_until(xpath_str):
    WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.XPATH, xpath_str)))

browser = webdriver.Chrome()
# browser.maximize_window()

url = 'https://flight.naver.com/'
browser.get(url)

#팝업창닫기
wait_until('//*[@id="__next"]/div/div[1]/div[9]/div/div[2]/button[2]')
first_close = browser.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div[9]/div/div[2]/button[2]')    #//두번은 HTML문서전체
first_close.click()

#날짜선택
begin_date = browser.find_element(By.XPATH, '//button[text() = "가는 날"]')
begin_date.click()

#출발:27일선택
wait_until( '//b[text() = "27"]')
day27 = browser.find_elements(By.XPATH, '//b[text() = "27"]')   #element's'가 붙어서 [0]을 붙혀야함 
day27[0].click()    #len(day27)로 확인 가능

#도착:31일선택
wait_until('//b[text() = "31"]' )
day31 = browser.find_elements(By.XPATH, '//b[text() = "31"]')
day31[0].click()

#도착지선택
wait_until('//b[text() = "도착"]' )
arrival = browser.find_elements(By.XPATH, '//b[text() = "도착"]')
arrival[0].click()

wait_until('//button[text() = "국내"]')
domestic = browser.find_element(By.XPATH, '//button[text() = "국내"]')
domestic.click()

wait_until('//i[contains(text(), "제주국제공항")]')
jeju = browser.find_elements(By.XPATH, '//i[contains(text(), "제주국제공항")]')
jeju[0].click()

#항공권검색
wait_until('//span[contains(text(), "항공권 검색")]')
search = browser.find_elements(By.XPATH, '//span[contains(text(), "항공권 검색")]')
search[0].click()

#결과출력
elem = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.XPATH, '//div[@class="domestic_Flight__sK0eA result"]')))
print('\n')
print(elem.text)

#종료
input('\n종료하려면 Enter 키를 입력하세요')
browser.quit()