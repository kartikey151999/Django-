import datetime
from django.utils.deprecation import MiddlewareMixin

class RequestTimeMiddleware(MiddlewareMixin):
    def process_request(self, request):
        request.start_time = datetime.datetime.now()
        print(f"Request started at: {request.start_time} and Url is {request.path}")

    def process_response(self, request, response):  
        request_end_time = datetime.datetime.now()
        print(f"Request ended at: {request_end_time} and Status is {response.status_code}")