# -*- coding: utf-8 -*-
"""
Created on Thu May  5 14:00:00 2022

@author: Marcus
"""
#this cose is gonna be for making gain/timing plots

#gain:
#%matplotlib qt
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

def gainfilecreator(sensor):
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

def gainfilegrabber(sensor):
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
    #plt.yscale('log')
    #plt.xlim(0, 800)
    #plt.ylim(0, 1.8e-9)
    ax.minorticks_on()
    ax.grid(which='major', linestyle='-', linewidth='0.5', color='grey')
    ax.grid(which='minor', linestyle=':', linewidth='0.5', color='grey')
    plt.title('Charge Injection Plot for LGAD for \nVarying LASER Power Parameters', fontsize=22)
    plt.xticks(fontsize = 20)
    plt.yticks(fontsize = 20)
    for sensor in sensorlist:
        LGADavgintegrals, LGADstdlist, beamavgintegrals, beamstdlist, LGADvoltages = filegrabber(sensor)
        plt.errorbar(LGADvoltages, LGADavgintegrals, yerr = LGADstdlist, capsize = 3, label = f'{sensor.type} {sensor.size} on Wafer {sensor.wafer} Loc. {sensor.location}. Laser Power = {sensor.laserpower}%')
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
    ax.minorticks_on()
    ax.grid(which='major', linestyle='-', linewidth='0.5', color='grey')
    ax.grid(which='minor', linestyle=':', linewidth='0.5', color='grey')
    plt.title(f'Charge Injection Plot for LGAD with \nBeam Monitor Calibration Applied', fontsize=22)
    plt.xticks(fontsize = 20)
    plt.yticks(fontsize = 20)
    plt.errorbar(LGADvoltages, LGADavgintegrals_35p, yerr = LGADstdlist_35p, capsize = 3, label = f'LGAD 1mm on Wafer 6 Loc. 5 \nLaser Power = 35%')
    plt.errorbar(LGADvoltages, shifter(LGAD40, LGAD35)[0], yerr = shifter(LGAD40, LGAD35)[1], capsize = 3, label = 'LGAD 1mm on Wafer 6 Loc. 5 \nLaser Power = 40% normalised to 35%')
    plt.errorbar(LGADvoltages, shifter(LGAD45, LGAD35)[0], yerr = shifter(LGAD45, LGAD35)[1], capsize = 3, label = 'LGAD 1mm on Wafer 6 Loc. 5 \nLaser Power = 45% normalised to 35%')
    plt.errorbar(LGADvoltages, shifter(LGAD50, LGAD35)[0], yerr = shifter(LGAD50, LGAD35)[1], capsize = 3, label = 'LGAD 1mm on Wafer 6 Loc. 5 \nLaser Power = 50% normalised to 35%')
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
    and does this scalar factor shifting stuff and plots it
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
    plots the internal gain as a function of bias for the inputted LGAD and PiN combination
    """
    LGADavgintegrals, LGADstdlist, LGADbeamavgintegrals, LGADbeamstdlist, LGADvoltages = gainfilegrabber(LGAD)
    PiNavgintegrals, PiNstdlist, PiNbeamavgintegrals, PiNbeamstdlist, PiNvoltages = gainfilegrabber(PiN)
    
    
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
    """
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
    """
    return gain, gainerror, plottingvoltages
    
def gainatvoltage(sensor, voltage):
    """
    returns the gain, gain error at the requested voltage for a given sensor
    """
    gain, gainerror, plottingvoltages = internalgain(sensor)
    return gain[plottingvoltages.index(voltage)], gainerror[plottingvoltages.index(voltage)]

def internalgainplotter():
    gain3, gainerror3, plottingvoltages3 = internalgain(LGAD1mm5_3_45p_9010_new, PiN1mm1_6_10p_9010_new)#w3
    gain6, gainerror6, plottingvoltages6 = internalgain(LGAD1mm5_6_45p_9010_new, PiN1mm1_6_10p_9010_new)#w6
    gain11, gainerror11, plottingvoltages11 = internalgain(LGAD1mm5_11_45p_9010_new, PiN1mm1_11_10p_9010_new)#w6
    
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
    

def plotter(sensorlist):
    """
    legacy function
    """
    sensor = sensorlist[0]
    
    def creator(sensor):
        filelist = os.listdir(sensor.filelist)  #gets all the files of this sensors data
        currentfile = []
        for i in range(0, len(filelist)):
            currentfile.append(f'{sensor.filelist}/{filelist[i]}')  #currentfile is a list of files all in the correct format for us below
        
        LGADvoltages = []
        for i in np.arange(5, len(filelist), 10):
            LGADvoltages.append(int(filelist[i][:3]))
        #voltages is a list of the tested voltages for this sensor - some do 0->100, others have steps in between!
        
        filevoltages = []
        for i in range(0, len(filelist)):
            filevoltages.append(int(filelist[i][:3]))   #filevoltages is a list of all voltages tested in a file, including repeats
        
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
            
            timetag = timetag[11000:13000]
            chan2 = chan2[11000:13000]
            #made a manual cut on where we expect the peak to be after, as it is the same time after the trigger always
            #did this to ensure the np.argmax() I take is indeed the one assosiated with the charge injection peak
            #not some other random large peak, that exists in some of the files
            
            idx1 = (np.abs(np.array(timetag) - (timetag[np.argmax(chan2)] - 1.25*10**-9))).argmin()
            idx2 = (np.abs(np.array(timetag) - (timetag[np.argmax(chan2)] + 3*10**-9))).argmin()
            #choose the integral range to be that of -1.25ns -> +1.55ns around max value (closest point to this)
    
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
            
        
        #plot the integral values now for LGAD
        fig, ax = plt.subplots()
        plt.rcParams["figure.figsize"] = [12,9]
        plt.ylabel('Integral Value [V$\cdot$ns]', fontsize = 22)
        plt.xlabel('Bias Voltage [V]', fontsize = 22)
        #plt.yscale('log')
        #plt.xlim(0, 800)
        #plt.ylim(0, 50)
        ax.minorticks_on()
        ax.grid(which='major', linestyle='-', linewidth='0.5', color='grey')
        ax.grid(which='minor', linestyle=':', linewidth='0.5', color='grey')
        plt.title(f'Charge Injection Plot for LGAD. LASER Power = {sensor.laserpower}', fontsize=22)
        plt.xticks(fontsize = 20)
        plt.yticks(fontsize = 20)
        plt.errorbar(LGADvoltages, LGADavgintegrals, yerr = LGADstdlist, capsize = 3, label = f'{sensor.type} {sensor.size} on Wafer {sensor.wafer} Loc. {sensor.location}', color = 'rebeccapurple')
        plt.legend(fontsize = 18, title = 'Sensor', title_fontsize = 18)
        
        #plot the average integral vaues for beam monitor
        fig, ax = plt.subplots()
        plt.rcParams["figure.figsize"] = [12,9]
        plt.ylabel('Integral Value [V$\cdot$ns]', fontsize = 22)
        plt.xlabel('Bias Voltage [V]', fontsize = 22)
        #plt.yscale('log')
        #plt.xlim(0)
        #plt.ylim(0, 50)
        ax.minorticks_on()
        ax.grid(which='major', linestyle='-', linewidth='0.5', color='grey')
        ax.grid(which='minor', linestyle=':', linewidth='0.5', color='grey')
        plt.title(f'Beam Monitor Integration. LASER Power = {sensor.laserpower}', fontsize=22)
        plt.xticks(fontsize = 20)
        plt.yticks(fontsize = 20)
        #plt.errorbar(LGADvoltages, beamavgintegrals, yerr = beamstdlist, capsize = 3, label = 'beam for LGAD1mm5_6_45p', color = 'rebeccapurple')
        plt.plot(LGADvoltages, beamavgintegrals, label = f'{sensor.type} {sensor.size} on Wafer {sensor.wafer} Loc. {sensor.location}', color = 'rebeccapurple')
        plt.legend(fontsize = 18, title = 'Sensor', title_fontsize = 18)
        
        return LGADavgintegrals, beamavgintegrals, LGADvoltages, LGADstdlist, beamstdlist
    
    #okay so now i want to do the same thing with sensor[2]!
    #made the above a function just to make it easier
    #I NOW NEED TO MAKE A FUNCTION THAT SAVES ALL THIS DATA TO .TXT FILES FOR MUCH QUICKER PLOTTING
    #SO IT DOESNT NEED TO DO THE INTEGRALS EVERY SINGLE TIME
    LGAD1, beam1, voltages1, LGAD1err, beam1err = creator(sensorlist[0])
    LGAD2, beam2, voltages2, LGAD2err, beam2err = creator(sensorlist[1])
    
    #calculate the scalar factor
    scalarfactor = np.divide(beam2, beam1)
    print('scalar factor', scalarfactor)
    shiftedLGAD1 = np.multiply(scalarfactor, LGAD1)
    
    scalarfactorpercentageerror = np.add(np.divide(beam1err, beam1), np.divide(beam2err, beam2))
    #scalarfactorabsoluteerror = np.multiply(scalarfactorpercentageerror, scalarfactor)
    
    LGAD2percentageerr = np.divide(LGAD2err, LGAD2)
    
    shiftedLGAD2percentageerr = np.add(scalarfactorpercentageerror, LGAD2percentageerr)
    shiftedLGAD2absoluteerr = np.multiply(shiftedLGAD2percentageerr, LGAD2)
    #just quickly propagating the errors through^^^
    
    fig, ax = plt.subplots()
    plt.rcParams["figure.figsize"] = [12,9]
    plt.ylabel('Integral Value [V$\cdot$ns]', fontsize = 22)
    plt.xlabel('Bias Voltage [V]', fontsize = 22)
    #plt.yscale('log')
    #plt.xlim(0)
    #plt.ylim(0, 50)
    ax.minorticks_on()
    ax.grid(which='major', linestyle='-', linewidth='0.5', color='grey')
    ax.grid(which='minor', linestyle=':', linewidth='0.5', color='grey')
    plt.title(f'LGAD Calibration Test: Shifting 40% to 45% with Beam Monitor', fontsize=22)
    plt.xticks(fontsize = 20)
    plt.yticks(fontsize = 20)
    plt.errorbar(voltages1, LGAD2, yerr = LGAD1err, capsize = 2, label = 'LGAD 1mm Wafer 6 Loc. 5 @ 45% Power')
    plt.errorbar(voltages1, shiftedLGAD1, yerr = shiftedLGAD2absoluteerr, capsize = 2, label = 'LGAD 1mm Wafer 6 Loc. 5 @ 40% Power, Shifted to 45% ')
    plt.legend(fontsize = 18, title = 'Sensor', title_fontsize = 18)
    
    #print(LGAD1)
    #print(LGAD2)
    #print(beam1)
    #print(beam2)
    
    
    
    
    
    
    
    
    
    #now do the same for PiN
    #dont need the PiN atm
    """
    PiN = sensor[1] #previously i used plotter([LGAD, PiN]), but I'm not sure what ill need in the future
    
    filelist = os.listdir(PiN.filelist)  #gets all the files of this sensors data
    currentfile = []
    for i in range(0, len(filelist)):
        currentfile.append(f'{PiN.filelist}/{filelist[i]}')  #currentfile is a list of files all in the correct format for us below
    
    PiNvoltages = []
    for i in np.arange(5, len(filelist), 10):
        PiNvoltages.append(int(filelist[i][:3]))
    #voltages is a list of the tested voltages for this sensor - some do 0->100, others have steps in between!
    
    PiNintegrals = []
    for file in currentfile:
        timetag, chan1, chan2 = getdata(file)    #get the data from each .csv file of this sensor
        
        timetag = timetag[8000:12000]
        chan2 = chan2[8000:12000]
        #made a manual cut on where we expect the peak to be after, as it is the same time after the trigger always
        #did this to ensure the np.argmax() I take is indeed the one assosiated with the charge injection peak
        #not some other random large peak, that exists in some of the files
        
        idx1 = (np.abs(np.array(timetag) - (timetag[np.argmax(chan2)] - 1.25*10**-9))).argmin()
        idx2 = (np.abs(np.array(timetag) - (timetag[np.argmax(chan2)] + 3*10**-9))).argmin() #previously 1.55*10**-9
        #choose the integral range to be that of -1.25ns -> +1.55ns around max value (closest point to this)
        
        #plt.axvline(x = timetag[idx1])
        #plt.axvline(x = timetag[idx2])
        print(f'{file}', idx1, idx2)
        
        
        integral = integrate.simpson(chan2[idx1:idx2], x = timetag[idx1:idx2], dx = 0.01)
        #integrate the charge peak between the indexes
        PiNintegrals.append(integral)  #add them all to a list
    
    
    PiNavgintegrals =  np.average(np.array(PiNintegrals).reshape(-1, 10), axis=1) #average each 10 items in the list of integral values to get the average integral value at each voltage
    
    fig, ax = plt.subplots()
    plt.rcParams["figure.figsize"] = [12,9]
    plt.ylabel('Integral Value [V$\cdot$ns]', fontsize = 22)
    plt.xlabel('Bias Voltage [V]', fontsize = 22)
    #plt.yscale('log')
    #plt.xlim(0, 800)
    #plt.ylim(0, 50)
    ax.minorticks_on()
    ax.grid(which='major', linestyle='-', linewidth='0.5', color='grey')
    ax.grid(which='minor', linestyle=':', linewidth='0.5', color='grey')
    plt.title('Charge Injection Plot', fontsize=22)
    plt.xticks(fontsize = 20)
    plt.yticks(fontsize = 20)
    plt.plot(PiNvoltages, PiNavgintegrals, label = 'F7PS1FD1_40p', color = 'rebeccapurple')
    plt.legend(fontsize = 18, title = 'Sensor', title_fontsize = 18)
    
    """
    #dont need to be doing gain yet either
    """
    newLGADavgintegrals = []    #this will have the voltages the PiN doesnt have from the LGAD list
    newLGADvoltages = []
    
    #need ratio, but need to use only PiN voltages, as the LGAD always has more voltage steps
    for i in range(0, len(LGADvoltages)):
        if LGADvoltages[i] in PiNvoltages:
            newLGADvoltages.append(LGADvoltages[i])
            newLGADavgintegrals.append(LGADavgintegrals[i])     #take the LGAD integrals only from the voltages the PiN has
    
    
    #need to find scalar factor 
    
    gain = []
    for i in range(0, len(newLGADavgintegrals)):
        gain.append((newLGADavgintegrals[i]*3.10)/(PiNavgintegrals[i])) #random integar multiplation is the scsalar factor frmo calibration
    
    
    fig, ax = plt.subplots()
    plt.rcParams["figure.figsize"] = [12,9]
    plt.ylabel('Gain', fontsize = 22)
    plt.xlabel('Bias Voltage [V]', fontsize = 22)
    #plt.yscale('log')
    #plt.xlim(0, 800)
    #plt.ylim(0, 50)
    ax.minorticks_on()
    ax.grid(which='major', linestyle='-', linewidth='0.5', color='grey')
    ax.grid(which='minor', linestyle=':', linewidth='0.5', color='grey')
    plt.title('Gain', fontsize=22)
    plt.xticks(fontsize = 20)
    plt.yticks(fontsize = 20)
    plt.plot(newLGADvoltages, gain, color = 'rebeccapurple', linewidth = 1.2, label = 'F7PS1FD1')
    plt.legend(fontsize = 18, title = 'Sensor', title_fontsize = 18)
    """
    
def calibration(sensorlist):
    """
    for LGAD power sweep
    Takes in a list of power sweeps of 10%, 20%, 30%, 40%, 50%..
    does the integral at 0V, 40V, 50V, 60V
    lagacy function - beam monitor calibration preferred
    """
    powerlist = [10, 20, 30, 40, 50]
    #powerlist = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60]
    powerintegrals = []
    
    i = 0
    for sensor in sensorlist:
        
        filelist = os.listdir(sensor.filelist)  #gets all the files of this sensors data
        currentfile = []
        for i in range(0, len(filelist)):
            currentfile.append(f'{sensor.filelist}/{filelist[i]}')  #currentfile is a list of files all in the correct format for us below
        
        voltages = []
        for i in np.arange(5, len(filelist), 10):
            voltages.append(int(filelist[i][:3]))
            
        integrals = []
        for file in currentfile:
            timetag, chan1, chan2 = getdata(file)    #get the data from each .csv file of this sensor
            
            timetag = timetag[8000:12000]
            chan2 = chan2[8000:12000]
            
            idx1 = (np.abs(np.array(timetag) - (timetag[np.argmax(chan2)] - 1.25*10**-9))).argmin()
            idx2 = (np.abs(np.array(timetag) - (timetag[np.argmax(chan2)] + 3*10**-9))).argmin()
            #choose the integral range to be that of -1.25ns -> +1.55ns around max value (closest point to this)
    
            print(f'{file}', idx1, idx2)
            
            integral = integrate.simpson(chan2[idx1:idx2], x = timetag[idx1:idx2], dx = 0.01)
            #integrate the charge peak between the indexes
            integrals.append(integral)  #add them all to a list
            
        avgintegrals =  np.average(np.array(integrals).reshape(-1, 10), axis=1)
        powerintegrals.append(avgintegrals)
        
        
    #print(powerlist)
    #print(powerintegrals)
    #need to change how i plot it to get a correct legend
    
    labels = ['0V', '40V', '50V', '60V', '70V']
    colors = ['red', 'green', 'blue', 'orange', 'rebeccapurple']
    
    fig, ax = plt.subplots()
    plt.rcParams["figure.figsize"] = [12,9]
    plt.ylabel('Integral Value [V$\cdot$ns]', fontsize = 22)
    plt.xlabel('Laser Power [%]', fontsize = 22)
    #plt.yscale('log')
    plt.xlim(0, 60)
    #plt.ylim(0, 50)
    ax.minorticks_on()
    ax.grid(which='major', linestyle='-', linewidth='0.5', color='grey')
    ax.grid(which='minor', linestyle=':', linewidth='0.5', color='grey')
    plt.title('Integral Value vs. LASER Power for Sensor W3_F7LS1FD2', fontsize=22)
    plt.xticks(powerlist, fontsize = 20)
    plt.yticks(fontsize = 20)
    for i in range(0, len(voltages)):
        plottingline = []
        for j in range(0, len(powerlist)):
            plottingline.append(powerintegrals[j][i])   #needed to do this flip to get the labels to work coreectly
            
        #calc the conversion ratio from 50% to 40%
        #avg = 4.90
        print(plottingline[4]/plottingline[3])
        plt.plot(powerlist, plottingline, label = f'{labels[i]}', color = colors[i], marker = 'x')
    
    
    plt.legend(fontsize = 18, title = 'Bias Voltage', title_fontsize = 18)
    
def calibration2(sensorlist):
    """
    for PiN power sweep
    power sweeps: 0, 5, 10, 20, 25, 30, 35, 40, 45, 50, 55, 60%
    does the integral for: 0V, 40V, 50V, 60V, 70V
    
    in reality, only one calibraion faunction is needed, just change the powerlist and sensoes you pass in
    
    legacy fuction - beam monitor calibration preferred
    """
    
    powerlist = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60]
    powerintegrals = []
    
    i = 0
    for sensor in sensorlist:
        
        filelist = os.listdir(sensor.filelist)  #gets all the files of this sensors data
        currentfile = []
        for i in range(0, len(filelist)):
            currentfile.append(f'{sensor.filelist}/{filelist[i]}')  #currentfile is a list of files all in the correct format for us below
        
        voltages = []
        for i in np.arange(5, len(filelist), 10):
            voltages.append(int(filelist[i][:3]))
        
            
        integrals = []
        for file in currentfile:
            timetag, chan1, chan2 = getdata(file)    #get the data from each .csv file of this sensor
            
            timetag = timetag[8000:12000]
            chan2 = chan2[8000:12000]
            
            idx1 = (np.abs(np.array(timetag) - (timetag[np.argmax(chan2)] - 1.25*10**-9))).argmin()
            idx2 = (np.abs(np.array(timetag) - (timetag[np.argmax(chan2)] + 3*10**-9))).argmin()
            #choose the integral range to be that of -1.25ns -> +1.55ns around max value (closest point to this)
    
            print(f'{file}', idx1, idx2)
            
            integral = integrate.simpson(chan2[idx1:idx2], x = timetag[idx1:idx2], dx = 0.01)
            #integrate the charge peak between the indexes
            integrals.append(integral)  #add them all to a list
            
        avgintegrals =  np.average(np.array(integrals).reshape(-1, 10), axis=1)
        powerintegrals.append(avgintegrals)
        
    labels = ['0V', '40V', '50V', '60V', '70V']
    colors = ['red', 'green', 'blue', 'orange', 'rebeccapurple']
    
    fig, ax = plt.subplots()
    plt.rcParams["figure.figsize"] = [12,9]
    plt.ylabel('Integral Value [V$\cdot$ns]', fontsize = 22)
    plt.xlabel('Laser Power [%]', fontsize = 22)
    #plt.yscale('log')
    plt.xlim(-10, 70)
    #plt.ylim(0, 50)
    ax.minorticks_on()
    ax.grid(which='major', linestyle='-', linewidth='0.5', color='grey')
    ax.grid(which='minor', linestyle=':', linewidth='0.5', color='grey')
    plt.title('Integral Value vs. LASER Power for Sensor W3_F25PS1FD1', fontsize=22)
    plt.xticks(powerlist, fontsize = 20)
    plt.yticks(fontsize = 20)
    for i in range(0, len(voltages)):   #this 5 is the number of voltages you're testing
        plottingline = []
        for j in range(0, len(powerlist)):
            plottingline.append(powerintegrals[j][i])   #needed to do this flip to get the labels to work coreectly
            
        #calc the conversion ratio from 50% to 40%
        #avg = 3.10 for 50% -> 40%
        print(plottingline[10]/plottingline[8])
        plt.plot(powerlist, plottingline, label = f'{labels[i]}', color = colors[i], marker = 'x')
    
    
    plt.legend(fontsize = 18, title = 'Bias Voltage', title_fontsize = 18)





#timing code now:






#%matplotlib qt
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
    
def timingfilecreator(sensor):
    """
    creates a file with the deltaT values in it
    """
    deltatime = deltaTcalc(sensor, 0.25)
    file = open(f'TIMINGdata\deltaTvalues\{sensor.name}.txt', 'w+')
    
    file.write(f'deltaTinseconds for {sensor.name}\n')
    for i in range(0, len(deltatime)):
        file.write(f'{deltatime[i]}\n')
    file.close()

def timingfilegrabber(sensor):
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
    print(deltatime)
    return deltatime

def timeplotter(sensor, CFDvalue):
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
    deltatime = timingfilegrabber(sensor)
    
    fig, ax = plt.subplots()
    plt.rcParams["figure.figsize"] = [12,9]
    plt.ylabel('Number of Coincidences in Time Bin', fontsize = 22)
    plt.xlabel('Time Difference Between Detection, $\Delta T$ [s]', fontsize = 22)
    #plt.yscale('log')
    #plt.xlim(-50e-9, 50-9)
    plt.ylim(0, 200)
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
    #x, n = x[x.index(1.175e-9):x.index(1.525e-9)], n[x.index(1.175e-9):x.index(1.525e-9)]
    popt, pcov = curve_fit(gauss, x, n, p0 = [20, 1.35e-9, 0.2e-9])
    
    fittedy = gauss(x, popt[0], popt[1], popt[2])
    fittedsigma = popt[2]*10**12    #intops
    fittedsigmaerror = (pcov[2][2]**0.5)*10**12     #into ps
    plt.plot(x, fittedy, label = f'Gaussian Fit \n$\sigma_{{hist}}$ = ({round(abs(fittedsigma), 2)} $\pm$ {round(fittedsigmaerror, 2)})ps', color = 'orange')
    plt.legend(fontsize = 18, loc = 'upper right')
    plt.show()
    print(f'{fittedsigma}ps pm {(fittedsigmaerror)}ps') #sigma, error on sigma
    
    
    return fittedsigma, fittedsigmaerror

def CFDsweep(sensor):
    """
    does a CFD sweep and plots the time resolution
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
    plt.errorbar(CFDvalues, timereslist, yerr = timereserrrorlist, capsize = 3, label = f'Wafer 11 Loc. 1 1mm LGAD', fmt = 'x', color = 'green')
    plt.legend(fontsize = 18)

def VoltageSweep(sensorlist):
    """
    does a sweep of the voltages tested (very manual because will only use twice!)
    """
    #change manually below 
    #voltages = [80, 120, 160, 200, 240, 280, 320, 340, 360, 380, 400, 420, 425, 430, 435]
    voltages = [125, 130, 135, 140, 145, 150]
    
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
    plt.ylim(30, 80)
    ax.minorticks_on()
    ax.grid(which='major', linestyle='-', linewidth='0.5', color='grey')
    ax.grid(which='minor', linestyle=':', linewidth='0.5', color='grey')
    plt.title('Time Resolution as a Function of Bias Voltage', fontsize=22)
    plt.xticks(fontsize = 20)
    plt.yticks(fontsize = 20)
    plt.errorbar(voltages, timereslist, yerr = timereserrrorlist, capsize = 3, label = f'Wafer 3 1mm LGAD', fmt = 'x', color = 'green')
    plt.legend(fontsize = 18)




#filecreator(LGAD1mm5_11)

#plotter(LGAD1mm5_11, 0.25)
#CFDsweep(LGAD1mm5_11)


#plotter(LGAD1mm5_11_320V, 0.25)

#VoltageSweep([LGAD1mm5_11_80V, LGAD1mm5_11_120V, LGAD1mm5_11_160V, LGAD1mm5_11_200V, LGAD1mm5_11_240V, LGAD1mm5_11_280V, LGAD1mm5_11_320V, LGAD1mm5_11_340V, LGAD1mm5_11_360V, LGAD1mm5_11_380V, LGAD1mm5_11_400V, LGAD1mm5_11_420V, LGAD1mm5_11_425V, LGAD1mm5_11_430V, LGAD1mm5_11_435V])
#VoltageSweep([LGAD1mm5_3_125V, LGAD1mm5_3_130V, LGAD1mm5_3_135V, LGAD1mm5_3_140V, LGAD1mm5_3_145V, LGAD1mm5_3_150V])

def gaintiming():
    #firstly, wafer 3 to prove concept
    

    timereslist3 = []
    timereserrrorlist3 = []
    for sensor in [LGAD1mm5_3_125V, LGAD1mm5_3_130V, LGAD1mm5_3_135V, LGAD1mm5_3_140V, LGAD1mm5_3_145V, LGAD1mm5_3_150V]:
        width, error = timeplotter(sensor, 0.25)
        timereslist3.append(np.sqrt(width**2 - 45.92**2)) #in-line calculation of time res from reference board and its assosiated error below
        timereserrrorlist3.append(np.sqrt(((width*error)/(np.sqrt(width**2 - 45.92**2)))**2 + ((45.92*2.655)/(np.sqrt(width**2 - 45.92)))**2))
    #okay now have a list of time res at the above voltages, just gotta get the gain at those voltages
    gainlist3 = []
    gainerrorlist3 = []
    voltagelist = [125, 130, 135, 140, 145, 150]
    i = 0
    for voltage in voltagelist:
        gain, gainerror = gainatvoltage(LGAD1mm5_3_45p_9010_new, voltagelist[i])
        print(voltage, gain)
        gainlist3.append(gain)
        gainerrorlist3.append(gainerror)
        i+=1
    
    #plt.plot(gainlist, timereslist)
    
    
    
    timereslist11 = []
    timereserrrorlist11 = []
    for sensor in [LGAD1mm5_11_120V, LGAD1mm5_11_160V, LGAD1mm5_11_200V, LGAD1mm5_11_240V, LGAD1mm5_11_280V, LGAD1mm5_11_320V, LGAD1mm5_11_360V, LGAD1mm5_11_400V, LGAD1mm5_11_420V, LGAD1mm5_11_425V]:
        width, error = timeplotter(sensor, 0.25)
        timereslist11.append(np.sqrt(width**2 - 45.92**2)) #in-line calculation of time res from reference board and its assosiated error below
        timereserrrorlist11.append(np.sqrt(((width*error)/(np.sqrt(width**2 - 45.92**2)))**2 + ((45.92*2.655)/(np.sqrt(width**2 - 45.92)))**2))
    #okay now have a list of time res at the above voltages, just gotta get the gain at those voltages
    gainlist11 = []
    gainerrorlist11 = []
    voltagelist = [120, 160, 200, 240, 280, 320, 360, 400, 420, 425]
    i = 0
    for voltage in voltagelist:
        gain, gainerror = gainatvoltage(LGAD1mm5_11_45p_9010_new, voltagelist[i])
        print(voltage, gain)
        gainlist11.append(gain)
        gainerrorlist11.append(gainerror)
        i+=1
    
    
    fig, ax = plt.subplots()
    plt.rcParams["figure.figsize"] = [12,9]
    plt.ylabel('Time Resolution [ps]', fontsize = 22)
    plt.xlabel('Internal Gain', fontsize = 22)
    #plt.yscale('log')
    plt.xlim(0, 80)
    plt.ylim(20, 80)
    ax.minorticks_on()
    ax.grid(which='major', linestyle='-', linewidth='0.5', color='grey')
    ax.grid(which='minor', linestyle=':', linewidth='0.5', color='grey')
    plt.title('Time Resolution as a Function of Internal Gain', fontsize=22)
    plt.xticks(fontsize = 20)
    plt.yticks(fontsize = 20)
    plt.errorbar(gainlist3, timereslist3, yerr = timereserrrorlist3, xerr = gainerrorlist3, capsize = 3, label = f'Wafer 3 1mm LGAD', fmt = 'x', color = 'green')
    plt.errorbar(gainlist11, timereslist11, yerr = timereserrrorlist11, xerr = gainerrorlist11, capsize = 3, label = f'Wafer 11 1mm LGAD Loc. 5', fmt = 'x', color = 'blue')
    plt.legend(fontsize = 18)
    #plt.plot(gainlist, timereslist)
    
    

#filecreator(LGAD1mm5_3_45p_9010_new)

#standardplotter([LGAD1mm5_6_35p, LGAD1mm5_6_40p, LGAD1mm5_6_45p, LGAD1mm5_6_50p])
#plotter2([LGAD1mm5_6_35p, LGAD1mm5_6_40p, LGAD1mm5_6_45p, LGAD1mm5_6_50p])
#standardplotter([LGAD1mm5_6_45p_first, LGAD1mm5_6_45p_second, LGAD1mm5_6_45p_third])
#plotter3([LGAD1mm5_6_45p_first, LGAD1mm5_6_45p_second, LGAD1mm5_6_45p_third])
#standardplotter([LGAD1mm5_6_35p_9010, LGAD1mm5_6_40p_9010, LGAD1mm5_6_45p_9010, LGAD1mm5_6_50p_9010])
#plotter2([LGAD1mm5_6_35p_9010, LGAD1mm5_6_40p_9010, LGAD1mm5_6_45p_9010, LGAD1mm5_6_50p_9010])



#standardplotter([LGAD1mm5_3_45p_9010_new])

#internalgain(LGAD1mm5_3_45p_9010_new, PiN1mm1_6_10p_9010_new)
#internalgainplotter()

gaintiming()

#filecreator(W3_F7LS1FD2_40p)
#filecreator(W3_F25PS1FD1_40p)
#standardplotter([W3_F7LS1FD2_40p])
#standardplotter([W3_F25PS1FD1_40p])



