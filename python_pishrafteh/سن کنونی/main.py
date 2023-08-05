import datetime
class age:
    def __init__(self,date_list):
        (year,month,day) = date_list
        self.year = int(year)
        self.day = int(day)
        self.month =int(month)
    def check_date(self):
        try:
            datetime.datetime(self.year,self.month,self.day)
            age.calculate_age(self)
        except:
            print("WRONG")
    def calculate_age(self):
        date_now = datetime.datetime.now()
        if self.month > date_now.month:
            self.year -= 1
        else:
            print(date_now.year- self.year)

    
date = age(input().split("/"))
date.check_date()
