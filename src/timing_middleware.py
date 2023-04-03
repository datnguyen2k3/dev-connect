import time

class TimingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = time.time()
        response = self.get_response(request)
        response_time = (time.time() - start_time) * 1000
        print(f"Time taken to process request: {response_time:.2f} ms")
        return response
