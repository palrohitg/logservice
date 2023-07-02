from rest_framework import serializers


class LogSerializer(serializers.BaseSerializer):

	def to_internal_value(self, data):
		
		if data is None:
			error = (2, "Bad Request")
			raise serializers.ValidationError({"status": error[0], "message": error[1]})

		if data.get("user_id") is None:
			error = (2, "User Id is missing")
			raise serializers.ValidationError({"status": error[0], "message": error[1]})

		if data.get("event_name") is None:
			error = (2, "Event Name is missing")
			raise serializers.ValidationError({"status": error[0], "message": error[1]})

		if data.get("unix_ts") is None:
			error = (2, "Unix TimeStamp is missing")
			raise serializers.ValidationError({"status": error[0], "message": error[1]})

		if data.get("id") is None:
			error = (2, "Id is missing")
			raise serializers.ValidationError({"status": error[0], "message": error[1]})

		return data