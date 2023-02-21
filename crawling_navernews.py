from bs4 import BeautifulStoneSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support import expected_conditions as EC
import requests
import time
import pyautogui as pg

driver = webdriver.Chrome()
url = 'https://news.naver.com/main/ranking/popularMemo.naver'
driver.get(url)

# 기사1
n1 = driver.find_element(By.XPATH, '//*[@id="wrap"]/div[4]/div[2]/div/div[1]/ul/li[1]/div/a')
n1.click()

t1 = driver.find_element(By.XPATH, '//*[@id="title_area"]/span').text

# 정치섹션 기사의 본문 하단에는 댓글 서비스를 제공하지 않음
if driver.find_element(By.XPATH, '//*[@id="cbox_module"]/div/div/a[1]') :
    comments_link = driver.find_element(By.XPATH, '//*[@id="cbox_module"]/div/div/a[1]').click()
    # comments_link.click()
else :
    pass

# Wait 후 댓글스크랩
driver.implicitly_wait(time_to_wait=20)
c1  = driver.find_element(By.XPATH,'//*[@id="cbox_module_wai_u_cbox_content_wrap_tabpanel"]/ul/li[1]/div[1]/div/div[2]/span[1]').text
c1g = driver.find_element(By.XPATH,'//*[@id="cbox_module_wai_u_cbox_content_wrap_tabpanel"]/ul/li[1]/div[1]/div/div[4]/div/a[1]/em').text
c1b = driver.find_element(By.XPATH,'//*[@id="cbox_module_wai_u_cbox_content_wrap_tabpanel"]/ul/li[1]/div[1]/div/div[4]/div/a[2]/em').text

c2  = driver.find_element(By.XPATH,'//*[@id="cbox_module_wai_u_cbox_content_wrap_tabpanel"]/ul/li[2]/div[1]/div/div[2]/span[1]').text
c2g = driver.find_element(By.XPATH,'//*[@id="cbox_module_wai_u_cbox_content_wrap_tabpanel"]/ul/li[2]/div[1]/div/div[4]/div/a[1]/em').text
c2b = driver.find_element(By.XPATH,'//*[@id="cbox_module_wai_u_cbox_content_wrap_tabpanel"]/ul/li[2]/div[1]/div/div[4]/div/a[2]/em').text

c3  = driver.find_element(By.XPATH,'//*[@id="cbox_module_wai_u_cbox_content_wrap_tabpanel"]/ul/li[3]/div[1]/div/div[2]/span[1]').text
c3g = driver.find_element(By.XPATH,'//*[@id="cbox_module_wai_u_cbox_content_wrap_tabpanel"]/ul/li[3]/div[1]/div/div[4]/div/a[1]/em').text
c3b = driver.find_element(By.XPATH,'//*[@id="cbox_module_wai_u_cbox_content_wrap_tabpanel"]/ul/li[3]/div[1]/div/div[4]/div/a[2]/em').text

c4  = driver.find_element(By.XPATH,'//*[@id="cbox_module_wai_u_cbox_content_wrap_tabpanel"]/ul/li[4]/div[1]/div/div[2]/span[1]').text
c4g = driver.find_element(By.XPATH,'//*[@id="cbox_module_wai_u_cbox_content_wrap_tabpanel"]/ul/li[4]/div[1]/div/div[4]/div/a[1]/em').text
c4b = driver.find_element(By.XPATH,'//*[@id="cbox_module_wai_u_cbox_content_wrap_tabpanel"]/ul/li[4]/div[1]/div/div[4]/div/a[1]/em').text

c5  = driver.find_element(By.XPATH,'//*[@id="cbox_module_wai_u_cbox_content_wrap_tabpanel"]/ul/li[5]/div[1]/div/div[2]/span[1]').text
c5g = driver.find_element(By.XPATH,'//*[@id="cbox_module_wai_u_cbox_content_wrap_tabpanel"]/ul/li[5]/div[1]/div/div[4]/div/a[2]/em').text
c5b = driver.find_element(By.XPATH,'//*[@id="cbox_module_wai_u_cbox_content_wrap_tabpanel"]/ul/li[5]/div[1]/div/div[4]/div/a[2]/em').text


# 정치기사는 '댓글보기' 눌러서 이동해야하고
# '순공감순'배열이 아닌 '최신순'배열인 기사도 있다
# 'alert 창 크기 변경 가능한지?'
alertbox = pg.alert(title='댓글 스크랩',text='제목:{0}\n댓글1[{1}/{2}]:{3}\n댓글2[{4}/{5}]:{6}\n댓글3[{7}/{8}]:{9}\n댓글4[{10}/{11}]:{12}\n댓글5[{13}/{14}]:{15}'.format(t1, c1g,c1b,c1, c2g,c2b,c2, c3g,c3b,c3, c4g,c4b,c4, c5g,c5b,c5),button='OK')

# driver.back()


# #기사2
# n2 = driver.find_element(By.XPATH, '//*[@id="wrap"]/div[4]/div[2]/div/div[1]/ul/li[2]/div/a')
# n2.click()
# driver.back()

# #기사3
# n3 = driver.find_element(By.XPATH, '//*[@id="wrap"]/div[4]/div[2]/div/div[1]/ul/li[3]/div/a')
# n3.click()
# driver.back()

# #기사4
# n4 = driver.find_element(By.XPATH, '//*[@id="wrap"]/div[4]/div[2]/div/div[1]/ul/li[4]/div/a')
# n4.click()
# driver.back()

# #기사5
# n5 = driver.find_element(By.XPATH, '//*[@id="wrap"]/div[4]/div[2]/div/div[1]/ul/li[5]/div/a')
# n5.click()
# driver.back()