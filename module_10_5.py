import multiprocessing
import datetime


def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            else:
                all_data.append(line)


filenames = [f'./file {number}.txt' for number in range(1, 5)]

# линейный вызов
#start = datetime.datetime.now()
#for name in filenames:
#    read_info(name)
#end = datetime.datetime.now()
#print(end - start)

# многопроцессный
if __name__ == '__main__':
    start = datetime.datetime.now()
    with multiprocessing.Pool(processes=4) as pool:
        pool.map(read_info, filenames)
    end = datetime.datetime.now()
    print(end - start)

 # 0:00:08.731669
 # 0:00:03.404381