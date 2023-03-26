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
                    headers = message.get("headers", [])
                    headers.append(
                        (b"x-runtime", str((time.time() - start_time) * 1000).encode())
                    )
                    headers.append(
                        (b"x-cpu-used", str(start_cpu).encode())
                    )
                    headers.append(
                        (b"x-memory-used", str(start_mem).encode())
                    )
                    message["headers"] = headers
                await send(message)

            await self.app(scope, receive, send_wrapper)
        else:
            await self.app(scope, receive, send)
