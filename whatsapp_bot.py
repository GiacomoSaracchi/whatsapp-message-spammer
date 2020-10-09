#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 10:40:05 2020

@author: GiacomoSaracchi
"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import time
import os

class MessageSpammer:
    
    ''' 
Spam people on Whatsapp. Save your details below or incorporate them in the class on your own copy of this file
    
My details:
driver_path = "my_path"
personal_class_code = "my_class_code"
    '''

    def __init__(self, driver_path, personal_class_code):
        self.class_code = personal_class_code
        self.max_iter = 10
        options = webdriver.ChromeOptions()
        options.add_argument("--use-fake-ui-for-media-stream")
        self.driver = webdriver.Chrome(options=options, executable_path=driver_path)
        self.driver.get("https://web.whatsapp.com/")
        time.sleep(2)
        print(f"I'm on {self.driver.title}.\nScan QR code, then Return")
        # Input stops code until you click enter
        input()
    
    # Search for contact and go to their chat
    # Whatsapp automatically selects the input div to type messages
    def contact(self, contact):
        search_contact_xpath = f'//div[@class="{self.class_code} copyable-text selectable-text"][@contenteditable="true"][@data-tab="3"][@dir="ltr"]'
        search_box = WebDriverWait(self.driver, 10).until(lambda driver:
            driver.find_element_by_xpath(search_contact_xpath))
        search_box.click()
        search_box.send_keys(contact, Keys.RETURN)
    
    # Send a single message to a chat
    def send_message(self, message):
        msg_box_xpath = f'//div[@class="{self.class_code} copyable-text selectable-text"][@contenteditable="true"][@data-tab="1"][@dir="ltr"][@spellcheck="true"]'
        input_box = WebDriverWait(self.driver, 10).until(lambda driver:
            driver.find_element_by_xpath(msg_box_xpath))
        input_box.send_keys(message + Keys.RETURN)
    
    # Send a single audio message to a chat
    def send_audio(self, mp3_path=None):
        start_recording = WebDriverWait(self.driver, 10).until(lambda driver: 
                driver.find_element_by_xpath("//button[@class='_2r1fJ']"))
        start_recording.click()
        ss_buttons = WebDriverWait(self.driver, 10).until(lambda driver: 
                driver.find_elements_by_class_name("gyFxq"))
        stop_audio = ss_buttons[0]
        send_audio = ss_buttons[1]
        if mp3_path is not None:
            time.sleep(0.5)
            os.system(f"afplay {mp3_path}")
        decision = input("Send? [y/n]")
        if decision == "y":
            # Slow. Adds a couple of seconds to voice messages. Needs improvement
            ActionChains(self.driver).move_to_element(send_audio).click().perform()
        else:
            ActionChains(self.driver).move_to_element(stop_audio).click().perform()
    
    # Send a number of messages to a chat
    def spam_message(self, message, num_times, interval):
        if num_times <= self.max_iter:
            for i in range(num_times):
                self.send_message(message)
                time.sleep(interval)
        else:
            raise Exception("Too many iterations. Whatsapp may block your number")
            
    def close(self):
        self.driver.quit()
