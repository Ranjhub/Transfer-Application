from django.db import models
import random
import string

# Create your models here.
def gen_ac_no():
    return ''.join(random.choices(string.digits, k=12))

gender=[
    ('','select'),
    ('Male','Male'),
    ('Female','Female'),
    ('Transender','Transender')
]



class Accounts(models.Model):
    name = models.CharField(max_length=100, null=True)
    age=models.IntegerField(default=0)
    gender=models.CharField(max_length=100,choices=gender,default='none')
    date_of_birth = models.DateField('Data of Birth (ex:yyyy-mm-dd)')
    account_no = models.CharField(max_length=100, default=gen_ac_no, unique=True, editable=False)
    ac_balance = models.FloatField(default=1000)
    ph_number = models.IntegerField()
    create_date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.name

class Transfer(models.Model):
    sender = models.ForeignKey(Accounts, related_name='Senter_transfer', on_delete=models.CASCADE)
    receiver = models.ForeignKey(Accounts, related_name='receiver_transfer', on_delete=models.CASCADE)
    amount = models.FloatField()
    time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.sender.name
    
    @property
    def debit(self):
        return self.sender.name ,self.sender.account_no, -self.amount, self.time
    
    @property
    def credit(self):
        return self.receiver.name, self.receiver.account_no, +self.amount, self.time        
    
    
     