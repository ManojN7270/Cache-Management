import numpy as np
from matplotlib import pyplot as plt

ys = 200 + np.random.randn(100)
x = [x for x in range(len(ys))]

plt.plot(x, ys, '-')
plt.fill_between(x, ys, 195, where=(ys > 195), facecolor='g', alpha=0.6)

plt.title("Sample Visualization")
plt.show()
requests = []
cache = []

def main():
    while True:
        try:
            num = int(input("Enter an integer. Please enter 0 to end"))
            if num != 0: requests.append(num)
        except ValueError:
            print("Please enter a valid integer")
            continue
        if num == 0:
            choice = input('Choosing the eviction algorithm:\n 1.FIFO \n 2.LFU \n Q.Quit the program')

            if choice in ['Q', 'q']:
                print("Exiting the program")
            else:
                if choice == '1':
                    fifo()
                elif choice == '2':
                    lfu()
            exit()
        else:
            continue

def fifo():

    print("You have chosen 1. FIFO")
    for item in requests:
        if len(cache) < 8:
            if item not in cache:
                print("Miss")
                cache.append(item)
            else:
                print("Hit")
        else:
            if item not in cache:
                print("Miss")
                cache.pop(0)
                cache.append(item)
            else:
                print("Hit")
    print('Cache:', cache)
    cache.clear()
    requests.clear()
    main()

def lfu():
    cache_dict = {}
    print("You have chosen 2. LFU")

    for item in requests:
        if len(cache) < 8:
            if item not in cache_dict:
                cache_dict[item] = 1
                if item not in cache:
                    cache.append(item)
                    print("Miss")
            else:
                cache_dict[item] += 1
                print("Hit")
        else:
            if item not in cache:
                min_number = {}
                min_numbers = []
                for key, value in cache_dict.items():
                    if key in cache:
                        min_number[key] = value

                min_value = min(min_number.values())

                for key, value in min_number.items():
                    if value == min_value:
                        min_numbers.append(key)
                cache.remove(min(min_numbers))
                if item in cache_dict:
                    cache_dict[item] += 1
                else:
                    cache_dict[item] = 1
                cache.append(item)
                print("Miss")
            else:
                print("Hit")
                cache_dict[item] += 1

    print('Cache:', cache)
    cache.clear()
    requests.clear()
    main()

main()

