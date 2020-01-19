import time


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
