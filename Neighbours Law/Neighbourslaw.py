import numpy as np
import matplotlib.pyplot as plt
import sys




def main():

    # Create array that contains all the data
    with open(sys.argv, 'r') as f:
        data = f.read().split('\n')

    
    # Split the data into seperate arrays and remove the space from each end of the array
    for i in range(len(data)):
        data[i] = data[i].split(' ')
        data[i] = data[i][:-1]
        data[i] = [float(j) for j in data[i]]


    data = np.array(data)

    # count the amount of numbers in each array
    count = []

    for i in range(len(data)):

        count.append(len(data[i]))


    # Print the average, maximum and minimum amount of neighbours
    print("The average amount of neighbours is: ", np.mean(count))
    print("The maximum amount of neighbours is: ", np.max(count))
    print("The minimum amount of neighbours is: ", np.min(count))
    

    # Create a histogram of the amount of numbers in each array
    plt.hist(count, bins=np.arange(min(count), max(count) + 1, 1))
    plt.xticks(np.arange(min(count), max(count) + 1, 1))
    plt.xlabel('Amount of neighbours')
    plt.ylabel('Frequency')
    plt.title('Histogram of the amount of neighbours')
    plt.savefig('Figures/Neighbourslaw.png')

if __name__ == '__main__':
    main()