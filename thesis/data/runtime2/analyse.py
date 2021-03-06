import os
from scipy.stats import sem
import numpy as np

numbers = np.loadtxt("data/runtime2/numbers.txt", dtype=np.int64)

# determine an array where each n appears only once
n = []
y = 0
for _n in np.array([len(bin(N))-2 for N in numbers]):
    if len(n) == 0:
        n.append(_n)
    elif np.in1d(np.array([_n]), np.array(n)) == False:
        n.append(_n)
    y += 1
n = np.array(n)

# find the index of a n value in the n list
def nFind(val):
    for i in range(0, n.shape[0]):
        if n[i] == val:
            return i
    return None

# create empty arrays for success, time, steps and their errors
success           = []
successError      = []
time              = []
timeError         = []
steps             = []
stepsError        = []
timeClean         = []
timeErrorClean    = []
stepsClean        = []
stepsErrorClean   = []
for i in range(0, n.shape[0]):
    success.append([])
    successError.append([])
    time.append([])
    timeError.append([])
    steps.append([])
    stepsError.append([])
    timeClean.append([])
    timeErrorClean.append([])
    stepsClean.append([])
    stepsErrorClean.append([])

# load all datasets
for i in range(0, numbers.shape[0]):
    _run, _success, _time, _steps = np.loadtxt("data/runtime2/data/"+str(i)+".txt", unpack=True, dtype=np.int64)

    pos = nFind(len(bin(numbers[i]))-2)

    success[pos].append(np.mean(_success))
    successError[pos].append(sem(_success))
    time[pos].append(np.mean(_time))
    timeError[pos].append(sem(_time))
    steps[pos].append(np.mean(_steps))
    stepsError[pos].append(sem(_steps))

    tmp1 = []
    tmp2 = []
    for j in range(0, _run.shape[0]):
        if _success[j] != 0:
            tmp1.append(_time[j])
            tmp2.append(_steps[j])
    if len(tmp1) == 0:
        tmp1 = [0]
        tmp2 = [0]

    timeClean[pos].append(np.mean(tmp1))
    timeErrorClean[pos].append(sem(tmp1))
    stepsClean[pos].append(np.mean(tmp2))
    stepsErrorClean[pos].append(sem(tmp2))

# calculate average values and their errors
for i in range(0, n.shape[0]):
    success[i]      = np.mean(success[i])
    time[i]         = np.mean(time[i])
    steps[i]        = np.mean(steps[i])
    timeClean[i]    = np.mean(timeClean[i])
    stepsClean[i]   = np.mean(stepsClean[i])
    
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    for j in range(0, len(successError[i])):
        a += successError[i][j]**2
        b += timeError[i][j]**2
        c += stepsError[i][j]**2
        d += timeErrorClean[i][j]**2
        e += stepsErrorClean[i][j]**2
    a = np.sqrt(a)/len(successError[i])
    b = np.sqrt(b)/len(successError[i])
    c = np.sqrt(c)/len(successError[i])
    d = np.sqrt(d)/len(timeErrorClean[i])
    e = np.sqrt(e)/len(timeErrorClean[i])

    successError[i] = a
    timeError[i] = b
    stepsError[i] = c
    timeErrorClean[i] = d
    stepsErrorClean[i] = e

np.savetxt("data/runtime2/results.txt", np.c_[n, success, successError, time, timeError, steps, stepsError, timeClean, timeErrorClean, stepsClean, stepsErrorClean], fmt="%4f")
