import os
import concurrent.futures

def pid():
    return os.getppid(), os.getpid()

if __name__ == '__main__':
	parent, this = pid()
    print("Main:\n{}->{}".format(parent, this))
    print("Siblings:")
    with concurrent.futures.ProcessPoolExecutor() as executor:
        futures = [executor.submit(pid) for _ in range(10)]
        for future in futures:
            if future.exception():
                print(future.exception())
            else:
            	parent, this = future.result()
                print('{1}->{0}'.format(parent, this))