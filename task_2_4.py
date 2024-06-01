from multiprocessing import Pool

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_twin_primes(start, end):
    return [(n, n+2) for n in range(start, end) if is_prime(n) and is_prime(n+2)]

if __name__ == "__main__":
    range_start = 1
    range_end = 10000
    num_processes = 4

    pool = Pool(processes=num_processes)
    step = (range_end - range_start) // num_processes
    ranges = [(i, i + step if i + step < range_end else range_end) for i in range(range_start, range_end, step)]
    results = pool.starmap(find_twin_primes, ranges)

    twin_primes = [pair for sublist in results for pair in sublist]
    print(twin_primes)