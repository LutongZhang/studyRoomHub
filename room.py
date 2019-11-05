class room:
    def __init__(self,columns,name,date):
        avail = columns
        self.name = name
        self.availTimes = []
        self.times = []
        for i in avail:
            title = i.get_attribute('title')
            i1 = title.find(',') 
            i2 =title.rfind(',')
            dateFind = title[i1+2:i2]
            blankIndex = dateFind.find(' ')
            dateNumber = int(dateFind[blankIndex+1:i2])
            if date == dateNumber:
                self.availTimes.append(i)        
        
        for i in self.availTimes:
            title = i.get_attribute('title')
            maoIndex = title.find(":")
            front = int(title[0:maoIndex]) 
            end = int(title[maoIndex+1:maoIndex+2])
            AmPm = title[maoIndex+3:maoIndex+5]
            add = 0
            if AmPm == "pm":
                add = 12
            if end != 0:
                end = 0.5
            timeGet =front + end + add

            if front == 12 and AmPm == "pm":
                timeGet -=12
            if front == 12 and AmPm == "am":
                timeGet -=12
            self.times.append(timeGet)

