from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from room import room
from ExcelOperator import ExcelOperator
from function import process
from function import chooseRoom
from function import chooseKnowRoom
from function import chooseRandomroom
import datetime
import calendar
from getpass import getpass

#####################instruction: import Excell 两页：sheet1和sheet2在template中 ，，每次最多定14天，，sheet1第一天必须和startDate一致，，output 新excel


#main       
excelOperator = ExcelOperator()



trueUserName = input("enter userName:")
#truePassWord = input("enter passWord: ")
truePassWord = getpass("password: ")
today = int(datetime.date.today().__str__()[8:10])
lastDateThisMonth = calendar.monthrange(int(datetime.date.today().__str__()[0:4]),int(datetime.date.today().__str__()[5:7]))[1]

startDate = int(input("Enter startDate: "))
period = int(input("Enter period: "))
startTime = float(input("Enter startTime: "))

chosen = 1
print("unknow room : choose 1   know room : choose 2")
chosen = int(input())

knownRooms = []
#know rooms
if chosen == 2:
    i = 0
    while i < period:
        print("enter roon or -1")
        knownRooms.append(input())
        i+=1


index= 0
while True:
    if today == startDate:
        break
    index += 1
    today += 1
    if today == lastDateThisMonth+1:
        today = 1
###################
login = True
test = 1
driver = webdriver.Chrome("this is a malicious edit")
driver.get("https://ufl.libcal.com/reserve/studyMSL")

#优先级：4,6,7,15
#1,2,3,8,10,12,14,16,17,18,19,20,21

dict = {1:"L115",4:"L118",6:"L120",7:"L121",10:"L124",12:"L126",15:"L129",16:"L130",17:"L131",18:"L132",19:"L133",20:"L134",21:"L135"}

rooms = []   
knownRoomsMap = {"115" : 0, "118" : 1,"120": 2,"121":3, "124":4, "126":5,"129":6,"130":7,"131":8,"132":9,"133":10,"134":11,"135":12}  

indexChosen2 = 0

time.sleep(1)
#create rooms
startPoint = index

while index < startPoint + period:
    '''
    if chosen == 2 and knownRooms[indexChosen2] == "-1":
        indexChosen2+=1
        index+=1
        startDate+=1
    if startDate ==lastDateThisMonth+1 :
        startDate = 1
        continue
    '''
    nextButton = driver.find_element_by_class_name('fc-next-button')
    numberNext = index / 3
    j = 1
    while j <= numberNext:
        nextButton.click()
        time.sleep(2)
        j += 1
    i = 1
    while i <= 21:
        if not i in dict:
            i+=1
            continue
        path = "//*[@id='eq-time-grid']/div[2]/div/table/tbody/tr/td[3]/div/div/div/div[1]/div/table/tbody/tr["+str(i)+"]/td/div/div"
        elem = driver.find_element_by_xpath(path) 
        columns = elem.find_elements_by_class_name('s-lc-eq-avail')
        r = room(columns,dict[i],startDate)
        rooms.append(r)
        i+=1
    ############test

    ##########################
    

    #algorithm
    if chosen == 1:
        r = chooseRoom(rooms,startTime)
        if r == None:
            r = chooseRandomroom(rooms,startTime)
            if r != None:
                print(r.get_attribute('title') + "     Random")
            
        else:
            print(r.get_attribute('title'))
    else :
        if knownRooms[indexChosen2] != "-1":
            r = chooseKnowRoom(rooms[knownRoomsMap[knownRooms[indexChosen2]]],startTime)
            print(r.get_attribute('title'))
        else :
            r = chooseRandomroom(rooms,startTime)  
            if r != None:
                print(r.get_attribute('title') + "     Random")

    
    if r != None:
        length = len(r.get_attribute('title'))
        excelOperator.fillCell(index - startPoint+1,startTime,r.get_attribute('title')[length-4:length])
        process(r,driver,login,trueUserName,truePassWord)
        login = False
    else :
        print(startDate, "not exist")        

#################################################################
    driver.get("https://ufl.libcal.com/reserve/studyMSL") 
    time.sleep(2)
    startDate +=1
    if startDate ==lastDateThisMonth + 1 :
        startDate = 1
    rooms = []
    index += 1
    indexChosen2+=1
    #test StartDate
    print(startDate)


