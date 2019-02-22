import httplib2
import serial
import requests
import time

from twilio.rest import Client
#account = "AC87b15bfd3a62ff7b07fe498901d9e07a"
account = "AC8523fe84591ebdd873362860f3e8f851"
#token = "4a8347e2f1cd1f18b8db8fbfd32cfc29"
token = "ea78a56b16adf0259dc1a7fd88016303"

client = Client(account, token)

ser=serial.Serial('COM4',9600,timeout=2)
print("Hello")
while (True):
    ch=''
    while(ch==''):
        ch=ser.readline().strip().decode('utf-8')
    ch=int(ch)
    print(ch)
    print("got")
    t1=requests.get("https://api.thingspeak.com/update?api_key=Q5EBGVB2SO0UMXGF&field1=%s"%(ch))
    print(t1)    # r=str(ch).split('$')
    if(ch<=3):  
        msg=""
        msg="The Eggs are les than the limit"
        if msg!="":
            print("---->>>message")
            print(client.messages.create(to="+917530003304", from_="+17176742749",body=msg))
        #54FY4DRVHN2S6GZJ
        print(t1)
        print("Uploaded")
        
