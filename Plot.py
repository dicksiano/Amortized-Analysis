import matplotlib.pyplot as plt

with open("log.txt") as f:
    lines = f.readlines()
    x = [int(line.split()[0]) for line in lines]
    y = [int(line.split()[1]) for line in lines]
    z = [float(y[i] / x[i]) for i in range(len(x))]
    fig1 = plt.figure(figsize=(15,10))
    ax1 = fig1.add_subplot(111)
    ax1.set_title('Amortized Analysis')
    ax1.set_xlabel('Input Size')
    ax1.set_ylabel('Cost / InputSize')
    ax1.plot(x, z)

    fig1=plt.gcf()
    plt.show()
    plt.draw()

    fig2 = plt.figure(figsize=(15,10))
    ax2 = fig2.add_subplot(111)
    ax2.set_title('Time Analysis')
    ax2.set_xlabel('Input Size')
    ax2.set_ylabel('Cost')
    ax2.plot(x, y)

    fig2=plt.gcf()
    plt.show()
    plt.draw()