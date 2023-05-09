import time
import psutil

class PerformanceMiddleware:
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        start_time = time.time()
        start_cpu = psutil.cpu_percent()
        start_mem = psutil.virtual_memory().percent

        def start_response_wrapper(status, headers, exc_info=None):
            # Get metrics
            response_time = (time.time() - start_time) * 1000
            cpu_usage = start_cpu
            memory_usage = start_mem
            # Print the performance metrics to the console
            print(f"Response Time: {response_time} ms")
            print(f"CPU Usage: {cpu_usage}%")
            print(f"Memory Usage: {memory_usage}%")
            return start_response(status, headers, exc_info)

        return self.app(environ, start_response_wrapper)