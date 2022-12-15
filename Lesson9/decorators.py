import time


def new_dec(func):
  def new_wrapper(*args, **kwargs):
    func(*args, **kwargs)
    func(*args, **kwargs)
  return new_wrapper



def timer(func):
  def wrapper(*args, **kwargs):
    start_time = time.perf_counter()
    value = func(*args, **kwargs)
    end_time = time.perf_counter()
    run_time = end_time - start_time
    print(f"Finished {func.__name__} in {run_time:.4f} secs")
    return value
  return wrapper