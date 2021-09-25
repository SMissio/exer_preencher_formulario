#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from selenium import webdriver as opSeleneium
from selenium.webdriver.common.keys import Keys
import pyautogui as tempoEspera

navegadorform = opSeleneium.Chrome()
navegadorform.get("https://pt.surveymonkey.com/r/J3TFMVK")


tempoEspera.sleep(3)

navegadorform.find_element_by_name("708067749").send_keys("Sylvia Missio")
tempoEspera.sleep(1)
navegadorform.find_element_by_name("708067895").send_keys("hssmissio@hotmail.com")
tempoEspera.sleep(1)
navegadorform.find_element_by_name("708067938").send_keys("(00)000000000")
tempoEspera.sleep(1)
navegadorform.find_element_by_name("708068386").send_keys("Python")
tempoEspera.sleep(1)
navegadorform.find_element_by_id("708068326_4657067886_label").click()

tempoEspera.sleep(7)
navegadorform.find_element_by_xpath('//*[@id="patas"]/main/article/section/form/div[2]/button').click()


