from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import time, sys

filepath = sys.argv[1]
filename = filepath.split('.')[-2]
filename = filepath.split('\\')[-1]
#driver = webdriver.Firefox()
driver = webdriver.PhantomJS('phantomjs')
driver.implicitly_wait(30)
base_url = "https://software.clickback.com/"
verificationErrors = []
accept_next_alert = True
driver.get(base_url + "/login.aspx")
driver.find_element_by_id("ctl00_ContentPlaceHolder1_txtUser").clear()
driver.find_element_by_id("ctl00_ContentPlaceHolder1_txtUser").send_keys("USERNAME")
driver.find_element_by_id("ctl00_ContentPlaceHolder1_txtPass").clear()
driver.find_element_by_id("ctl00_ContentPlaceHolder1_txtPass").send_keys("PASSWORD")
driver.find_element_by_id("ctl00_ContentPlaceHolder1_ibtnLogin").click()
driver.find_element_by_link_text("My Lists").click()
driver.find_element_by_link_text("Import New List").click()
driver.find_element_by_id("ctl00_ContentPlaceHolder1_inputFile").send_keys(filepath)
driver.find_element_by_id("ctl00_ContentPlaceHolder1_lbtnUpload").click()
driver.find_element_by_id("ctl00_ContentPlaceHolder1_ddlListFolder_Arrow").click()
driver.find_element_by_xpath("/html/body/form/div/div/div/ul/li/div/div/ul/li[2]/div/span[2]").click() #li[9]
driver.find_element_by_id("ctl00_ContentPlaceHolder1_lbtnAddList").click()
driver.find_element_by_id("ctl00_ContentPlaceHolder1_txtListName").send_keys(filename)
driver.find_element_by_id("ctl00_ContentPlaceHolder1_lbtnSave").click()
driver.find_element_by_id("ctl00_ContentPlaceHolder1_cmbUploadType_Arrow").click()
time.sleep(2)
driver.find_element_by_xpath("/html/body/form/div/div/div/ul/li[2]").click()
driver.find_element_by_xpath("//*[@id='ctl00_ContentPlaceHolder1_ddlOptStatus']/option[text()='Single Opted In']").click() 
driver.find_element_by_id("ctl00_ContentPlaceHolder1_lbuttonSubmit").click()
time.sleep(3)
driver.find_element_by_id("ctl00_ContentPlaceHolder1_lbtnImport").click()
time.sleep(3)
driver.find_element_by_id("ctl00_ContentPlaceHolder1_lbtnContinue").click()
driver.quit()