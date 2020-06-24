#!/usr/bin/env python3
#Alisher Yokubjonov
from selenium import webdriver
from selenium.webdriver.common.keys import Keys  
from selenium.webdriver.common.by import By
import random as r
import string
import time 
import names as n 

data_right_answers=[] 
data_qus=0 # number questions

#Note: there is no support for kahoots with random nick generators yet. 
#There is no support for kahoots with open ended questions 
#There is no support for kahoots with bolded text and or untraditional symbols(emojis are included I think).


def collect_data(link, code):
    global data_qus, data_right_answers
    driver = webdriver.Chrome(executable_path='/home/alisher/Desktop/IB/Drivers/chromedriver')
    dummy=0
    driver.get(link)
    if link=='https://kahoot.it/': 
        #if link is not given
        button = driver.find_element_by_xpath('//*[@id="game-input"]')
        button.send_keys(code)
        button = driver.find_element_by_xpath("//*[text()='Enter']")
        button.click()
    #Set nickname
    while not driver.find_elements_by_xpath('//*[@id="nickname"] '): 
        dummy+=1
    button = driver.find_element_by_xpath('//*[@id="nickname"] ')
    button.send_keys(str(r.randint(0,100000))) #The name the bot will have

    # Submit nick and start
    while not driver.find_element_by_xpath('//*[@id="challenge-game-router"]/main/section/div[1]/form/button'):
        dummy+=1
    button = driver.find_element_by_xpath('//*[@id="challenge-game-router"]/main/section/div[1]/form/button')
    button.click()
    time.sleep(8)
    while not driver.find_elements_by_xpath("//*[text()='You have completed the challenge']"): #Not completed 
        page_num= data_qus % 2
        page_num_reverse= (data_qus+1) % 2 
        while not driver.find_elements_by_xpath("//*[@id='challenge-game-router']/main/div[2]/div[1]"): #While can't press an option 
            dummy+=1                                                                                  
        button = driver.find_element_by_xpath("//*[@id='challenge-game-router']/main/div[2]/div[1]")
        button.click() 
        button = driver.find_element_by_xpath("//*[@id='check']/../../..") 
        data_right_answers.append('"'+button.text+'"') #append right answers!!!! 
        print("Correct Answer: "+str(button.text))
        data_qus+=1
        driver.find_element_by_xpath("//*[text()='Next']").click()
        try: 
            button= driver.find_element_by_xpath("//*[text()='Next']")
            button.click()
        except: 
            if driver.find_elements_by_xpath("//*[text()='You have completed the challenge']"): 
                break 
            
    print("DATA HAS BEEN COLLECTED")
    print(data_right_answers)
    driver.close()
    return 
    

##########################################################################################################################################################################################

##########################################################################################################################################################################################

##########################################################################################################################################################################################

##########################################################################################################################################################################################


def kahoot(link, code, your_name):
    driver = webdriver.Chrome(executable_path='/home/alisher/Desktop/IB/Drivers/chromedriver')
    question=0
    dummy=0
    person= your_name #Your name 
    driver.get(link) 

    if link=='https://kahoot.it/': 
        #if link is not given
        button = driver.find_element_by_xpath('//*[@id="game-input"]')
        button.send_keys(code)
        button = driver.find_element_by_xpath('/html/body/div/div/div/div/main/div/form/button')
        button.click()
        
    #Set nickname
    while not driver.find_elements_by_xpath('//*[@id="nickname"]'): 
        dummy+=1
    button = driver.find_element_by_xpath('//*[@id="nickname"]')
    button.send_keys(person)

    # Submit nick and start
    button = driver.find_element_by_xpath('/html/body/div/div/div/div/main/section/div[1]/form/button')
    button.click()
    time.sleep(8)

    #Question
    while question < data_qus-1: 
        complete= int((question/data_qus)*100)
        print(str(complete)+"% complete")
        path= "//*[text()="+data_right_answers[question]+"]" 
        while not driver.find_elements_by_xpath(path): 
            dummy+=1
        button= driver.find_element_by_xpath(path)
        button.click()
        #Next 1
        while not driver.find_elements_by_xpath("//*[text()='Next']"): 
            dummy+=1
        button= driver.find_element_by_xpath("//*[text()='Next']").click()
        #Next 2
        try: 
            driver.find_element_by_xpath("//*[text()='Next']").click() 
        except: 
            dummy+=1
            
        question+=1

    complete= int((question/data_qus)*100)
    print(str(complete)+"% complete")
    path= "//*[text()="+data_right_answers[question]+"]" 
    (driver.page_source).encode('ascii', 'ignore')
    while not driver.find_elements_by_xpath(path): 
        dummy+=1 
    driver.find_element_by_xpath(path).click()
    while not driver.find_elements_by_xpath("//*[text()='Next']"): 
        dummy+=1    
    driver.find_element_by_xpath("//*[text()='Next']").click()     
    print("100% complete") 
    print("K A H O O T   C O M P L E T E D   S U C C E S S F U L L Y ! ! !")
    time.sleep(10) #allows you to look at the score you got. You should get all answers correct but if you do not email me at 'ekubjanov2016@gmail.com'. My guess would be either the questions have weird symbols or there are open ended questions.
    driver.close()
    return 



def complete(link, code, your_name): 
    collect_data(link, str(code)) #Collect answers
    kahoot(link, str(code), your_name) #Answer questions
    return

#Input the code or link below, then run the script. Make sure you have installed Selenium. (pip install selenium)

complete('https://kahoot.it/challenge/02458870?challenge-id=813074e7-44c0-451a-9982-624a5bd2fbfa_1591016300706', '0434421', 'Alisher') #If you're not using the link as invitation, leave it as 'https://kahoot.it/'. ('kahoot.it' will send an error as the WebDriver requires https:// and stuff)
