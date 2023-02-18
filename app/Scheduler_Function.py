from datetime import datetime, timedelta
from Protocol_Function import Protocol_Function
from SQL_Function import SQL_Function
from datetime import datetime, timedelta

def round_dt(dt, delta):
	return datetime.min + round((dt - datetime.min) / delta) * delta

def get_schedulerTime():
	dateSchedule = round_dt(dt, timedelta(minutes=15)) #Get the nearest time to 15 min ago
	sql = SQL_Function()
	rows = sql.select("SELECT id, User_ID, device_id, time, job, status FROM schedule WHERE time = '"+ str(dateSchedule.time()) +"'")

	countJob = 0
	for row in rows :
		response = Protocol_Function.control_tuya(str(row["deviceID"]), str(row["job"]), eval(str(row["status"])))
		isPushSuccess = Protocol_Function.control_tuya_isSuccess(response)
		Protocol_Function.push_history_tuya(SystemDeviceID, CommandType, str(isPushSuccess), "CRON")
		countJob += 1
	
	del sql
	return countJob



if __name__ == "__main__":
	get_schedulerTime()