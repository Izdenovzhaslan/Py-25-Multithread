import csv
import threading
import time
import random

filename = 'file.txt'

# def create_random():
#     time.sleep(1)
#     print(random.randrange(1,1000))
#     file.write()

def write_random_number_to_file(filename):
    random_number = random.randint(1, 100)
    
    with open(filename, 'w') as file:
        file.write(str(random_number))
    
    time.sleep(1)

def run_with_threads(num_threads):
    start_time = time.time()
    
    threads = []
    
    for _ in range(num_threads):
        thread = threading.Thread(target=write_random_number_to_file, args=(f'file_{_}.txt',))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()
    
    end_time = time.time()
    
    print(f"Time taken with {num_threads} threads: {end_time - start_time} seconds")

if __name__ == "__main__":
    # а) Одиночный вызов функции
    write_random_number_to_file('single_file.txt')

    print('запуск цикла')

    # б) Запуск циклом 1000 функций
    start_time = time.time()
    for i in range(1000):
        write_random_number_to_file(f'file_{i}.txt')
    end_time = time.time()
    print(f"Time taken for 1000 functions without threading: {end_time - start_time} seconds")

    # в) Мультипоточный запуск с замером времени
    run_with_threads(1000)
