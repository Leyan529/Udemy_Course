# coding=UTF-8
import sys
from selenium import webdriver
from bs4 import BeautifulSoup
import xlsxwriter
import time
import logging
from selenium.webdriver.common.keys import Keys
import datetime
import os
import threading
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import win_unicode_console
win_unicode_console.enable()



today = datetime.date.today()
print(str(today) + " - RIS CRAWL")

# start = 起始頁數
start = 101
maxSearchNum = 0
#interval = 儲存頁數間隔
interval = 20
print("起始頁數 : " + str(start) + "，每" + str(interval) + "頁為間隔做輸出")

#------------------------------------------------------------------------------------------
def open_web():
    try:
        url = "http://www.researcherid.com/ViewProfileSearch.action"
        driver = webdriver.Chrome("C:\\Python34\\chromedriver.exe")    
        driver.get(url)
        driver.implicitly_wait(3)

        element = WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.ID, "country"))
        )  
        driver.find_element_by_id('country').find_elements_by_tag_name("option")[220].click() #點擊頁面上"Country/Region"的"Taiwan"的項目

        element = WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.ID, "submitImage"))
        )
        driver.find_element_by_id('submitImage').click() #點擊頁面上"Submit"的項目

        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "resultsPerPage"))
        )
        driver.find_element_by_id('resultsPerPage').find_elements_by_tag_name("option")[2].click() #修改頁面上Results的顯示筆數

        return driver
    except:
        driver.close()  
        print('網頁錯誤，等候重新開啟')        
        return None
#------------------------------------------------------------------------------------------
#網頁開啟  
driver = None
while(driver == None):        
    driver = open_web()    

        
#網頁成功開啟後開啟logger
logger = logging.getLogger("RIS")   #不加名稱設置root logger
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s: - %(message)s' ,
    datefmt= '%Y-%m-%d %H:%M:%S' )
log_filter=logging.Filter("RIS")

# 使用FileHandler輸出到文件
loggerPath = 'RI_CRAWL_THREAD/' + str(start) + "-" + str(start + interval - 1) + '/RIS - log - '+ str(today) +'.txt' 
directory = os.path.dirname(loggerPath)
if not os.path.exists(directory):
    os.makedirs(directory)
fh = logging.FileHandler(loggerPath)

fh.setLevel(logging.DEBUG)
fh.setFormatter(formatter)

# 使用StreamHandler輸出到屏幕
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(formatter)
# 添加兩個Handler
logger.addHandler(ch)
logger.addHandler(fh)
#Handler只啟動一次
#設置logger

#------------------------------------------------------------------------------------------

def write_excel(sheet,p0,p1,p2,p3,p4,p5,p6,p7):
    try:
        if sheet == Work_sheet: 
            global Work_row
            Work_sheet.write(Work_row, 0, p0)
            Work_sheet.set_column(Work_row, 0, len(p0))

            Work_sheet.write(Work_row, 1, p1)
            Work_sheet.set_column(Work_row, 1, len(p1))

            Work_sheet.write(Work_row, 2, p2)
            Work_sheet.set_column(Work_row, 2, len(p2))

            Work_sheet.write(Work_row, 3, p3)
            Work_sheet.set_column(Work_row, 3, len(p3))

            Work_sheet.write(Work_row, 4, p4)
            if len(p4) == 0:
                Work_sheet.set_column(Work_row, 4, 20) 
            else:
                Work_sheet.set_column(Work_row, 4, len(p4))

            Work_sheet.write(Work_row, 5, p5)
            if len(p5) == 0:
                Work_sheet.set_column(Work_row, 5, 20) 
            else:
                Work_sheet.set_column(Work_row, 5, len(p5)) 

            Work_sheet.write(Work_row, 6, p6)
            if len(p6) == 0:
                Work_sheet.set_column(Work_row, 6, 20) 
            else:
                Work_sheet.set_column(Work_row, 6, len(p6))       

            Work_row = Work_row + 1        

        elif sheet == Institution_sheet: 
            global Institution_row
            Institution_sheet.write(Institution_row, 0, p0)        
            Institution_sheet.set_column(Institution_row, 0, len(p0))

            Institution_sheet.write(Institution_row, 1, p1)
            Institution_sheet.set_column(Institution_row, 1, len(p1))

            Institution_sheet.write(Institution_row, 2, p2)
            if len(p2) == 0:
                Institution_sheet.set_column(Institution_row, 2, 20) 
            else:
                Institution_sheet.set_column(Institution_row, 2, len(p2))

            Institution_sheet.write(Institution_row, 3, p3)
            if len(p3) == 0:
                Institution_sheet.set_column(Institution_row, 3, 20) 
            else:
                Institution_sheet.set_column(Institution_row, 3, len(p3))

            Institution_sheet.write(Institution_row, 4, p4)
            if len(p4) == 0:
                Institution_sheet.set_column(Institution_row, 4, 20) 
            else:
                Institution_sheet.set_column(Institution_row, 4, len(p4))

            Institution_sheet.write(Institution_row, 5, p5)
            if len(p5) == 0:
                Institution_sheet.set_column(Institution_row, 5, 20) 
            else:
                Institution_sheet.set_column(Institution_row, 5, len(p5))

            Institution_sheet.write(Institution_row, 6, p6)
            if len(p6) == 0:
                Institution_sheet.set_column(Institution_row, 6, 20) 
            else:
                Institution_sheet.set_column(Institution_row, 6, len(p6))

            Institution_sheet.write(Institution_row, 7, p7)
            if len(p7) == 0:
                Institution_sheet.set_column(Institution_row, 7, 20) 
            else:
                Institution_sheet.set_column(Institution_row, 7, len(p7))    

            Institution_row = Institution_row + 1        

        elif sheet == Info_sheet: 
            global Info_row
            Info_sheet.write(Info_row, 0, p0)
            Info_sheet.set_column(Info_row, 0, 20)

            Info_sheet.write(Info_row, 1, p1)
            Info_sheet.set_column(Info_row, 1, len(p1))

            Info_sheet.write(Info_row, 2, p2)
            if len(p2) == 0:
                Info_sheet.set_column(Info_row, 2, 20) 
            else:
                Info_sheet.set_column(Info_row, 2, len(p2))

            Info_sheet.write(Info_row, 3, p3)
            if len(p3) == 0:
                Info_sheet.set_column(Info_row, 3, 20) 
            else:
                Info_sheet.set_column(Info_row, 3, len(p3))

            Info_sheet.write(Info_row, 4, p4)
            if len(p4) == 0:
                Info_sheet.set_column(Info_row, 4, 20) 
            else:
                Info_sheet.set_column(Info_row, 4, len(p4))

            Info_sheet.write(Info_row, 5, p5)
            if len(p5) == 0:
                Info_sheet.set_column(Info_row, 5, 20) 
            else:
                Info_sheet.set_column(Info_row, 5, len(p5))

            Info_sheet.write(Info_row, 6, p6)
            if len(p6) == 0:
                Info_sheet.set_column(Info_row, 6, 20) 
            else:
                Info_sheet.set_column(Info_row, 6, len(p6))     

            Info_sheet.write(Info_row, 7, p7)
            if len(p7) == 0:
                Info_sheet.set_column(Info_row, 7, 20) 
            else:
                Info_sheet.set_column(Info_row, 7, len(p7))      

            Info_row = Info_row + 1
    except Exception as e:
        logger.info('Excel寫入失敗')
        traceback = sys.exc_info()[2]
        logger.error(sys.exc_info())
        logger.error(traceback.tb_lineno)
        logger.error(e)
#------------------------------------------------------------------------------------------
def Info_Crawl(RI,work_driver):
    try:
        Name =''
        Other_Names = ''
        ORCID = ''
        Email = ''
        My_URLs = ''
        Keywords =''
        Subject = ''

        Name = work_driver.find_element_by_xpath('//div[@class="profileName"]').text
        profileTable_key = work_driver.find_elements_by_xpath('//table[@class="profileTable"]//tr//td[@class="profileFieldLabel"]') 
        profileTable_value = work_driver.find_elements_by_xpath('//table[@class="profileTable"]//tr//td[@class="profileDataCells"]') 
        
        profileTableInst_key = work_driver.find_elements_by_xpath('//table[@class="profileTableInst"]//tr//td[@class="profileFieldLabel"]')
        profileTableInst_value = work_driver.find_elements_by_xpath('//table[@class="profileTableInst"]//tr//td[@class="profileDataCells"]')
        
        profileTableDesc_key = work_driver.find_elements_by_xpath('//table[@class="profileTableDesc"]//tr//td[@class="profileFieldLabel"]')
        profileTableDesc_value = work_driver.find_elements_by_xpath('//table[@class="profileTableDesc"]//tr//td[@class="profileDataCells"]//a')
        
#         logger.info(profileTable_value)
        key =[]
        value = []
        for index, item in enumerate(profileTable_key):
            title = item.text.replace("  ","").replace("\r\n","").replace(":","")
            key.append(title)
            if title == 'ORCID':
                value.append(profileTable_value[index].find_element_by_xpath('a').text)
            elif title == 'E-mail':
                value.append(profileTable_value[index].find_element_by_xpath('label').text.replace("  ","").replace("\r\n",""))
            else:
                value.append(profileTable_value[index].text) 
            
        for index, item in enumerate(profileTableInst_key):
            key.append(item.text.replace("  ","").replace("\r\n","").replace(":",""))
            if  len(profileTableInst_value)>index:
                value.append(profileTableInst_value[index].text.replace("  ","").replace("\r\n",""))  
            else:
                value.append('')
        
        for index, item in enumerate(profileTableDesc_key):
            key.append(item.text.replace("  ","").replace("\r\n","").replace(":",""))
            if  len(profileTableDesc_value)>index:
                value.append(profileTableDesc_value[0].text.replace("  ","").replace("\r\n",""))
            else:
                value.append('')              


        Info_item = {}
        
        Info_item['RI'] = RI
        Info_item['Name'] = Name
        Info_item['Other_Names'] = ''
        Info_item['ORCID'] = ''
        Info_item['E-mail'] = ''
        Info_item['My URLs'] = ''
        Info_item['Keywords'] = ''
        Info_item['Subject'] = ''
        
        
        
        for index,item in enumerate (key):
            Info_item[item] = value[index]

        Info_item_list.append(Info_item)
    
        #logger.info(Info_item)
        write_excel(Info_sheet,
                            RI,
                            Name,
                            Info_item['Other_Names'],
                            Info_item['ORCID'],
                            Info_item['E-mail'],
                            Info_item['My URLs'],
                            Info_item['Keywords'],
                            Info_item['Subject'])        
           
        
        logger.info('Info_item抓取完成')
    except Exception as e:
        logger.info('Info_item抓取失敗')
        traceback = sys.exc_info()[2]
        logger.error(sys.exc_info())
        logger.error(traceback.tb_lineno)
        logger.error(e)
#------------------------------------------------------------------------------------------
def Institution_Crawl(RI,work_driver):
    try:
        href = work_driver.find_element_by_xpath('//table[@class="profileTableInst"]//tbody//tr//td//a').get_attribute('href').replace("javascript:getInstitutionDetails('","").replace("')","")
        url = 'http://www.researcherid.com/DisplayPublicProfileInstitutions.action?rid=' + href
        data = requests.get(url)
        soup = BeautifulSoup(data.text,'html.parser')
        
        Primary_Institution =''
        Joint_Affiliation =''
        Past_Institution_Name =''

        SubOrg_Dept_1 = ''
        SubOrg_Dept_2 = ''
        SubOrg_Dept_3 = ''

        Role_1 =''
        Role_2 =''
        Role_3 =''

        Start_Date_1 = ''
        Start_Date_2 = ''
        Start_Date_3 = ''
        End_Date = ''

        profileFieldLabelLeft = soup.find_all('td',{'class':'profileFieldLabelLeft'})
        if profileFieldLabelLeft != []:
            Past_Institution_Name = profileFieldLabelLeft[0].text.replace("  ","")
            if len(profileFieldLabelLeft) > 1:
                SubOrg_Dept_3 = profileFieldLabelLeft[1].text.replace("  ","")
            if len(profileFieldLabelLeft) > 3:
                Role_3 = profileFieldLabelLeft[3].text.replace("  ","")
            if len(profileFieldLabelLeft) > 4:
                Start_Date_3 = profileFieldLabelLeft[4].text.replace("  ","").replace("\r\n","")
            if len(profileFieldLabelLeft) > 5:
                End_Date = profileFieldLabelLeft[5].text.replace("  ","").replace("\r\n","")

        profileDataCells = soup.find_all('td',{'class':'profileDataCells'})
        if profileDataCells != []:
            if len(profileDataCells) > 4:
                SubOrg_Dept_1 = profileDataCells[4].text.replace("  ","")
            if len(profileDataCells) > 9:
                SubOrg_Dept_2 = profileDataCells[9].text.replace("  ","")
         
        affiliationName = soup.find('label',{'id':'researcher_affiliationName'})
        if affiliationName != None:
            Joint_Affiliation = affiliationName.text.replace("\n","").replace("  ","")
            
        role_description = soup.find('label',{'id':'researcher_role_description'})
        if role_description != None:
            Role_1 = role_description.text

        researcher_institution = soup.find('label',{'id':'researcher_institution'})
        if researcher_institution != None:
            Primary_Institution = soup.find('label',{'id':'researcher_institution'}).text    

        role_description = soup.find('label',{'id':'researcher_affiliationAddress_role_description'})
        if role_description != None:
            Role_2 = role_description.text.replace("  ","")

        address_startDate = soup.find('label',{'id':'researcher_address_startDate'})
        if address_startDate!= None:
            Start_Date_1 = address_startDate.text.replace("  ","")

        affiliationAddress_startDate = soup.find('label',{'id':'researcher_affiliationAddress_startDate'})    
        if affiliationAddress_startDate!= None:
            Start_Date_2 = affiliationAddress_startDate.text.replace("  ","")

        Institution_item={}
        Institution_item['RI'] = RI
        Institution_item['Primary_Institution'] = Primary_Institution
        Institution_item['Joint_Affiliation'] = Joint_Affiliation
        Institution_item['Past_Institution_Name'] = Past_Institution_Name
        Institution_item['SubOrg_Dept'] = SubOrg_Dept_1.replace("  ","").replace("\r\n","")
        Institution_item['Role'] = Role_1.replace("  ","").replace("\r\n","")
        Institution_item['Start_Date'] = Start_Date_1.replace("  ","").replace("\r\n","")
        Institution_item['End_Date'] =''        
        Institution_item_list.append(Institution_item)
        #logger.error(Institution_item)
        
        write_excel(Institution_sheet,
                                RI,
                                Primary_Institution,
                                Joint_Affiliation,
                                Past_Institution_Name,
                                Institution_item['SubOrg_Dept'],
                                Institution_item['Role'],
                                Institution_item['Start_Date'],
                                Institution_item['End_Date'])


        
        Institution_item['SubOrg_Dept'] = SubOrg_Dept_2.replace("  ","").replace("\r\n","")
        Institution_item['Role'] = Role_2.replace("  ","").replace("\r\n","")
        Institution_item['Start_Date'] = Start_Date_2.replace("  ","").replace("\r\n","")
        Institution_item_list.append(Institution_item)
#        logger.error(Institution_item)
        
        write_excel(Institution_sheet,
                                RI,
                                Primary_Institution,
                                Joint_Affiliation,
                                Past_Institution_Name,
                                Institution_item['SubOrg_Dept'],
                                Institution_item['Role'],
                                Institution_item['Start_Date'],
                                Institution_item['End_Date'])
  

        Institution_item['SubOrg_Dept'] = SubOrg_Dept_3.replace("  ","").replace("\r\n","")
        Institution_item['Role'] = Role_3.replace("  ","").replace("\r\n","")
        Institution_item['Start_Date'] = Start_Date_3.replace("  ","").replace("\r\n","")
        Institution_item['End_Date'] = End_Date.replace("  ","").replace("\r\n","")
        Institution_item_list.append(Institution_item)   
#        logger.error(Institution_item)
        
        write_excel(Institution_sheet,
                                RI,
                                Primary_Institution,
                                Joint_Affiliation,
                                Past_Institution_Name,
                                Institution_item['SubOrg_Dept'],
                                Institution_item['Role'],
                                Institution_item['Start_Date'],
                                Institution_item['End_Date'])

        logger.info('Institution_item 抓取完成')
    except Exception as e:
        logger.info('Institution_item 抓取失敗')
        logger.error(e)
        traceback = sys.exc_info()[2]
        logger.error(sys.exc_info())
        logger.error(traceback.tb_lineno)
        logger.error(e)
#------------------------------------------------------------------------------------------

def Work_Search(url,work_driver):
    logger.info(url)  
    
    update_per_data_action = work_driver.find_elements_by_xpath('//select [@id="resultsPerPage"]//option[@value="50"]')
    if update_per_data_action != []:
        update_per_data_action[0].click() #修改頁面上Results的顯示筆數 
    driver.implicitly_wait(1)    

    RI = work_driver.find_elements_by_xpath('//td[@class="profileDataCells"]')[0].text  #RID欄位資料

       
    Institution_Crawl_thread = threading.Thread(target=Institution_Crawl(RI,work_driver), name='Institution_Crawl')
    Info_Crawl_thread = threading.Thread(target=Info_Crawl(RI,work_driver), name='Info_Crawl')
    
    Institution_Crawl_thread.start()
    Info_Crawl_thread.start()

    Crawls(RI,work_driver)     
    
    Info_Crawl_thread.join()
    Institution_Crawl_thread.join()    

#------------------------------------------------------------------------------------------
def Crawls(RI,work_driver):
    current_metadata_total = work_driver.find_elements_by_id('current_metadata_total')
    total = 0
    temp_count = 0
    if current_metadata_total!=[]:
        total = int(current_metadata_total[0].text) 
        temp_count = total
    
    table = work_driver.find_elements_by_xpath('//table[@class="vcrNavBar"]//tbody//tr//td[@class="goto"]')
    
    Crawl_pages = 0
    if table!= []:
        Crawl_pages = table[1].text.replace(" ","").replace("Pageof","")        
        logger.info('總共有' + str(total) + '個 publishes' + '，' + str(Crawl_pages) + '個分頁')
        for i in range(0,int(Crawl_pages)):
            logger.info("第"+str(i+1)+"分頁抓取中...")  
            time.sleep(5)       
            Work_Crawl(RI,work_driver,50*i)
            element = WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.XPATH, '//img[@title="Next Page"]'))
            )                     
            work_driver.find_element_by_xpath('//img[@title="Next Page"]').click() #切換下一分頁
            temp_count = temp_count - 50
            if temp_count <=0 :
                logger.info('Work_item抓取完成，'+ RI+'底下共抓取'+ str(total) +'項publishes')
    else:
        logger.info('Work_item抓取完成，' + RI+'底下並無任何publishes')
#------------------------------------------------------------------------------------------
def Work_Crawl(RI,work_driver,start):
    try:
        item_list=[]
        try :
            element = WebDriverWait(driver, 30).until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, "summary_recnum"))
            )
            summary_recnum_list = work_driver.find_elements_by_class_name('summary_recnum')
        except Exception as e:
            summary_recnum_list = []

        try :
            element = WebDriverWait(driver, 30).until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, "summary_data"))
            )
            summary_data_list = work_driver.find_elements_by_class_name('summary_data')
        except Exception as e:
            summary_data_list = []

        try :
            element = WebDriverWait(driver, 30).until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, "summary_date"))
            )
            summary_date_list = work_driver.find_elements_by_class_name('summary_date')
        except Exception as e:
            summary_date_list = []

        try :
            element = WebDriverWait(driver, 30).until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, "summary_recnum_2"))
            )
            summary_recnum2_list = work_driver.find_elements_by_class_name('summary_recnum_2')
        except Exception as e:
            summary_recnum2_list = []

        try :
            element = WebDriverWait(driver, 30).until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, "summary_data_2"))
            )
            summary_data2_list = work_driver.find_elements_by_class_name('summary_data_2')
        except Exception as e:
            summary_data2_list = []

        try :
            element = WebDriverWait(driver, 30).until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, "summary_date_2"))
            )
            summary_date2_list = work_driver.find_elements_by_class_name('summary_date_2')
        except Exception as e:
            summary_date2_list = []     
        

        length = len(summary_recnum_list) + len(summary_recnum2_list)
        goal = 0

        for i in range(0,length): 
            goal = i+1 
            index = int(i/2)
            try :
                if i%2 == 0:
                    if len(summary_data_list) > index : #63 - 3150 list index out of range
                        summary_recnum = summary_recnum_list[index]
                        summary_data = summary_data_list[index]
                        summary_date = summary_date_list[index]
                else:
                    if len(summary_data2_list) > index :
                        summary_recnum = summary_recnum2_list[index]
                        summary_data = summary_data2_list[index]
                        summary_date = summary_date2_list[index]
            except Exception as e:
                logger.error('第'+ str(start+goal)+'項publishes ，抓取失敗') 
                logger.error(e)
                traceback = sys.exc_info()[2]
                logger.error(sys.exc_info())
                logger.error(traceback.tb_lineno) 
                summary_recnum == None
                summary_data == None
                summary_date == None


            if summary_data != None:
                input_elements = summary_data.find_elements_by_tag_name('input')
                data_bold = summary_data.find_elements_by_class_name('data_bold')
                Number = summary_recnum.text.replace(".","") 
                Title =''
                Authors = ''
                Source = ''
                DOI = ''
                Published = ''          
                if len(input_elements) > 2 :
                    Title = input_elements[2].get_attribute('value')
                if len(input_elements) > 3 :
                    Authors = input_elements[3].get_attribute('value')
                if len(input_elements) > 5 :       
                    Source = input_elements[5].get_attribute('value')
                    
                Published_path = '//input[@name="artifacts[' + str(i) + '].publicationYear"]'
                elements_Published = work_driver.find_elements_by_xpath(Published_path)
                if elements_Published!=[]:
                    Published = elements_Published[0].get_attribute('value')
                
                DOI_path = '//input[@name="artifacts[' + str(i) + '].doi"]'
                elements_DOI = work_driver.find_elements_by_xpath(DOI_path)
                if elements_DOI!= []:
                    DOI = elements_DOI[0].get_attribute('value')              
                
                added = summary_date.text.replace("added","").replace(" ","").replace("\r","").replace("\n","")

                work_item={}
                work_item['RI'] = RI
                work_item['Number'] = Number
                work_item['Title'] = Title
                work_item['Authors'] = Authors
                work_item['Source'] = Source
                work_item['Published'] = Published
                work_item['DOI'] = DOI
                work_item['added'] = added
                work_item_list.append(work_item)  
                write_excel(Work_sheet,RI,Title,Authors,Source,Published,DOI,added,None)  
            else:
                work_item={}
                work_item['RI'] = RI
                work_item['Number'] = start+goal
                work_item['Title'] = ''
                work_item['Authors'] = ''
                work_item['Source'] = ''
                work_item['Published'] = ''
                work_item['DOI'] = ''
                work_item['added'] = ''
                work_item_list.append(work_item)                 
                write_excel(Work_sheet,RI,'','','','','','',None)
              

#             if int(total) == int(Number):
#                 logger.info('Work_item抓取完成，'+ RI+'底下共抓取'+ str(total) +'項publishes')
#                 break
    except Exception as e:               
            logger.error(e)
            traceback = sys.exc_info()[2]
            logger.error(sys.exc_info())
            logger.error(traceback.tb_lineno)
            
#------------------------------------------------------------------------------------------
def Results_Search(driver):
    namelist=[]
    nameUrlist=[]
    try :
        element = WebDriverWait(driver, 30).until(
            EC.presence_of_all_elements_located((By.XPATH, '//td[@class="summary_data"]//a'))
        )
        title_list = driver.find_elements_by_xpath('//td[@class="summary_data"]//a') 
    except Exception as e:
        logger.error('連結抓取錯誤')     

    try :
        element = WebDriverWait(driver, 30).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, 'authorSetsNum'))
        )
        authorSetsNums = driver.find_elements_by_class_name('authorSetsNum') 
    except Exception as e:
        logger.error('編號抓取錯誤')

    
    for index, title in enumerate(title_list):                                         
        nameUrlist.append('http://www.researcherid.com/rid/' + title.get_attribute('title'))
        namelist.append(authorSetsNums[index].text +" : "+ title.text)

    for index, element in enumerate(namelist):  
        logger.info('--------------------------------------------------------------------------')
        logger.info("NAME : " + element.encode("utf8").decode("cp950", "ignore"))    
        try :
            #if index > 17 :
            script = "window.open('"+ nameUrlist[index] + "', 'new_window')"
            logger.info(script)
            driver.execute_script(script)
            driver.switch_to_window(driver.window_handles[1])
            Work_Search(nameUrlist[index],driver) 
            time.sleep(3)
            #driver.implicitly_wait(5)
            driver.switch_to_window(driver.window_handles[0])            
        except Exception as e:
            driver.switch_to_window(driver.window_handles[0])
            logger.info("NAME : " + element + ' Crawl Failed ' + str(e))
            traceback = sys.exc_info()[2]
            logger.error(sys.exc_info())
            logger.error(traceback.tb_lineno)
            logger.error(e)
            continue
        logger.info("NAME : " + element.encode("utf8").decode("cp950", "ignore") + ' Crawl Over')
        logger.info('--------------------------------------------------------------------------')


# In[27]:

# In[28]:


#主程式
try :
    element = WebDriverWait(driver, 30).until(
                    EC.presence_of_all_elements_located((By.XPATH, '//table[@class="vcrNavBar"]//tbody//tr//td[@class="goto"]'))
                )
    pages = driver.find_elements_by_xpath('//table[@class="vcrNavBar"]//tbody//tr//td[@class="goto"]')[1].text.replace(" ","").replace("Pageof","")
    pages = int(pages) + 1
except Exception as e:
    pages = 0

for start_pages in range(start,pages,interval):   
    pageNumBoxes = driver.find_element_by_class_name('pageNumBoxes')
    pageNumBoxes.send_keys(Keys.BACK_SPACE) #清空內容
    pageNumBoxes.send_keys(Keys.BACK_SPACE) #清空內容
    pageNumBoxes.send_keys(Keys.BACK_SPACE) #清空內容
    pageNumBoxes.send_keys(start_pages) #清空內容
    driver.find_elements_by_tag_name('a')[11].click() #前往指定頁面
        
    today = datetime.date.today()
    

    work_item_list = []

    Institution_item_list = []

    Info_item_list = []
    
    if start_pages +interval <= pages :
        maxSearchNum = start_pages +interval       
    else:
        maxSearchNum = pages
        
    file_path = 'RI_CRAWL_THREAD/' +str(start_pages) +'-' + str(maxSearchNum-1) +'/' + str(today)  + '.xlsx'        
        
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)
    workbook = xlsxwriter.Workbook(file_path)
    #   Work_sheet
    Work_sheet = workbook.add_worksheet('Work')
    Work_row = 0
    Work_col = 0
    Work_sheet.write(Work_row, 0, 'RI')
    Work_sheet.write(Work_row, 1, 'Title')
    Work_sheet.write(Work_row, 2, 'Authors')
    Work_sheet.write(Work_row, 3, 'Source')
    Work_sheet.write(Work_row, 4, 'Published')
    Work_sheet.write(Work_row, 5, 'DOI')
    Work_sheet.write(Work_row, 6, 'added')
    Work_row = 1

    #   Institution_sheet
    Institution_sheet = workbook.add_worksheet('Institution')
    Institution_row = 0
    Institution_col = 0
    Institution_sheet.write(Institution_row, 0, 'RI')
    Institution_sheet.write(Institution_row, 1, 'Primary_Institution')
    Institution_sheet.write(Institution_row, 2, 'Joint_Affiliation')
    Institution_sheet.write(Institution_row, 3, 'Past_Institution_Name')
    Institution_sheet.write(Institution_row, 4, 'SubOrg_Dept')
    Institution_sheet.write(Institution_row, 5, 'Role')
    Institution_sheet.write(Institution_row, 6, 'Start_Date')
    Institution_sheet.write(Institution_row, 7, 'End_Date')
    Institution_row = 1


    #   Info_sheet
    Info_sheet = workbook.add_worksheet('Info')
    Info_row = 0
    Info_col = 0
    Info_sheet.write(Info_row, 0, 'RI')
    Info_sheet.write(Info_row, 1, 'Name')
    Info_sheet.write(Info_row, 2, 'Other_Names')
    Info_sheet.write(Info_row, 3, 'ORCID')
    Info_sheet.write(Info_row, 4, 'Email')
    Info_sheet.write(Info_row, 5, 'My_URLs')
    Info_sheet.write(Info_row, 6, 'Keywords')
    Info_sheet.write(Info_row, 7, 'Subject')
    Info_row = 1
    try:          
        current_pages = driver.find_element_by_class_name('pageNumBoxes').get_attribute('value')
        logger.info(current_pages)
        logger.info('從第'+ str(start_pages) + '頁開始查詢')
        for i in range(int(current_pages),maxSearchNum):  
            logger.info("第" + str(i) + "個Results查詢分頁") 
            logger.info("Results逐筆查詢開始...")
            try:
                Results_Search(driver)   
            except Exception as e:
                continue                 
            time.sleep(5)
            element = WebDriverWait(driver, 100).until(
                EC.presence_of_element_located((By.XPATH, '//img[@title="Next Page"]'))
            )
            driver.find_element_by_xpath('//img[@title="Next Page"]').click() #切換下一分頁
        time.sleep(5)    
        workbook.close()
        logger.info('xls file outputed')    
        logger.info('--------------------------------------------------------------------------')
#         driver.close()
    except Exception as e:
        #workbook.close()
        #logger.error("xls file outputed")           
        driver.switch_to_window(driver.window_handles[0])
        traceback = sys.exc_info()[2]
        logger.error(sys.exc_info())
        logger.error(traceback.tb_lineno)
        logger.error(e)    
    #finally:    
        #workbook.close()       
    #強制輸出至EXCEL    
    workbook.close()

logger.info('finished')      
#------------------------------------------------------------------------------------------ for end    
handlers = logger.handlers[:]
for handler in handlers:
    handler.close()
    logger.removeHandler(handler)
logger.info('RIS Close logger') 
logger.info('RIS finished output') 




