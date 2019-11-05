import time

def process(avail,driver,login,trueUserName,truePassWord):
    avail.click()
    time.sleep(3)
    timeChoose = driver.find_element_by_id('bookingend_1')
    chosens = timeChoose.find_elements_by_tag_name('option')
    fourth = chosens[len(chosens)-1]
    fourth.click()
    time.sleep(3)
    submitButton = driver.find_element_by_id('submit_times')
    submitButton.click()


    if login:
        time.sleep(3)
        userName = driver.find_element_by_id('username')
        userName.send_keys(trueUserName)
        passWord = driver.find_element_by_id('password')
        passWord.send_keys(truePassWord)
        time.sleep(3)
        login = driver.find_element_by_id('submit')
        login.click()

    time.sleep(3)
    Continue = driver.find_element_by_id('terms_accept')
    Continue.click()

    time.sleep(3)
    finalSubmit = driver.find_element_by_id('s-lc-eq-bform-submit')
    finalSubmit.click()


def filter(rooms):
    biggerRooms = [rooms[3],rooms[4],rooms[5],rooms[10]]

    for big in biggerRooms:
        times = big.times
        
        index = start12(times)
        
        if index != -1 and len(times) - index == 24:
            return big

    i = 0
    while i < len(rooms) :
        if i == 3 or i == 4 or i == 5 or i == 10:
            i+=1
            continue
        
        room = rooms[i]
        times = room.times
        index = start12(times)

        if index != -1 and len(times) - index == 24:
            return room    
        i+=1    

    return None    

def chooseRoom(rooms,startTime):
    r = filter(rooms)
    if r != None :
        i = start12(r.times)
        while i < len(r.times):
            if r.times[i] == startTime:
                break
            i+=1
        return r.availTimes[i]
    else:
        return None    


def start12(times):
    
    index = -1
    i =0
    while i < len(times):
        if times[i] == 12:
            index = i
            break
        i+=1
    
    return index        


def chooseKnowRoom(room,startTime):
    i = findTime(room.times,startTime)
    
    if i != -1:
        return room.availTimes[i]
    else :
        return None

def findTime(times,time):
    index = -1
    i = 0
    while i < len(times):
        if times[i] == time:
            index = i
            break
        i+=1
    return index


#change
def chooseRandomroom(rooms,startTime):
    biggerRooms = [rooms[3],rooms[4],rooms[5],rooms[10]]

    for big in biggerRooms:
        times = big.times
        index = findTime(times,startTime)
        determine = True
        if index == -1:
            determine = False
        else:
            end = index + 3
            if end >= len(times):
                determine = False
            elif times[end] != startTime+2-0.5:
                determine = False
        if determine :
            return big.availTimes[index]


    i = 0
    while i < len(rooms) :
        if i == 3 or i == 4 or i == 5 or i == 10:
            i+=1
            continue
        
        determine = True
        room = rooms[i]
        times = room.times 
        index = findTime(times,startTime)
        if index == -1:
            determine = False
            i+=1
            continue
        else :
            end = index + 3
            if end >= len(times):
                determine = False
            elif times[end] != startTime + 2 - 0.5:
                determine = False
        if determine:
            return room.availTimes[index]

        i+=1    
    
    return None