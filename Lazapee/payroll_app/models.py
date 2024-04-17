from django.db import models


# Create your models here.
'''Employee
Attributes
name – CharField
id_number – CharField
rate – FloatField
overtime_pay – FloatField (set as nullable)
allowance – FloatField (set as nullable)
'''

class Employee(models.Model):
    name = models.CharField(max_length=300)
    id_number = models.CharField(max_length=300)
    rate = models.FloatField()
    overtime_pay = models.FloatField(null=True)
    allowance = models.FloatField(null=True)
    
    '''Methods
getName(self) – returns the name
getID(self) – returns the id_number
getRate(self) – returns the rate
getOvertime(self) – returns the overtime_pay
resetOvertime(self) – sets overtime_pay to 0
getAllowance(self) – returns the allowance
__str__(self) should print:
pk: id_number, rate: rate'''
    
    def getName(self):
        return self.name
    def getID(self):
        return self.id_number
    def getRate(self):
        return self.rate
    def getOvertime(self):
        return self.overtime_pay
    def resetOvertime(self):
        self.overtime_pay = 0
        self.save()
        return self.overtime_pay
    def getAllowance(self):
        return self.allowance
    def __str__(self):
        return f"pk:{self.id_number}, rate {self.rate}"

class Payslip(models.Model):
    
    '''Attributes
id_number – ForeignKey [NOTE: This is in relation with the employee id_number]
month – CharField
date_range – CharField
year – CharField
pay_cycle – IntegerField
rate - FloatField
earnings_allowance – FloatField
deductions_tax – FloatField
deductions_health – FloatField
pag_ibig – FloatField
sss – FloatField
overtime – FloatField
total_pay – FloatField
'''
    id_number= models.ForeignKey(Employee,on_delete=models.CASCADE)
    month = models.CharField(max_length=300)
    date_range = models.CharField(max_length=300)
    year = models.CharField(max_length=300)
    pay_cycle = models.IntegerField()
    rate = models.FloatField()
    earnings_allowance = models.FloatField()
    deductions_tax = models.FloatField()
    deductions_health = models.FloatField()
    pag_ibig = models.FloatField()
    sss= models.FloatField()
    overtime = models.FloatField()
    total_pay = models.FloatField()
    
    '''Methods
getIDNumber(self) – returns the id number
getMonth(self) – returns the month
getDate_range(self) – returns the date range
getYear(self) – returns the year
getPay_cycle(self) – returns the pay cycle
getRate(self) - returns the rate
getCycleRate(self) - returns the ½ of the rate
getEarnings_allowance(self) – returns the earnings allowance
getDeductions_tax(self) – returns the tax deductions
getDeductions_health(self) – returns the health deductions
getPag_ibig(self) – returns the pag-ibig value
getSSS(self) – returns the sss value
getOvertime(self) – returns the overtime value
getTotal_pay(self) – returns the total pay
__str__(self) should print:
pk: pk, Employee: Employee ID Number, Period: Month Date Range, Year, Cycle: Pay Cycle, Total Pay: Total Pay
'''
    def getIDNumber(self):
        return self.id_number.id_number
    
    def getMonth(self):
        return self.month 
    
    def getDate_range(self):
        return self.date_range
    
    def getYear(self):
        return self.year
    
    def getPay_cycle(self):
        return self.pay_cycle
    
    def getCycle_rate(self):
        return (0.5) * self.rate
    
    def getEarnings_allowance(self):
        return self.earnings_allowance
    
    def getDeductions_tax(self):
        return 0.2 * self.total_pay
    
    def getDeductions_health(self):
        return 0.04 * self.total_pay
    
    def getPag_ibig(self):
        return self.total_pay - 100
    
    def getSSS(self):
        return 0.04 * self.total_pay
    
    def getOvertime(self):
        return self.overtime
    
    def getTotal_pay(self):
        return self.total_pay
    
    def __str__(self):
        return f"pk: {self.pk}, Employee: {self.id_number.id_number}, Period: {self.month} {self.date_range}, {self.year}, Cycle: {self.pay_cycle}, Total Pay: {self.total_pay}"
        
    