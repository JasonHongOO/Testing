# import undetected_chromedriver as uc
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.keys import Keys

# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager

import random
import time
import sys
# import pyperclip
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# def ShrotUrl(driver, CurUrl):
#     r_min = 0.5
#     r_max = 2
#     WebUrl = 'https://www.ifreesite.com/shorturl/' 
#     #======================  輸入網址  ===========================
#     driver.get(WebUrl)
#     UrlField = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//form[@action='https://tinyurl.com/api-create.php']//input[@name='url']"))) 
#     UrlField.click()
#     time.sleep(round(random.uniform(r_min, r_max), 2))
#     UrlField.send_keys(  CurUrl  )
#     time.sleep(round(random.uniform(r_min, r_max), 2))

#     ConfirmBtn = driver.find_element(By.XPATH, "//form[@action='https://tinyurl.com/api-create.php']//input[@name='submit']")   
#     ConfirmBtn.click()
#     time.sleep(round(random.uniform(r_min, r_max), 2))

#     driver.switch_to.window(driver.window_handles[1])
#     Href = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//pre"))).text
#     return Href

# def youtube(driver, TargetUrl, Quality):
#     r_min = 0.5
#     r_max = 2
#     WebUrl = 'https://x2download.app/zh-tw22'
#     #======================  輸入網址  ===========================
#     #進入指定網址
#     driver.get(WebUrl)
#     #定義一個物件，以name標籤找到youtube的關鍵字搜尋欄位
#     UrlField = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@type = 'search']")))
#     UrlField.click()
#     time.sleep(round(random.uniform(r_min, r_max), 2))
#     UrlField.send_keys(  TargetUrl  )
#     time.sleep(round(random.uniform(r_min, r_max), 2))

#     ConfirmBtn = driver.find_element(By.XPATH, "//button[@class = 'btn-red']")
#     ConfirmBtn.click()
#     time.sleep(round(random.uniform(r_min, r_max), 2))

#     #======================  輸入網址  ===========================
#     if Quality == 0:
#         QualityBtn = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//option[@value = '360p']")))
#     elif Quality == 1:
#         QualityBtn = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//option[@value = '720p']")))
#     QualityBtn.click()
#     time.sleep(round(random.uniform(r_min, r_max), 2))

#     ConfirmBtn = driver.find_element(By.XPATH, "//button[@id = 'btn-action']")
#     ConfirmBtn.click()
#     time.sleep(round(random.uniform(r_min, r_max), 2))

#     Target = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[@id = 'asuccess'][@class = 'form-control mesg-convert success']")))
#     Href = Target.get_attribute("href")
#     return Href

# def FB(driver, TargetUrl, Quality):
#     r_min = 0.5
#     r_max = 2
#     WebUrl = 'https://fdown.net/'
#     #======================  輸入網址  ===========================
#     #進入指定網址
#     driver.get(WebUrl)
#     #定義一個物件，以name標籤找到youtube的關鍵字搜尋欄位
#     UrlField = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@name = 'URLz']")))
#     UrlField.click()
#     time.sleep(round(random.uniform(r_min, r_max), 2))
#     UrlField.send_keys(  TargetUrl  )
#     time.sleep(round(random.uniform(r_min, r_max), 2))

#     ConfirmBtn = driver.find_element(By.XPATH, "//button[@type = 'submit']")
#     ConfirmBtn.click()
#     time.sleep(round(random.uniform(r_min, r_max), 2))
#     #======================  輸入網址  ===========================
#     if Quality == 0:
#         Target = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[@class = 'btn btn-primary btn-sm'][@id ='sdlink']")))
#     elif Quality == 1:
#         Target = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[@class = 'btn btn-primary btn-sm'][@id ='hdlink']")))
    
#     Href = Target.get_attribute("href")
#     return Href

# def OpenSite():

#     #建立chrome設定
#     # chromeOption = uc.ChromeOptions()
#     chromeOption = Options()
#     #設定瀏覽器的user agent
#     # chromeOption.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0')
    
#     chromeOption.add_argument("start-maximized")
#     # chromeOption.add_argument('window-size=1920x1080')
#     # chromeOption.add_argument('--headless')
#     chromeOption.add_argument("--disable-gpu")  # 確保 GPU 加速關閉
#     chromeOption.add_argument('--no-sandbox')
#     chromeOption.add_argument('--disable-dev-shm-usage')
#     #開啟Chrome瀏覽器
#     # driver = uc.Chrome(service=Service(ChromeDriverManager().install()), options=chromeOption)
#     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chromeOption)
#     #調整瀏覽器視窗大小
#     # driver.maximize_window()    #全螢幕
#     driver.set_window_size(1024, 960)
#     return driver


    

def VideoUrlDecoder(msg, Quality):
    TargetUrl = msg
    
    try :
        # driver = OpenSite()

        print("取得連結")
        # if "youtube.com" in msg:
        #     Href = youtube(driver, TargetUrl, Quality)
        # elif "facebook.com" in msg:
        #     Href = FB(driver, TargetUrl, Quality)
        print("取得連結完畢")

        Href =  'https://www.google.com/search?q=google+%E7%99%BB%E5%85%A5&oq=&gs_lcrp=EgZjaHJvbWUqCQgAEEUYOxjCAzIJCAAQRRg7GMIDMgkIARBFGDsYwgMyCQgCEEUYOxjCAzIJCAMQRRg7GMIDMgkIBBBFGDsYwgMyCQgFEEUYOxjCAzIJCAYQRRg7GMID0gEJMTAwNjFqMGo3qAIHsAIB&sourceid=chrome&ie=UTF-8'
        
        print("取得短網址")
        # result = ShrotUrl(driver, Href)
        print("取得短網址完畢") 

        # driver.close()

        # print(result)
        return Href
    except Exception as e:
        print("Error : ",e)

    

if __name__ == "__main__":
    msg = 'https://www.youtube.com/watch?v=VD1wbRf70XY'
    VideoUrlDecoder(msg,0)
    












# backup
# def ShrotUrl(driver, CurUrl):
#     r_min = 0.5
#     r_max = 2
#     WebUrl = 'https://picsee.io/' 
#     #======================  輸入網址  ===========================
#     driver.get(WebUrl)
#     UrlField = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@type = 'url']"))) 
#     UrlField.click()
#     time.sleep(round(random.uniform(r_min, r_max), 2))
#     UrlField.send_keys(  CurUrl  )
#     time.sleep(round(random.uniform(r_min, r_max), 2))

#     ConfirmBtn = driver.find_element(By.XPATH, "//button[@class = 'btn btn btn-fill btn-md btn-shorten-link animated fadeInDown btn-none']")   
#     ConfirmBtn.click()

#     WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//span[text() = '關閉並取得縮網址']"))).click()
#     time.sleep(round(random.uniform(r_min, r_max), 2))
#     WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[@class = 'btn btn-fill btn-none btn-sm']"))).click()
#     time.sleep(round(random.uniform(r_min, r_max), 2))
#     Href = pyperclip.paste()
#     return Href