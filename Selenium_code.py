from operator import index
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import pandas as pd

driver = webdriver.Chrome(
    executable_path='chromedriver_win32/chromedriver.exe')
if __name__ == "__main__":
    url = "https://result.ganpatuniversity.ac.in/"

driver.get(url)
actionobj = ActionChains(driver)
print()

df = pd.read_csv (r'Enroll_Num.csv') 
dfN = pd.DataFrame(columns=["Fetch_enroll", "Fetch_name", "Fetch_branch", "Fetch_sem", "Fetch_exam", "Fetch_sgpa", "Fetch_cgpa"] 
                )

for i in range (0,len(df['EnrollNum'])):

    # time.sleep(1)
    select1 = Select(driver.find_element_by_id('ddlInst'))
    # select by value "16 - ICT"
    select1.select_by_value('17')

    # time.sleep(1)
    select2 = Select(driver.find_element_by_id('ddlDegree'))
    # select by value "B.TECH-CSE(CS)"
    select2.select_by_value('207')

    # time.sleep(1)
    select3 = Select(driver.find_element_by_id('ddlSem'))
    # select by value "V"
    select3.select_by_value('5')

    # time.sleep(1)
    select4 = Select(driver.find_element_by_id('ddlScheduleExam'))
    # select by value "NOV - DEC 2021 [ REGULAR ]"
    select4.select_by_value('10480')

    # time.sleep(1)
    enrollnum = str(df['EnrollNum'][i])
    
    enroll = driver.find_element(By.XPATH,
                                "/html/body/form/div[3]/table[2]/tbody/tr[5]/td[2]/input")
    enroll.send_keys(enrollnum)

    # time.sleep(1)
    button_show = driver.find_element(By.XPATH,
                                "/html/body/form/div[3]/table[2]/tbody/tr[7]/td/input[1]")
                                
    button_show.click()

    # Fetch the result
    # time.sleep(1)
    dfN.loc[len(dfN)] = [driver.find_element_by_id('uclGrd_lblExamNo').text,
                driver.find_element_by_id('uclGrd_lblStudentName').text, 
                driver.find_element_by_id('uclGrd_lblDegreeName').text, 
                driver.find_element_by_id('uclGrd_lblSemester').text,
                driver.find_element_by_id('uclGrd_lblMnthYr').text,
                driver.find_element_by_id('uclGrd_lblSGPA').text,
                driver.find_element_by_id('uclGrd_lblPrgCGPA').text]
    
    # Go to Back
    # time.sleep(1)
    button_back = driver.find_element(By.XPATH,
                                "/html/body/form/div[3]/input")
                                
    button_back.click()
              
time.sleep(1)
driver.quit()
dfN.to_csv('Result.csv' , index=False)
print(dfN)
