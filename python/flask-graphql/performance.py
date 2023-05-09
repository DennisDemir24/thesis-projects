import time
import psutil

class PerformanceMiddleware:
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        if environ["REQUEST_METHOD"] == "POST" and environ["CONTENT_TYPE"] == "application/json":
            start_time = time.time()
            start_cpu = psutil.cpu_percent()
            start_mem = psutil.virtual_memory().percent

            def start_response_wrapper(status, headers, exc_info=None):
                headers.append(("x-runtime", str((time.time() - start_time) * 1000)))
                headers.append(("x-cpu-used", str(start_cpu)))
                headers.append(("x-memory-used", str(start_mem)))
                return start_response(status, headers, exc_info)

            return self.app(environ, start_response_wrapper)
        else:
            return self.app(environ, start_response)
