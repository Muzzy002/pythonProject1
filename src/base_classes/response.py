from jsonschema import validate
from src.enums.global_enums import GlobalErrorsMessages as WRONG_EUMS

class Response:

	def __init__(self, response):
		self.response = response
		self.response_json = response.json
		self.response_status = response.status_code

	def validate(self, schema):
		if isinstance(self.response_json, list):
			for item in self.response_json:
				validate(item, schema)
			else:
				validate(self.response_json, schema)

	def assert_status_code(self, status_code):
		if isinstance(status_code, list):
			assert self.response_status in status_code, WRONG_EUMS.WRONG_STATUS_CODE.value
		else:
			assert self.response_status == status_code, WRONG_EUMS.WRONG_STATUS_CODE.value

		return self







