from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge import service
from selenium.webdriver.support.ui import Select

from lxml import objectify

import os
os.system("cls") #clear screen from previous sessions
import time

options = webdriver.EdgeOptions()
options.use_chromium = True
options.add_argument("start-maximized")
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")
my_service=service.Service(r'msedgedriver.exe')
options.page_load_strategy = 'eager' #do not wait for images to load
options.add_experimental_option("detach", True)
options.add_argument('--no-sandbox')
#options.add_argument('--disable-dev-shm-usage') # uses disk instead of RAM, may be slow

s = 30 #time to wait for a single component on the page to appear, in seconds; increase it if you get server-side errors «try again later»

driver = webdriver.Edge(service=my_service, options=options)
action = ActionChains(driver)
wait = WebDriverWait(driver,s)

username = "the_best_professor_in_the_world"
password = "Super_Mega_Password"
login_page = "https://moodle.rea.perm.ru/login/index.php"
course_page = "https://moodle.rea.perm.ru/question/edit.php?cmid=36423"
question_url = "https://moodle.rea.perm.ru/question/bank/editquestion/question.php?courseid=143&sesskey=NwJlX3IhPz&qtype=multichoice&returnurl=%2Fquestion%2Fedit.php%3Fcmid%3D36423&cmid=36423&category=375"

def scroll_to_bottom(): 
    reached_page_end= False
    last_height = driver.execute_script("return document.body.scrollHeight")
    
    #expand the skills list:
    while not reached_page_end:
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        time.sleep(2)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if last_height == new_height:
            reached_page_end = True
        else:
            last_height = new_height
            
def open_new_question():
    driver.get(question_url)
    time.sleep(5)
    
    action.click(wait.until(EC.element_to_be_clickable((By.XPATH, '//select[@id="id_category"]')))).perform()
    category = Select(wait.until(EC.element_to_be_clickable((By.XPATH, '//select[@id="id_category"]'))))
    category.select_by_index(0)
    
def input_data_from_xml_into_the_form():
    with open('questions-answers-dummies.xml') as a:
        xml = a.read()
    o = objectify.fromstring(xml)
    #iterate over the <section> elements one by one:
    for section in o.section:
        open_new_question()
        
        if(hasattr(section, 'answer') and hasattr(section, 'dummy')):
            necessary_input_fields = section.number_of_answers + section.number_of_dummies
        elif(hasattr(section, 'answer')):
            necessary_input_fields = section.number_of_answers
        elif(hasattr(section, 'dummy')):
            necessary_input_fields = section.number_of_dummies
        else:
            necessary_input_fields = 0 
            
        while (necessary_input_fields > 5):
            action.click(wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@id="id_addanswers"]')))).perform()
            time.sleep(5)
            scroll_to_bottom()
            necessary_input_fields -= 3
        
        question = section.question.text
        wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@id="id_name"]'))).send_keys(question)
        wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@id="id_questiontexteditable"]'))).send_keys(question)
        
        single_vs_multichoice = Select(wait.until(EC.element_to_be_clickable((By.XPATH, '//select[@id="id_single"]'))))
        
        if(hasattr(section, 'answer')):
            if (section.number_of_answers > 1):
                single_vs_multichoice.select_by_visible_text("Допускается несколько ответов")
                answers = section.answer
                filled_answers_counter=0
                for answer in answers:
                    wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@id="id_answer_' + str(filled_answers_counter) + 'editable"]'))).send_keys(answer.text)
                    grade = Select(wait.until(EC.element_to_be_clickable((By.XPATH, '//select[@id="id_fraction_' + str(filled_answers_counter) + '"]'))))
                    match section.number_of_answers:
                        case 2:
                            percentage = "50%"
                        case 3:
                            percentage = "33,33333%"
                        case 4:
                            percentage = "25%"
                        case 5:
                            percentage = "20%"
                        case 6:
                            percentage = "16,66667%"
                        case 7:
                            percentage = "14,28571%"
                        case 8:
                            percentage = "12,5%"
                        case 9:
                            percentage = "11,11111%"
                        case 10:
                            percentage = "10%"                        
                        case _:
                            percentage = "5%"
                    grade.select_by_visible_text(percentage)
                    filled_answers_counter += 1
                    
            elif (section.number_of_answers == 1):
                single_vs_multichoice.select_by_visible_text("Только один ответ")
                wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@id="id_answer_0editable"]'))).send_keys(section.answer.text)
                grade = Select(wait.until(EC.element_to_be_clickable((By.XPATH, '//select[@id="id_fraction_0"]'))))
                grade.select_by_visible_text("100%")
                
        if(hasattr(section, 'dummy')):
            dummies = section.dummy
            if(hasattr(section, 'answer') and hasattr(section, 'number_of_answers')): 
                dummy_and_answer_counter = section.number_of_answers
            else:
                dummy_and_answer_counter = 1
            for dummy in dummies:
                wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@id="id_answer_' + str(dummy_and_answer_counter) + 'editable"]'))).send_keys(dummy.text)
                dummy_and_answer_counter += 1
                
        action.click(wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@id="id_submitbutton"]')))).perform()
        time.sleep(3)

def login():
    driver.get(login_page)
    wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@name="username"]'))).send_keys(username)
    wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@name="password"]'))).send_keys(password)
    action.click(wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@id="loginbtn"]')))).perform()
              
def main():
    login()
    driver.get(course_page)
    time.sleep(1)
    
    input_data_from_xml_into_the_form()
    
    os.system("cls") #clear screen from unnecessary logs since the operation has completed successfully
    print("All questions, answers and dummies are added to the questions' bank!!! \n \nSincerely Yours, \nNAKIGOE.ORG\n")
    
    # Close the only tab, will also close the browser.
    driver.close()
    driver.quit()
main()
