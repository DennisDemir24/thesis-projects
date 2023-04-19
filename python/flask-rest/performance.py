import time
import psutil

class PerformanceMiddleware:
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        start_time = time.time()
        start_cpu = psutil.cpu_percent()
        start_mem = psutil.virtual_memory().percent

        def start_response_wrapper(status, headers, *args, **kwargs):
            headers += [
                ("x-runtime", str((time.time() - start_time) * 1000)),
                ("x-cpu-used", str(start_cpu)),
                ("x-memory-used", str(start_mem)),
            ]
            return start_response(status, headers, *args, **kwargs)

        return self.app(environ, start_response_wrapper)
