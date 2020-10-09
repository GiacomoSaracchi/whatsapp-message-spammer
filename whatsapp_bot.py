#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 10:40:05 2020

@author: giacomosaracchi
"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import time
import os

# INSTRUCTIONS FOR USE

# Call MessageSpammer
# Use go_to_chat to access any chat
# Send one or multiple messages
# Quit chrome using done

# First class 'argument' (_3FRCZ in my case) is not the same across all phones
# Go on your whatsapp web page and inspect the message input box or the contact
# search box to find your own code
# This is relevant across all xpaths

# contact, message, driver_path and class_code are strings
# num_times is integer
# interval can be integer or float

# To print out your details stored in the class generator use 
    # print(MessageSpammer.__doc__)

class MessageSpammer:
    
    ''' Spam people on Whatsapp. Save your details below
    
My details:
driver_path = "/Users/giacomosaracchi/opt/anaconda3/pkgs/chromedriver"
personal_class_code = "_3FRCZ"
noot-noot mp3 = "/Users/giacomosaracchi/Documents/Coding/Python/Projects/Bots/WhatsappBot/noot-noot.mp3"
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
            raise Exception("Too many iterations. Whatsapp will block your number")
            
    def close(self):
        self.driver.quit()
