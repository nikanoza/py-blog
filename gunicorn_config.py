import multiprocessing

bind = "0.0.0.0:8000"  # Change to your desired host and port
workers = multiprocessing.cpu_count() * 2 + 1
worker_class = "gthread"
threads = 2 * multiprocessing.cpu_count()