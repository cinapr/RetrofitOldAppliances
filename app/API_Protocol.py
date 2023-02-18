from flask import Flask, request
from Protocol_Function import Protocol_Function

app = Flask(__name__)

@app.route("/", methods=["GET"])
def tuya_control_get():
	return {"message": "API Server of System is Ready"}


@app.route("/changeDeviceStatus", methods=["POST"])
def tuya_control_post():
	data = request.get_json()
	SystemDeviceID = data.get("SystemDeviceID", "")
	CommandType = data.get("CommandType", "")
	CommandStatus = data.get("CommandStatus", False)
	PhoneChargerReason = data.get("PhoneChargerReason", "")
	response = Protocol_Function.control_tuya(SystemDeviceID, CommandType, CommandStatus)

	if (CommandType == "CHANGEDEVICESTATUS"):
		isPushSuccess = Protocol_Function.control_tuya_isSuccess(response)
		Protocol_Function.push_history_tuya(SystemDeviceID, CommandType, str(isPushSuccess), "API", PhoneChargerReason)
		return {"pushResult": isPushSuccess, "message": f"{response}"}
	else :
		return {"message": f"{response}"}


@app.route("/getDeviceStatus", methods=["POST"])
def tuya_control_getDeviceStatus():
	data = request.get_json()
	SystemDeviceID = data.get("SystemDeviceID", "")
	CommandType = "GETVICESTATUS"
	CommandStatus = False
	response = Protocol_Function.control_tuya(SystemDeviceID, CommandType, CommandStatus)
	if (CommandType == "GETVICESTATUS"):
		isPushSuccess = Protocol_Function.control_tuya_isSuccess_forDeviceStatus(response)
		Protocol_Function.push_history_tuya(SystemDeviceID, CommandType, str(isPushSuccess), "API")
		return {"deviceStatus": isPushSuccess, "message": f"{response}"}
	else :
		return {"message": f"{response}"}




if __name__ == "__main__":
	#print (control_tuya("SystemDeviceID", "GETDEVICEINFO", False))
	app.run(debug=True, port=8001)
	#control_tuya("SystemDeviceID", "GETDEVICEINFO", False)