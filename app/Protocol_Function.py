"""This module has components that are used for testing tuya's device control and Pulsar massage queue."""
import logging

from tuya_connector import (
	TuyaOpenAPI,
	TuyaOpenPulsar,
	TuyaCloudPulsarTopic,
	TUYA_LOGGER,
)

from SQL_Function import SQL_Function

class Protocol_Function():
	# Set up system connection to tuya API
	ACCESS_ID = "drwy7a5x853u74qx85dr"
	ACCESS_KEY = "cbd12905c676413c87a4b8b7f3cf98b6"
	API_ENDPOINT = "https://openapi.tuyaus.com"
	MQ_ENDPOINT = "wss://mqe.tuyaus.com:8285/"


	def get_accessID(SystemDeviceID):
		sql = SQL_Function()
		df = sql.select("SELECT TUYA_DEVICE_ID FROM devices WHERE id = '"+SystemDeviceID+"'")
		# Set up device_id
		#DEVICE_ID ="ebdbab7cc697bcbcb13ijq"
		DEVICE_ID = df[0][0]
		del sql
		return Protocol_Function.ACCESS_ID, Protocol_Function.ACCESS_KEY, DEVICE_ID



	def control_tuya_isSuccess_forDeviceStatus(response):
		# if Protocol_Function.SUCCESS_MSG in response:
		#if (response.get("success") == True):
		if not 'result' in response or len(response['result']) == 0:
			return False
		else :
			result = response.get("result")
			if (result[0].get("value") == True):
				return True
			else:
				return False

	def control_tuya_isSuccess(response):
		# if Protocol_Function.SUCCESS_MSG in response:
		if (response.get("result") == True):
			return True
		else :
			return False


	def push_history_tuya(SystemDeviceID, task, description, source, PhoneChargerReason=""):
		sql_func = SQL_Function()
		query = "INSERT INTO history (device_id, history_datetime, job, description, source, PhoneChargerReason) VALUES (%s, NOW(), %s, %s, %s, %s)"
		values = (str(SystemDeviceID), task, description, source, PhoneChargerReason)
		sql_func.insert(query, values)
		del sql_func


	def control_tuya(SystemDeviceID, CommandType, CommandStatus = False):
		ACCESS_ID, ACCESS_KEY, DEVICE_ID = Protocol_Function.get_accessID(SystemDeviceID)

		# Enable debug log
		TUYA_LOGGER.setLevel(logging.DEBUG)

		# Init OpenAPI and connect
		openapi = TuyaOpenAPI(Protocol_Function.API_ENDPOINT, ACCESS_ID, ACCESS_KEY)
		openapi.connect()

		response = Protocol_Function.API_ENDPOINT + " | " + ACCESS_ID + " | " + ACCESS_KEY + " | " + SystemDeviceID + " | " + CommandType + " | " + str(CommandStatus)
		if (CommandType == "GETDEVICEINFO"):
			# Call APIs from Tuya
			# Get the device information
			response = openapi.get("/v1.0/iot-03/devices/{}".format(DEVICE_ID))

		elif (CommandType == "GETDEVICEFUNCTION"):
			# Get the instruction set of the device
			response = openapi.get("/v1.0/iot-03/devices/{}/functions".format(DEVICE_ID))

		elif (CommandType == "GETVICESTATUS"):
			# Get the status of a single device
			response = openapi.get("/v1.0/iot-03/devices/{}/status".format(DEVICE_ID))
			
		elif (CommandType == "CHANGEDEVICESTATUS"):
			commands = {'commands': [{'code': 'switch_1', 'value': eval(CommandStatus)}]}
			response = openapi.post('/v1.0/iot-03/devices/{}/commands'.format(DEVICE_ID), commands)

		else :
			response = "{'msg': 'COMMEND IS NOT REGISTERED IN THE SYSTEM', 'success': False}"
			
		print(response)
		return response