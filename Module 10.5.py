import os
from time import time
import multiprocessing

def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        for _ in file:
            if file.readline() == '':
                break
            all_data.append(file.readline())

names_files = [name for name in os.listdir() if os.path.isfile(name) and name.endswith('.txt')]

# start_time = time()
#
# for name in names_files:
#     read_info(name)
#
# end_time = time()
#
# time_1 = end_time - start_time
# print((time_1))

if __name__ == '__main__':
    start_time = time()
    with multiprocessing.Pool(4) as p:
        p.map(read_info, names_files)
    end_time = time()

    time_2 = end_time - start_time
    print((time_2))
