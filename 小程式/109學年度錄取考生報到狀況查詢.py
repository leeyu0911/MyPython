# https://sites.google.com/a/chromium.org/chromedriver/home
# /Library/Frameworks/Python.framework/Versions/3.7/bin/chromedriver
# C:\Users\Yu\python37\Scripts
# pip3 install selenium

from selenium import webdriver
from selenium.webdriver.common.keys import Keys  
from time import sleep

url = 'https://nbk.acad.ncku.edu.tw/netcheckin/index.php?c=quall_rwd'
search = [{'exam_id': '2', 'group_no': '690'},  # [電資學院]資訊工程學系 [690]
         {'exam_id': '2', 'group_no': '270'},  # [電資學院]醫學資訊研究所 [270]
         {'exam_id': '2', 'group_no': '070'}]  # [電資學院]人工智慧科技碩士學位學程[070]

def open_url(i):
    driver.get(url)
    driver.find_element_by_xpath('//select[@name="exam_id"]' + f'//option[@value="{search[i].get("exam_id")}"]').click()
    driver.find_element_by_xpath('//select[@name="group_no"]' + f'//option[@value="{search[i].get("group_no")}"]').click()
    driver.find_element_by_name('B1').click()

def open_tab(i):
    driver.execute_script(f"window.open('about:blank', 'tab{i}');")
    driver.switch_to.window(f"tab{i}")


driver = webdriver.Chrome()
sleep(1)
driver.maximize_window()

for i in range(3):
    open_url(i)
    if i < 2:
        open_tab(i)
