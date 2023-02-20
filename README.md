## 1. PREPARING THE LIBRARY
Install all the python library required to run the system

(The libraries were listed inside app folder in requirements.txt)

```pip install -r requirements.txt```


## 2. REGISTERING DEVELOPER ACCOUNT
Follow the tutorial of the libraries to register the account to the manufacturer:
```https://github.com/tuya/tuya-connector-python```



## 3. CONFIGURE TUYA DEVELOPER CREDENTIAL
Change the credential of your Tuya Protocol on the file app/Protocol_Function.py according to the credential generated from the 2nd step.

Fill these string from class Protocol_Function(), with the suitable credentials' value :
```
ACCESS_ID = ""
ACCESS_KEY = ""
API_ENDPOINT = ""
MQ_ENDPOINT = ""
```



## 4. SQL
Make a MYSQL server and make a new database with name : ```IOT_Project```

And then import this file to the mysql server : ```IOT_Project.sql```



## 5. CONFIGURE SQL CREDENTIAL
Change the credential of your SQL on the file app/SQL_Function.py according to the credential generated from the 2nd step.

Fill these string from class SQL_Function(), with the suitable credentials' value :
```
HOSTNAME = ""
USERNAME = ""
PASSWORD = ""
DATABASE = "IOT_Project"
```


## 6. WEB APPLICATION FOR REGISTERING USER, DEVICE, SCHEDULE :
Make an webserver for the frontend to registering users, controlled devices, and the schedule.
Follow the instruction here :
```https://github.com/Bamistand/IOT_Frontend_Project.git```



## 7. SCHEDULER FOR SMART-GRID SMART APPLIANCES :
Run scheduler every minute 00, 15, 30, and 45 to run the */app/Scheduler_Function.py* .
For windows : Use task scheduler
For ubuntu linux : Use cron with time setting -> */15 * * * *



## 8. OVER-CHARGING PREVENTION SERVER
#### a. Run the python application server inside an ubuntu VM : 
```python .\API_Protocol.py```


#### b. Do not forget to try it
- Turn off your tuya device.
- Run this testing with postman :
##### Handling : 
```POST```
##### URL :  
```http://[YOUR_SERVER_IP]:8001/changeDeviceStatus```
##### Body Parameter :
```
{
    "SystemDeviceID": "[DEVICE_ID_FROM_POINT_6]",
    "CommandType": "CHANGEDEVICESTATUS",
    "CommandStatus": "True",
    "PhoneChargerReason": "TEST"
}
```
- Make sure it return like this :
```
{
    "message": "{'result': True, 'success': True, 't': ...., 'tid': .....}",
    "pushResult": true
}
```
- And, make sure the testing device now on


## 9. OVER-CHARGING PREVENTION MOBILE APPLICATION
Install the mobile application for over-charging prevention according to this :
```https://github.com/KorawitRupanya/```

