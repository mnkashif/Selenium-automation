from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
import time
import getpass

driver=webdriver.Firefox()
driver.set_page_load_timeout("10")
driver.get("http://www.youtube.com")
driver.maximize_window()

body=driver.find_element_by_xpath('/html/body')
body.send_keys(Keys.CONTROL + 't')
time.sleep(3)
sgn = driver.find_element_by_link_text("SIGN IN")
sgn.click()
#tree=raw_input("Do yo have an existing account Yes or No ")
'''if tree=="No":
    driver.find_element_by_css_selector('.oG5Srb').click()
    kgf=driver.find_element_by_css_selector('#firstName')
    t=raw_input("")
    kgf.send_keys(t)
    kgl=driver.find_element_by_css_selector('#lastName')
    b=raw_input("")
    kgl.send_keys(b)
    driver.find_element_by_css_selector('.uBOgn').click()
    kg=driver.find_element_by_css_selector('#username')
    f=raw_input("")
    kg.send_keys(f)
    kgp=driver.find_element_by_css_selector('#passwd > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > input:nth-child(1)')
    r=raw_input("")
    kgp.send_keys(r)
    kgp1=driver.find_element_by_css_selector('#confirm-passwd > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > input:nth-child(1)')
    o=raw_input("")
    kgp1.send_keys(o)
    klpt=driver.find_element_by_css_selector('#accountDetailsNext')
    klpt.click()
    klpt1=driver.find_element_by_css_selector('#phoneNumberId')
    v=raw_input("")
    klpt1.send_keys(v)
    driver.find_element_by_css_selector('#gradsIdvPhoneNext').click()
    r=raw_input("")
    driver.find_element_by_css_selector('#code').send_keys(r)
    driver.find_element_by_css_selector('#gradsIdvVerifyNext > content > span').click()
    e=raw_input("")
    driver.find_element_by_css_selector('#day').send_keys(e)
    m=raw_input("")
    driver.find_element_by_css_selector('#year').send_keys(m)
    k=raw_input("")
    el=driver.find_element_by_css_selector('#month')
    for option in el.find_elements_by_tag_name('option'):
        if option.text==k:
            option.click()
            break
    n=raw_input("Male or Female")
    el1=driver.find_element_by_css_selector('#gender')
    for options in el1.find_elements_by_tag_name('option'):
        if options.text==n:
            options.click()
            break
    driver.find_element_by_css_selector('#personalDetailsNext').click()
    WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[2]/div[1]/div[2]/form/div[2]/div/div[2]/div[1]/div[2]')));
    driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div[2]/form/div[2]/div/div[2]/div[1]/div[2]').click()
    #driver.find_element_by_css_selector('#termsofserviceNext > content:nth-child(3)').click()
    driver.find_element_by_css_selector('.xjKiLb > span:nth-child(1) > svg:nth-child(1)').click()
    driver.find_element_by_css_selector('.xjKiLb > span:nth-child(1) > svg:nth-child(1)').click()
    driver.find_element_by_css_selector('#termsofserviceNext').click()'''


sgn1=raw_input('enter email ')
sgn2=driver.find_element_by_xpath('//*[@id="identifierId"]')
sgn2.send_keys(sgn1)
sgn2.send_keys(Keys.ENTER)
pss1=getpass.getpass("enter gmail password")
pss=driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
pss.send_keys(pss1)
pss.send_keys(Keys.ENTER)
'''def addch():
    ben="Yes"
    while ben=="Yes":
        ben=raw_input("Do you want to subscribe to any new channel?  ")
        if ben=="Yes":
            e=raw_input("Which Channel? ")
            driver.get('https://www.youtube.com/results?search_query='+e)
    #tre=driver.find_element_by_css_selector('#search').send_keys(e)
            try: 
                driver.find_element_by_xpath('/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[2]/ytd-channel-renderer/div/ytd-subscribe-button-renderer').click()
            except:
                print "Channel not found"
    
        

addch()'''
driver.implicitly_wait(10)
sbs=WebDriverWait(driver,10).until(expected_conditions.element_to_be_clickable((By.XPATH,'//*[@id="endpoint"and @title="Subscriptions"]')))
sbs.click()
time.sleep(2)

def videos(id):
    driver.get(id)
    driver.find_element_by_css_selector('ytd-button-renderer.style-scope:nth-child(4) > a:nth-child(1) > yt-icon-button:nth-child(1) > button:nth-child(1)').click()

lst=driver.find_element_by_css_selector('ytd-browse.style-scope:nth-child(2) > ytd-two-column-browse-results-renderer:nth-child(7) > ytd-section-list-renderer:nth-child(1) > div:nth-child(2) > ytd-item-section-renderer:nth-child(1) > div:nth-child(3) > ytd-shelf-renderer:nth-child(1) > div:nth-child(1) > div:nth-child(2) > ytd-grid-renderer:nth-child(1)')
lst1=lst.find_elements_by_tag_name('ytd-grid-video-renderer')

lst2=[]
for i in range(len(lst1)):
    lst2.insert(i,'')
    lst2[i]=lst1[i].find_element_by_tag_name('h3').find_element_by_tag_name('a').get_attribute('href')
print len(lst2)

for video in range(len(lst2)):
    if video==0:
        videos(lst2[video])
        driver.find_element_by_css_selector('paper-item.ytd-compact-link-renderer').click()
        play=driver.find_element_by_css_selector('#input-1')
        z=raw_input("enter playlist name")
        play.send_keys(z)
        driver.find_element_by_css_selector('iron-icon.style-scope').click()
        driver.find_element_by_css_selector('ytd-privacy-dropdown-item-renderer.style-scope:nth-child(3) > paper-item:nth-child(1) > paper-item-body:nth-child(1)').click()
        driver.find_element_by_css_selector('ytd-button-renderer.ytd-add-to-playlist-create-renderer > a:nth-child(1) > paper-button:nth-child(1)').click()
    else:
        time.sleep(2)
        videos(lst2[video])
        WebDriverWait(driver,10).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,'ytd-playlist-add-to-option-renderer.style-scope:nth-child(2) > paper-checkbox:nth-child(1) > div:nth-child(1)'))).click()
        #driver.find_element_by_css_selector('ytd-playlist-add-to-option-renderer.style-scope:nth-child(2) > paper-checkbox:nth-child(1) > div:nth-child(1)').click()



driver.find_element_by_css_selector('yt-icon-button.ytd-masthead:nth-child(3) > button:nth-child(1)').click()
driver.find_element_by_css_selector('#header-entry > a:nth-child(1)').click()
driver.find_element_by_css_selector('#playlist-thumbnails').click()

     

