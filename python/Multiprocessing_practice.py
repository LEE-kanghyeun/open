## 참고 자료
# https://docs.python.org/ko/3/library/multiprocessing.html
# http://daplus.net/python-multiprocessing-process%EC%97%90-%EC%A0%84%EB%8B%AC-%EB%90%9C-%ED%95%A8%EC%88%98%EC%9D%98-%EB%B0%98%ED%99%98-%EA%B0%92%EC%9D%84-%EC%96%B4%EB%96%BB%EA%B2%8C-%EB%B3%B5%EA%B5%AC-%ED%95%A0/
# https://www.programcreek.com/python/example/111529/torch.multiprocessing.Manager
# https://ahnty0122.tistory.com/12
# https://ahnty0122.tistory.com/21
# https://superfastpython.com/multiprocessing-pool-wait-for-all-tasks/
# https: // m.blog.naver.com / townpharm / 220951524843
# https: // docs.python.org / ko / 3 / library / multiprocessing.html
# https://stackoverflow.com/questions/64162994/using-the-manager-for-pool-in-the-function-for-multiprocessing-windows-10
# https: // docs.python.org / ko / 3 / library / asyncio - subprocess.html
# https://zetcode.com/python/multiprocessing/
# https://tempdev.tistory.com/27

# from Multiprocessing_practice import Process, Manager
# import Multiprocessing_practice
# import os
# import numpy as np
# import time
# from glob import glob
#
#
# def info(title):
#     print(title)
#     print('module name:', __name__)
#     print('parent process:', os.getppid())
#     print('process id:', os.getpid())
#
# def montihall(a, return_dict):
#     begin_time = time.time()
#     # a = [1, 2, 3]
#     count = 0
#     for j in range(20000):
#         choice = np.random.choice(a, 1, True)
#         answer = np.random.choice(a, 1, True)
#         # print('choice: ', choice)
#         # print('answer: ', answer)
#
#         b = a.copy()
#
#         if choice == answer:
#             b.remove(answer)
#         else:
#             b.remove(answer)
#             b.remove(choice)
#         # print(b)
#         open = np.random.choice(b, 1, True)
#         # print('open: ', open)
#
#         c = a.copy()
#         c.remove(open)
#         c.remove(choice)
#
#         new_choice = c[0]
#
#         if new_choice == answer:
#             count += 1
#
#
#     end_time = time.time()
#     print('beign_time: ',begin_time, 'end_time: ',end_time)
#     return_dict[str(count)]=count
#
#     # return count
#
# def f(name):
#     info('function f')
#     print('hello', name)
#
#
#
#
# if __name__ == '__main__':
#     # info('main line')
#
#     # monti()
#
#     # p = Process(target=f, args=('bob',))
#     # p.start()
#     # p.join()
#     Multiprocessing_practice.set_start_method('spawn', force=' True')
#     manager = Manager()
#     return_dict = manager.dict()
#
#     processes = []
#     a = [[1,2,3], [3,2,1], [1,2,3,4], [1,3,2]]
#
#     result = []
#     for i in range(4):
#         p = Process(target=montihall, args=(a[i],return_dict))
#         p.start()
#         # print(p)
#         processes.append(p)
#
#     # print(processes)
#
#     for p in processes:
#         p.join()
#         print(p.is_alive())
#
#     result = return_dict.values()
#     print(return_dict)
#     print(result)


###############################################################################################################

#
# import Multiprocessing_practice
#
# def worker(procnum, return_dict):
#     '''worker function'''
#     print (str(procnum) + ' represent!')
#     return_dict[procnum] = procnum
#
#
# if __name__ == '__main__':
#     manager = Multiprocessing_practice.Manager()
#     return_dict = manager.dict()
#     jobs = []
#     for i in range(5):
#         p = Multiprocessing_practice.Process(target=worker, args=(i, return_dict))
#         jobs.append(p)
#         p.start()
#
#     for proc in jobs:
#         proc.join()
#     print (return_dict.values())
#     dic = {}
#     dic[str(os.getpid())]= 'a'
#     print(str(os.getpid()))
#     print(dic)



###############################################################################################

from multiprocessing import Process, Manager
import multiprocessing
import os
import numpy as np
import time
from glob import glob
import math


def list_split(path_list, n):
    mok = math.ceil(len(path_list) / n )
    path_split_list = []
    for i in range(n-1):
        path_split_list.append(path_list[i*mok :(i+1)*mok])
    else:
        path_split_list.append(path_list[(n-1) * mok:])
    return path_split_list

def inference(path):

    print(glob(os.path.join(path, '*')))
    path_list = glob(os.path.join(path, '*'))

    multiprocessing.set_start_method('spawn', force=' True')
    manager = Manager()
    return_list = manager.list()
    processes = []
    n=4  ## 프로세스를 분할할 개수
    print(len(path_list))

    path_split_list = list_split(path_list, n)
    print(path_split_list)
    print(len(path_split_list))

    for i in range(n):
        p = Process(target=result_collect, args=(path_split_list[i],return_list))
        p.start()
        processes.append(p)
    for p in processes:
        p.join()
        print(p.is_alive())

    return sorted(return_list, key=lambda x: x['filename'])


def result_collect(path_list, return_list):
    print('1')
    # print(len(path_list))
    for path in path_list:
        return_list.append(
            {
        'filename' : path.split('\\')[-1],
        'text' : single_infer(path)
            }
        )


def single_infer(audio_path):
    sentence = 'Good!!' + audio_path
    return sentence


if __name__ == '__main__':
    path = r'C:\Users\6509504\Desktop'
    path = r'C:\Users\6509504\Desktop\test_folder'
    result = inference(path)
    print(result)
    print(len(result))


###############################################################################################

from multiprocessing import Process, Manager, Pool
import multiprocessing
import os
import numpy as np
import time
from glob import glob
import math
from contextlib import contextmanager

@contextmanager
def poolcontext(*args, **kwargs):
    pool = multiprocessing.Pool(*args, **kwargs)
    yield pool
    pool.terminate()

def inference(path):
    path_list = glob(os.path.join(path, '*'))
    n=4  ## 프로세스를 분할할 개수
    startTime = int(time.time())

    with poolcontext(processes=n) as pool:  ## pool.starmap 방식을 쓰면 인자를 2개 이상 쓸수 있음
        results = pool.starmap(result_collect, zip(path_list))
    print(results)
    endTime = int(time.time())
    print("총 작업 시간", (endTime - startTime))

    return sorted(results, key=lambda x: x['filename'])


def result_collect(path):
    results =    {
        'filename' : path.split('\\')[-1],
        'text' : single_infer(path)
            }

    return results


def single_infer(audio_path):
    sentence = 'Good!!' + audio_path
    return sentence


if __name__ == '__main__':
    path = r'C:\Users\6509504\Desktop'
    # path = r'C:\Users\com\Desktop\이강현 바탕화면'
    result = inference(path)
    print(result)
    print(len(result))



###############################################################################################

from multiprocessing import Process, Manager, Pool
import multiprocessing
import os
import numpy as np
import time
from glob import glob
import math
from contextlib import contextmanager

@contextmanager
def poolcontext(*args, **kwargs):
    pool = multiprocessing.Pool(*args, **kwargs)
    yield pool
    pool.terminate()

def f(x,y):
    # print("값", x, "에 대한 작업 Pid = ",os.getpid())
    time.sleep(1)
    return x*y

if __name__ == '__main__':

    startTime = int(time.time())

    with poolcontext(processes = 4) as pool:   ## pool.starmap 방식을 쓰면 함수 인자를 2개 이상 쓸수 있음
        result = pool.starmap(f, zip(range(0,100), range(0,100)))
    print(result)
    endTime = int(time.time())
    print("총 작업 시간", (endTime - startTime))



###############################################################################################

# def list_split(path_list, n):
#     mok = math.ceil(len(path_list) / n )
#     path_split_list = []
#     for i in range(n-1):
#         path_split_list.append(path_list[i*mok :(i+1)*mok])
#     else:
#         path_split_list.append(path_list[(n-1) * mok:])
#     return path_split_list
#
# def inference(path):
#
#     path_list = glob(os.path.join(path, '*'))
#     n=4  ## 프로세스를 분할할 개수
#
#     path_split_list = list_split(path_list, n)
#     print(path_split_list)
#     print(len(path_split_list))
#
#     p =Pool(4)
#     results = p.map(result_collect, path_list)   # p.map 방식은 함수 인자를 1개만 받을수 있음
#     print('result:', results)
#     print(len(results))
#     return sorted(results, key=lambda x: x['filename'])
#
#
# def result_collect(path):
#     print('1')
#     results =    {
#         'filename' : path.split('\\')[-1],
#         'text' : single_infer(path)
#             }
#     # results = []
#     # for path in path_list:
#     #     results .append(
#     #         {
#     #     'filename' : path.split('\\')[-1],
#     #     'text' : single_infer(path)
#     #         }
#     #     )
#     return results
#
#
# def single_infer(audio_path):
#     sentence = 'Good!!' + audio_path
#     return sentence
#
#
#
# if __name__ == '__main__':
#     # path = r'C:\Users\6509504\Desktop'
#     path = r'C:\Users\com\Desktop\이강현 바탕화면'
#     result = inference(path)
#     print(result)
#     print(len(result))


###############################################################################################

@contextmanager
def poolcontext(*args, **kwargs):
    pool = multiprocessing.Pool(*args, **kwargs)
    yield pool
    pool.terminate()

def inference(path):
    path_list = glob(os.path.join(path, '*'))
    n=4  ## 프로세스를 분할할 개수
    model = 'Good!!!'
    startTime = int(time.time())
    items = [(model, path) for path in path_list]

    with poolcontext(processes=4) as pool:
        results = pool.starmap(result_collect, items)
        pool.close()
        pool.join()
    print(results)
    endTime = int(time.time())
    print("총 작업 시간", (endTime - startTime))

    return sorted(results, key=lambda x: x['filename'])


def result_collect(model, path):
    results =    {
        'filename' : path.split('\\')[-1],
        'text' : single_infer(model, path)
            }
    # results = []
    # for path in path_list:
    #     results .append(
    #         {
    #     'filename' : path.split('\\')[-1],
    #     'text' : single_infer(path)
    #         }
    #     )
    return results


def single_infer(model, audio_path):
    sentence = model + audio_path
    return sentence


if __name__ == '__main__':
    path = r'C:\Users\6509504\Desktop'
    # path = r'C:\Users\com\Desktop\이강현 바탕화면'
    result = inference(path)
    print(result)
    print(len(result))
