# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 16:55:53 2022

@author: Marcus
"""

%matplotlib qt
import matplotlib.pyplot as plt
import pandas as pd
import os
import numpy as np
import scipy.integrate as integrate
from scipy.stats import norm
from scipy.optimize import curve_fit
import shutil

class sensor():
    """
    Defines a sensor
    """
    def __init__(self, filelist, wafer, size, location, sensortype, newdatastyle, name):
        self.filelist = filelist
        self.wafer = wafer
        self.size = size
        self.location = location
        self.type = sensortype
        self.newdatastyle = newdatastyle
        self.name = name
        
#wafer 11 
LGAD1mm5_11 = sensor('TIMINGdata\wafer11\LGAD1mm1_5', 11, '1mm', 5, 'LGAD', 'normal', 'LGAD1mm5_11_first_run')
#voltagesweep
LGAD1mm5_11_80V = sensor('TIMINGdata\wafer11\LGAD1mm5_11_voltage_sweep\LGAD1mm5_11_80V', 11, '1mm', 5, 'LGAD', 'normal', 'LGAD1mm5_11_80V')
LGAD1mm5_11_120V = sensor('TIMINGdata\wafer11\LGAD1mm5_11_voltage_sweep\LGAD1mm5_11_120V', 11, '1mm', 5, 'LGAD', 'normal', 'LGAD1mm5_11_120V')
LGAD1mm5_11_160V = sensor('TIMINGdata\wafer11\LGAD1mm5_11_voltage_sweep\LGAD1mm5_11_160V', 11, '1mm', 5, 'LGAD', 'normal', 'LGAD1mm5_11_160V')
LGAD1mm5_11_200V = sensor('TIMINGdata\wafer11\LGAD1mm5_11_voltage_sweep\LGAD1mm5_11_200V', 11, '1mm', 5, 'LGAD', 'normal', 'LGAD1mm5_11_200V')
LGAD1mm5_11_240V = sensor('TIMINGdata\wafer11\LGAD1mm5_11_voltage_sweep\LGAD1mm5_11_240V', 11, '1mm', 5, 'LGAD', 'normal', 'LGAD1mm5_11_240V')
LGAD1mm5_11_280V = sensor('TIMINGdata\wafer11\LGAD1mm5_11_voltage_sweep\LGAD1mm5_11_280V\Data', 11, '1mm', 5, 'LGAD', 'normal', 'LGAD1mm5_11_280V')
LGAD1mm5_11_320V = sensor('TIMINGdata\wafer11\LGAD1mm5_11_voltage_sweep\LGAD1mm5_11_320V', 11, '1mm', 5, 'LGAD', 'normal', 'LGAD1mm5_11_320V')
LGAD1mm5_11_340V = sensor('TIMINGdata\wafer11\LGAD1mm5_11_voltage_sweep\LGAD1mm5_11_340V', 11, '1mm', 5, 'LGAD', 'normal', 'LGAD1mm5_11_340V')
LGAD1mm5_11_360V = sensor('TIMINGdata\wafer11\LGAD1mm5_11_voltage_sweep\LGAD1mm5_11_360V', 11, '1mm', 5, 'LGAD', 'normal', 'LGAD1mm5_11_360V')
LGAD1mm5_11_380V = sensor('TIMINGdata\wafer11\LGAD1mm5_11_voltage_sweep\LGAD1mm5_11_380V', 11, '1mm', 5, 'LGAD', 'normal', 'LGAD1mm5_11_380V')
LGAD1mm5_11_400V = sensor('TIMINGdata\wafer11\LGAD1mm5_11_voltage_sweep\LGAD1mm5_11_400V', 11, '1mm', 5, 'LGAD', 'normal', 'LGAD1mm5_11_400V')
LGAD1mm5_11_420V = sensor('TIMINGdata\wafer11\LGAD1mm5_11_voltage_sweep\LGAD1mm5_11_420V', 11, '1mm', 5, 'LGAD', 'normal', 'LGAD1mm5_11_420V')
LGAD1mm5_11_425V = sensor('TIMINGdata\wafer11\LGAD1mm5_11_voltage_sweep\LGAD1mm5_11_425V', 11, '1mm', 5, 'LGAD', 'normal', 'LGAD1mm5_11_425V')
LGAD1mm5_11_430V = sensor('TIMINGdata\wafer11\LGAD1mm5_11_voltage_sweep\LGAD1mm5_11_430V', 11, '1mm', 5, 'LGAD', 'normal', 'LGAD1mm5_11_430V')
LGAD1mm5_11_435V = sensor('TIMINGdata\wafer11\LGAD1mm5_11_voltage_sweep\LGAD1mm5_11_435V', 11, '1mm', 5, 'LGAD', 'normal', 'LGAD1mm5_11_435V')


#wafer 3 voltage sweep
LGAD1mm5_3_125V = sensor('TIMINGdata\wafer3\sweep\Vbias_-125V\Data', 3, '1mm', 5, 'LGAD', 'normal', 'LGAD1mm5_3_125V')
LGAD1mm5_3_130V = sensor('TIMINGdata\wafer3\sweep\Vbias_-130V\Data', 3, '1mm', 5, 'LGAD', 'normal', 'LGAD1mm5_3_130V')
LGAD1mm5_3_135V = sensor('TIMINGdata\wafer3\sweep\Vbias_-135V\Data', 3, '1mm', 5, 'LGAD', 'normal', 'LGAD1mm5_3_135V')
LGAD1mm5_3_140V = sensor('TIMINGdata\wafer3\sweep\Vbias_-140V\Data', 3, '1mm', 5, 'LGAD', 'normal', 'LGAD1mm5_3_140V')
LGAD1mm5_3_145V = sensor('TIMINGdata\wafer3\sweep\Vbias_-145V\Data', 3, '1mm', 5, 'LGAD', 'normal', 'LGAD1mm5_3_145V')
LGAD1mm5_3_150V = sensor('TIMINGdata\wafer3\sweep\Vbias_-150V\Data', 3, '1mm', 5, 'LGAD', 'normal', 'LGAD1mm5_3_150V')

def getdata(file):
    """
    fetches the data from a given file
    returns timetag, chan1, chan2, chan3
    """
    rawdata = []
    chan1 = []
    chan2 = []
    chan3 = []
    timetag = []
    data = []
    
    with open(file, 'r') as filestream:  #change  -1 to something mmore general
            for line in filestream:
                currentline = line.split(',')
                rawdata.append(currentline)
            rawdata = rawdata[24:]
    for i in range(0, len(rawdata)):
        data.append(rawdata[i][0:3])
        timetag.append(float(data[i][0]))
        chan1.append(float(data[i][1]))
        chan2.append(float(data[i][2]))

    return timetag, chan1, chan2

def CFD(channel, fraction):
    """
    returns the index of the (fraction) CFD of that channel from the largest peak
    """
    maxvalueidx = np.argmax(channel)
    #now got index where max occurs, now move in index to the LHS until reach zero
    for i in list(np.arange(len(channel[:maxvalueidx])-1, 0, -1)):
        if channel[:maxvalueidx][i] < 0:
            minvalueidx = i
            break
    #nearest index to 0.25 times the max value within the range set by the cut range above
    #must add back on minvaueidx cus i cut anything below it just to find the nearest
    channeltriggertimeidx = (np.abs(np.array(channel[minvalueidx:maxvalueidx]) - fraction*max(channel))).argmin() + minvalueidx
    return channeltriggertimeidx
    
def coincidencefinder(sensor):
    """
    Takes in a sensor and finds the files with coincidences in
    returns: list of file indexs in which there are coincidences
    but now, to save space, the non-coincidence files will be deleted for good
    """
    filelist = os.listdir(sensor.filelist)  #gets all the files of this sensors data
    currentfile = []
    for i in range(0, len(filelist)):
        currentfile.append(f'{sensor.filelist}/{filelist[i]}')  #currentfile is a list of files all in the correct format for us below
    
    coincidenceindexlist = []
    index = 0   #chnage this into a loop in real thing
    for index in range(0, len(filelist)):
        print(index)
        timetag, chan1, chan2 = getdata(currentfile[index])
        
        #if chan2 contains a peak >threshold. searching for coicidences
        threshold = 50e-3
        if any(i > threshold for i in chan2):
            coincidenceindexlist.append(index)
        else:
            os.remove(currentfile[index])  #if its not a coincidence, DELETE IT NOW!!!!
        #remove ringing peaks that go below -120mV. there's only one in the first 1000 events
        #if any(i < -120e-3 for i in chan2):
    return coincidenceindexlist

#coincidencefinder(LGAD1mm5_11_80V)

def deltaTcalc(sensor, CFDvalue):
    """
    returns list of deltatime list for sensor usin the CFDvalue
    """
    filelist = os.listdir(sensor.filelist)  #gets all the files of this sensors data
    currentfile = []
    for i in range(0, len(filelist)):
        currentfile.append(f'{sensor.filelist}/{filelist[i]}')  #currentfile is a list of files all in the correct format for us below
    
    #coincidenceindexlist = filegrabber(sensor)
    
    deltatime = []
    for file in currentfile:
        timetag, chan1, chan2 = getdata(file)
        
        print(file)
        chan1triggertimeidx = CFD(chan1, CFDvalue)
        chan2triggertimeidx = CFD(chan2, CFDvalue)
        
        deltat = timetag[chan1triggertimeidx] - timetag[chan2triggertimeidx]
        deltatime.append(deltat)
    return deltatime
    
def filecreator(sensor):
    """
    creates a file with the deltaT values in it
    """
    deltatime = deltaTcalc(sensor, 0.25)
    file = open(f'TIMINGdata\deltaTvalues\{sensor.name}.txt', 'w+')
    
    file.write(f'deltaTinseconds for {sensor.name}\n')
    for i in range(0, len(deltatime)):
        file.write(f'{deltatime[i]}\n')
    file.close()

def filegrabber(sensor):
    """
    grabs the coincidence list from the created file
    legacy function now that i just delete the non-coincidence files
    """
    deltatime = []
    rawdata = []
    datapath = f'TIMINGdata\deltaTvalues\{sensor.name}.txt'
    file = open(datapath, 'r')
    for line in file:
        line = line.rstrip('\n')
        rawdata.append(line)
    rawdata = rawdata[1:]
    for i in range(0, len(rawdata)):
        deltatime.append(float(rawdata[i]))
    return deltatime

def plotter(sensor, CFDvalue):
    """
    plots the deltaT histogram and returns its fitted sigma and sigma error
    """
    """
    #still need to file data in order to do all the CFD and timing stuff
    filelist = os.listdir(sensor.filelist)  #gets all the files of this sensors data
    currentfile = []
    for i in range(0, len(filelist)):
        currentfile.append(f'{sensor.filelist}/{filelist[i]}')  #currentfile is a list of files all in the correct format for us below
    
    #coincidenceindexlist = filegrabber(sensor)
    
    deltatime = []
    for file in currentfile:
        timetag, chan1, chan2 = getdata(file)
        
        print(file)
        chan1triggertimeidx = CFD(chan1, CFDvalue)
        chan2triggertimeidx = CFD(chan2, CFDvalue)
        
        deltat = timetag[chan1triggertimeidx] - timetag[chan2triggertimeidx]
        deltatime.append(deltat)
        #if 0.8e-9 < deltat < 2e-9:
        #    deltatime.append(deltat)
        
        #plt.plot(timetag, chan2, label = f'chan2 {index}')
        #plt.plot(timetag, chan1, label = f'chan1 {index}')
        #plt.axvline(x = timetag[chan1triggertimeidx], label = 'CFD')
        #plt.axvline(x = timetag[chan2triggertimeidx], label = 'CFD')
    #plt.legend(fontsize = 18)
    """
    deltatime = filegrabber(sensor)
    
    fig, ax = plt.subplots()
    plt.rcParams["figure.figsize"] = [12,9]
    plt.ylabel('Number of Coincidences in Time Bin', fontsize = 22)
    plt.xlabel('Time Difference Between Detection, $\Delta T$ [s]', fontsize = 22)
    #plt.yscale('log')
    #plt.xlim(-50e-9, 50-9)
    plt.ylim(0, 600)
    ax.minorticks_on()
    ax.grid(which='major', linestyle='-', linewidth='0.5', color='grey')
    ax.grid(which='minor', linestyle=':', linewidth='0.5', color='grey')
    plt.title('Histogram of Time Difference Between Detection \n in Sensors from Wafer 11 and 3', fontsize=22)
    plt.xticks(fontsize = 20)
    plt.yticks(fontsize = 20)
    n, bins, patches = plt.hist(deltatime, bins = 49, range = (0.8e-9, 2e-9), label = 'Coincidence Events \nCFD = 25%', color= 'rebeccapurple')
    
    def gauss(x, A, mu, sigma):
        return A*np.exp(-(x-mu)**2/(2*sigma**2))
    
    x = list(np.linspace(0.8e-9, 2e-9, 49))   #needs to be lowerrange, upperrange, numberofbins. bins = 49 means 25ps bins!
    print(x)
    print(n)
    #index at which x = 1.2e-9 -> index at which x = 1.5e-9
    x, n = x[x.index(1.175e-9):x.index(1.525e-9)], n[x.index(1.175e-9):x.index(1.525e-9)]
    """
    #truncating the tails of the fit
    for i in range(0, len(n)):
        if n[i] < 20:
            n[i] = 0
    newn = []
    newx = []
    for i in range(0, len(x)):
        if n[i] != 0:
            newn.append(n[i])
            newx.append(x[i])
    x = newx
    n = newn
    """
    #x, n = x[x.index(1.175e-9):x.index(1.475e-9)], n[x.index(1.175e-9):x.index(1.475e-9)]
    popt, pcov = curve_fit(gauss, x, n, p0 = [20, 1.35e-9, 0.2e-9])
    
    fittedy = gauss(x, popt[0], popt[1], popt[2])
    fittedsigma = popt[2]*10**12    #intops
    fittedsigmaerror = (pcov[2][2]**0.5)*10**12     #into ps
    plt.plot(x, fittedy, label = f'Gaussian Fit \n$\sigma_{{hist}}$ = ({round(abs(fittedsigma), 2)} $\pm$ {round(fittedsigmaerror, 2)})ps', color = 'orange')
    plt.legend(fontsize = 18, loc = 'upper right')
    #print(f'{fittedsigma}ps pm {(fittedsigmaerror)}ps') #sigma, error on sigma
    
    
    return fittedsigma, fittedsigmaerror

def CFDsweep(sensor):
    """
    does a CFD sweep and plots the time resolution
    this CFD sweep doesnt work anymore now that ive changed the files to output delta T to a text file, because the same 0.25CFD is used in there
    """
    CFDvalues = [0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40, 0.45, 0.50, 0.55, 0.60, 0.65, 0.70, 0.75, 0.80, 0.85, 0.90]
    #CFDvalues = [0.10, 0.15, 0.20, 0.25, 0.30]
    
    timereslist = []
    timereserrrorlist = []
    for CFDvalue in CFDvalues:
        print(CFDvalue)
        width, error = plotter(sensor, CFDvalue)
        timereslist.append(np.sqrt(width**2 - 45.92**2)) #in-line calculation of time res from reference board
        timereserrrorlist.append(np.sqrt(((width*error)/(np.sqrt(width**2 - 45.92**2)))**2 + ((45.92*2.655)/(np.sqrt(width**2 - 45.92)))**2))
        #also, do i make a fitting cut to ignore tails? is there justification for that?
    
    print(timereslist, timereserrrorlist)
    fig, ax = plt.subplots()
    plt.rcParams["figure.figsize"] = [12,9]
    plt.ylabel('Time Resolution [ps]', fontsize = 22)
    plt.xlabel('CFD Value', fontsize = 22)
    #plt.yscale('log')
    #plt.xlim(-50e-9, 50-9)
    plt.ylim(0, 100)
    ax.minorticks_on()
    ax.grid(which='major', linestyle='-', linewidth='0.5', color='grey')
    ax.grid(which='minor', linestyle=':', linewidth='0.5', color='grey')
    plt.title('Time Resolution as a Function of CFD Value', fontsize=22)
    plt.xticks(fontsize = 20)
    plt.yticks(fontsize = 20)
    plt.errorbar(CFDvalues, timereslist, yerr = timereserrrorlist, capsize = 3, label = f'Wafer 11 Loc. 1 1mm LGAD', fmt = 'x', color = 'orangered')
    plt.legend(fontsize = 18)

def VoltageSweep(sensorlist):
    """
    does a sweep of the voltages tested (very manual because will only use twice!)
    """
    #change manually below 
    voltages = [120, 160, 200, 240, 280, 320, 340, 360, 380, 400, 420, 425, 430, 435]
    #voltages = [125, 130, 135, 140, 145, 150]
    
    timereslist = []
    timereserrrorlist = []
    for sensor in sensorlist:
        width, error = plotter(sensor, 0.25)
        timereslist.append(np.sqrt(width**2 - 45.92**2)) #in-line calculation of time res from reference board and its assosiated error below
        timereserrrorlist.append(np.sqrt(((width*error)/(np.sqrt(width**2 - 45.92**2)))**2 + ((45.92*2.655)/(np.sqrt(width**2 - 45.92)))**2))
        
    fig, ax = plt.subplots()
    plt.rcParams["figure.figsize"] = [12,9]
    plt.ylabel('Time Resolution [ps]', fontsize = 22)
    plt.xlabel('Bias Voltage [V]', fontsize = 22)
    #plt.yscale('log')
    #plt.xlim(-50e-9, 50-9)
    plt.ylim(0, 80)
    ax.minorticks_on()
    ax.grid(which='major', linestyle='-', linewidth='0.5', color='grey')
    ax.grid(which='minor', linestyle=':', linewidth='0.5', color='grey')
    plt.title('Time Resolution as a Function of Bias Voltage', fontsize=22)
    plt.xticks(fontsize = 20)
    plt.yticks(fontsize = 20)
    plt.errorbar(voltages, timereslist, yerr = timereserrrorlist, capsize = 3, label = f'Wafer 11 1mm Loc. 5 LGAD', fmt = 'x', color = 'blue')
    plt.legend(fontsize = 18)




#filecreator(LGAD1mm5_11)

#plotter(LGAD1mm5_11, 0.25)
#CFDsweep(LGAD1mm5_11)


#plotter(LGAD1mm5_11_320V, 0.25)

VoltageSweep([LGAD1mm5_11_120V, LGAD1mm5_11_160V, LGAD1mm5_11_200V, LGAD1mm5_11_240V, LGAD1mm5_11_280V, LGAD1mm5_11_320V, LGAD1mm5_11_340V, LGAD1mm5_11_360V, LGAD1mm5_11_380V, LGAD1mm5_11_400V, LGAD1mm5_11_420V, LGAD1mm5_11_425V, LGAD1mm5_11_430V, LGAD1mm5_11_435V])
#VoltageSweep([LGAD1mm5_3_125V, LGAD1mm5_3_130V, LGAD1mm5_3_135V, LGAD1mm5_3_140V, LGAD1mm5_3_145V, LGAD1mm5_3_150V])


