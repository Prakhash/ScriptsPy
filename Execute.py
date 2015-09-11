from distutils.util import execute
import subprocess
import math
import statistics
import os, subprocess
import sys
import time

# Number of samples used
NO_OF_SAMPLES = 100

# Compile all the source codes
def compileAll():
    subprocess.call(['g++', '-o', 'MatrixMultiplicationSequential', 'MatrixMultiplicationSequential.CPP'])
    subprocess.call(['g++', '-o', 'MatrixMultiplicationParallel', 'MatrixMultiplicationParallel.CPP', '-lm', '-fopenmp'])
    subprocess.call(['g++', '-o', 'MatrixMultiplicationParallelOptimized', 'MatrixMultiplicationParallelOptimized.cpp', '-lm', '-fopenmp'])


# Execute a given process and calculate the average and standard deviation
def execute(command):
    listCommand=[]
    elapsedTimes = []
    listCommand.append(command)
    sizeToRun=100;
    while(sizeToRun<1000):
        for i in range(NO_OF_SAMPLES):
            listCommand.append(str(sizeToRun))
            time = subprocess.Popen(listCommand,stdout=subprocess.PIPE).communicate()[0]
            listCommand.remove(str(sizeToRun))
            elapsedTimes.append(float(time))

            average = statistics.mean(elapsedTimes)
            standardDeviation = statistics.stdev(elapsedTimes)
            print('Average: ' + str(average))
            print('Std.Dev: ' + str(standardDeviation))
        sizeToRun=sizeToRun+100


# Compile all the files
compileAll()
print("Sequential")
execute('./MatrixMultiplicationSequential')
print("\nParallel")
execute('./MatrixMultiplicationParallel')
print("\nParallel Optimized")
execute('./MatrixMultiplicationParallelOptimized')
