#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 21:18:58 2021

@author: srijita
"""
import csv
import numpy as np
import matplotlib
#matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
logfolder="logs"
algo="qlearn"
logging_file="all_logs"
plotfolder="Plots"
#print (plt.isinteractive())
#plt.ioff()
if __name__ == "__main__":
   #Load the csv file
   my_data = np.genfromtxt(f"{logfolder}/{algo}_episode_reward.csv", delimiter=' ',skip_header=1)
   episode=my_data[:,0].astype(int)
   plt.plot(episode, my_data[:,2])
   #plt.show()
   plt.savefig(f"{plotfolder}/{algo}_episode_reward.png")
   
