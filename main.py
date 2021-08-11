"""Tinder Swiping Bot

This script uses your Tinder account to
swipe right to match your account with other users. It is required
that the user has a Tinder and Facebook account so that the
user can sign in using their Facebook account.

This script requires that 'selenium', 'python_dotenv' be installed within the Python
environment you are running this script in.

"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
import datetime as dt
from dotenv import load_dotenv
import os

load_dotenv('.env')
TINDER_URL = 'https://tinder.com'
FACEBOOK_USER = os.getenv('FACEBOOK_USER')
FACEBOOK_PW = os.getenv('FACEBOOK_PW')
CHROME_DRIVER_EXECUTABLE = 'C:/Development/chromedriver.exe'

driver = webdriver.Chrome(CHROME_DRIVER_EXECUTABLE)
driver.get(TINDER_URL)
time.sleep(3)
login_element = driver.find_element_by_css_selector('#t-429325247 > div > div.App__body.H\(100\%\).Pos\(r\).Z\(0\) > div > main > div.H\(100\%\) > div > div > div > div > header > div > div.H\(100\%\).D\(f\).Ai\(c\) > div.H\(40px\).Px\(28px\) > button')
login_element.click()
time.sleep(5)
login_element = driver.find_element_by_css_selector('#t--1610880557 > div > div > div.Ta\(c\).H\(100\%\).D\(f\).Fxd\(c\).Pos\(r\) > div > div:nth-child(4) > span > div:nth-child(2) > button')
login_element.click()
time.sleep(5)
facebook_window_handle = driver.window_handles[1]
driver.switch_to_window(facebook_window_handle)
print(driver.title)
facebook_user_element = driver.find_element_by_id('email')
facebook_user_element.send_keys(FACEBOOK_USER)
facebook_pw_element = driver.find_element_by_id('pass')
facebook_pw_element.send_keys(FACEBOOK_PW)
facebook_login = driver.find_element_by_css_selector('#buttons label input')
facebook_login.click()
base_window_handle = driver.window_handles[0]
driver.switch_to_window(base_window_handle)
print(driver.title)
time.sleep(30)

# Step 4 Dismiss all requests

location_button = driver.find_element_by_css_selector('#t--1610880557 > div > div > div > div > div.Pb\(24px\).Px\(24px\).D\(f\).Fxd\(rr\).Ai\(st\) > button.button.Lts\(\$ls-s\).Z\(0\).CenterAlign.Mx\(a\).Cur\(p\).Tt\(u\).Ell.Bdrs\(100px\).Px\(24px\).Px\(20px\)--s.Py\(0\).Mih\(40px\).Pos\(r\).Ov\(h\).C\(\#fff\).Bg\(\$c-pink\)\:h\:\:b.Bg\(\$c-pink\)\:f\:\:b.Bg\(\$c-pink\)\:a\:\:b.Trsdu\(\$fast\).Trsp\(\$background\).Bg\(\$primary-gradient\).button--primary-shadow.StyledButton.Fw\(\$semibold\).focus-button-style.W\(225px\).W\(a\)')
location_button.click()
time.sleep(3)
not_interested_button = driver.find_element_by_css_selector('#t--1610880557 > div > div > div > div > div.Pb\(24px\).Px\(24px\).D\(f\).Fxd\(rr\).Ai\(st\) > button.button.Lts\(\$ls-s\).Z\(0\).CenterAlign.Mx\(a\).Cur\(p\).Tt\(u\).Ell.Bdrs\(100px\).Px\(24px\).Px\(20px\)--s.Py\(0\).Mih\(40px\).Fw\(\$semibold\).focus-button-style.W\(a\).C\(\$c-bluegray\)')
not_interested_button.click()
time.sleep(3)
try:
    maybe_later_button = driver.find_element_by_css_selector('#t--1610880557 > div > div > div > div.Px\(44px\).Px\(20px\)--s > button.button.Lts\(\$ls-s\).Z\(0\).CenterAlign.Mx\(a\).Cur\(p\).Tt\(u\).Ell.Bdrs\(100px\).Px\(24px\).Px\(20px\)--s.Py\(0\).Mih\(40px\).C\(\$c-secondary\).C\(\$c-base\)\:h.Fw\(\$semibold\).focus-button-style.D\(b\).My\(20px\).Mx\(a\)')
    maybe_later_button.click()
    time.sleep(3)
except NoSuchElementException:
    pass
finally:
    i_accept_button = driver.find_element_by_css_selector('#t-429325247 > div > div.Pos\(f\).Start\(0\).End\(0\).Z\(2\).Bxsh\(\$bxsh-4-way-spread\).B\(0\).Bgc\(\#fff\).C\(\$c-secondary\) > div > div > div:nth-child(1) > button')
    i_accept_button.click()
number_of_likes = 0
begin_time = time.time()
while True:
    try:
        like_button = driver.find_element_by_css_selector('#t-429325247 > div > div.App__body.H\(100\%\).Pos\(r\).Z\(0\) > div > main > div.H\(100\%\) > div > div > div.recsCardboard.W\(100\%\).Mt\(a\).H\(100\%\)--s.Px\(4px\)--s.Pos\(r\) > div.recsCardboard__cardsContainer.H\(100\%\).Pos\(r\).Z\(1\) > div.Pos\(r\).Py\(16px\).Py\(12px\)--s.Px\(4px\).Px\(8px\)--ml.D\(f\).Jc\(sb\).Ai\(c\).Maw\(375px\)--m.Mx\(a\).Pe\(n\).Mt\(-1px\) > div:nth-child(4) > button')
        like_button.click()
        time.sleep(2)
        try:
            close_match_button = driver.find_element_by_css_selector('#t-2080897886 > div > div > div.M\(a\).Expand.Pos\(r\).Fx\(\$flx1\).Pb\(36px\)--ml.Maw\(375px\)--ml.Mah\(620px\)--ml > div > div.Pos\(a\).T\(0\).P\(20px\).P\(12px\)--xs.End\(0\) > button')
            close_match_button.click()
        except NoSuchElementException:
            pass
        try:
            super_like_button = driver.find_element_by_css_selector('#t--1610880557 > div > div > button.button.Lts\(\$ls-s\).Z\(0\).CenterAlign.Mx\(a\).Cur\(p\).Tt\(u\).Ell.Bdrs\(100px\).Px\(24px\).Px\(20px\)--s.Py\(0\).Mih\(40px\).Fw\(\$semibold\).focus-button-style.D\(b\).My\(20px\).Mx\(a\)')
            super_like_button.click()
        except NoSuchElementException:
            pass
        try:
            not_interested_button = driver.find_element_by_css_selector('#t--1610880557 > div > div > div.Pt\(12px\).Pb\(8px\).Px\(36px\).Px\(24px\)--s > button.button.Lts\(\$ls-s\).Z\(0\).CenterAlign.Mx\(a\).Cur\(p\).Tt\(u\).Ell.Bdrs\(100px\).Px\(24px\).Px\(20px\)--s.Py\(0\).Mih\(42px\)--s.Mih\(50px\)--ml.C\(\$c-secondary\).C\(\$c-base\)\:h.Fw\(\$semibold\).focus-button-style.D\(b\).Mx\(a\)')
            not_interested_button.click()
        except NoSuchElementException:
            pass
        finally:
            number_of_likes += 1
            time.sleep(2)
    except ElementClickInterceptedException:
        end_time = time.time()
        duration = end_time - begin_time
        time_now = dt.datetime.now()
        print(f'Liked {number_of_likes} people. Time ended at {time_now}. Code ran for {duration}.')
        break


