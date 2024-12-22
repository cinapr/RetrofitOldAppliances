# IoT-Enhanced Retrofitting Old into Smart Appliance 
Welcome to our IoT project aimed at creating a sustainable and cost-effective solution for turning traditional analog appliances into smart appliances. This initiative addresses critical challenges in urban living, such as energy efficiency, parking space dependency, and environmental sustainability.

## Demo and Presentation
Please kindly check our youtube video : [https://youtu.be/JrmqSYBcZCY](https://youtu.be/JrmqSYBcZCY)

## Background
The increasing population leads to higher transportation demands, intensifying parking space dependency. While public transportation remains a sustainable option, private vehicles offer unmatched convenience. Although driverless shared cars could be a future solution, the immediate need lies in enhancing existing infrastructure. IoT-based parking systems provide a smarter and more achievable solution than traditional methods, which often result in traffic congestion and minor collisions due to difficulty in locating vacant slots.

## Project Goal
Our project focuses on retrofitting traditional analog appliances with smart functionalities without replacing them entirely, reducing e-waste. This approach makes existing appliances:

## Remotely Controllable
Energy Efficient through features like overcharging prevention and reduced vampire energy consumption.
Vampire energy accounts for 5–10% of residential electricity use and approximately 1% of global CO2 emissions. To combat this, our solution automatically switches off appliances when fully charged.

## Scope
- Retrofitting analog appliances with smart plugs.
- No development of new IoT devices or smart home systems.

## Tech Stack
- Frontend: PHP, HTML
- Backend: Python
- Database: MySQL
- Mobile Connectivity: Flutter
- Hardware : Tuya Smart Plug
- IOT Connection : Tuya SDK

## Documentation
Full documentation can be access on these files inside this repo : `Presentation.pdf` and `Documentation.pdf`

## How to run the system?

### 1. PREPARING THE LIBRARY
Install all the python library required to run the system

(The libraries were listed inside app folder in requirements.txt)

```pip install -r requirements.txt```


### 2. REGISTERING DEVELOPER ACCOUNT
Follow the tutorial of the libraries to register the account to the manufacturer:
```https://github.com/tuya/tuya-connector-python```



### 3. CONFIGURE TUYA DEVELOPER CREDENTIAL
Change the credential of your Tuya Protocol on the file app/Protocol_Function.py according to the credential generated from the 2nd step.

Fill these string from class Protocol_Function(), with the suitable credentials' value :
```
ACCESS_ID = ""
ACCESS_KEY = ""
API_ENDPOINT = ""
MQ_ENDPOINT = ""
```



### 4. SQL
Make a MYSQL server and make a new database with name : ```IOT_Project```

And then import this file to the mysql server : ```IOT_Project.sql```



### 5. CONFIGURE SQL CREDENTIAL
Change the credential of your SQL on the file app/SQL_Function.py according to the credential generated from the 2nd step.

Fill these string from class SQL_Function(), with the suitable credentials' value :
```
HOSTNAME = ""
USERNAME = ""
PASSWORD = ""
DATABASE = "IOT_Project"
```


### 6. WEB APPLICATION FOR REGISTERING USER, DEVICE, SCHEDULE :
Make a web server for the frontend to registering users, controlled devices, and the schedule.
Follow the instruction here :
```https://github.com/Bamistand/IOT_Frontend_Project.git```



### 7. SCHEDULER FOR SMART-GRID SMART APPLIANCES :
Run scheduler every minute 00, 15, 30, and 45 to run the */app/Scheduler_Function.py* .

For windows : Use task scheduler

For ubuntu linux : Use cron with time setting -> ``` */15 * * * * ```



### 8. OVER-CHARGING PREVENTION SERVER
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


### 9. OVER-CHARGING PREVENTION MOBILE APPLICATION
Install the mobile application for over-charging prevention according to this :
```https://github.com/KorawitRupanya/BatteryCheckerFlutter```

## How to run with Docker?
1. Use docker build command which it will use the Dockerfile to build a new container image(protocol is the name of the image which you can specify to whatever you want)
```
docker build -t protocol .
```
2. Start your container using docker run command and specify the name of the image you just created:
```
docker run -dp 3000:8001 protocol
```
3. Now the API should run at [localhost:3000](localhost:3000). You can check by go directly to the port, if you see the massage ``{"message":"API Server of System is Ready"} `` that means the API is running and ready to be used.
