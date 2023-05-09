import time
import psutil

class PerformanceMiddleware:
    def __init__(self, app):
        self.app = app

    async def __call__(self, scope, receive, send):
        if scope["type"] == "http":
            start_time = time.time()
            start_cpu = psutil.cpu_percent()
            start_mem = psutil.virtual_memory().percent

            async def send_wrapper(message):
                if message["type"] == "http.response.start":
                    # Print the performance metrics to the console
                    response_time = (time.time() - start_time) * 1000
                    cpu_usage = start_cpu
                    memory_usage = start_mem
                    print(f"Response Time: {response_time} ms")
                    print(f"CPU Usage: {cpu_usage}%")
                    print(f"Memory Usage: {memory_usage}%")
                await send(message)

            await self.app(scope, receive, send_wrapper)
        else:
            await self.app(scope, receive, send)
