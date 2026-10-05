from concurrent.futures import ThreadPoolExecutor
from collections.abc import Callable

import threading

def run_func_in_pool(func: Callable, n_threads: int = 1, args: list[dict] = [], **fixed_args) -> list:
    results = []
    with ThreadPoolExecutor(max_workers=n_threads) as executor:
        futures = [executor.submit(func, **func_args, **fixed_args) for func_args in args]
        for future in futures:
            results.append(future.result())
    return results
