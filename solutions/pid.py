import os
import concurrent.futures

def pid():
    return os.getpid(), os.getppid()

if __name__ == '__main__':
    print("Main:\n{1}->{0}".format(*pid()))
    print("Siblings:")
    with concurrent.futures.ProcessPoolExecutor() as executor:
        futures = [executor.submit(pid) for _ in range(10)]
    for future in futures:
        if future.exception():
            print(future.exception())
        else:
            print('{1}->{0}'.format(*future.result()))