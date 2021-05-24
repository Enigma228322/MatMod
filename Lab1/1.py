import numpy as np
import imageio
import matplotlib.pyplot as plt
import os
import shutil


def create_field(n):
    field = np.random.randint(0, 2, (n + 1, n + 1))
    for i in range(n + 1):
        field[i][0] = 0
        field[i][n] = 0
        field[0][i] = 0
        field[n][i] = 0
    return field


def life_cycle(field, n):
    for i in range(1, n - 1):
        for j in range(1, n - 1):
            sum = field[i][j + 1] + field[i + 1][j + 1] + field[i + 1][j] + field[i + 1][j - 1] + field[i][j - 1] + field[i - 1][j - 1] + field[i - 1][j] + field[i - 1][j + 1]
            if sum == 2:
                field[i][j] = 1
            elif sum > 2:
                field[i][j] = 0

def gif(n):
    images = []
    filenames = ["cycles/%s.png" % i for i in range(n)]
    for filename in filenames:
        images.append(imageio.imread(filename))
    imageio.mimsave('life.gif', images)

if __name__ == "__main__":
    n = 32
    k = 30
    field = create_field(n)
    if not os.path.exists("cycles"):
        os.mkdir("cycles")
    for i in range(k):
        life_cycle(field, n)
        plt.imshow(field, interpolation='none')
        plt.savefig('cycles/%s.png' % i)
    gif(k)
    shutil.rmtree('cycles')
