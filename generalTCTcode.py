# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 22:41:11 2022

@author: Marcus
"""
%matplotlib qt
import matplotlib.pyplot as plt
import pandas as pd
import os
import numpy as np
import scipy.integrate as integrate

class sensor():
    """
    Defines a sensor
    """
    def __init__(self, filelist, wafer, size, location, sensortype, newdatastyle, laserpower, name):
        self.filelist = filelist
        self.wafer = wafer
        self.size = size
        self.location = location
        self.type = sensortype
        self.newdatastyle = newdatastyle
        self.laserpower = laserpower
        self.name = name
        
F7LS1FD1_50p = sensor('TCTData\wafer3\TCTBoard_W3_F7LS1FD1_50%_1650mV_50Hz_ND0.0_6.5VAmpBias\Data', 3, '1mm', 1, 'LGAD', 'normal', 50, 'F7LS1FD1_50p')
F7PS1FD1_10p = sensor('TCTData\wafer3\TCTBoard_W3_F7PS1FD1_10%_330mV_50Hz_ND0.0_6.5VAmpBias\Data', 3, '1mm', 1, 'PiN', 'normal', 10, 'F7PS1FD1_10p')
F7PS1FD1_40p = sensor('TCTData\wafer3\TCTBoard_W3_F7PS1FD1_40%_1320mV_50Hz_ND0.0_6.5VAmpBias\Data', 3, '1mm', 1, 'PiN', 'normal', 40, 'F7PS1FD1_40p')
F25LS1FD1_50p = sensor('TCTData\wafer3\TCTBoard_W3_F25LS1FD1_50%_1650mV_50Hz_ND0.0_6.5VAmpBias\Data', 3, '1mm', 1, 'LGAD', 'normal', 50, 'F25LS1FD1_50p')
F25PS1FD1_40p = sensor('TCTData\wafer3\TCTBoard_W3_F25PS1FD1_40%_1320mV_50Hz_ND0.0_6.5VAmpBias\Data', 3, '1mm', 1, 'LGAD', 'normal', 40, 'F25PS1FD1_40p')

#LGAD power sweep files:
W3_F7LS1FD2_10p = sensor('TCTData\wafer3\PowerSweeps\TCTBoard_W3_F7LS1FD2_10%_330mV_50Hz_ND0.0_6.5VAmpBias_PowerSweep\Data', 3, '1mm', 1, 'LGAD', 'normal', 10, 'W3_F7LS1FD2_10p')
W3_F7LS1FD2_20p = sensor('TCTData\wafer3\PowerSweeps\TCTBoard_W3_F7LS1FD2_20%_660mV_50Hz_ND0.0_6.5VAmpBias_PowerSweep\Data', 3, '1mm', 1, 'LGAD', 'normal', 20, 'W3_F7LS1FD2_20p')
W3_F7LS1FD2_30p = sensor('TCTData\wafer3\PowerSweeps\TCTBoard_W3_F7LS1FD2_30%_990mV_50Hz_ND0.0_6.5VAmpBias_PowerSweep\Data', 3, '1mm', 1, 'LGAD', 'normal', 30, 'W3_F7LS1FD2_30p')
W3_F7LS1FD2_40p = sensor('TCTData\wafer3\PowerSweeps\TCTBoard_W3_F7LS1FD2_40%_1320mV_50Hz_ND0.0_6.5VAmpBias_PowerSweep\Data', 3, '1mm', 1, 'LGAD', 'normal', 40, 'W3_F7LS1FD2_40p')
W3_F7LS1FD2_50p = sensor('TCTData\wafer3\PowerSweeps\TCTBoard_W3_F7LS1FD2_50%_1650mV_50Hz_ND0.0_6.5VAmpBias_PowerSweep\Data', 3, '1mm', 1, 'LGAD', 'normal', 50, 'W3_F7LS1FD2_50p')

#PiN power sweep files:
W3_F25PS1FD1_00p = sensor('TCTData\wafer3\PowerSweeps\TCTBoard_W3_F25PS1FD1_00%_0000mV_50Hz_ND0.0_6.5VAmpBias_PowerSweep\Data', 3, '1mm', 1, 'PiN', 'normal', 0, '')
W3_F25PS1FD1_05p = sensor('TCTData\wafer3\PowerSweeps\TCTBoard_W3_F25PS1FD1_05%_0165mV_50Hz_ND0.0_6.5VAmpBias_PowerSweep\Data', 3, '1mm', 1, 'PiN', 'normal', 5, '')
W3_F25PS1FD1_10p = sensor('TCTData\wafer3\PowerSweeps\TCTBoard_W3_F25PS1FD1_10%_0330mV_50Hz_ND0.0_6.5VAmpBias_PowerSweep\Data', 3, '1mm', 1, 'PiN', 'normal', 10, '')
W3_F25PS1FD1_15p = sensor('TCTData\wafer3\PowerSweeps\TCTBoard_W3_F25PS1FD1_15%_0495mV_50Hz_ND0.0_6.5VAmpBias_PowerSweep\Data', 3, '1mm', 1, 'PiN', 'normal', 15, '')
W3_F25PS1FD1_20p = sensor('TCTData\wafer3\PowerSweeps\TCTBoard_W3_F25PS1FD1_20%_0660mV_50Hz_ND0.0_6.5VAmpBias_PowerSweep\Data', 3, '1mm', 1, 'PiN', 'normal', 20, '')
W3_F25PS1FD1_25p = sensor('TCTData\wafer3\PowerSweeps\TCTBoard_W3_F25PS1FD1_25%_0825mV_50Hz_ND0.0_6.5VAmpBias_PowerSweep\Data', 3, '1mm', 1, 'PiN', 'normal', 25, '')
W3_F25PS1FD1_30p = sensor('TCTData\wafer3\PowerSweeps\TCTBoard_W3_F25PS1FD1_30%_0990mV_50Hz_ND0.0_6.5VAmpBias_PowerSweep\Data', 3, '1mm', 1, 'PiN', 'normal', 30, '')
W3_F25PS1FD1_35p = sensor('TCTData\wafer3\PowerSweeps\TCTBoard_W3_F25PS1FD1_35%_1155mV_50Hz_ND0.0_6.5VAmpBias_PowerSweep\Data', 3, '1mm', 1, 'PiN', 'normal', 35, '')
W3_F25PS1FD1_40p = sensor('TCTData\wafer3\PowerSweeps\TCTBoard_W3_F25PS1FD1_40%_1320mV_50Hz_ND0.0_6.5VAmpBias_PowerSweep\Data', 3, '1mm', 1, 'PiN', 'normal', 40, 'W3_F25PS1FD1_40p')
W3_F25PS1FD1_45p = sensor('TCTData\wafer3\PowerSweeps\TCTBoard_W3_F25PS1FD1_45%_1485mV_50Hz_ND0.0_6.5VAmpBias_PowerSweep\Data', 3, '1mm', 1, 'PiN', 'normal', 45, '')
W3_F25PS1FD1_50p = sensor('TCTData\wafer3\PowerSweeps\TCTBoard_W3_F25PS1FD1_50%_1650mV_50Hz_ND0.0_6.5VAmpBias_PowerSweep\Data', 3, '1mm', 1, 'PiN', 'normal', 50, '')
W3_F25PS1FD1_55p = sensor('TCTData\wafer3\PowerSweeps\TCTBoard_W3_F25PS1FD1_55%_1815mV_50Hz_ND0.0_6.5VAmpBias_PowerSweep\Data', 3, '1mm', 1, 'PiN', 'normal', 55, '')
W3_F25PS1FD1_60p = sensor('TCTData\wafer3\PowerSweeps\TCTBoard_W3_F25PS1FD1_60%_1980mV_50Hz_ND0.0_6.5VAmpBias_PowerSweep\Data', 3, '1mm', 1, 'PiN', 'normal', 60, '')

#wafer 6:
LGAD1mm5_6_45p_first = sensor('TCTData\wafer6\TCTBoard_W6_LGAD_loc5_1mm_D2_45%_1485mV_50Hz_ND0.0_6.5VAmpBias_March30\Data', 6, '1mm', 5, 'LGAD', 'normal', 45, 'LGAD1mm5_6_45p_first')
LGAD1mm5_6_45p_second = sensor('TCTData\wafer6\TCTBoard_W6_LGAD_loc5_1mm_D2_45%_1485mV_50Hz_ND0.0_6.5VAmpBias_March31\Data', 6, '1mm', 5, 'LGAD', 'normal', 45, 'LGAD1mm5_6_45p_second')
LGAD1mm5_6_45p_third = sensor('TCTData\wafer6\TCTBoard_W6_LGAD_loc5_1mm_D2_45%_1485mV_50Hz_ND0.0_6.5VAmpBias_April1\Data', 6, '1mm', 5, 'LGAD', 'normal', 45, 'LGAD1mm5_6_45p_third')
LGAD1mm1_6_45p = sensor('TCTData\wafer6\TCTBoard_W6_LGAD_loc1_1mm_D2_45%_1485mV_50Hz_ND0.0_6.5VAmpBias\Data', 6, '1mm', 1, 'LGAD', 'normal', 45, 'LGAD1mm1_6_45p')
#powersweep
LGAD1mm5_6_35p = sensor('TCTData\wafer6\TCTBoard_W6_LGAD_loc5_1mm_D2_35%_1155mV_50Hz_ND0.0_6.5VAmpBias_PowerSweep1\Data', 6, '1mm', 5, 'LGAD', 'normal', 35, 'LGAD1mm5_6_35p')
LGAD1mm5_6_40p = sensor('TCTData\wafer6\TCTBoard_W6_LGAD_loc5_1mm_D2_40%_1320mV_50Hz_ND0.0_6.5VAmpBias_PowerSweep2\Data', 6, '1mm', 5, 'LGAD', 'normal', 40, 'LGAD1mm5_6_40p')
LGAD1mm5_6_45p = sensor('TCTData\wafer6\TCTBoard_W6_LGAD_loc5_1mm_D2_45%_1485mV_50Hz_ND0.0_6.5VAmpBias_PowerSweep3\Data', 6, '1mm', 5, 'LGAD', 'normal', 45, 'LGAD1mm5_6_45p')
LGAD1mm5_6_50p = sensor('TCTData\wafer6\TCTBoard_W6_LGAD_loc5_1mm_D2_50%_1650mV_50Hz_ND0.0_6.5VAmpBias_PowerSweep4\Data', 6, '1mm', 5, 'LGAD', 'normal', 50, 'LGAD1mm5_6_50p')

#okay, now we have the 90/10 stuff below
LGAD1mm5_6_35p_9010 = sensor('TCTData\wafer6\9010stuff\TCTBoard_W6_LGAD_loc5_1mm_D2_35%_1155mV_50Hz_ND0.0_6.5VAmpBias_April29\Data', 6, '1mm', 5, 'LGAD', 'normal', 35, 'LGAD1mm5_6_35p_9010')
LGAD1mm5_6_40p_9010 = sensor('TCTData\wafer6\9010stuff\TCTBoard_W6_LGAD_loc5_1mm_D2_40%_1320mV_50Hz_ND0.0_6.5VAmpBias_April29\Data', 6, '1mm', 5, 'LGAD', 'normal', 40, 'LGAD1mm5_6_40p_9010')
LGAD1mm5_6_45p_9010 = sensor('TCTData\wafer6\9010stuff\TCTBoard_W6_LGAD_loc5_1mm_D2_45%_1485mV_50Hz_ND0.0_6.5VAmpBias_April29\Data', 6, '1mm', 5, 'LGAD', 'normal', 45, 'LGAD1mm5_6_45p_9010')
LGAD1mm5_6_50p_9010 = sensor('TCTData\wafer6\9010stuff\TCTBoard_W6_LGAD_loc5_1mm_D2_50%_1155mV_50Hz_ND0.0_6.5VAmpBias_April29\Data', 6, '1mm', 5, 'LGAD', 'normal', 50, 'LGAD1mm5_6_50p_9010')
PiN1mm1_6_10p_9010 = sensor('TCTData\wafer6\9010stuff\TCTBoard_W6_PiN_loc1_1mm_D2_10%_330mV_50Hz_ND0.0_6.5VAmpBias_April29\Data', 6, '1mm', 5, 'PiN', 'normal', 10, 'PiN1mm1_6_10p_9010')

#calibration done, now to open the appature a bit for actual gain measurement
LGAD1mm1_6_45p_9010_new = sensor('TCTData\wafer6\9010stuff\TCTBoard_W6_LGAD_loc1_1mm_D2_45%_1485mV_50Hz_ND0.0_6.5VAmpBias_May03\Data', 6, '1mm', 1, 'LGAD', 'normal', 45, 'LGAD1mm1_6_45p_9010_new')
LGAD1mm5_6_45p_9010_new = sensor('TCTData\wafer6\9010stuff\TCTBoard_W6_LGAD_loc5_1mm_D2_45%_1485mV_50Hz_ND0.0_6.5VAmpBias_May03\Data', 6, '1mm', 5, 'LGAD', 'normal', 45, 'LGAD1mm5_6_45p_9010_new')
PiN1mm1_6_10p_9010_new = sensor('TCTData\wafer6\9010stuff\TCTBoard_W6_PiN_loc1_1mm_D2_10%_330mV_50Hz_ND0.0_6.5VAmpBias_May03\Data', 6, '1mm', 1, 'PiN', 'normal', 10, 'PiN1mm1_6_10p_9010_new')
LGAD1mm5_11_45p_9010_new = sensor('TCTData\wafer6\9010stuff\TCTBoard_W11_LGAD_loc5_1mm_D2_45%_1485mV_50Hz_ND0.0_6.5VAmpBias_May04\Data', 11, '1mm', 5, 'LGAD', 'normal', 45, 'LGAD1mm5_11_45p_9010_new')
PiN1mm1_11_10p_9010_new = sensor('TCTData\wafer6\9010stuff\TCTBoard_W11_PiN_loc5_1mm_D2_10%_330mV_50Hz_ND0.0_6.5VAmpBias_May04\Data', 11, '1mm', 1, 'PiN', 'normal', 10, 'PiN1mm1_11_10p_9010_new')
#sensor,size,location,power,9010splitterused,differing appature

#final sensor 3 sweep
LGAD1mm5_3_45p_9010_new = sensor('TCTData\wafer3\9010stuff\TCTBoard_W3_LGAD_loc5_1mm_D2_45%_1485mV_50Hz_ND0.0_6.5VAmpBias_May05\Data', 3, '1mm', 5, 'LGAD', 'normal', 45, 'LGAD1mm5_3_45p_9010_new')

def getdata(file):
    """
    fetches the data from a given file
    returns timetag, chan1, chan2
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
        data.append(rawdata[i][0:4])
        timetag.append(abs(float(data[i][0])))
        chan1.append(abs(float(data[i][1])))
        chan2.append(abs(float(data[i][2])))
        chan3.append(abs(float(data[i][3])))
    
    #plt.plot(timetag[np.argmax(chan2)-1300:np.argmax(chan2)+1800], chan2[np.argmax(chan2)-1300:np.argmax(chan2)+1800])
    return timetag, chan1, chan2, chan3

def integrator(sensor):
    """
    does all the integration for a given sensor (beam monitored)
    returns: LGADavgintegrals, LGADstdlist, beamavgintegrals, beamstdlist, LGADvoltages
    """
    filelist = os.listdir(sensor.filelist)  #gets all the files of this sensors data
    currentfile = []
    for i in range(0, len(filelist)):
        currentfile.append(f'{sensor.filelist}/{filelist[i]}')  #currentfile is a list of files all in the correct format for us below
    
    filevoltages = []
    for i in range(0, len(filelist)):
        filevoltages.append(int(filelist[i][:3]))   #filevoltages is a list of all voltages tested in a file, including repeats
    
    LGADvoltages = []
    for voltage in filevoltages:
        if voltage not in LGADvoltages:
            LGADvoltages.append(voltage)
    #voltages is a list of the tested voltages for this sensor - some do 0->100, others have steps in between!
    
    countlist = []
    
    for voltage in LGADvoltages:
        countlist.append(filevoltages.count(voltage))
    #countlist is a list of how mant times each voltage value appears in filevoltages (in order)
    
    LGADintegrals = []
    beamintegrals = []
    for file in currentfile:
        timetag, chan1, chan2, chan3 = getdata(file)    #get the data from each .csv file of this sensor
        
        #idx1 = (np.abs(np.array(timetag) - (0.19e-7))).argmin()
        #idx2 = len(chan3)-1
        idx1 = 0
        idx2 = len(chan3)-1
        #integral range for beam monitor peak (pr much the whole timebase)
        print(f'{file}', idx1, idx2, 'beam')
        
        integral = integrate.trapz(chan3[idx1:idx2], x = timetag[idx1:idx2], dx = 0.1)
        #integral gives NaN?????? fixed by using .trapz
        #integrate the charge peak between the indexes
        beamintegrals.append(integral)  #add them all to a list
        
        
        
        #do LGAD integrals (after beam because LGAD requires manual cut, beam does not)
        #i added a second loop in the end anyway cus the LGAD manual cut was causing issues
    for file in currentfile:
        timetag, chan1, chan2, chan3 = getdata(file)
        
        timetag = timetag[8000:12000]
        chan2 = chan2[8000:12000]
        #made a manual cut on where we expect the peak to be after, as it is the same time after the trigger always
        #did this to ensure the np.argmax() I take is indeed the one assosiated with the charge injection peak
        #not some other random large peak, that exists in some of the files
        
        idx1 = (np.abs(np.array(timetag) - (timetag[np.argmax(chan2)] - 1.25*10**-9))).argmin()
        idx2 = (np.abs(np.array(timetag) - (timetag[np.argmax(chan2)] + 3*10**-9))).argmin()
        #choose the integral range to be that of -1.25ns -> +3ns around max value (closest point to this)
        #note these indexes are for within the cute timetag and chan2 ONLY, which is fine, cus that's all im working with here

        print(f'{file}', idx1, idx2, 'LGAD')
        
        integral = integrate.simpson(chan2[idx1:idx2], x = timetag[idx1:idx2], dx = 0.01)
        #integrate the charge peak between the indexes
        LGADintegrals.append(integral)  #add them all to a list
    
    beamavgintegrals = []
    beamstdlist = []
    LGADavgintegrals = []
    LGADstdlist = []
    #element is how many repeats we got at each voltage
    for element in countlist:
        
        beamavg = sum(beamintegrals[0:element])/element
        beamstdlist.append(np.std(beamintegrals[0:element]))
        beamavgintegrals.append(beamavg)
        del beamintegrals[:element]
        
        LGADavg = sum(LGADintegrals[0:element])/element     #find the average over however many repeats we managed to get
        #can now include an error calculation here!
        LGADstdlist.append(np.std(LGADintegrals[0:element]))
        LGADavgintegrals.append(LGADavg)
        del LGADintegrals[:element]     #remove the integrals from the list once they are averaged
    
    return LGADavgintegrals, LGADstdlist, beamavgintegrals, beamstdlist, LGADvoltages

def filecreator(sensor):
    """
    creates a file with all the integrals in for that sensor and saves them in a file with their name as the name
    """
    LGADavgintegrals, LGADstdlist, beamavgintegrals, beamstdlist, LGADvoltages = integrator(sensor)
    #LGADavgintegrals, LGADstdlist, beamavgintegrals, beamstdlist, LGADvoltages = [[1, 1, 0], [1, 2, 0], [1, 1, 0], [1, 1, 0], [1, 1, 8]]
    file = open(f'TCTdata\wafer6\integralvalues\{sensor.name}.txt', 'w+')
    file.write('LGADavgintegrals\tLGADstdlist\tbeamavgintegrals\tbeamstdlist\tLGADvoltages\n')
    for i in range(0, len(LGADavgintegrals)):
        file.write(f'{LGADavgintegrals[i]}\t{LGADstdlist[i]}\t{beamavgintegrals[i]}\t{beamstdlist[i]}\t{LGADvoltages[i]}\n')
    file.close()

def filegrabber(sensor):
    """
    grabs the integral data from the files
    """
    LGADavgintegrals = []
    LGADstdlist = []
    beamavgintegrals = []
    beamstdlist = []
    LGADvoltages = []
    rawdata = []
    datapath = f'TCTdata\wafer6\integralvalues\{sensor.name}.txt'
    file = open(datapath, 'r')
    for line in file:
        line = line.rstrip('\n').split('\t')
        rawdata.append(line)
    rawdata = rawdata[1:]
    for i in range(0, len(rawdata)):
        LGADavgintegrals.append(float(rawdata[i][0]))
        LGADstdlist.append(float(rawdata[i][1]))
        beamavgintegrals.append(float(rawdata[i][2]))
        beamstdlist.append(float(rawdata[i][3]))
        LGADvoltages.append(float(rawdata[i][4]))
    
    return LGADavgintegrals, LGADstdlist, beamavgintegrals, beamstdlist, LGADvoltages
    

def standardplotter(sensorlist):
    """
    reads out the data from the created files
    and plots them just standardly. there is no scaling here! just plotting integration values
    of LGAD charge and beam monitor channels
    """
    #plot below to plot more precise things, like specific day labels
    """
    fig, ax = plt.subplots()
    plt.rcParams["figure.figsize"] = [12,9]
    plt.ylabel('Integral Value [V$\cdot$s]', fontsize = 22)
    plt.xlabel('Bias Voltage [V]', fontsize = 22)
    #plt.yscale('log')
    #plt.xlim(0, 800)
    plt.ylim(0, 1.75e-9)
    ax.minorticks_on()
    ax.grid(which='major', linestyle='-', linewidth='0.5', color='grey')
    ax.grid(which='minor', linestyle=':', linewidth='0.5', color='grey')
    plt.title('Charge Injection Plot for LGAD. Laser Power = 45%', fontsize=22)
    plt.xticks(fontsize = 20)
    plt.yticks(fontsize = 20)
    
    LGADavgintegrals, LGADstdlist, beamavgintegrals, beamstdlist, LGADvoltages = filegrabber(sensorlist[0])
    plt.errorbar(LGADvoltages, LGADavgintegrals, yerr = LGADstdlist, capsize = 3, label = f'{sensorlist[0].type} {sensorlist[0].size} on Wafer {sensorlist[0].wafer} Loc. {sensorlist[0].location}: March 30')
    LGADavgintegrals, LGADstdlist, beamavgintegrals, beamstdlist, LGADvoltages = filegrabber(sensorlist[1])
    plt.errorbar(LGADvoltages, LGADavgintegrals, yerr = LGADstdlist, capsize = 3, label = f'{sensorlist[0].type} {sensorlist[0].size} on Wafer {sensorlist[0].wafer} Loc. {sensorlist[0].location}: March 31')
    LGADavgintegrals, LGADstdlist, beamavgintegrals, beamstdlist, LGADvoltages = filegrabber(sensorlist[2])
    plt.errorbar(LGADvoltages, LGADavgintegrals, yerr = LGADstdlist, capsize = 3, label = f'{sensorlist[0].type} {sensorlist[0].size} on Wafer {sensorlist[0].wafer} Loc. {sensorlist[0].location}: April 1')
    plt.legend(fontsize = 18, title = 'Sensor', title_fontsize = 18)
    
    fig, ax = plt.subplots()
    plt.rcParams["figure.figsize"] = [12,9]
    plt.ylabel('Integral Value [V$\cdot$s]', fontsize = 22)
    plt.xlabel('Bias Voltage [V]', fontsize = 22)
    #plt.yscale('log')
    plt.ylim(0, 2e-7)
    #plt.ylim(0, 50)
    ax.minorticks_on()
    ax.grid(which='major', linestyle='-', linewidth='0.5', color='grey')
    ax.grid(which='minor', linestyle=':', linewidth='0.5', color='grey')
    plt.title('Beam Monitor Integration. Laser Power = 45%', fontsize=22)
    plt.xticks(fontsize = 20)
    plt.yticks(fontsize = 20)
    
    LGADavgintegrals, LGADstdlist, beamavgintegrals, beamstdlist, LGADvoltages = filegrabber(sensorlist[0])
    plt.errorbar(LGADvoltages, beamavgintegrals, yerr = beamstdlist, capsize = 3, label = f'{sensorlist[0].type} {sensorlist[0].size} on Wafer {sensorlist[0].wafer} Loc. {sensorlist[0].location}: March 30')
    LGADavgintegrals, LGADstdlist, beamavgintegrals, beamstdlist, LGADvoltages = filegrabber(sensorlist[1])
    plt.errorbar(LGADvoltages, beamavgintegrals, yerr = beamstdlist, capsize = 3, label = f'{sensorlist[0].type} {sensorlist[0].size} on Wafer {sensorlist[0].wafer} Loc. {sensorlist[0].location}: March 31')
    LGADavgintegrals, LGADstdlist, beamavgintegrals, beamstdlist, LGADvoltages = filegrabber(sensorlist[2])
    plt.errorbar(LGADvoltages, beamavgintegrals, yerr = beamstdlist, capsize = 3, label = f'{sensorlist[0].type} {sensorlist[0].size} on Wafer {sensorlist[0].wafer} Loc. {sensorlist[0].location}: April 1')
    plt.legend(fontsize = 18, title = 'Sensor', title_fontsize = 18, loc = 'upper left')
    """
    #plot below for more sensors, but less flexability on specifics of the labels
    fig, ax = plt.subplots()
    plt.rcParams["figure.figsize"] = [12,9]
    plt.ylabel('Integral Value [V$\cdot$s]', fontsize = 22)
    plt.xlabel('Bias Voltage [V]', fontsize = 22)
    plt.yscale('log')
    #plt.xlim(0, 800)
    #plt.ylim(0, 1.8e-9)
    plt.ylim(10**-11, 10**-8)
    ax.minorticks_on()
    ax.grid(which='major', linestyle='-', linewidth='0.5', color='grey')
    ax.grid(which='minor', linestyle=':', linewidth='0.5', color='grey')
    plt.title('Charge Injection Plot for LGAD for \nVarying LASER Power Parameters', fontsize=22)
    plt.xticks(fontsize = 20)
    plt.yticks(fontsize = 20)
    for sensor in sensorlist:
        LGADavgintegrals, LGADstdlist, beamavgintegrals, beamstdlist, LGADvoltages = filegrabber(sensor)
        plt.errorbar(LGADvoltages, LGADavgintegrals, yerr = LGADstdlist, capsize = 3, label = f'Laser Power = {sensor.laserpower}%')
        plt.legend(fontsize = 18, title = 'Sensor', title_fontsize = 18)
        
        
    #setup the figure 
    fig, ax = plt.subplots()
    plt.rcParams["figure.figsize"] = [12,9]
    plt.ylabel('Integral Value [V$\cdot$s]', fontsize = 22)
    plt.xlabel('Bias Voltage [V]', fontsize = 22)
    #plt.yscale('log')
    plt.ylim(0, 15e-9)
    #plt.ylim(0, 50)
    ax.minorticks_on()
    ax.grid(which='major', linestyle='-', linewidth='0.5', color='grey')
    ax.grid(which='minor', linestyle=':', linewidth='0.5', color='grey')
    plt.title('Beam Monitor Integration for \nVarying LASER Power Parameters', fontsize=22)
    plt.xticks(fontsize = 20)
    plt.yticks(fontsize = 20)
    for sensor in sensorlist:
        LGADavgintegrals, LGADstdlist, beamavgintegrals, beamstdlist, LGADvoltages = filegrabber(sensor)
        plt.errorbar(LGADvoltages, beamavgintegrals, yerr = beamstdlist, capsize = 3, label = f'{sensor.type} {sensor.size} on Wafer {sensor.wafer} Loc. {sensor.location}. Laser Power = {sensor.laserpower}%')
        #plt.plot(LGADvoltages, beamavgintegrals, label = f'{sensor.type} {sensor.size} on Wafer {sensor.wafer} Loc. {sensor.location}. Laser power = {sensor.laserpower}')
        plt.legend(fontsize = 18, title = 'Sensor', title_fontsize = 18, loc = 'upper left')
    
def plotter2(sensorlist):
    """
    takes in a sensor list of power sweeps;
    LGAD1mm5_6_35p, LGAD1mm5_6_40p, LGAD1mm5_6_45p, LGAD1mm5_6_50p
    and does this scalar factor shifting stuff and plots it
    """
    LGAD35, LGAD40, LGAD45, LGAD50 = sensorlist[0], sensorlist[1], sensorlist[2], sensorlist[3]
    
    LGADavgintegrals_35p, LGADstdlist_35p, beamavgintegrals_35p, beamstdlist_35p, LGADvoltages_35p = filegrabber(sensorlist[0])
    LGADavgintegrals_40p, LGADstdlist_40p, beamavgintegrals_40p, beamstdlist_40p, LGADvoltages_40p = filegrabber(sensorlist[1])
    LGADavgintegrals_45p, LGADstdlist_45p, beamavgintegrals_45p, beamstdlist_45p, LGADvoltages_45p = filegrabber(sensorlist[2])
    LGADavgintegrals_50p, LGADstdlist_50p, beamavgintegrals_50p, beamstdlist_50p, LGADvoltages_50p = filegrabber(sensorlist[3])
    LGADvoltages = LGADvoltages_35p
    
    def shifter(sensor1, sensor2):
        """
        shifts sensor 1 -> sensor 2
        returns; shiftedLGAD, shiftedLGADerror, shiftedBEAM, shiftedBEAMerror
        """
        LGADavgintegrals1, LGADstdlist1, beamavgintegrals1, beamstdlist1, LGADvoltages1 = filegrabber(sensor1)
        LGADavgintegrals2, LGADstdlist2, beamavgintegrals2, beamstdlist2, LGADvoltages2 = filegrabber(sensor2)
        
        #LGAD error propagation to shift the LGAD
        scalarfactor = np.divide(beamavgintegrals2, beamavgintegrals1)
        shiftedLGAD1 = np.multiply(scalarfactor, LGADavgintegrals1)
        scalarfactorpercentageerror = np.add(np.divide(beamstdlist1, beamavgintegrals1), np.divide(beamstdlist2, beamavgintegrals2))    #add percentage errors because shiftedLGAD = SF*LGAD
        LGADavgintegrals1percentageerror = np.divide(LGADstdlist1, LGADavgintegrals1)
        
        shiftedLGAD1percentageerror = np.add(scalarfactorpercentageerror, LGADavgintegrals1percentageerror)
        shiftedLGAD1absoluteerror = np.multiply(shiftedLGAD1percentageerror, LGADavgintegrals1)
        
        #BEAM error propagation to shift the beam
        shiftedbeam1 = np.multiply(scalarfactor, beamavgintegrals1)
        beamavgintegrals1percentageerror = np.divide(beamstdlist1, beamavgintegrals1)
        
        shiftedbeam1percentageerror = np.add(scalarfactorpercentageerror, beamavgintegrals1percentageerror)
        shiftedbeam1absoluteerror = np.multiply(shiftedbeam1percentageerror, beamavgintegrals1)
        
        return shiftedLGAD1, shiftedLGAD1absoluteerror, shiftedbeam1, shiftedbeam1absoluteerror
    
    fig, ax = plt.subplots()
    plt.rcParams["figure.figsize"] = [12,9]
    plt.ylabel('Integral Value [V$\cdot$s]', fontsize = 22)
    plt.xlabel('Bias Voltage [V]', fontsize = 22)
    plt.yscale('log')
    #plt.xlim(400, 438)
    #plt.ylim(0, 1.8e-9)
    plt.ylim(10**-11, 10**-8)
    ax.minorticks_on()
    ax.grid(which='major', linestyle='-', linewidth='0.5', color='grey')
    ax.grid(which='minor', linestyle=':', linewidth='0.5', color='grey')
    plt.title(f'Charge Injection Plot for LGAD with \nBeam Monitor Calibration Applied', fontsize=22)
    plt.xticks(fontsize = 20)
    plt.yticks(fontsize = 20)
    plt.errorbar(LGADvoltages, LGADavgintegrals_35p, yerr = LGADstdlist_35p, capsize = 3, label = f'Laser Power = 35%')
    plt.errorbar(LGADvoltages, shifter(LGAD40, LGAD35)[0], yerr = shifter(LGAD40, LGAD35)[1], capsize = 3, label = 'Laser Power = 40% normalised to 35%')
    plt.errorbar(LGADvoltages, shifter(LGAD45, LGAD35)[0], yerr = shifter(LGAD45, LGAD35)[1], capsize = 3, label = 'Laser Power = 45% normalised to 35%')
    plt.errorbar(LGADvoltages, shifter(LGAD50, LGAD35)[0], yerr = shifter(LGAD50, LGAD35)[1], capsize = 3, label = 'Laser Power = 50% normalised to 35%')
    #plt.plot(LGADvoltages, LGADavgintegrals_35p, label = '35%')
    #plt.plot(LGADvoltages, shifter(LGAD40, LGAD35)[0], label = '40% normalised to 35%')
    #plt.plot(LGADvoltages, shifter(LGAD45, LGAD35)[0], label = '40% normalised to 35%')
    #plt.plot(LGADvoltages, shifter(LGAD50, LGAD35)[0], label = '40% normalised to 35%')
    plt.legend(fontsize = 18, title = 'Power', title_fontsize = 18)
    
    
def plotter3(sensorlist):
    """
    takes in a given sensor over multiple days;
    LGAD1mm5_6_45p_first, LGAD1mm5_6_45p_second, LGAD1mm5_6_45p_third
    March30, March31, April1
    and does this scalar factor shifting stuff and plots it to see if the beam monitor calibration is working
    """
    LGAD1, LGAD2, LGAD3 = sensorlist[0], sensorlist[1], sensorlist[2]
    
    LGADavgintegrals_1, LGADstdlist_1, beamavgintegrals_1, beamstdlist_1, LGADvoltages_1 = filegrabber(sensorlist[0])
    LGADavgintegrals_2, LGADstdlist_2, beamavgintegrals_2, beamstdlist_2, LGADvoltages_2 = filegrabber(sensorlist[1])
    LGADavgintegrals_3, LGADstdlist_3, beamavgintegrals_3, beamstdlist_3, LGADvoltages_3 = filegrabber(sensorlist[2])
    LGADvoltages = LGADvoltages_1
    
    def shifter(sensor1, sensor2):
        """
        shifts sensor 1 -> sensor 2
        returns; shiftedLGAD, shiftedLGADerror, shiftedBEAM, shiftedBEAMerror
        """
        LGADavgintegrals1, LGADstdlist1, beamavgintegrals1, beamstdlist1, LGADvoltages1 = filegrabber(sensor1)
        LGADavgintegrals2, LGADstdlist2, beamavgintegrals2, beamstdlist2, LGADvoltages2 = filegrabber(sensor2)
        
        #LGAD error propagation to shift the LGAD
        scalarfactor = np.divide(beamavgintegrals2, beamavgintegrals1)
        shiftedLGAD1 = np.multiply(scalarfactor, LGADavgintegrals1)
        scalarfactorpercentageerror = np.add(np.divide(beamstdlist1, beamavgintegrals1), np.divide(beamstdlist2, beamavgintegrals2))    #add percentage errors because shiftedLGAD = SF*LGAD
        LGADavgintegrals1percentageerror = np.divide(LGADstdlist1, LGADavgintegrals1)
        
        shiftedLGAD1percentageerror = np.add(scalarfactorpercentageerror, LGADavgintegrals1percentageerror)
        shiftedLGAD1absoluteerror = np.multiply(shiftedLGAD1percentageerror, LGADavgintegrals1)
        
        #BEAM error propagation to shift the beam
        shiftedbeam1 = np.multiply(scalarfactor, beamavgintegrals1)
        beamavgintegrals1percentageerror = np.divide(beamstdlist1, beamavgintegrals1)
        
        shiftedbeam1percentageerror = np.add(scalarfactorpercentageerror, beamavgintegrals1percentageerror)
        shiftedbeam1absoluteerror = np.multiply(shiftedbeam1percentageerror, beamavgintegrals1)
        
        return shiftedLGAD1, shiftedLGAD1absoluteerror, shiftedbeam1, shiftedbeam1absoluteerror
    
    fig, ax = plt.subplots()
    plt.rcParams["figure.figsize"] = [12,9]
    plt.ylabel('Integral Value [V$\cdot$s]', fontsize = 22)
    plt.xlabel('Bias Voltage [V]', fontsize = 22)
    #plt.yscale('log')
    #plt.xlim(0, 800)
    #plt.ylim(0, 1.75e-9)
    ax.minorticks_on()
    ax.grid(which='major', linestyle='-', linewidth='0.5', color='grey')
    ax.grid(which='minor', linestyle=':', linewidth='0.5', color='grey')
    plt.title('Charge Injection Plot for LGAD with Beam Monitor Calibration Applied\nSame Laser Parameters Across Different Days', fontsize=22)
    plt.xticks(fontsize = 20)
    plt.yticks(fontsize = 20)
    plt.errorbar(LGADvoltages, LGADavgintegrals_1, yerr = LGADstdlist_1, capsize = 3, label = f'{LGAD1.type} {LGAD1.size} on Wafer {LGAD1.wafer} Loc. {LGAD1.location}: March 30th')
    plt.errorbar(LGADvoltages, shifter(LGAD2, LGAD1)[0], yerr = shifter(LGAD2, LGAD1)[1], capsize = 3, label = f'{LGAD1.type} {LGAD1.size} on Wafer {LGAD1.wafer} Loc. {LGAD1.location}: March 31st Normalised to March 30th')
    plt.errorbar(LGADvoltages, shifter(LGAD3, LGAD1)[0], yerr = shifter(LGAD3, LGAD1)[1], capsize = 3, label = f'{LGAD1.type} {LGAD1.size} on Wafer {LGAD1.wafer} Loc. {LGAD1.location}: April 1st Normalised to March 30th')
    #plt.plot(LGADvoltages, LGADavgintegrals_1, label = f'{LGAD1.type} {LGAD1.size} on Wafer {LGAD1.wafer} Loc. {LGAD1.location}: March 30th')
    #plt.plot(LGADvoltages, shifter(LGAD2, LGAD1)[0], label = f'{LGAD1.type} {LGAD1.size} on Wafer {LGAD1.wafer} Loc. {LGAD1.location}: March 31st Normalised to March 30th')
    #plt.plot(LGADvoltages, shifter(LGAD3, LGAD1)[0], label = f'{LGAD1.type} {LGAD1.size} on Wafer {LGAD1.wafer} Loc. {LGAD1.location}: April 1st Normalised to March 30th')
    plt.legend(fontsize = 16, title = 'Day of Sweep', title_fontsize = 18)
    
def internalgain(LGAD, PiN = PiN1mm1_6_10p_9010_new):
    """
    plots the internal gain of the LGAD as a function of bias for the inputted LGAD and PiN combination
    """
    LGADavgintegrals, LGADstdlist, LGADbeamavgintegrals, LGADbeamstdlist, LGADvoltages = filegrabber(LGAD)
    PiNavgintegrals, PiNstdlist, PiNbeamavgintegrals, PiNbeamstdlist, PiNvoltages = filegrabber(PiN)
    
    
    #all this shit below to account for if different voltages are used for the LGAD and PiN
    newLGADavgintegrals = []
    newLGADstdlist = []
    newLGADbeamavgintegrals = []
    newLGADbeamstdlist = []
    newPiNavgintegrals = []
    newPiNstdlist = []
    newPiNbeamavgintegrals = []
    newPiNbeamstdlist = []
    
    plottingvoltages = []
    for i in range(0, len(PiNvoltages)):
        if PiNvoltages[i] in LGADvoltages:
            plottingvoltages.append(PiNvoltages[i])
            newLGADavgintegrals.append(LGADavgintegrals[LGADvoltages.index(PiNvoltages[i])])
            newLGADstdlist.append(LGADstdlist[LGADvoltages.index(PiNvoltages[i])])
            newLGADbeamavgintegrals.append(LGADbeamavgintegrals[LGADvoltages.index(PiNvoltages[i])])
            newLGADbeamstdlist.append(LGADbeamstdlist[LGADvoltages.index(PiNvoltages[i])])
            newPiNavgintegrals.append(PiNavgintegrals[LGADvoltages.index(PiNvoltages[i])])
            newPiNstdlist.append(PiNstdlist[LGADvoltages.index(PiNvoltages[i])])
            newPiNbeamavgintegrals.append(PiNbeamavgintegrals[LGADvoltages.index(PiNvoltages[i])])
            newPiNbeamstdlist.append(PiNbeamstdlist[LGADvoltages.index(PiNvoltages[i])])
    
    LGADavgintegrals = newLGADavgintegrals
    LGADstdlist = newLGADstdlist
    LGADbeamavgintegrals = newLGADbeamavgintegrals
    LGADbeamstdlist = newLGADbeamstdlist
    PiNavgintegrals = newPiNavgintegrals
    PiNstdlist = newPiNstdlist
    PiNbeamavgintegrals = newPiNbeamavgintegrals
    PiNbeamstdlist = newPiNbeamstdlist
    
        
    scalarfactor = np.divide(PiNbeamavgintegrals, LGADbeamavgintegrals)
    #scalarfactorpercentageerror = np.add(np.divide(LGADbeamstdlist, LGADbeamavgintegrals), np.divide(PiNbeamstdlist, PiNbeamavgintegrals))    #add percentage errors bc SF*
    LGADbeamavgintegralspercentageerror = np.divide(LGADbeamstdlist, LGADbeamavgintegrals)
    PiNbeamavgintegralspercentageerror = np.divide(PiNbeamstdlist, PiNbeamavgintegrals)
    LGADavgintegralspercentageerror = np.divide(LGADstdlist, LGADavgintegrals)
    PiNavgintegralspercentageerror = np.divide(PiNstdlist, PiNavgintegrals)
    
    gainpercentageerror = np.add(LGADavgintegralspercentageerror, PiNavgintegralspercentageerror)   #add together the four percentage differences
    gainpercentageerror += np.add(PiNbeamavgintegralspercentageerror, LGADbeamavgintegralspercentageerror)  #negligable contribution
    gain = np.multiply(np.divide(LGADavgintegrals, PiNavgintegrals), scalarfactor)
    gainerror = np.multiply(gainpercentageerror, gain)  #absolute error
    
    fig, ax = plt.subplots()
    plt.rcParams["figure.figsize"] = [12,9]
    plt.ylabel('Internal Gain', fontsize = 22)
    plt.xlabel('Bias Voltage [V]', fontsize = 22)
    #plt.yscale('log')
    #plt.xlim(400, 430)
    plt.ylim(0, 80)
    ax.minorticks_on()
    ax.grid(which='major', linestyle='-', linewidth='0.5', color='grey')
    ax.grid(which='minor', linestyle=':', linewidth='0.5', color='grey')
    plt.title('Internal Gain as a Function of Bias Voltage', fontsize=22)
    plt.xticks(fontsize = 20)
    plt.yticks(fontsize = 20)
    #plt.plot(LGADvoltages, gain, label = '1mm LGAD Loc. 5 on Wafer 11', color = 'red')
    plt.errorbar(plottingvoltages, gain, yerr = gainerror, capsize = 3, label = f'{LGAD.size} {LGAD.type} Loc. {LGAD.location} on Wafer {LGAD.wafer}', color = 'red')
    plt.legend(fontsize = 16, title = 'Sensor', title_fontsize = 18, loc = 'upper left')
    
    return gain, gainerror, plottingvoltages
    
def internalgainplotter():
    """
    plots all the internal gain of all wafers on the same plot (cba to do anything properly anymore)
    """
    gain3, gainerror3, plottingvoltages3 = internalgain(LGAD1mm5_3_45p_9010_new, PiN1mm1_6_10p_9010_new)#w3
    gain6, gainerror6, plottingvoltages6 = internalgain(LGAD1mm5_6_45p_9010_new, PiN1mm1_6_10p_9010_new)#w6
    gain11, gainerror11, plottingvoltages11 = internalgain(LGAD1mm5_11_45p_9010_new, PiN1mm1_11_10p_9010_new)#w11
    
    fig, ax = plt.subplots()
    plt.rcParams["figure.figsize"] = [12,9]
    plt.ylabel('Internal Gain', fontsize = 22)
    plt.xlabel('Bias Voltage [V]', fontsize = 22)
    #plt.yscale('log')
    #plt.xlim(400, 430)
    plt.ylim(0, 80)
    ax.minorticks_on()
    ax.grid(which='major', linestyle='-', linewidth='0.5', color='grey')
    ax.grid(which='minor', linestyle=':', linewidth='0.5', color='grey')
    plt.title('Internal Gain as a Function of Bias Voltage', fontsize=22)
    plt.xticks(fontsize = 20)
    plt.yticks(fontsize = 20)
    #plt.plot(plottingvoltages3, gain3, label = '1mm LGAD on Wafer 3', color = 'green')
    #plt.plot(plottingvoltages6, gain6, label = '1mm LGAD Loc. 5 on Wafer 6', color = 'red')
    #plt.plot(plottingvoltages11, gain11, label = '1mm LGAD Loc. 5 on Wafer 11', color = 'blue')
    plt.errorbar(plottingvoltages3, gain3, yerr = gainerror3, capsize = 3, label = f'1mm LGAD on Wafer 3', color = 'green')
    plt.errorbar(plottingvoltages6, gain6, yerr = gainerror6, capsize = 3, label = f'1mm LGAD Loc. 5 on Wafer 6', color = 'red')
    plt.errorbar(plottingvoltages11, gain11, yerr = gainerror11, capsize = 3, label = f'1mm LGAD Loc. 5 on Wafer 11', color = 'blue')
    plt.legend(fontsize = 16, title = 'Sensor', title_fontsize = 18, loc = 'upper left')
    



#filecreator(LGAD1mm5_3_45p_9010_new)

#standardplotter([LGAD1mm5_6_35p, LGAD1mm5_6_40p, LGAD1mm5_6_45p, LGAD1mm5_6_50p])
#plotter2([LGAD1mm5_6_35p, LGAD1mm5_6_40p, LGAD1mm5_6_45p, LGAD1mm5_6_50p])
#standardplotter([LGAD1mm5_6_45p_first, LGAD1mm5_6_45p_second, LGAD1mm5_6_45p_third])
#plotter3([LGAD1mm5_6_45p_first, LGAD1mm5_6_45p_second, LGAD1mm5_6_45p_third])
#standardplotter([LGAD1mm5_6_35p_9010, LGAD1mm5_6_40p_9010, LGAD1mm5_6_45p_9010, LGAD1mm5_6_50p_9010])
#plotter2([LGAD1mm5_6_35p_9010, LGAD1mm5_6_40p_9010, LGAD1mm5_6_45p_9010, LGAD1mm5_6_50p_9010])



#standardplotter([LGAD1mm5_3_45p_9010_new])

#internalgain(LGAD1mm5_6_45p_9010_new, PiN1mm1_6_10p_9010_new)
#internalgainplotter()

#filecreator(W3_F7LS1FD2_40p)
#filecreator(W3_F25PS1FD1_40p)
#standardplotter([W3_F7LS1FD2_40p])
#standardplotter([W3_F25PS1FD1_40p])



