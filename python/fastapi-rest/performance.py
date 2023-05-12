import time
import psutil

class PerformanceMiddleware:
    def __init__(self, app):
        self.app = app

    async def __call__(self, scope, receive, send):
        start_time = time.time()
        
        await self.app(scope, receive, send)

        end_time = time.time()
        elapsed_time = int((end_time - start_time) * 1000)

        # Get the CPU usage as a percentage.
        cpu_percent = psutil.cpu_percent()
    
        # Calculate the amount of heap memory used in MB.
        mem_used = (psutil.Process().memory_info().rss) / 1024 / 1024
        mem_used = round(mem_used, 2)

        # Return time as ms, CPU usage as a percentage and memory in MB.
        performance_metrics = {
            "time": elapsed_time,
            "cpuUsage": cpu_percent,
            "memUsed": mem_used
        }

        print(performance_metrics)
