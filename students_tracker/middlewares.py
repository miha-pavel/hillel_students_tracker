import time

from students.models import Logger


class QueryDurationMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request.start_time = time.time()

        response = self.get_response(request)

        query_duration = time.time() - request.start_time

        response["query_duration"] = int(query_duration * 1000)
        print(f"Django spent {response['query_duration']} ms for query")

        return response


class LoggerAdminMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        current_url = request.path
        request.start_time = time.time()

        response = self.get_response(request)

        if 'admin' in current_url:
            current_user = request.user
            query_duration = time.time() - request.start_time
            Logger.objects.create(
                path=current_url,
                method=Logger.METHODS_REVERSED_MAP[request.method],
                ime_delta=int(query_duration * 1000),
                user_id=current_user.id
            )
        return response
