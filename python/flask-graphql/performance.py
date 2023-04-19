import time
import psutil
from flask import request


class PerformanceMiddleware:
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        request_start_time = time.time()
        request_start_cpu = psutil.cpu_percent()
        request_start_mem = psutil.virtual_memory().percent

        def custom_start_response(status, headers, *args, **kwargs):
            headers.append(
                (b"x-runtime", str((time.time() - request_start_time) * 1000).encode())
            )
            headers.append(
                (b"x-cpu-used", str(request_start_cpu).encode())
            )
            headers.append(
                (b"x-memory-used", str(request_start_mem).encode())
            )
            return start_response(status, headers, *args, **kwargs)

        return self.app(environ, custom_start_response)
