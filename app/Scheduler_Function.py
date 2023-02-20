from datetime import datetime, timedelta
from Protocol_Function import Protocol_Function
from SQL_Function import SQL_Function
from datetime import datetime, timedelta

def round_dt(dt, delta):
	return datetime.min + round((dt - datetime.min) / delta) * delta

def get_schedulerTime():
	dt = datetime.now()
	dateSchedule = round_dt(dt, timedelta(minutes=1)) #Get the nearest time to 15 min ago
	#print (dateSchedule)
	sql = SQL_Function()
	query = "SELECT id, User_ID, device_id, time, job, status FROM schedule WHERE time = '"+ str(dateSchedule.time()) +"'"
	rows = sql.select(query)
	#print(dateSchedule)
	#print(query)
	#print(rows)

	countJob = 0
	for row in rows :
		response = Protocol_Function.control_tuya(str(row[2]), str(row[4]), str(row[5]))
		isPushSuccess = Protocol_Function.control_tuya_isSuccess(response)
		Protocol_Function.push_history_tuya(str(row[2]), str(row[4]), str(isPushSuccess), "CRON")
		countJob += 1
	
	del sql
	return countJob



if __name__ == "__main__":
	get_schedulerTime()
