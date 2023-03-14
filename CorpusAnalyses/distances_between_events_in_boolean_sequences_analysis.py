import os.path
import random
import matplotlib.pyplot as plt
from Auxiliaries.utils import FOLDER_OF_FIGURES


def extract_distances(boolean_series):
    indices_where_true = [i for i in range(len(boolean_series)) if boolean_series[i]]
    distances_between_true = [indices_where_true[j+1]-indices_where_true[j] for j in range(len(indices_where_true)-1)]
    return distances_between_true

def calc_frequency(distances):
    if len(distances) == 0:
        f = []
    else:
        max_distance = max(distances)
        f = [0 for _ in range(max_distance + 1)]

        for d in distances:
            f[d] += 1

    return f

def calc_relative_frequency(frequency_counter):
    total_sum = sum(frequency_counter)
    r = [frequency_counter[d] / total_sum for d in range(len(frequency_counter))]
    return r



def calc_hazards(r):
    h = [0 for _ in range(len(r))]
    for n in range(len(h)):
        den = sum([r[k] for k in range(len(r)) if k >= n])
        num = r[n]
        h[n] = num/den
    return h


def generate_series(h, n=10, d=1):
    s = []

    while len(s) <= n:
        if d >= len(h):
            print("Failure: Input distance should be less than maximal hazard")

        next_value = random.choices([True, False], [h[d], 1-h[d]])[0]
        s.append(next_value)

        if next_value:
            d = 1
        else:
            d += 1

    return s


def relative_frequency_comparison(r1, r2, ):
    x1 = [i for i in range(0, len(r1))]
    x2 = [i for i in range(0, len(r2))]

    plt.plot(x1, r1, '.')
    plt.plot(x2, r2, '.')

    plt.xlabel('Distances between True values')
    plt.ylabel('relative Frequency')
    plt.title("Relative Frequency Comparison")

    plt.show()

    diff = sum([abs(r1[i]-r2[i]) for i in range(min(len(r1), len(r2)))])
    print("The difference between the relative frequencies adds up to: {}".format(diff))
    # input('waiting for any-key...')


def plot_relative_frequency(r, title="Relative Frequency Plot"):
    x = [i for i in range(1, len(r))]
    y = r[1:]  # without the 0 @ the 0 index

    # plt.plot(x, y, '.')
    plt.loglog(x, y, '.')

    plt.xlabel('Distances between True values')
    plt.ylabel('relative Frequency')
    plt.title(title)
    plt.savefig(os.path.join(FOLDER_OF_FIGURES, title))
    plt.show()

    # input('waiting for any-key...')
