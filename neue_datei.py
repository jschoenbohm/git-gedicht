import matplotlib.pyplot as plt

def f(x):
    y = x*x
    return y

def plot(x,y):
    plt.plot(x,y)
    plt.grid()
    plt.show()

if __name__ == "__main__":
    x = [i for i in range(10)]
    y = [f(k) for k in x]
    plot(x,y)