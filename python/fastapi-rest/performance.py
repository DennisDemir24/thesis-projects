import time
import psutil

class PerformanceMiddleware:
    def __init__(self, app):
        self.app = app

    async def __call__(self, scope, receive, send):
        start_time = time.time()
        start_usage = psutil.cpu_times()
        start_memory = psutil.Process().memory_info().rss

        await self.app(scope, receive, send)

        end_time = time.time()
        elapsed_time = int((end_time - start_time) * 1000)

        cpu_used = (psutil.cpu_times().user - start_usage.user) / 1000
        cpu_used = round(cpu_used, 3)
        mem_used = (psutil.Process().memory_info().rss - start_memory) / 1024 / 1024
        mem_used = round(mem_used, 2)

        performance_metrics = {
            "time": elapsed_time,
            "cpuUsed": cpu_used,
            "memUsed": mem_used
        }

        print(performance_metrics)
