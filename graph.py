import sys
import glob
import os

if __name__ == "__main__":
    print "Searching directory {0}.".format( sys.argv[1] )

    avg = []
    mxs = []
    for filename in sorted(glob.glob(os.path.join(sys.argv[1], '*.txt'))):
        f = open(filename)
        total = 0
        individuals = 0
        max = 0
        for line in f:
            if "------------------------------------" in line:
                num = float(line[:-37])
                total += num
                if num > max:
                    max = num
                individuals += 1
        avg.append(total / individuals)
        mxs.append(max)

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
    #ax.plot(xs, ysmax)

    plt.show()
