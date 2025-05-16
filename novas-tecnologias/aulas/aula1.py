import psutil

print(f"x: {psutil.cpu_percent(interval=1)}")
mem = psutil.virtual_memory()
print(f"A: {round(mem.total / (1024 ** 2), 2)}")
print(f"B: {round(mem.available / (1024 ** 2), 2)}")
print(f"C: {mem.percent}")