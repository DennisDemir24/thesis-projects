import time
import psutil

class PerformanceMiddleware:
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        if environ["REQUEST_METHOD"] == "GET":
            start_time = time.time()
            start_cpu = psutil.cpu_percent()
            start_mem = psutil.virtual_memory().percent

            def start_response_wrapper(status, headers, exc_info=None):
                headers.append(
                    (b"x-runtime", str((time.time() - start_time) * 1000).encode())
                )
                headers.append(
                    (b"x-cpu-used", str(start_cpu).encode())
                )
                headers.append(
                    (b"x-memory-used", str(start_mem).encode())
                )
                return start_response(status, headers, exc_info)

            return self.app(environ, start_response_wrapper)
        else:
            return self.app(environ, start_response)
