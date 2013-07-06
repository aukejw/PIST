import sys
import glob
import os
import numpy as np
import matplotlib.pyplot as plt
import re
import matplotlib.cm as cm

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

def parse_one_dir(dirname, maxgen_nr):
    avg = []
    mxs = []
    filenames = glob.glob(os.path.join(dirname, '*.txt'))

    sort_nicely(filenames)

    if len(filenames) < maxgen_nr:
        print "Insufficient generations in '{0}'".format(dirname)

    for filename in filenames[:maxgen_nr]:
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
    return avg, mxs

if __name__ == "__main__":
    if len(sys.argv) != 3 or not sys.argv[2].isdigit():
        raise Exception('Usage: graph.py top_dirname maxgeneration')

    print "Searching directory {0}.".format( sys.argv[1] )
    dirnames = [o for o in os.listdir(sys.argv[1]) if os.path.isdir(o)]
    colors = iter( cm.rainbow(np.linspace(0, 1, len(dirnames))))

    fig_max = plt.figure()
    ax_max = fig_max.gca()
    ax_max.set_xlabel("Generation Number")
    ax_max.set_ylabel("Maximum fitness")

    fig_avg = plt.figure()
    ax_avg = fig_avg.gca()
    ax_avg.set_xlabel("Generation Number")
    ax_avg.set_ylabel("Average fitness")

    for dirname, color in zip(dirnames, colors):
        avg, mxs = parse_one_dir(dirname, int(sys.argv[2]))
        xs = np.arange(len(avg))
        ysavg = np.array(avg)
        ysmax = np.array(mxs)

        ax_avg.plot(xs, ysavg, color=color)
        ax_max.plot(xs, ysmax, color=color)


    plt.legend(['{}'.format(dirname) for dirname in dirnames], loc=8,
           ncol=2, mode="expand", bbox_to_anchor=(1.05, 1), borderaxespad=0.)
    plt.show()


