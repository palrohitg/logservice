from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from logapp.serializer.log_serializer import LogSerializer
from logapp.controller.log_controller import LogController
from logapp.utils.constants import Constants 



class Log(APIView):

    serializer_class = LogSerializer
    
    def post(self, request):
        
        serializer = self.serializer_class(self, data=request.data)
        serializer.is_valid(raise_exception=True)
        
        data, error = LogController().process_log(**serializer.validated_data)
        
        if not data or not error:
            response = {"message" : Constants.Response.Message.LOG_NOT_INSERTED}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
        
        response = {
            "message" : Constants.Response.Message.SUCCESS,
            "log_id":Constants.Response.Message.LOG_NOT_INSERTED
            }
        return Response(response, status=status.HTTP_200_OK)
