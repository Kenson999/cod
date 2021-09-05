#https://medium.com/marketingdatascience/selenium教學-一-如何使用webdriver-send-keys-988816ce9bed
# 動態網頁爬蟲第一道鎖 — Selenium教學：如何使用Webdriver、send_keys(附Python 程式碼)
# Clarissa RJ Tai
# Oct 6, 2020 
# 本篇文章會依序介紹以下7大步驟，
# 讓大家可以依此打開動態網頁爬蟲第一道鎖:
# Selenium 介紹# Selenium 安裝# Webdriver 下載# Chromedriver使用
# 使用Selenium輸入及點擊# send_keys模擬鍵盤輸入# 瀏覽紀錄
# 1. Selenium 介紹
# Selenium提供了一個簡單的API應用程式介面（英語：Application Programming Interface），
# 使用者可以利用Selenium Webdriver 編寫功能及測試。
# 2. Selenium 安裝
# 在python裡執行以下程式碼，即可安裝Selenium套件。
# pip install selenium
# 3. Webdriver 下載
# 要使用Selenium爬蟲前，Webdriver是必備的，而不同的瀏覽器會有不同的driver。
# 以下提供四種常見的瀏覽器driver供大家參考及下載。
# Chrome
# https://sites.google.com/a/chromium.org/chromedriver/downloads
# Edge
# Firefox
# Safari
# 選定了瀏覽器，在下載前，請記得檢查目前的瀏覽器版本，再下載對應的Webdriver，
# 之後也要適時更新版本以維護程式碼運行喔！
# 4. Chromedriver 使用
# 載入需要的套件
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
# 開啟瀏覽器視窗(Chrome)
#driver = webdriver.Chrome()
# 方法二：或是直接指定exe檔案路徑
# option = webdriver.ChromeOptions()
# 防止打印一些无用的日志
# option.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging'])
driver = webdriver.Chrome("C:\Program Files\Google\Chrome\Application\chromedriver.exe")
driver.maximize_window()
#雖這裡只提供了Chromedriver的程式碼範例給大家，但是不用擔心~
# 若是想要運用以上其他的瀏覽器，那只要在瀏覽器的名稱上作更改，其他的方法幾乎一樣，如下程式碼。
# 有興趣的同好，可以多試幾個不同的瀏覽器方法。
# driver = webdriver.Firefox()
# driver = webdriver.Safari()
# 開啟網頁後，使用get()輸入網址，即可前往特定網頁。close()則可關閉目前網頁視窗。

driver.get("http://www.google.com") # 更改網址以前往不同網頁
# driver.close() # 關閉瀏覽器視窗
# 5. 使用Selenium輸入及點擊
# 可以使用在網頁需要輸入某個字串才能執行下一步驟時，
# 例如：輸入帳號密碼、搜尋特定關鍵字等等。
# 以google首頁為例，假設:
# 我們需要搜索關鍵字「Selenium Python」，那就必須先找到搜尋框的網頁元素(Web element)
#程式碼如下：
# 定位搜尋框
element = driver.find_element_by_class_name("gLFyf.gsfi")
# 傳入字串
element.send_keys("Selenium Python")
#driver.find_element_by_name("q").send_keys("Selenium Python")
#回到受Webdriver控制的網頁，神奇的事情發生了！搜尋框裡有文字了
#如果想要刪掉原先已經輸入的文字，可以使用clear()清除網頁元素原先的字串或搜索詞。
n=3
while n>0:
    if n==0:
        break
    time.sleep(1)
    element.clear()
    element.send_keys(n)
    time.sleep(1)
    n-=1
element.clear()
element.send_keys("Kenson Chan's first crawler")
time.sleep(2)
#那填入關鍵字之後，要怎麼點擊搜尋按鈕呢？
element.send_keys(Keys.ENTER)
# element.send_keys(Keys.ENTER)
# button = driver.find_element_by_class_name("gNO89b")
# button.click()
# driver.find_element_by_class_name("gNO89b").click()
# driver.find_element_by_tag_name("btnK").click()
# driver.find_element_by_css_selector("input[type='submit'][value='Google 搜尋']").click()
# driver.find_element_by_xpath("//label[contains(text(),'Google 搜尋')]").click()
# driver.find_element_by_partial_link_text("Google 搜尋").click()
#執行以上程式碼之後網頁就會點擊搜尋按鈕並前往搜尋頁面(注意：搜尋框裡要有東西)。
