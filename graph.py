import sys
import glob
import os


import re

def tryint(s):
    try:
        return int(s)
    except:
        return s

def alphanum_key(s):
    """ Turn a string into a list of string and number chunks.
    "z23a" -> ["z", 23, "a"]
    """
    return [ tryint(c) for c in re.split('([0-9]+)', s) ]

def sort_nicely(l):
    """ Sort the given list in the way that humans expect.
    """
    l.sort(key=alphanum_key)

if __name__ == "__main__":
    print "Searching directory {0}.".format( sys.argv[1] )

    avg = []
    mxs = []
    filenames = glob.glob(os.path.join(sys.argv[1], '*.txt'))

    sort_nicely(filenames)

    for filename in filenames:
        f = open(filename)
        total = 0
        individuals = 0
        maximum = 0
        for line in f:
            if "------------------------------------" in line:
                num = float(line[:-37])
                total += num
                if num > maximum:
                    maximum = num
                individuals += 1
        avg.append(total / float(individuals))
        mxs.append(maximum)

    import numpy as np
    import matplotlib.pyplot as plt

    fig = plt.figure()
    ax = fig.gca()
    ax.set_xlabel("Generation Number")
    ax.set_ylabel("Average fitness")

    xs = np.arange(len(avg))
    ysavg = np.array(avg)
    ysmax = np.array(mxs)

    ax.plot(xs, ysavg)
    plt.show()


