# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 12:36:37 2021

@author: Marcus
"""

#%matplotlib qt

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm #for 3D plot
import pandas as pd
from pandas import read_excel
import scipy.stats as stats
from scipy.optimize import curve_fit
import scipy.integrate as integrate

class sensor():
    """
    Defines a sensor
    """
    def __init__(self, file, wafer, size, location, sensortype, newdatastyle, diced = False):
        self.file = file
        self.wafer = wafer
        self.size = size
        self.location = location
        self.type = sensortype
        self.newdatastyle = newdatastyle
        self.diced = diced


    
#generate all the sensor objects

LGAD4mm1_6 = sensor('CVdata\wafer6\Te2V_Batch1_Wafer6_LGAD_4mm_No1_pad_only_floatingCV.txt', 6, '4mm', 1, 'LGAD', 'old')
LGAD4mm3_6 = sensor('CVdata\wafer6\CV_Te2V_Batch1_Wafer6_LGAD_4mm_No3_pad_only_floating.txt', 6, '4mm', 3, 'LGAD', 'new')
LGAD4mm4_6 = sensor('CVdata\wafer6\Te2V_Batch1_Wafer6_LGAD_4mm_No4_pad_only_floatingCV.txt', 6, '4mm', 4, 'LGAD', 'old')
LGAD4mm5_6 = sensor('CVdata\wafer6\CV_Te2V_Batch1_Wafer6_LGAD_4mm_No5_pad_only_floating.txt', 6, '4mm', 5, 'LGAD', 'new')
PiN4mm1_6 = sensor('CVdata\wafer6\CV_Te2V_Batch1_Wafer6_PiN_4mm_No1_pad_only_floating.txt', 6, '4mm', 1, 'PiN', 'new')
LGAD2mm1_6 = sensor('CVdata\wafer6\CV_Te2V_Batch1_Wafer6_LGAD_2mm_No1_pad_only_floating_final.txt', 6, '2mm', 1, 'LGAD', 'new')
LGAD2mm3_6 = sensor('CVdata\wafer6\CV_Te2V_Batch1_Wafer6_LGAD_2mm_No3_pad_only_floating_final.txt', 6, '2mm', 3, 'LGAD', 'new')
LGAD2mm5_6 = sensor('CVdata\wafer6\CV_Te2V_Batch1_Wafer6_LGAD_2mm_No5_pad_only_floating_final.txt', 6, '2mm', 5, 'LGAD', 'new')
LGAD1mm1_6 = sensor('CVdata\wafer6\CV_Te2V_Batch1_Wafer6_LGAD_1mm_No1_pad_only_floating_final.txt', 6, '1mm', 1, 'LGAD', 'new')
LGAD1mm3_6 = sensor('CVdata\wafer6\CV_Te2V_Batch1_Wafer6_LGAD_1mm_No3_pad_only_floating_final.txt', 6, '1mm', 3, 'LGAD', 'new')
LGAD1mm5_6 = sensor('CVdata\wafer6\CV_Te2V_Batch1_Wafer6_LGAD_1mm_No5_pad_only_floating_final.txt', 6, '1mm', 5, 'LGAD', 'new')
PiN4mm4_6 = sensor('CVdata\wafer6\Te2V_Batch1_Wafer6_PiN_4mm_No4_pad_only_floatingCV.txt', 6, '4mm', 4, 'PiN', 'old')
PiN4mm1_6 = sensor('CVdata\wafer6\CV_Te2V_Batch1_Wafer6_PiN_4mm_No1_pad_only_floating.txt', 6, '4mm', 1, 'PiN', 'new')
PiN1mm1_6 = sensor('CVdata\wafer6\CV_Te2V_Batch1_Wafer6_PiN_1mm_No1_pad_only_floating_final.txt', 6, '1mm', 1, 'PiN', 'new')
PiN2mm1_6 = sensor('CVdata\wafer6\CV_Te2V_Batch1_Wafer6_PiN_2mm_No1_pad_only_floating_final.txt', 6, '2mm', 1, 'PiN', 'new')



LGAD4mm1_11 = sensor('CVdata\wafer11\CV_Te2V_Batch1_Wafer11_LGAD_4mm_No1_pad_only_floating.txt', 11, '4mm', 1, 'LGAD', 'new')
LGAD4mm2_11 = sensor('CVdata\wafer11\CV_Te2V_Batch1_Wafer11_LGAD_4mm_No2_pad_only_floating.txt', 11, '4mm', 2, 'LGAD', 'new')
LGAD4mm3_11 = sensor('CVdata\wafer11\CV_Te2V_Batch1_Wafer11_LGAD_4mm_No3_pad_only_floating.txt', 11, '4mm', 3, 'LGAD', 'new')
LGAD4mm5_11 = sensor('CVdata\wafer11\CV_Te2V_Batch1_Wafer11_LGAD_4mm_No5_pad_only_floating.txt', 11, '4mm', 5, 'LGAD', 'new')
LGAD2mm1_11 = sensor('CVdata\wafer11\CV_Te2V_Batch1_Wafer11_LGAD_2mm_No1_pad_only_floating.txt', 11, '2mm', 1, 'LGAD', 'new')
LGAD2mm3_11 = sensor('CVdata\wafer11\CV_Te2V_Batch1_Wafer11_LGAD_2mm_No3_pad_only_floating.txt', 11, '2mm', 3, 'LGAD', 'new')
LGAD2mm5_11 = sensor('CVdata\wafer11\CV_Te2V_Batch1_Wafer11_LGAD_2mm_No5_pad_only_floating.txt', 11, '2mm', 5, 'LGAD', 'new')
LGAD1mm1_11 = sensor('CVdata\wafer11\CV_Te2V_Batch1_Wafer11_LGAD_1mm_No1_pad_only_floating.txt', 11, '1mm', 1, 'LGAD', 'new')
LGAD1mm3_11 = sensor('CVdata\wafer11\CV_Te2V_Batch1_Wafer11_LGAD_1mm_No3_pad_only_floating.txt', 11, '1mm', 3, 'LGAD', 'new')
LGAD1mm5_11 = sensor('CVdata\wafer11\CV_Te2V_Batch1_Wafer11_LGAD_1mm_No5_pad_only_floating.txt', 11, '1mm', 5, 'LGAD', 'new')
PiN4mm1_11 = sensor('CVdata\wafer11\CV_Te2V_Batch1_Wafer11_PiN_4mm_No1_pad_only_floating.txt', 11, '4mm', 1, 'PiN', 'new')
PiN2mm1_11 = sensor('CVdata\wafer11\CV_Te2V_Batch1_Wafer11_PiN_2mm_No1_pad_only_floating_final.txt', 11, '2mm', 1, 'PiN', 'new')
PiN1mm1_11 = sensor('CVdata\wafer11\CV_Te2V_Batch1_Wafer11_PiN_1mm_No1_pad_only_floating_final.txt', 11, '1mm', 1, 'PiN', 'new')

#jonathans data below

LGAD4mm1_3 = sensor('CVdata\wafer3\Te2V_Batch1_Wafer3_LGAD_4mm_No1_pad_only', 3, '4mm', 1, 'LGAD', 'labview')
LGAD4mm3_3 = sensor('CVdata\wafer3\Te2V_Batch1_Wafer3_LGAD_4mm_No3_pad_only_floating', 3, '4mm', 3, 'LGAD', 'labview')
LGAD4mm5_3 = sensor('CVdata\wafer3\Te2V_Batch1_Wafer3_LGAD_4mm_No5_pad_only_floating', 3, '4mm', 5, 'LGAD', 'labview')
LGAD2mm1_3 = sensor('CVdata\wafer3\Te2V_Batch1_Wafer3_LGAD_2mm_No1_pad_only', 3, '2mm', 1, 'LGAD', 'labview')
LGAD1mm1_3 = sensor('CVdata\wafer3\Te2V_Batch1_Wafer3_LGAD_1mm_No1_pad_only', 3, '1mm', 1, 'LGAD', 'labview')
LGAD1mm3_3 = sensor('CVdata\wafer3\Te2V_Batch1_Wafer3_LGAD_1mm_No3_pad_only_floating', 3, '1mm', 3, 'LGAD', 'labview')
LGAD1mm5_3 = sensor('CVdata\wafer3\Te2V_Batch1_Wafer3_LGAD_1mm_No5_pad_only_floating', 3, '1mm', 5, 'LGAD', 'labview')
PiN4mm1_3 = sensor('CVdata\wafer3\Te2V_Batch1_Wafer3_PiN_4mm_No1_pad_only', 3, '4mm', 1, 'PiN', 'labview')
PiN4mm3_3 = sensor('CVdata\wafer3\Te2V_Batch1_Wafer3_PiN_4mm_No3_pad_only_floating', 3, '4mm',3, 'PiN', 'labview')
PiN4mm5_3 = sensor('CVdata\wafer3\Te2V_Batch1_Wafer3_PiN_4mm_No5_pad_only_floating', 3, '4mm', 5, 'PiN', 'labview')
PiN2mm1_3 = sensor('CVdata\wafer3\Te2V_Batch1_Wafer3_PiN_2mm_No1_pad_only', 3, '2mm', 1, 'PiN', 'labview')
PiN1mm1_3 = sensor('CVdata\wafer3\Te2V_Batch1_Wafer3_PiN_1mm_No1_pad_only', 3, '1mm', 1, 'PiN', 'labview')
PiN1mm3_3 = sensor('CVdata\wafer3\Te2V_Batch1_Wafer3_PiN_1mm_No3_pad_only_floating', 3, '1mm', 3, 'PiN', 'labview')
PiN1mm5_3 = sensor('CVdata\wafer3\Te2V_Batch1_Wafer3_PiN_1mm_No5_pad_only_floating', 3, '1mm', 5, 'PiN', 'labview')


LGAD4mm1_16 = sensor('CVdata\wafer16\Te2V_Batch1_Wafer16_LGAD_4mm_No1_pad_only', 16, '4mm', 1, 'LGAD', 'labview')
LGAD4mm3_16 = sensor('CVdata\wafer16\Te2V_Batch1_Wafer16_LGAD_4mm_No3_pad_only', 16, '4mm', 3, 'LGAD', 'labview')
LGAD4mm5_16 = sensor('CVdata\wafer16\Te2V_Batch1_Wafer16_LGAD_4mm_No5_pad_only', 16, '4mm', 5, 'LGAD', 'labview')
LGAD1mm1_16 = sensor('CVdata\wafer16\Te2V_Batch1_Wafer16_LGAD_1mm_No1_pad_only', 16, '1mm', 1, 'LGAD', 'labview')
LGAD1mm3_16 = sensor('CVdata\wafer16\Te2V_Batch1_Wafer16_LGAD_1mm_No3_pad_only', 16, '1mm', 3, 'LGAD', 'labview')
LGAD1mm5_16 = sensor('CVdata\wafer16\Te2V_Batch1_Wafer16_LGAD_1mm_No5_pad_only', 16, '1mm', 5, 'LGAD', 'labview')
PiN4mm1_16 = sensor('CVdata\wafer16\Te2V_Batch1_Wafer16_PiN_4mm_No1_pad_only', 16, '4mm', 1, 'PiN', 'labview')
PiN4mm3_16 = sensor('CVdata\wafer16\Te2V_Batch1_Wafer16_PiN_4mm_No3_pad_only', 16, '4mm', 3, 'PiN', 'labview')
PiN4mm5_16 = sensor('CVdata\wafer16\Te2V_Batch1_Wafer16_PiN_4mm_No5_pad_only', 16, '4mm', 5, 'PiN', 'labview')
PiN1mm1_16 = sensor('CVdata\wafer16\Te2V_Batch1_Wafer16_PiN_1mm_No1_pad_only', 16, '1mm', 1, 'PiN', 'labview')
PiN1mm3_16 = sensor('CVdata\wafer16\Te2V_Batch1_Wafer16_PiN_1mm_No3_pad_only', 16, '1mm', 3, 'PiN', 'labview')
PiN1mm5_16 = sensor('CVdata\wafer16\Te2V_Batch1_Wafer16_PiN_1mm_No5_pad_only', 16, '1mm', 5, 'PiN', 'labview')


LGAD4mm1_20 = sensor('CVdata\wafer20\Te2V_Batch1_Wafer20_LGAD_4mm_No1_pad_only', 20, '4mm', 1, 'LGAD', 'labview')
LGAD4mm3_20 = sensor('CVdata\wafer20\Te2V_Batch1_Wafer20_LGAD_4mm_No3_pad_only_floating', 20, '4mm', 3, 'LGAD', 'labview')
LGAD4mm5_20 = sensor('CVdata\wafer20\Te2V_Batch1_Wafer20_LGAD_4mm_No5_pad_only_floating', 20, '4mm', 5, 'LGAD', 'labview')
LGAD2mm1_20 = sensor('CVdata\wafer20\Te2V_Batch1_Wafer20_LGAD_2mm_No1_pad_only', 20, '2mm', 1, 'LGAD', 'labview')
LGAD1mm1_20 = sensor('CVdata\wafer20\Te2V_Batch1_Wafer20_LGAD_1mm_No1_pad_only', 20, '1mm', 1, 'LGAD', 'labview')
LGAD1mm3_20 = sensor('CVdata\wafer20\Te2V_Batch1_Wafer20_LGAD_1mm_No3_pad_only_floating', 20, '1mm', 3, 'LGAD', 'labview')
LGAD1mm5_20 = sensor('CVdata\wafer20\Te2V_Batch1_Wafer20_LGAD_1mm_No5_pad_only_floating', 20, '1mm', 5, 'LGAD', 'labview')
PiN4mm1_20 = sensor('CVdata\wafer20\Te2V_Batch1_Wafer20_PiN_4mm_No1_pad_only_148Vremoved.txt', 20, '4mm', 1, 'PiN', 'labview')
PiN4mm3_20 = sensor('CVdata\wafer20\Te2V_Batch1_Wafer20_PiN_4mm_No3_pad_only_floating', 20, '4mm', 3, 'PiN', 'labview')
PiN4mm5_20 = sensor('CVdata\wafer20\Te2V_Batch1_Wafer20_PiN_4mm_No5_pad_only_floating', 20, '4mm', 5, 'PiN', 'labview')
PiN2mm1_20 = sensor('CVdata\wafer20\Te2V_Batch1_Wafer20_PiN_2mm_No1_pad_only', 20, '2mm', 1, 'PiN', 'labview')
PiN1mm1_20 = sensor('CVdata\wafer20\Te2V_Batch1_Wafer20_PiN_1mm_No1_pad_only', 20, '1mm', 1, 'PiN', 'labview')
PiN1mm3_20 = sensor('CVdata\wafer20\Te2V_Batch1_Wafer20_PiN_1mm_No3_pad_only_floating', 20, '1mm', 1, 'PiN', 'labview')
PiN1mm5_20 = sensor('CVdata\wafer20\Te2V_Batch1_Wafer20_PiN_1mm_No5_pad_only_floating_WrongPiN(One Next to LGAD)', 20, '1mm', 1, 'PiN', 'labview')
#final PiN here is wrong data (ask jonathan)

#diced sensors now

LGAD1mm1_6_diced = sensor('CVdata\diced\CV_wafer_6_LGAD_loc1_1mm_D2.txt', 6, '1mm', 1, 'LGAD', 'new', True)
LGAD1mm5_6_diced = sensor('CVdata\diced\CV_wafer_6_LGAD_loc5_1mm_D2.txt', 6, '1mm', 5, 'LGAD', 'new', True)
PiN1mm1_6_diced = sensor('CVdata\diced\CV_wafer_6_PiN_loc1_1mm_D2.txt', 6, '1mm', 1, 'PiN', 'new', True)

LGAD1mm1_11_diced = sensor('CVdata\diced\CV_wafer_11_LGAD_loc1_1mm_D2.txt', 11, '1mm', 1, 'LGAD', 'new', True)
LGAD1mm5_11_diced = sensor('CVdata\diced\CV_wafer_11_LGAD_loc5_1mm_D2.txt', 11, '1mm', 5, 'LGAD', 'new', True)
PiN1mm1_11_diced = sensor('CVdata\diced\CV_wafer_11_PiN_loc1_1mm_D2.txt', 11, '1mm', 1, 'PiN', 'new', True)

#generate all the sensor dictionaries with the corresponding key parameters
edata = pd.read_csv('Sensor-Data-Table-Live.csv')   #can i change this to read_excel and keep .xlsx format?

LGAD4mm1_6_dic = {'Kbreakdown':edata['Breakdown Voltage (K=4) [V]'][0], 'ATLASbreakdown':edata['ALTLAS Breakdown [V]'][0], 'GLD':edata['Gain Layer Depletion [V]'][0], 'FD':edata['Full Depletion [V]'][0], 'PeakDope':edata['Peak Doping Value [*10^15cm^-3]'][0], 'PeakDopeDepth':edata['Peak Doping Depth [um]'][0], 'FittedPeakDope':edata['Fitted Peak Doping Value [*10^15cm^-3]'][0], 'FittedPeakDopeDepth':edata['Fitted Peak Doping Depth [um]'][0], 'EpiDope':edata['Epitaxial Doping @ 20 um[*10^12cm^-3]'][0], 'ImplantDepth':edata['Implant Depth [um]'][0], 'TotalDope':edata['Integral of Dope Peak [*10^15]'][0]}
LGAD4mm2_6_dic = {'Kbreakdown':edata['Breakdown Voltage (K=4) [V]'][1], 'ATLASbreakdown':edata['ALTLAS Breakdown [V]'][1]}
LGAD4mm3_6_dic = {'Kbreakdown':edata['Breakdown Voltage (K=4) [V]'][2], 'ATLASbreakdown':edata['ALTLAS Breakdown [V]'][2], 'GLD':edata['Gain Layer Depletion [V]'][2], 'FD':edata['Full Depletion [V]'][2], 'PeakDope':edata['Peak Doping Value [*10^15cm^-3]'][2], 'PeakDopeDepth':edata['Peak Doping Depth [um]'][2], 'FittedPeakDope':edata['Fitted Peak Doping Value [*10^15cm^-3]'][2], 'FittedPeakDopeDepth':edata['Fitted Peak Doping Depth [um]'][2], 'EpiDope':edata['Epitaxial Doping @ 20 um[*10^12cm^-3]'][2], 'ImplantDepth':edata['Implant Depth [um]'][2], 'TotalDope':edata['Integral of Dope Peak [*10^15]'][2]}
LGAD4mm4_6_dic = {'Kbreakdown':edata['Breakdown Voltage (K=4) [V]'][3], 'ATLASbreakdown':edata['ALTLAS Breakdown [V]'][3]}
LGAD4mm5_6_dic = {'Kbreakdown':edata['Breakdown Voltage (K=4) [V]'][4], 'ATLASbreakdown':edata['ALTLAS Breakdown [V]'][4], 'GLD':edata['Gain Layer Depletion [V]'][4], 'FD':edata['Full Depletion [V]'][4], 'PeakDope':edata['Peak Doping Value [*10^15cm^-3]'][4], 'PeakDopeDepth':edata['Peak Doping Depth [um]'][4], 'FittedPeakDope':edata['Fitted Peak Doping Value [*10^15cm^-3]'][4], 'FittedPeakDopeDepth':edata['Fitted Peak Doping Depth [um]'][4], 'EpiDope':edata['Epitaxial Doping @ 20 um[*10^12cm^-3]'][4], 'ImplantDepth':edata['Implant Depth [um]'][4], 'TotalDope':edata['Integral of Dope Peak [*10^15]'][4]}
PiN4mm1_6_dic = {'Kbreakdown':edata['Breakdown Voltage (K=4) [V]'][5], 'ATLASbreakdown':edata['ALTLAS Breakdown [V]'][5], 'GLD':edata['Gain Layer Depletion [V]'][5], 'FD':edata['Full Depletion [V]'][5], 'PeakDope':edata['Peak Doping Value [*10^15cm^-3]'][5], 'PeakDopeDepth':edata['Peak Doping Depth [um]'][5], 'FittedPeakDope':edata['Fitted Peak Doping Value [*10^15cm^-3]'][5], 'FittedPeakDopeDepth':edata['Fitted Peak Doping Depth [um]'][5], 'EpiDope':edata['Epitaxial Doping @ 20 um[*10^12cm^-3]'][5], 'ImplantDepth':edata['Implant Depth [um]'][5], 'TotalDope':edata['Integral of Dope Peak [*10^15]'][5]}
LGAD2mm1_6_dic = {'Kbreakdown':edata['Breakdown Voltage (K=4) [V]'][6], 'ATLASbreakdown':edata['ALTLAS Breakdown [V]'][6], 'GLD':edata['Gain Layer Depletion [V]'][6], 'FD':edata['Full Depletion [V]'][6], 'PeakDope':edata['Peak Doping Value [*10^15cm^-3]'][6], 'PeakDopeDepth':edata['Peak Doping Depth [um]'][6], 'FittedPeakDope':edata['Fitted Peak Doping Value [*10^15cm^-3]'][6], 'FittedPeakDopeDepth':edata['Fitted Peak Doping Depth [um]'][6], 'EpiDope':edata['Epitaxial Doping @ 20 um[*10^12cm^-3]'][6], 'ImplantDepth':edata['Implant Depth [um]'][6], 'TotalDope':edata['Integral of Dope Peak [*10^15]'][6]}
LGAD2mm2_6_dic = {'Kbreakdown':edata['Breakdown Voltage (K=4) [V]'][7], 'ATLASbreakdown':edata['ALTLAS Breakdown [V]'][7]}
LGAD2mm3_6_dic = {'Kbreakdown':edata['Breakdown Voltage (K=4) [V]'][8], 'ATLASbreakdown':edata['ALTLAS Breakdown [V]'][8], 'GLD':edata['Gain Layer Depletion [V]'][8], 'FD':edata['Full Depletion [V]'][8], 'PeakDope':edata['Peak Doping Value [*10^15cm^-3]'][8], 'PeakDopeDepth':edata['Peak Doping Depth [um]'][8], 'FittedPeakDope':edata['Fitted Peak Doping Value [*10^15cm^-3]'][8], 'FittedPeakDopeDepth':edata['Fitted Peak Doping Depth [um]'][8], 'EpiDope':edata['Epitaxial Doping @ 20 um[*10^12cm^-3]'][8], 'ImplantDepth':edata['Implant Depth [um]'][8], 'TotalDope':edata['Integral of Dope Peak [*10^15]'][8]}
LGAD2mm4_6_dic = {'Kbreakdown':edata['Breakdown Voltage (K=4) [V]'][9], 'ATLASbreakdown':edata['ALTLAS Breakdown [V]'][9]}
LGAD2mm5_6_dic = {'Kbreakdown':edata['Breakdown Voltage (K=4) [V]'][10], 'ATLASbreakdown':edata['ALTLAS Breakdown [V]'][10], 'GLD':edata['Gain Layer Depletion [V]'][10], 'FD':edata['Full Depletion [V]'][10], 'PeakDope':edata['Peak Doping Value [*10^15cm^-3]'][10], 'PeakDopeDepth':edata['Peak Doping Depth [um]'][10], 'FittedPeakDope':edata['Fitted Peak Doping Value [*10^15cm^-3]'][10], 'FittedPeakDopeDepth':edata['Fitted Peak Doping Depth [um]'][10], 'EpiDope':edata['Epitaxial Doping @ 20 um[*10^12cm^-3]'][10], 'ImplantDepth':edata['Implant Depth [um]'][10], 'TotalDope':edata['Integral of Dope Peak [*10^15]'][10]}
PiN2mm1_6_dic = {'Kbreakdown':edata['Breakdown Voltage (K=4) [V]'][11], 'ATLASbreakdown':edata['ALTLAS Breakdown [V]'][11], 'GLD':edata['Gain Layer Depletion [V]'][11], 'FD':edata['Full Depletion [V]'][11], 'PeakDope':edata['Peak Doping Value [*10^15cm^-3]'][11], 'PeakDopeDepth':edata['Peak Doping Depth [um]'][11], 'FittedPeakDope':edata['Fitted Peak Doping Value [*10^15cm^-3]'][11], 'FittedPeakDopeDepth':edata['Fitted Peak Doping Depth [um]'][11], 'EpiDope':edata['Epitaxial Doping @ 20 um[*10^12cm^-3]'][11], 'ImplantDepth':edata['Implant Depth [um]'][11], 'TotalDope':edata['Integral of Dope Peak [*10^15]'][11]}
LGAD1mm1_6_dic = {'Kbreakdown':edata['Breakdown Voltage (K=4) [V]'][12], 'ATLASbreakdown':edata['ALTLAS Breakdown [V]'][12], 'GLD':edata['Gain Layer Depletion [V]'][12], 'FD':edata['Full Depletion [V]'][12], 'PeakDope':edata['Peak Doping Value [*10^15cm^-3]'][12], 'PeakDopeDepth':edata['Peak Doping Depth [um]'][12], 'FittedPeakDope':edata['Fitted Peak Doping Value [*10^15cm^-3]'][12], 'FittedPeakDopeDepth':edata['Fitted Peak Doping Depth [um]'][12], 'EpiDope':edata['Epitaxial Doping @ 20 um[*10^12cm^-3]'][12], 'ImplantDepth':edata['Implant Depth [um]'][12], 'TotalDope':edata['Integral of Dope Peak [*10^15]'][12]}
LGAD1mm2_6_dic = {'Kbreakdown':edata['Breakdown Voltage (K=4) [V]'][13], 'ATLASbreakdown':edata['ALTLAS Breakdown [V]'][13], 'GLD':edata['Gain Layer Depletion [V]'][13], 'FD':edata['Full Depletion [V]'][13], 'PeakDope':edata['Peak Doping Value [*10^15cm^-3]'][13], 'PeakDopeDepth':edata['Peak Doping Depth [um]'][13], 'FittedPeakDope':edata['Fitted Peak Doping Value [*10^15cm^-3]'][13], 'FittedPeakDopeDepth':edata['Fitted Peak Doping Depth [um]'][13], 'EpiDope':edata['Epitaxial Doping @ 20 um[*10^12cm^-3]'][13], 'ImplantDepth':edata['Implant Depth [um]'][13], 'TotalDope':edata['Integral of Dope Peak [*10^15]'][13]}
LGAD1mm3_6_dic = {'Kbreakdown':edata['Breakdown Voltage (K=4) [V]'][14], 'ATLASbreakdown':edata['ALTLAS Breakdown [V]'][14], 'GLD':edata['Gain Layer Depletion [V]'][14], 'FD':edata['Full Depletion [V]'][14], 'PeakDope':edata['Peak Doping Value [*10^15cm^-3]'][14], 'PeakDopeDepth':edata['Peak Doping Depth [um]'][14], 'FittedPeakDope':edata['Fitted Peak Doping Value [*10^15cm^-3]'][14], 'FittedPeakDopeDepth':edata['Fitted Peak Doping Depth [um]'][14], 'EpiDope':edata['Epitaxial Doping @ 20 um[*10^12cm^-3]'][14], 'ImplantDepth':edata['Implant Depth [um]'][14], 'TotalDope':edata['Integral of Dope Peak [*10^15]'][14]}
LGAD1mm4_6_dic = {'Kbreakdown':edata['Breakdown Voltage (K=4) [V]'][15], 'ATLASbreakdown':edata['ALTLAS Breakdown [V]'][15], 'GLD':edata['Gain Layer Depletion [V]'][15], 'FD':edata['Full Depletion [V]'][15], 'PeakDope':edata['Peak Doping Value [*10^15cm^-3]'][15], 'PeakDopeDepth':edata['Peak Doping Depth [um]'][15], 'FittedPeakDope':edata['Fitted Peak Doping Value [*10^15cm^-3]'][15], 'FittedPeakDopeDepth':edata['Fitted Peak Doping Depth [um]'][15], 'EpiDope':edata['Epitaxial Doping @ 20 um[*10^12cm^-3]'][15], 'ImplantDepth':edata['Implant Depth [um]'][15], 'TotalDope':edata['Integral of Dope Peak [*10^15]'][15]}
LGAD1mm5_6_dic = {'Kbreakdown':edata['Breakdown Voltage (K=4) [V]'][16], 'ATLASbreakdown':edata['ALTLAS Breakdown [V]'][16], 'GLD':edata['Gain Layer Depletion [V]'][16], 'FD':edata['Full Depletion [V]'][16], 'PeakDope':edata['Peak Doping Value [*10^15cm^-3]'][16], 'PeakDopeDepth':edata['Peak Doping Depth [um]'][16], 'FittedPeakDope':edata['Fitted Peak Doping Value [*10^15cm^-3]'][16], 'FittedPeakDopeDepth':edata['Fitted Peak Doping Depth [um]'][16], 'EpiDope':edata['Epitaxial Doping @ 20 um[*10^12cm^-3]'][16], 'ImplantDepth':edata['Implant Depth [um]'][16], 'TotalDope':edata['Integral of Dope Peak [*10^15]'][16]}
PiN1mm1_6_dic = {'Kbreakdown':edata['Breakdown Voltage (K=4) [V]'][17], 'ATLASbreakdown':edata['ALTLAS Breakdown [V]'][17], 'GLD':edata['Gain Layer Depletion [V]'][17], 'FD':edata['Full Depletion [V]'][17], 'PeakDope':edata['Peak Doping Value [*10^15cm^-3]'][17], 'PeakDopeDepth':edata['Peak Doping Depth [um]'][17], 'FittedPeakDope':edata['Fitted Peak Doping Value [*10^15cm^-3]'][17], 'FittedPeakDopeDepth':edata['Fitted Peak Doping Depth [um]'][17], 'EpiDope':edata['Epitaxial Doping @ 20 um[*10^12cm^-3]'][17], 'ImplantDepth':edata['Implant Depth [um]'][17], 'TotalDope':edata['Integral of Dope Peak [*10^15]'][17]}

LGAD4mm1_11_dic = {'Kbreakdown':edata['Breakdown Voltage (K=4) [V]'][19], 'ATLASbreakdown':edata['ALTLAS Breakdown [V]'][19], 'GLD':edata['Gain Layer Depletion [V]'][19], 'FD':edata['Full Depletion [V]'][19], 'PeakDope':edata['Peak Doping Value [*10^15cm^-3]'][19], 'PeakDopeDepth':edata['Peak Doping Depth [um]'][19], 'FittedPeakDope':edata['Fitted Peak Doping Value [*10^15cm^-3]'][19], 'FittedPeakDopeDepth':edata['Fitted Peak Doping Depth [um]'][19], 'EpiDope':edata['Epitaxial Doping @ 20 um[*10^12cm^-3]'][19], 'ImplantDepth':edata['Implant Depth [um]'][19], 'TotalDope':edata['Integral of Dope Peak [*10^15]'][19]}
LGAD4mm2_11_dic = {'Kbreakdown':edata['Breakdown Voltage (K=4) [V]'][20], 'ATLASbreakdown':edata['ALTLAS Breakdown [V]'][20], 'GLD':edata['Gain Layer Depletion [V]'][20], 'FD':edata['Full Depletion [V]'][20], 'PeakDope':edata['Peak Doping Value [*10^15cm^-3]'][20], 'PeakDopeDepth':edata['Peak Doping Depth [um]'][20], 'FittedPeakDope':edata['Fitted Peak Doping Value [*10^15cm^-3]'][20], 'FittedPeakDopeDepth':edata['Fitted Peak Doping Depth [um]'][20], 'EpiDope':edata['Epitaxial Doping @ 20 um[*10^12cm^-3]'][20], 'ImplantDepth':edata['Implant Depth [um]'][20], 'TotalDope':edata['Integral of Dope Peak [*10^15]'][20]}
LGAD4mm3_11_dic = {'Kbreakdown':edata['Breakdown Voltage (K=4) [V]'][21], 'ATLASbreakdown':edata['ALTLAS Breakdown [V]'][21], 'GLD':edata['Gain Layer Depletion [V]'][21], 'FD':edata['Full Depletion [V]'][21], 'PeakDope':edata['Peak Doping Value [*10^15cm^-3]'][21], 'PeakDopeDepth':edata['Peak Doping Depth [um]'][21], 'FittedPeakDope':edata['Fitted Peak Doping Value [*10^15cm^-3]'][21], 'FittedPeakDopeDepth':edata['Fitted Peak Doping Depth [um]'][21], 'EpiDope':edata['Epitaxial Doping @ 20 um[*10^12cm^-3]'][21], 'ImplantDepth':edata['Implant Depth [um]'][21], 'TotalDope':edata['Integral of Dope Peak [*10^15]'][21]}
LGAD4mm4_11_dic = {'Kbreakdown':edata['Breakdown Voltage (K=4) [V]'][22], 'ATLASbreakdown':edata['ALTLAS Breakdown [V]'][22], 'GLD':edata['Gain Layer Depletion [V]'][22], 'FD':edata['Full Depletion [V]'][22], 'PeakDope':edata['Peak Doping Value [*10^15cm^-3]'][22], 'PeakDopeDepth':edata['Peak Doping Depth [um]'][22], 'FittedPeakDope':edata['Fitted Peak Doping Value [*10^15cm^-3]'][22], 'FittedPeakDopeDepth':edata['Fitted Peak Doping Depth [um]'][22], 'EpiDope':edata['Epitaxial Doping @ 20 um[*10^12cm^-3]'][22], 'ImplantDepth':edata['Implant Depth [um]'][22], 'TotalDope':edata['Integral of Dope Peak [*10^15]'][22]}
LGAD4mm5_11_dic = {'Kbreakdown':edata['Breakdown Voltage (K=4) [V]'][23], 'ATLASbreakdown':edata['ALTLAS Breakdown [V]'][23], 'GLD':edata['Gain Layer Depletion [V]'][23], 'FD':edata['Full Depletion [V]'][23], 'PeakDope':edata['Peak Doping Value [*10^15cm^-3]'][23], 'PeakDopeDepth':edata['Peak Doping Depth [um]'][23], 'FittedPeakDope':edata['Fitted Peak Doping Value [*10^15cm^-3]'][23], 'FittedPeakDopeDepth':edata['Fitted Peak Doping Depth [um]'][23], 'EpiDope':edata['Epitaxial Doping @ 20 um[*10^12cm^-3]'][23], 'ImplantDepth':edata['Implant Depth [um]'][23], 'TotalDope':edata['Integral of Dope Peak [*10^15]'][23]}
PiN4mm1_11_dic = {'Kbreakdown':edata['Breakdown Voltage (K=4) [V]'][24], 'ATLASbreakdown':edata['ALTLAS Breakdown [V]'][24], 'GLD':edata['Gain Layer Depletion [V]'][24], 'FD':edata['Full Depletion [V]'][24], 'PeakDope':edata['Peak Doping Value [*10^15cm^-3]'][24], 'PeakDopeDepth':edata['Peak Doping Depth [um]'][24], 'FittedPeakDope':edata['Fitted Peak Doping Value [*10^15cm^-3]'][24], 'FittedPeakDopeDepth':edata['Fitted Peak Doping Depth [um]'][24], 'EpiDope':edata['Epitaxial Doping @ 20 um[*10^12cm^-3]'][24], 'ImplantDepth':edata['Implant Depth [um]'][24], 'TotalDope':edata['Integral of Dope Peak [*10^15]'][24]}
LGAD2mm1_11_dic = {'Kbreakdown':edata['Breakdown Voltage (K=4) [V]'][25], 'ATLASbreakdown':edata['ALTLAS Breakdown [V]'][25], 'GLD':edata['Gain Layer Depletion [V]'][25], 'FD':edata['Full Depletion [V]'][25], 'PeakDope':edata['Peak Doping Value [*10^15cm^-3]'][25], 'PeakDopeDepth':edata['Peak Doping Depth [um]'][25], 'FittedPeakDope':edata['Fitted Peak Doping Value [*10^15cm^-3]'][25], 'FittedPeakDopeDepth':edata['Fitted Peak Doping Depth [um]'][25], 'EpiDope':edata['Epitaxial Doping @ 20 um[*10^12cm^-3]'][25], 'ImplantDepth':edata['Implant Depth [um]'][25], 'TotalDope':edata['Integral of Dope Peak [*10^15]'][25]}
LGAD2mm2_11_dic = {'Kbreakdown':edata['Breakdown Voltage (K=4) [V]'][26], 'ATLASbreakdown':edata['ALTLAS Breakdown [V]'][26], 'GLD':edata['Gain Layer Depletion [V]'][26], 'FD':edata['Full Depletion [V]'][26], 'PeakDope':edata['Peak Doping Value [*10^15cm^-3]'][26], 'PeakDopeDepth':edata['Peak Doping Depth [um]'][26], 'FittedPeakDope':edata['Fitted Peak Doping Value [*10^15cm^-3]'][26], 'FittedPeakDopeDepth':edata['Fitted Peak Doping Depth [um]'][26], 'EpiDope':edata['Epitaxial Doping @ 20 um[*10^12cm^-3]'][26], 'ImplantDepth':edata['Implant Depth [um]'][26], 'TotalDope':edata['Integral of Dope Peak [*10^15]'][26]}
LGAD2mm3_11_dic = {'Kbreakdown':edata['Breakdown Voltage (K=4) [V]'][27], 'ATLASbreakdown':edata['ALTLAS Breakdown [V]'][27], 'GLD':edata['Gain Layer Depletion [V]'][27], 'FD':edata['Full Depletion [V]'][27], 'PeakDope':edata['Peak Doping Value [*10^15cm^-3]'][27], 'PeakDopeDepth':edata['Peak Doping Depth [um]'][27], 'FittedPeakDope':edata['Fitted Peak Doping Value [*10^15cm^-3]'][27], 'FittedPeakDopeDepth':edata['Fitted Peak Doping Depth [um]'][27], 'EpiDope':edata['Epitaxial Doping @ 20 um[*10^12cm^-3]'][27], 'ImplantDepth':edata['Implant Depth [um]'][27], 'TotalDope':edata['Integral of Dope Peak [*10^15]'][27]}
LGAD2mm4_11_dic = {'Kbreakdown':edata['Breakdown Voltage (K=4) [V]'][28], 'ATLASbreakdown':edata['ALTLAS Breakdown [V]'][28], 'GLD':edata['Gain Layer Depletion [V]'][28], 'FD':edata['Full Depletion [V]'][28], 'PeakDope':edata['Peak Doping Value [*10^15cm^-3]'][28], 'PeakDopeDepth':edata['Peak Doping Depth [um]'][28], 'FittedPeakDope':edata['Fitted Peak Doping Value [*10^15cm^-3]'][28], 'FittedPeakDopeDepth':edata['Fitted Peak Doping Depth [um]'][28], 'EpiDope':edata['Epitaxial Doping @ 20 um[*10^12cm^-3]'][28], 'ImplantDepth':edata['Implant Depth [um]'][28], 'TotalDope':edata['Integral of Dope Peak [*10^15]'][28]}
LGAD2mm5_11_dic = {'Kbreakdown':edata['Breakdown Voltage (K=4) [V]'][29], 'ATLASbreakdown':edata['ALTLAS Breakdown [V]'][29], 'GLD':edata['Gain Layer Depletion [V]'][29], 'FD':edata['Full Depletion [V]'][29], 'PeakDope':edata['Peak Doping Value [*10^15cm^-3]'][29], 'PeakDopeDepth':edata['Peak Doping Depth [um]'][29], 'FittedPeakDope':edata['Fitted Peak Doping Value [*10^15cm^-3]'][29], 'FittedPeakDopeDepth':edata['Fitted Peak Doping Depth [um]'][29], 'EpiDope':edata['Epitaxial Doping @ 20 um[*10^12cm^-3]'][29], 'ImplantDepth':edata['Implant Depth [um]'][29], 'TotalDope':edata['Integral of Dope Peak [*10^15]'][29]}
PiN2mm1_11_dic = {'Kbreakdown':edata['Breakdown Voltage (K=4) [V]'][30], 'ATLASbreakdown':edata['ALTLAS Breakdown [V]'][30], 'GLD':edata['Gain Layer Depletion [V]'][30], 'FD':edata['Full Depletion [V]'][30], 'PeakDope':edata['Peak Doping Value [*10^15cm^-3]'][30], 'PeakDopeDepth':edata['Peak Doping Depth [um]'][30], 'FittedPeakDope':edata['Fitted Peak Doping Value [*10^15cm^-3]'][30], 'FittedPeakDopeDepth':edata['Fitted Peak Doping Depth [um]'][30], 'EpiDope':edata['Epitaxial Doping @ 20 um[*10^12cm^-3]'][30], 'ImplantDepth':edata['Implant Depth [um]'][30], 'TotalDope':edata['Integral of Dope Peak [*10^15]'][30]}
LGAD1mm1_11_dic = {'Kbreakdown':edata['Breakdown Voltage (K=4) [V]'][31], 'ATLASbreakdown':edata['ALTLAS Breakdown [V]'][31], 'GLD':edata['Gain Layer Depletion [V]'][31], 'FD':edata['Full Depletion [V]'][31], 'PeakDope':edata['Peak Doping Value [*10^15cm^-3]'][31], 'PeakDopeDepth':edata['Peak Doping Depth [um]'][31], 'FittedPeakDope':edata['Fitted Peak Doping Value [*10^15cm^-3]'][31], 'FittedPeakDopeDepth':edata['Fitted Peak Doping Depth [um]'][31], 'EpiDope':edata['Epitaxial Doping @ 20 um[*10^12cm^-3]'][31], 'ImplantDepth':edata['Implant Depth [um]'][31], 'TotalDope':edata['Integral of Dope Peak [*10^15]'][31]}
LGAD1mm2_11_dic = {'Kbreakdown':edata['Breakdown Voltage (K=4) [V]'][32], 'ATLASbreakdown':edata['ALTLAS Breakdown [V]'][32], 'GLD':edata['Gain Layer Depletion [V]'][32], 'FD':edata['Full Depletion [V]'][32], 'PeakDope':edata['Peak Doping Value [*10^15cm^-3]'][32], 'PeakDopeDepth':edata['Peak Doping Depth [um]'][32], 'FittedPeakDope':edata['Fitted Peak Doping Value [*10^15cm^-3]'][32], 'FittedPeakDopeDepth':edata['Fitted Peak Doping Depth [um]'][32], 'EpiDope':edata['Epitaxial Doping @ 20 um[*10^12cm^-3]'][32], 'ImplantDepth':edata['Implant Depth [um]'][32], 'TotalDope':edata['Integral of Dope Peak [*10^15]'][32]}
LGAD1mm3_11_dic = {'Kbreakdown':edata['Breakdown Voltage (K=4) [V]'][33], 'ATLASbreakdown':edata['ALTLAS Breakdown [V]'][33], 'GLD':edata['Gain Layer Depletion [V]'][33], 'FD':edata['Full Depletion [V]'][33], 'PeakDope':edata['Peak Doping Value [*10^15cm^-3]'][33], 'PeakDopeDepth':edata['Peak Doping Depth [um]'][33], 'FittedPeakDope':edata['Fitted Peak Doping Value [*10^15cm^-3]'][33], 'FittedPeakDopeDepth':edata['Fitted Peak Doping Depth [um]'][33], 'EpiDope':edata['Epitaxial Doping @ 20 um[*10^12cm^-3]'][33], 'ImplantDepth':edata['Implant Depth [um]'][33], 'TotalDope':edata['Integral of Dope Peak [*10^15]'][33]}
LGAD1mm4_11_dic = {'Kbreakdown':edata['Breakdown Voltage (K=4) [V]'][34], 'ATLASbreakdown':edata['ALTLAS Breakdown [V]'][34], 'GLD':edata['Gain Layer Depletion [V]'][34], 'FD':edata['Full Depletion [V]'][34], 'PeakDope':edata['Peak Doping Value [*10^15cm^-3]'][34], 'PeakDopeDepth':edata['Peak Doping Depth [um]'][34], 'FittedPeakDope':edata['Fitted Peak Doping Value [*10^15cm^-3]'][34], 'FittedPeakDopeDepth':edata['Fitted Peak Doping Depth [um]'][34], 'EpiDope':edata['Epitaxial Doping @ 20 um[*10^12cm^-3]'][34], 'ImplantDepth':edata['Implant Depth [um]'][34], 'TotalDope':edata['Integral of Dope Peak [*10^15]'][34]}
LGAD1mm5_11_dic = {'Kbreakdown':edata['Breakdown Voltage (K=4) [V]'][35], 'ATLASbreakdown':edata['ALTLAS Breakdown [V]'][35], 'GLD':edata['Gain Layer Depletion [V]'][35], 'FD':edata['Full Depletion [V]'][35], 'PeakDope':edata['Peak Doping Value [*10^15cm^-3]'][35], 'PeakDopeDepth':edata['Peak Doping Depth [um]'][35], 'FittedPeakDope':edata['Fitted Peak Doping Value [*10^15cm^-3]'][35], 'FittedPeakDopeDepth':edata['Fitted Peak Doping Depth [um]'][35], 'EpiDope':edata['Epitaxial Doping @ 20 um[*10^12cm^-3]'][35], 'ImplantDepth':edata['Implant Depth [um]'][35], 'TotalDope':edata['Integral of Dope Peak [*10^15]'][35]}
PiN1mm1_11_dic = {'Kbreakdown':edata['Breakdown Voltage (K=4) [V]'][36], 'ATLASbreakdown':edata['ALTLAS Breakdown [V]'][36], 'GLD':edata['Gain Layer Depletion [V]'][36], 'FD':edata['Full Depletion [V]'][36], 'PeakDope':edata['Peak Doping Value [*10^15cm^-3]'][36], 'PeakDopeDepth':edata['Peak Doping Depth [um]'][36], 'FittedPeakDope':edata['Fitted Peak Doping Value [*10^15cm^-3]'][36], 'FittedPeakDopeDepth':edata['Fitted Peak Doping Depth [um]'][36], 'EpiDope':edata['Epitaxial Doping @ 20 um[*10^12cm^-3]'][36], 'ImplantDepth':edata['Implant Depth [um]'][36], 'TotalDope':edata['Integral of Dope Peak [*10^15]'][36]}

LGAD4mm1_16_dic = {'Kbreakdown':edata['Breakdown Voltage (K=4) [V]'][38], 'ATLASbreakdown':edata['ALTLAS Breakdown [V]'][38], 'GLD':edata['Gain Layer Depletion [V]'][38], 'FD':edata['Full Depletion [V]'][38], 'PeakDope':edata['Peak Doping Value [*10^15cm^-3]'][38], 'PeakDopeDepth':edata['Peak Doping Depth [um]'][38], 'FittedPeakDope':edata['Fitted Peak Doping Value [*10^15cm^-3]'][38], 'FittedPeakDopeDepth':edata['Fitted Peak Doping Depth [um]'][38], 'EpiDope':edata['Epitaxial Doping @ 20 um[*10^12cm^-3]'][38], 'ImplantDepth':edata['Implant Depth [um]'][38], 'TotalDope':edata['Integral of Dope Peak [*10^15]'][38]}
LGAD4mm3_16_dic = {'Kbreakdown':edata['Breakdown Voltage (K=4) [V]'][39], 'ATLASbreakdown':edata['ALTLAS Breakdown [V]'][39], 'GLD':edata['Gain Layer Depletion [V]'][39], 'FD':edata['Full Depletion [V]'][39], 'PeakDope':edata['Peak Doping Value [*10^15cm^-3]'][39], 'PeakDopeDepth':edata['Peak Doping Depth [um]'][39], 'FittedPeakDope':edata['Fitted Peak Doping Value [*10^15cm^-3]'][39], 'FittedPeakDopeDepth':edata['Fitted Peak Doping Depth [um]'][39], 'EpiDope':edata['Epitaxial Doping @ 20 um[*10^12cm^-3]'][39], 'ImplantDepth':edata['Implant Depth [um]'][39], 'TotalDope':edata['Integral of Dope Peak [*10^15]'][39]}
LGAD4mm5_16_dic = {'Kbreakdown':edata['Breakdown Voltage (K=4) [V]'][40], 'ATLASbreakdown':edata['ALTLAS Breakdown [V]'][40], 'GLD':edata['Gain Layer Depletion [V]'][40], 'FD':edata['Full Depletion [V]'][40], 'PeakDope':edata['Peak Doping Value [*10^15cm^-3]'][40], 'PeakDopeDepth':edata['Peak Doping Depth [um]'][40], 'FittedPeakDope':edata['Fitted Peak Doping Value [*10^15cm^-3]'][40], 'FittedPeakDopeDepth':edata['Fitted Peak Doping Depth [um]'][40], 'EpiDope':edata['Epitaxial Doping @ 20 um[*10^12cm^-3]'][40], 'ImplantDepth':edata['Implant Depth [um]'][40], 'TotalDope':edata['Integral of Dope Peak [*10^15]'][40]}
PiN4mm1_16_dic = {'Kbreakdown':edata['Breakdown Voltage (K=4) [V]'][41], 'ATLASbreakdown':edata['ALTLAS Breakdown [V]'][41], 'GLD':edata['Gain Layer Depletion [V]'][41], 'FD':edata['Full Depletion [V]'][41], 'PeakDope':edata['Peak Doping Value [*10^15cm^-3]'][41], 'PeakDopeDepth':edata['Peak Doping Depth [um]'][41], 'FittedPeakDope':edata['Fitted Peak Doping Value [*10^15cm^-3]'][41], 'FittedPeakDopeDepth':edata['Fitted Peak Doping Depth [um]'][41], 'EpiDope':edata['Epitaxial Doping @ 20 um[*10^12cm^-3]'][41], 'ImplantDepth':edata['Implant Depth [um]'][41], 'TotalDope':edata['Integral of Dope Peak [*10^15]'][41]}
PiN4mm3_16_dic = {'Kbreakdown':edata['Breakdown Voltage (K=4) [V]'][42], 'ATLASbreakdown':edata['ALTLAS Breakdown [V]'][42], 'GLD':edata['Gain Layer Depletion [V]'][42], 'FD':edata['Full Depletion [V]'][42], 'PeakDope':edata['Peak Doping Value [*10^15cm^-3]'][42], 'PeakDopeDepth':edata['Peak Doping Depth [um]'][42], 'FittedPeakDope':edata['Fitted Peak Doping Value [*10^15cm^-3]'][42], 'FittedPeakDopeDepth':edata['Fitted Peak Doping Depth [um]'][42], 'EpiDope':edata['Epitaxial Doping @ 20 um[*10^12cm^-3]'][42], 'ImplantDepth':edata['Implant Depth [um]'][42], 'TotalDope':edata['Integral of Dope Peak [*10^15]'][42]}
PiN4mm5_16_dic = {'Kbreakdown':edata['Breakdown Voltage (K=4) [V]'][43], 'ATLASbreakdown':edata['ALTLAS Breakdown [V]'][43], 'GLD':edata['Gain Layer Depletion [V]'][43], 'FD':edata['Full Depletion [V]'][43], 'PeakDope':edata['Peak Doping Value [*10^15cm^-3]'][43], 'PeakDopeDepth':edata['Peak Doping Depth [um]'][43], 'FittedPeakDope':edata['Fitted Peak Doping Value [*10^15cm^-3]'][43], 'FittedPeakDopeDepth':edata['Fitted Peak Doping Depth [um]'][43], 'EpiDope':edata['Epitaxial Doping @ 20 um[*10^12cm^-3]'][43], 'ImplantDepth':edata['Implant Depth [um]'][43], 'TotalDope':edata['Integral of Dope Peak [*10^15]'][43]}
LGAD1mm1_16_dic = {'Kbreakdown':edata['Breakdown Voltage (K=4) [V]'][44], 'ATLASbreakdown':edata['ALTLAS Breakdown [V]'][44], 'GLD':edata['Gain Layer Depletion [V]'][44], 'FD':edata['Full Depletion [V]'][44], 'PeakDope':edata['Peak Doping Value [*10^15cm^-3]'][44], 'PeakDopeDepth':edata['Peak Doping Depth [um]'][44], 'FittedPeakDope':edata['Fitted Peak Doping Value [*10^15cm^-3]'][44], 'FittedPeakDopeDepth':edata['Fitted Peak Doping Depth [um]'][44], 'EpiDope':edata['Epitaxial Doping @ 20 um[*10^12cm^-3]'][44], 'ImplantDepth':edata['Implant Depth [um]'][44], 'TotalDope':edata['Integral of Dope Peak [*10^15]'][44]}
LGAD1mm3_16_dic = {'Kbreakdown':edata['Breakdown Voltage (K=4) [V]'][45], 'ATLASbreakdown':edata['ALTLAS Breakdown [V]'][45], 'GLD':edata['Gain Layer Depletion [V]'][45], 'FD':edata['Full Depletion [V]'][45], 'PeakDope':edata['Peak Doping Value [*10^15cm^-3]'][45], 'PeakDopeDepth':edata['Peak Doping Depth [um]'][45], 'FittedPeakDope':edata['Fitted Peak Doping Value [*10^15cm^-3]'][45], 'FittedPeakDopeDepth':edata['Fitted Peak Doping Depth [um]'][45], 'EpiDope':edata['Epitaxial Doping @ 20 um[*10^12cm^-3]'][45], 'ImplantDepth':edata['Implant Depth [um]'][45], 'TotalDope':edata['Integral of Dope Peak [*10^15]'][45]}
LGAD1mm5_16_dic = {'Kbreakdown':edata['Breakdown Voltage (K=4) [V]'][46], 'ATLASbreakdown':edata['ALTLAS Breakdown [V]'][46], 'GLD':edata['Gain Layer Depletion [V]'][46], 'FD':edata['Full Depletion [V]'][46], 'PeakDope':edata['Peak Doping Value [*10^15cm^-3]'][46], 'PeakDopeDepth':edata['Peak Doping Depth [um]'][46], 'FittedPeakDope':edata['Fitted Peak Doping Value [*10^15cm^-3]'][46], 'FittedPeakDopeDepth':edata['Fitted Peak Doping Depth [um]'][46], 'EpiDope':edata['Epitaxial Doping @ 20 um[*10^12cm^-3]'][46], 'ImplantDepth':edata['Implant Depth [um]'][46], 'TotalDope':edata['Integral of Dope Peak [*10^15]'][46]}
PiN1mm1_16_dic = {'Kbreakdown':edata['Breakdown Voltage (K=4) [V]'][47], 'ATLASbreakdown':edata['ALTLAS Breakdown [V]'][47], 'GLD':edata['Gain Layer Depletion [V]'][47], 'FD':edata['Full Depletion [V]'][47], 'PeakDope':edata['Peak Doping Value [*10^15cm^-3]'][47], 'PeakDopeDepth':edata['Peak Doping Depth [um]'][47], 'FittedPeakDope':edata['Fitted Peak Doping Value [*10^15cm^-3]'][47], 'FittedPeakDopeDepth':edata['Fitted Peak Doping Depth [um]'][47], 'EpiDope':edata['Epitaxial Doping @ 20 um[*10^12cm^-3]'][47], 'ImplantDepth':edata['Implant Depth [um]'][47], 'TotalDope':edata['Integral of Dope Peak [*10^15]'][47]}
PiN1mm3_16_dic = {'Kbreakdown':edata['Breakdown Voltage (K=4) [V]'][48], 'ATLASbreakdown':edata['ALTLAS Breakdown [V]'][48], 'GLD':edata['Gain Layer Depletion [V]'][48], 'FD':edata['Full Depletion [V]'][48], 'PeakDope':edata['Peak Doping Value [*10^15cm^-3]'][48], 'PeakDopeDepth':edata['Peak Doping Depth [um]'][48], 'FittedPeakDope':edata['Fitted Peak Doping Value [*10^15cm^-3]'][48], 'FittedPeakDopeDepth':edata['Fitted Peak Doping Depth [um]'][48], 'EpiDope':edata['Epitaxial Doping @ 20 um[*10^12cm^-3]'][48], 'ImplantDepth':edata['Implant Depth [um]'][48], 'TotalDope':edata['Integral of Dope Peak [*10^15]'][48]}
PiN1mm5_16_dic = {'Kbreakdown':edata['Breakdown Voltage (K=4) [V]'][49], 'ATLASbreakdown':edata['ALTLAS Breakdown [V]'][49], 'GLD':edata['Gain Layer Depletion [V]'][49], 'FD':edata['Full Depletion [V]'][49], 'PeakDope':edata['Peak Doping Value [*10^15cm^-3]'][49], 'PeakDopeDepth':edata['Peak Doping Depth [um]'][49], 'FittedPeakDope':edata['Fitted Peak Doping Value [*10^15cm^-3]'][49], 'FittedPeakDopeDepth':edata['Fitted Peak Doping Depth [um]'][49], 'EpiDope':edata['Epitaxial Doping @ 20 um[*10^12cm^-3]'][49], 'ImplantDepth':edata['Implant Depth [um]'][49], 'TotalDope':edata['Integral of Dope Peak [*10^15]'][49]}

LGAD4mm1_20_dic = {'Kbreakdown':edata['Breakdown Voltage (K=4) [V]'][51], 'ATLASbreakdown':edata['ALTLAS Breakdown [V]'][51], 'GLD':edata['Gain Layer Depletion [V]'][51], 'FD':edata['Full Depletion [V]'][51], 'PeakDope':edata['Peak Doping Value [*10^15cm^-3]'][51], 'PeakDopeDepth':edata['Peak Doping Depth [um]'][51], 'FittedPeakDope':edata['Fitted Peak Doping Value [*10^15cm^-3]'][51], 'FittedPeakDopeDepth':edata['Fitted Peak Doping Depth [um]'][51], 'EpiDope':edata['Epitaxial Doping @ 20 um[*10^12cm^-3]'][51], 'ImplantDepth':edata['Implant Depth [um]'][51], 'TotalDope':edata['Integral of Dope Peak [*10^15]'][51]}
LGAD4mm3_20_dic = {'Kbreakdown':edata['Breakdown Voltage (K=4) [V]'][52], 'ATLASbreakdown':edata['ALTLAS Breakdown [V]'][52], 'GLD':edata['Gain Layer Depletion [V]'][52], 'FD':edata['Full Depletion [V]'][52], 'PeakDope':edata['Peak Doping Value [*10^15cm^-3]'][52], 'PeakDopeDepth':edata['Peak Doping Depth [um]'][52], 'FittedPeakDope':edata['Fitted Peak Doping Value [*10^15cm^-3]'][52], 'FittedPeakDopeDepth':edata['Fitted Peak Doping Depth [um]'][52], 'EpiDope':edata['Epitaxial Doping @ 20 um[*10^12cm^-3]'][52], 'ImplantDepth':edata['Implant Depth [um]'][52], 'TotalDope':edata['Integral of Dope Peak [*10^15]'][52]}
LGAD4mm5_20_dic = {'Kbreakdown':edata['Breakdown Voltage (K=4) [V]'][53], 'ATLASbreakdown':edata['ALTLAS Breakdown [V]'][53], 'GLD':edata['Gain Layer Depletion [V]'][53], 'FD':edata['Full Depletion [V]'][53], 'PeakDope':edata['Peak Doping Value [*10^15cm^-3]'][53], 'PeakDopeDepth':edata['Peak Doping Depth [um]'][53], 'FittedPeakDope':edata['Fitted Peak Doping Value [*10^15cm^-3]'][53], 'FittedPeakDopeDepth':edata['Fitted Peak Doping Depth [um]'][53], 'EpiDope':edata['Epitaxial Doping @ 20 um[*10^12cm^-3]'][53], 'ImplantDepth':edata['Implant Depth [um]'][53], 'TotalDope':edata['Integral of Dope Peak [*10^15]'][53]}
PiN4mm1_20_dic = {'Kbreakdown':edata['Breakdown Voltage (K=4) [V]'][54], 'ATLASbreakdown':edata['ALTLAS Breakdown [V]'][54], 'GLD':edata['Gain Layer Depletion [V]'][54], 'FD':edata['Full Depletion [V]'][54], 'PeakDope':edata['Peak Doping Value [*10^15cm^-3]'][54], 'PeakDopeDepth':edata['Peak Doping Depth [um]'][54], 'FittedPeakDope':edata['Fitted Peak Doping Value [*10^15cm^-3]'][54], 'FittedPeakDopeDepth':edata['Fitted Peak Doping Depth [um]'][54], 'EpiDope':edata['Epitaxial Doping @ 20 um[*10^12cm^-3]'][54], 'ImplantDepth':edata['Implant Depth [um]'][54], 'TotalDope':edata['Integral of Dope Peak [*10^15]'][54]}
PiN4mm3_20_dic = {'Kbreakdown':edata['Breakdown Voltage (K=4) [V]'][55], 'ATLASbreakdown':edata['ALTLAS Breakdown [V]'][55], 'GLD':edata['Gain Layer Depletion [V]'][55], 'FD':edata['Full Depletion [V]'][55], 'PeakDope':edata['Peak Doping Value [*10^15cm^-3]'][55], 'PeakDopeDepth':edata['Peak Doping Depth [um]'][55], 'FittedPeakDope':edata['Fitted Peak Doping Value [*10^15cm^-3]'][55], 'FittedPeakDopeDepth':edata['Fitted Peak Doping Depth [um]'][55], 'EpiDope':edata['Epitaxial Doping @ 20 um[*10^12cm^-3]'][55], 'ImplantDepth':edata['Implant Depth [um]'][55], 'TotalDope':edata['Integral of Dope Peak [*10^15]'][55]}
PiN4mm5_20_dic = {'Kbreakdown':edata['Breakdown Voltage (K=4) [V]'][56], 'ATLASbreakdown':edata['ALTLAS Breakdown [V]'][56], 'GLD':edata['Gain Layer Depletion [V]'][56], 'FD':edata['Full Depletion [V]'][56], 'PeakDope':edata['Peak Doping Value [*10^15cm^-3]'][56], 'PeakDopeDepth':edata['Peak Doping Depth [um]'][56], 'FittedPeakDope':edata['Fitted Peak Doping Value [*10^15cm^-3]'][56], 'FittedPeakDopeDepth':edata['Fitted Peak Doping Depth [um]'][56], 'EpiDope':edata['Epitaxial Doping @ 20 um[*10^12cm^-3]'][56], 'ImplantDepth':edata['Implant Depth [um]'][56], 'TotalDope':edata['Integral of Dope Peak [*10^15]'][56]}
LGAD2mm1_20_dic = {'Kbreakdown':edata['Breakdown Voltage (K=4) [V]'][57], 'ATLASbreakdown':edata['ALTLAS Breakdown [V]'][57], 'GLD':edata['Gain Layer Depletion [V]'][57], 'FD':edata['Full Depletion [V]'][57], 'PeakDope':edata['Peak Doping Value [*10^15cm^-3]'][57], 'PeakDopeDepth':edata['Peak Doping Depth [um]'][57], 'FittedPeakDope':edata['Fitted Peak Doping Value [*10^15cm^-3]'][57], 'FittedPeakDopeDepth':edata['Fitted Peak Doping Depth [um]'][57], 'EpiDope':edata['Epitaxial Doping @ 20 um[*10^12cm^-3]'][57], 'ImplantDepth':edata['Implant Depth [um]'][57], 'TotalDope':edata['Integral of Dope Peak [*10^15]'][57]}
PiN2mm1_20_dic = {'Kbreakdown':edata['Breakdown Voltage (K=4) [V]'][58], 'ATLASbreakdown':edata['ALTLAS Breakdown [V]'][58], 'GLD':edata['Gain Layer Depletion [V]'][58], 'FD':edata['Full Depletion [V]'][58], 'PeakDope':edata['Peak Doping Value [*10^15cm^-3]'][58], 'PeakDopeDepth':edata['Peak Doping Depth [um]'][58], 'FittedPeakDope':edata['Fitted Peak Doping Value [*10^15cm^-3]'][58], 'FittedPeakDopeDepth':edata['Fitted Peak Doping Depth [um]'][58], 'EpiDope':edata['Epitaxial Doping @ 20 um[*10^12cm^-3]'][58], 'ImplantDepth':edata['Implant Depth [um]'][58], 'TotalDope':edata['Integral of Dope Peak [*10^15]'][58]}
LGAD1mm1_20_dic = {'Kbreakdown':edata['Breakdown Voltage (K=4) [V]'][59], 'ATLASbreakdown':edata['ALTLAS Breakdown [V]'][59], 'GLD':edata['Gain Layer Depletion [V]'][59], 'FD':edata['Full Depletion [V]'][59], 'PeakDope':edata['Peak Doping Value [*10^15cm^-3]'][59], 'PeakDopeDepth':edata['Peak Doping Depth [um]'][59], 'FittedPeakDope':edata['Fitted Peak Doping Value [*10^15cm^-3]'][59], 'FittedPeakDopeDepth':edata['Fitted Peak Doping Depth [um]'][59], 'EpiDope':edata['Epitaxial Doping @ 20 um[*10^12cm^-3]'][59], 'ImplantDepth':edata['Implant Depth [um]'][59], 'TotalDope':edata['Integral of Dope Peak [*10^15]'][59]}
LGAD1mm3_20_dic = {'Kbreakdown':edata['Breakdown Voltage (K=4) [V]'][60], 'ATLASbreakdown':edata['ALTLAS Breakdown [V]'][60], 'GLD':edata['Gain Layer Depletion [V]'][60], 'FD':edata['Full Depletion [V]'][60], 'PeakDope':edata['Peak Doping Value [*10^15cm^-3]'][60], 'PeakDopeDepth':edata['Peak Doping Depth [um]'][60], 'FittedPeakDope':edata['Fitted Peak Doping Value [*10^15cm^-3]'][60], 'FittedPeakDopeDepth':edata['Fitted Peak Doping Depth [um]'][60], 'EpiDope':edata['Epitaxial Doping @ 20 um[*10^12cm^-3]'][60], 'ImplantDepth':edata['Implant Depth [um]'][60], 'TotalDope':edata['Integral of Dope Peak [*10^15]'][60]}
LGAD1mm5_20_dic = {'Kbreakdown':edata['Breakdown Voltage (K=4) [V]'][61], 'ATLASbreakdown':edata['ALTLAS Breakdown [V]'][61], 'GLD':edata['Gain Layer Depletion [V]'][61], 'FD':edata['Full Depletion [V]'][61], 'PeakDope':edata['Peak Doping Value [*10^15cm^-3]'][61], 'PeakDopeDepth':edata['Peak Doping Depth [um]'][61], 'FittedPeakDope':edata['Fitted Peak Doping Value [*10^15cm^-3]'][61], 'FittedPeakDopeDepth':edata['Fitted Peak Doping Depth [um]'][61], 'EpiDope':edata['Epitaxial Doping @ 20 um[*10^12cm^-3]'][61], 'ImplantDepth':edata['Implant Depth [um]'][61], 'TotalDope':edata['Integral of Dope Peak [*10^15]'][61]}
PiN1mm1_20_dic = {'Kbreakdown':edata['Breakdown Voltage (K=4) [V]'][62], 'ATLASbreakdown':edata['ALTLAS Breakdown [V]'][62], 'GLD':edata['Gain Layer Depletion [V]'][62], 'FD':edata['Full Depletion [V]'][62], 'PeakDope':edata['Peak Doping Value [*10^15cm^-3]'][62], 'PeakDopeDepth':edata['Peak Doping Depth [um]'][62], 'FittedPeakDope':edata['Fitted Peak Doping Value [*10^15cm^-3]'][62], 'FittedPeakDopeDepth':edata['Fitted Peak Doping Depth [um]'][62], 'EpiDope':edata['Epitaxial Doping @ 20 um[*10^12cm^-3]'][62], 'ImplantDepth':edata['Implant Depth [um]'][62], 'TotalDope':edata['Integral of Dope Peak [*10^15]'][62]}
PiN1mm3_20_dic = {'Kbreakdown':edata['Breakdown Voltage (K=4) [V]'][63], 'ATLASbreakdown':edata['ALTLAS Breakdown [V]'][63], 'GLD':edata['Gain Layer Depletion [V]'][63], 'FD':edata['Full Depletion [V]'][63], 'PeakDope':edata['Peak Doping Value [*10^15cm^-3]'][63], 'PeakDopeDepth':edata['Peak Doping Depth [um]'][63], 'FittedPeakDope':edata['Fitted Peak Doping Value [*10^15cm^-3]'][63], 'FittedPeakDopeDepth':edata['Fitted Peak Doping Depth [um]'][63], 'EpiDope':edata['Epitaxial Doping @ 20 um[*10^12cm^-3]'][63], 'ImplantDepth':edata['Implant Depth [um]'][63], 'TotalDope':edata['Integral of Dope Peak [*10^15]'][63]}
PiN1mm5_30_dic = {'Kbreakdown':edata['Breakdown Voltage (K=4) [V]'][64], 'ATLASbreakdown':edata['ALTLAS Breakdown [V]'][64], 'GLD':edata['Gain Layer Depletion [V]'][64], 'FD':edata['Full Depletion [V]'][64], 'PeakDope':edata['Peak Doping Value [*10^15cm^-3]'][64], 'PeakDopeDepth':edata['Peak Doping Depth [um]'][64], 'FittedPeakDope':edata['Fitted Peak Doping Value [*10^15cm^-3]'][64], 'FittedPeakDopeDepth':edata['Fitted Peak Doping Depth [um]'][64], 'EpiDope':edata['Epitaxial Doping @ 20 um[*10^12cm^-3]'][64], 'ImplantDepth':edata['Implant Depth [um]'][64], 'TotalDope':edata['Integral of Dope Peak [*10^15]'][64]}

LGAD4mm1_3_dic = {'Kbreakdown':edata['Breakdown Voltage (K=4) [V]'][66], 'ATLASbreakdown':edata['ALTLAS Breakdown [V]'][66], 'GLD':edata['Gain Layer Depletion [V]'][66], 'FD':edata['Full Depletion [V]'][66], 'PeakDope':edata['Peak Doping Value [*10^15cm^-3]'][66], 'PeakDopeDepth':edata['Peak Doping Depth [um]'][66], 'FittedPeakDope':edata['Fitted Peak Doping Value [*10^15cm^-3]'][66], 'FittedPeakDopeDepth':edata['Fitted Peak Doping Depth [um]'][66], 'EpiDope':edata['Epitaxial Doping @ 20 um[*10^12cm^-3]'][66], 'ImplantDepth':edata['Implant Depth [um]'][66], 'TotalDope':edata['Integral of Dope Peak [*10^15]'][66]}
LGAD4mm3_3_dic = {'Kbreakdown':edata['Breakdown Voltage (K=4) [V]'][67], 'ATLASbreakdown':edata['ALTLAS Breakdown [V]'][67], 'GLD':edata['Gain Layer Depletion [V]'][67], 'FD':edata['Full Depletion [V]'][67], 'PeakDope':edata['Peak Doping Value [*10^15cm^-3]'][67], 'PeakDopeDepth':edata['Peak Doping Depth [um]'][67], 'FittedPeakDope':edata['Fitted Peak Doping Value [*10^15cm^-3]'][67], 'FittedPeakDopeDepth':edata['Fitted Peak Doping Depth [um]'][67], 'EpiDope':edata['Epitaxial Doping @ 20 um[*10^12cm^-3]'][67], 'ImplantDepth':edata['Implant Depth [um]'][67], 'TotalDope':edata['Integral of Dope Peak [*10^15]'][67]}
LGAD4mm5_3_dic = {'Kbreakdown':edata['Breakdown Voltage (K=4) [V]'][68], 'ATLASbreakdown':edata['ALTLAS Breakdown [V]'][68], 'GLD':edata['Gain Layer Depletion [V]'][68], 'FD':edata['Full Depletion [V]'][68], 'PeakDope':edata['Peak Doping Value [*10^15cm^-3]'][68], 'PeakDopeDepth':edata['Peak Doping Depth [um]'][68], 'FittedPeakDope':edata['Fitted Peak Doping Value [*10^15cm^-3]'][68], 'FittedPeakDopeDepth':edata['Fitted Peak Doping Depth [um]'][68], 'EpiDope':edata['Epitaxial Doping @ 20 um[*10^12cm^-3]'][68], 'ImplantDepth':edata['Implant Depth [um]'][68], 'TotalDope':edata['Integral of Dope Peak [*10^15]'][68]}
PiN4mm1_3_dic = {'Kbreakdown':edata['Breakdown Voltage (K=4) [V]'][69], 'ATLASbreakdown':edata['ALTLAS Breakdown [V]'][69], 'GLD':edata['Gain Layer Depletion [V]'][69], 'FD':edata['Full Depletion [V]'][69], 'PeakDope':edata['Peak Doping Value [*10^15cm^-3]'][69], 'PeakDopeDepth':edata['Peak Doping Depth [um]'][69], 'FittedPeakDope':edata['Fitted Peak Doping Value [*10^15cm^-3]'][69], 'FittedPeakDopeDepth':edata['Fitted Peak Doping Depth [um]'][69], 'EpiDope':edata['Epitaxial Doping @ 20 um[*10^12cm^-3]'][69], 'ImplantDepth':edata['Implant Depth [um]'][69], 'TotalDope':edata['Integral of Dope Peak [*10^15]'][69]}
PiN4mm3_3_dic = {'Kbreakdown':edata['Breakdown Voltage (K=4) [V]'][70], 'ATLASbreakdown':edata['ALTLAS Breakdown [V]'][70], 'GLD':edata['Gain Layer Depletion [V]'][70], 'FD':edata['Full Depletion [V]'][70], 'PeakDope':edata['Peak Doping Value [*10^15cm^-3]'][70], 'PeakDopeDepth':edata['Peak Doping Depth [um]'][70], 'FittedPeakDope':edata['Fitted Peak Doping Value [*10^15cm^-3]'][70], 'FittedPeakDopeDepth':edata['Fitted Peak Doping Depth [um]'][70], 'EpiDope':edata['Epitaxial Doping @ 20 um[*10^12cm^-3]'][70], 'ImplantDepth':edata['Implant Depth [um]'][70], 'TotalDope':edata['Integral of Dope Peak [*10^15]'][70]}
PiN4mm5_3_dic = {'Kbreakdown':edata['Breakdown Voltage (K=4) [V]'][71], 'ATLASbreakdown':edata['ALTLAS Breakdown [V]'][71], 'GLD':edata['Gain Layer Depletion [V]'][71], 'FD':edata['Full Depletion [V]'][71], 'PeakDope':edata['Peak Doping Value [*10^15cm^-3]'][71], 'PeakDopeDepth':edata['Peak Doping Depth [um]'][71], 'FittedPeakDope':edata['Fitted Peak Doping Value [*10^15cm^-3]'][71], 'FittedPeakDopeDepth':edata['Fitted Peak Doping Depth [um]'][71], 'EpiDope':edata['Epitaxial Doping @ 20 um[*10^12cm^-3]'][71], 'ImplantDepth':edata['Implant Depth [um]'][71], 'TotalDope':edata['Integral of Dope Peak [*10^15]'][71]}
LGAD2mm1_3_dic = {'Kbreakdown':edata['Breakdown Voltage (K=4) [V]'][72], 'ATLASbreakdown':edata['ALTLAS Breakdown [V]'][72], 'GLD':edata['Gain Layer Depletion [V]'][72], 'FD':edata['Full Depletion [V]'][72], 'PeakDope':edata['Peak Doping Value [*10^15cm^-3]'][72], 'PeakDopeDepth':edata['Peak Doping Depth [um]'][72], 'FittedPeakDope':edata['Fitted Peak Doping Value [*10^15cm^-3]'][72], 'FittedPeakDopeDepth':edata['Fitted Peak Doping Depth [um]'][72], 'EpiDope':edata['Epitaxial Doping @ 20 um[*10^12cm^-3]'][72], 'ImplantDepth':edata['Implant Depth [um]'][72], 'TotalDope':edata['Integral of Dope Peak [*10^15]'][72]}
PiN2mm1_3_dic = {'Kbreakdown':edata['Breakdown Voltage (K=4) [V]'][73], 'ATLASbreakdown':edata['ALTLAS Breakdown [V]'][73], 'GLD':edata['Gain Layer Depletion [V]'][73], 'FD':edata['Full Depletion [V]'][73], 'PeakDope':edata['Peak Doping Value [*10^15cm^-3]'][73], 'PeakDopeDepth':edata['Peak Doping Depth [um]'][73], 'FittedPeakDope':edata['Fitted Peak Doping Value [*10^15cm^-3]'][73], 'FittedPeakDopeDepth':edata['Fitted Peak Doping Depth [um]'][73], 'EpiDope':edata['Epitaxial Doping @ 20 um[*10^12cm^-3]'][73], 'ImplantDepth':edata['Implant Depth [um]'][73], 'TotalDope':edata['Integral of Dope Peak [*10^15]'][73]}
LGAD1mm1_3_dic = {'Kbreakdown':edata['Breakdown Voltage (K=4) [V]'][74], 'ATLASbreakdown':edata['ALTLAS Breakdown [V]'][74], 'GLD':edata['Gain Layer Depletion [V]'][74], 'FD':edata['Full Depletion [V]'][74], 'PeakDope':edata['Peak Doping Value [*10^15cm^-3]'][74], 'PeakDopeDepth':edata['Peak Doping Depth [um]'][74], 'FittedPeakDope':edata['Fitted Peak Doping Value [*10^15cm^-3]'][74], 'FittedPeakDopeDepth':edata['Fitted Peak Doping Depth [um]'][74], 'EpiDope':edata['Epitaxial Doping @ 20 um[*10^12cm^-3]'][74], 'ImplantDepth':edata['Implant Depth [um]'][74], 'TotalDope':edata['Integral of Dope Peak [*10^15]'][74]}
LGAD1mm3_3_dic = {'Kbreakdown':edata['Breakdown Voltage (K=4) [V]'][75], 'ATLASbreakdown':edata['ALTLAS Breakdown [V]'][75], 'GLD':edata['Gain Layer Depletion [V]'][75], 'FD':edata['Full Depletion [V]'][75], 'PeakDope':edata['Peak Doping Value [*10^15cm^-3]'][75], 'PeakDopeDepth':edata['Peak Doping Depth [um]'][75], 'FittedPeakDope':edata['Fitted Peak Doping Value [*10^15cm^-3]'][75], 'FittedPeakDopeDepth':edata['Fitted Peak Doping Depth [um]'][75], 'EpiDope':edata['Epitaxial Doping @ 20 um[*10^12cm^-3]'][75], 'ImplantDepth':edata['Implant Depth [um]'][75], 'TotalDope':edata['Integral of Dope Peak [*10^15]'][75]}
LGAD1mm5_3_dic = {'Kbreakdown':edata['Breakdown Voltage (K=4) [V]'][76], 'ATLASbreakdown':edata['ALTLAS Breakdown [V]'][76], 'GLD':edata['Gain Layer Depletion [V]'][76], 'FD':edata['Full Depletion [V]'][76], 'PeakDope':edata['Peak Doping Value [*10^15cm^-3]'][76], 'PeakDopeDepth':edata['Peak Doping Depth [um]'][76], 'FittedPeakDope':edata['Fitted Peak Doping Value [*10^15cm^-3]'][76], 'FittedPeakDopeDepth':edata['Fitted Peak Doping Depth [um]'][76], 'EpiDope':edata['Epitaxial Doping @ 20 um[*10^12cm^-3]'][76], 'ImplantDepth':edata['Implant Depth [um]'][76], 'TotalDope':edata['Integral of Dope Peak [*10^15]'][76]}
PiN1mm1_3_dic = {'Kbreakdown':edata['Breakdown Voltage (K=4) [V]'][77], 'ATLASbreakdown':edata['ALTLAS Breakdown [V]'][77], 'GLD':edata['Gain Layer Depletion [V]'][77], 'FD':edata['Full Depletion [V]'][77], 'PeakDope':edata['Peak Doping Value [*10^15cm^-3]'][77], 'PeakDopeDepth':edata['Peak Doping Depth [um]'][77], 'FittedPeakDope':edata['Fitted Peak Doping Value [*10^15cm^-3]'][77], 'FittedPeakDopeDepth':edata['Fitted Peak Doping Depth [um]'][77], 'EpiDope':edata['Epitaxial Doping @ 20 um[*10^12cm^-3]'][77], 'ImplantDepth':edata['Implant Depth [um]'][77], 'TotalDope':edata['Integral of Dope Peak [*10^15]'][77]}
PiN1mm3_3_dic = {'Kbreakdown':edata['Breakdown Voltage (K=4) [V]'][78], 'ATLASbreakdown':edata['ALTLAS Breakdown [V]'][78], 'GLD':edata['Gain Layer Depletion [V]'][78], 'FD':edata['Full Depletion [V]'][78], 'PeakDope':edata['Peak Doping Value [*10^15cm^-3]'][78], 'PeakDopeDepth':edata['Peak Doping Depth [um]'][78], 'FittedPeakDope':edata['Fitted Peak Doping Value [*10^15cm^-3]'][78], 'FittedPeakDopeDepth':edata['Fitted Peak Doping Depth [um]'][78], 'EpiDope':edata['Epitaxial Doping @ 20 um[*10^12cm^-3]'][78], 'ImplantDepth':edata['Implant Depth [um]'][78], 'TotalDope':edata['Integral of Dope Peak [*10^15]'][78]}
PiN1mm5_3_dic = {'Kbreakdown':edata['Breakdown Voltage (K=4) [V]'][79], 'ATLASbreakdown':edata['ALTLAS Breakdown [V]'][79], 'GLD':edata['Gain Layer Depletion [V]'][79], 'FD':edata['Full Depletion [V]'][79], 'PeakDope':edata['Peak Doping Value [*10^15cm^-3]'][79], 'PeakDopeDepth':edata['Peak Doping Depth [um]'][79], 'FittedPeakDope':edata['Fitted Peak Doping Value [*10^15cm^-3]'][79], 'FittedPeakDopeDepth':edata['Fitted Peak Doping Depth [um]'][79], 'EpiDope':edata['Epitaxial Doping @ 20 um[*10^12cm^-3]'][79], 'ImplantDepth':edata['Implant Depth [um]'][79], 'TotalDope':edata['Integral of Dope Peak [*10^15]'][79]}


def getdata(sensor):
    
    if sensor.newdatastyle == 'new':
        rawdata = []
        data = []
        V = []
        C = []
        
        with open(sensor.file, 'r') as filestream:
            for line in filestream:
                currentline = line.split(' ')
                rawdata.append(currentline)
        rawdata = rawdata[14:-1]
        data = []
        #remove the fact it spills onto new lines
        for i in range(0, len(rawdata)-1):
            if i%2 == 0:
                data.append(rawdata[i] + rawdata[i+1])
        data = data[1::3]#gets just 100kHz values
        for i in range(0, len(data)):
            V.append(abs(float(data[i][1])))
            C.append(abs(float(data[i][4])))
            
        C_plot = []
        
        for i in range(0, len(C)):
            C_plot.append(1/(C[i]**2))
        return V, C_plot
    
    elif sensor.newdatastyle == 'old':
        rawdata = []
        data = []
        V = []
        C = []
        
        with open(sensor.file, 'r') as filestream:
            for line in filestream:
                currentline = line.split(' ')
                rawdata.append(currentline)
        rawdata = rawdata[7:-1]
        for i in range(0, len(rawdata)):
            data.append(rawdata[i][0:5])
            V.append(abs(float(data[i][1])))
            C.append(abs(float(data[i][3])))
            
        tempcap = []
        tempvoltage = []
        C_avg = []
        V_plot = []
        C_plot = []
    
        #split into chucnks of length 5
        for i in range(0, int((len(C) + 1)/5)):
            tempcap.append(C[(5*i):(5*i)+5])
            tempvoltage.append(V[(5*i):(5*i)+5])
            
        #take 100kHz values only
        temptempcap = tempcap[1::3]
        temptempvoltage = tempvoltage[1::3]
        
        for i in range(0, int(len(temptempcap))):
            #averaging of 100kHz values
            C_avg.append(sum(temptempcap[i])/5)
            V_plot.append(sum(temptempvoltage[i])/5)
        
        for i in range(0, len(C_avg)):
            #1/C^2 them
            C_plot.append(1/(C_avg[i]**2))
        return V_plot, C_plot
    
    elif sensor.newdatastyle == 'labview':
        rawdata = []
        data = []
        V = []
        C = []
        
        with open(sensor.file, 'r') as filestream:
            for line in filestream:
                currentline = line.split(' ')
                rawdata.append(str(currentline))
        rawdata = rawdata[41:-1]
        #print(rawdata)
        for i in range(0, len(rawdata)):
            thing = rawdata[i].split('\\t') #splitting lines
            V.append(float(thing[0][3:]))   #V from data
            C.append(float(thing[2]))   #C from data
            
            C_plot = []
        
        for i in range(0, len(C)):
            C_plot.append(1/(C[i]**2))
            
        return V, C_plot

def colourgrabber(sensor):
    """
    if sensor.wafer == 6:
        return 'red'
    elif sensor.wafer == 11:
        return 'blue'
    """
    """
    if sensor.type == 'PiN':
        return 'orange'
    else:
        return 'red'
    """
    #these can be changed willy-nilly to distinct better on plots
    """
    if sensor.location == 1:
        return 'red'
    elif sensor.location == 2:
        return 'green'
    elif sensor.location == 3:
        return 'blue'
    elif sensor.location == 4:
        return 'orange'
    elif sensor.location == 5:
        return 'magenta'
    """
    if sensor.type == 'LGAD':
        return 'blue'
    else:
        return 'red'
    
    
def linestylegrabber(sensor):
    if sensor.type == 'LGAD':
        return 'solid'
    elif sensor.type == 'PiN':
        return 'dashed'

def CV(sensorlist, Vs):
    
    #Vs is a list of the start and end fitting values
    #Vs[0] is the steep fit
    #Vs[1] is the RHS fit
    #Vs[2] is the LHS fit (N/A for PiNs)
    
    #plt.style.use('fast')
    fig, ax = plt.subplots()
    plt.rcParams["figure.figsize"] = [12,9]
    plt.ylabel('Capacitance$^{-2}$ [F$^{-2}$]', fontsize = 22)
    plt.xlabel('Bias Voltage [V]', fontsize = 22)
    #plt.yscale('log')
    #plt.ylim(1e17, 1e24)#CHANGE THESE TO NON-LOG IF FUTTUNG
    plt.xlim(-20, 160)
    ax.minorticks_on()
    ax.grid(which='major', linestyle='-', linewidth='0.5', color='grey')
    ax.grid(which='minor', linestyle=':', linewidth='0.5', color='grey')
    plt.title('CV Characteristics', fontsize=22)
    plt.xticks(fontsize = 20)
    plt.yticks(fontsize = 20)
    
    for sensor in sensorlist:
        
        V_plot, C_plot = getdata(sensor)
        
        #optional color = colourgrabber(sensor)
        #if the sensors dice then include diced in the label
        if sensor.diced == True:
            plt.plot(V_plot, C_plot, linewidth=1.5, label = f'CV of {sensor.type} {sensor.size} on Wafer {sensor.wafer} Loc. {sensor.location} Diced', linestyle = linestylegrabber(sensor), color = colourgrabber(sensor))
        else:
            plt.plot(V_plot, C_plot, linewidth=1.5, label = f'CV of {sensor.type} {sensor.size} on Wafer {sensor.wafer} Loc. {sensor.location}', linestyle = linestylegrabber(sensor), color = colourgrabber(sensor))
        
        print(V_plot, C_plot)
        #co = np.polyfit(V_plot, C_plot, 6)
        #fit = []
        #for V in V_plot:
        #    fit.append(co[0] + co[1]*V + co[2]*V**2 + co[3]*V**3 + co[4]*V**4 + co[5]*V**5 + co[5]*V**5)
        #plt.plot(V_plot,  fit)
        plt.legend(fontsize = 22, loc = 'upper left')
        

        #fitting lines:
        if sensor.type == 'LGAD' and Vs:
            #V1idx = V_plot.index(Vs[0][0])  #indexes at which which min and max V for fitting are located
            #V2idx = V_plot.index(Vs[0][1])
            V1idx = (np.abs(np.array(V_plot) - Vs[0][0])).argmin()
            V2idx = (np.abs(np.array(V_plot) - Vs[0][1])).argmin()  #find nearest always to account for shitty old data
            
            #create fitted line parameters from selected index values
            m1, b1 = np.polyfit(V_plot[V1idx:V2idx], C_plot[V1idx:V2idx], 1)
            #trying to plot longer line:
            fittedline = []
            #-3 and plus8 essentially just elongated the fitted line on plot
            longerindexlist = np.arange(V1idx-10, V2idx+25, 1)
            
            #creating the fitted line y values
            for i in longerindexlist:
                fittedline.append(m1*V_plot[i] + b1)
            
            #these are -2 and +4 by 'default'
            plt.plot(V_plot[V1idx-10:V2idx+25], fittedline, linewidth=1, color = 'black')  
            
            #SECOND FIT:
            V1idx = (np.abs(np.array(V_plot) - Vs[1][0])).argmin()
            V2idx = (np.abs(np.array(V_plot) - Vs[1][1])).argmin()
            #create fitted line parameters from selected index values of interest
            m2, b2 = np.polyfit(V_plot[V1idx:V2idx], C_plot[V1idx:V2idx], 1)
            #trying to plot longer line:
            fittedline2 = []
            #-3 and plus8 essentially just elongated the fitted line on plot
            longerindexlist2 = np.arange(V1idx-70, V2idx+25, 1)
            
            #creating the fitted line y values
            for i in longerindexlist2:
                fittedline2.append(m2*V_plot[i] + b2)
                
            #these are -15 and +12 by 'default'
            plt.plot(V_plot[V1idx-70:V2idx+25], fittedline2, linewidth=1, color = 'black')  
            
            #finding where the two fitted lines intercept
            
            V_fulldepletion = (b2 - b1)/(m1 - m2)   #derived manually
            #plot vertical line on full depletion voltage
            plt.axvline(x = V_fulldepletion, linewidth = 1, linestyle = 'dashed', color = 'black', label = f'LGAD Full Depletion Voltage = {round(V_fulldepletion, 2)}V')
            plt.legend(loc = 'right', fontsize = 12)
            
            #THIRD FIT:
            V1idx = (np.abs(np.array(V_plot) - Vs[2][0])).argmin()
            V2idx = (np.abs(np.array(V_plot) - Vs[2][1])).argmin()
            
            #create fitted line parameters from selected index values of interest
            m3, b3 = np.polyfit(V_plot[V1idx:V2idx], C_plot[V1idx:V2idx], 1)
            #trying to plot longer line:
            fittedline3 = []
            #-3 and plus8 essentially just elongated the fitted line on plot
            longerindexlist3 = np.arange(V1idx, V2idx+150, 1)
            
            #creating the fitted line y values
            for i in longerindexlist3:
                fittedline3.append(m3*V_plot[i] + b3)
            
            #these are +0 and +20 by 'default'
            plt.plot(V_plot[V1idx:V2idx+150], fittedline3, linewidth=1, color = 'black')  
            
            #finding where the two fitted lines intercept
            
            V_intersect = (b3 - b1)/(m1 - m3)   #derived manually
            #plot vertical line on full depletion voltage
            plt.axvline(x = V_intersect, linewidth = 1, linestyle = 'dashed', color = 'black', label = f'Gain Layer Depletion Voltage = {round(V_intersect, 2)}V')
            
            plt.legend(loc = 'lower right', fontsize = 12)
            
        elif sensor.type == 'PiN' and Vs:   #== 'PiN'
            V1idx = (np.abs(np.array(V_plot) - Vs[0][0])).argmin()
            V2idx = (np.abs(np.array(V_plot) - Vs[0][1])).argmin()  #find nearest always to account for shitty old data
            
            #create fitted line parameters from selected index values
            m1, b1 = np.polyfit(V_plot[V1idx:V2idx], C_plot[V1idx:V2idx], 1)
            #trying to plot longer line:
            fittedline = []
            #-3 and plus8 essentially just elongated the fitted line on plot
            longerindexlist = np.arange(V1idx, V2idx+8, 1)
            
            #creating the fitted line y values
            for i in longerindexlist:
                fittedline.append(m1*V_plot[i] + b1)
            
            #these are +0 and +3 by 'default'
            plt.plot(V_plot[V1idx:V2idx+8], fittedline, linewidth=1, color = 'black')  
            
            #SECOND FIT:
            V1idx = (np.abs(np.array(V_plot) - Vs[1][0])).argmin()
            V2idx = (np.abs(np.array(V_plot) - Vs[1][1])).argmin()
            #create fitted line parameters from selected index values of interest
            m2, b2 = np.polyfit(V_plot[V1idx:V2idx], C_plot[V1idx:V2idx], 1)
            #trying to plot longer line:
            fittedline2 = []
            #-3 and plus8 essentially just elongated the fitted line on plot
            longerindexlist2 = np.arange(V1idx-30, V2idx+22, 1)
            
            #creating the fitted line y values
            for i in longerindexlist2:
                fittedline2.append(m2*V_plot[i] + b2)
            
            #these are -20 and +0 by 'default'
            plt.plot(V_plot[V1idx-30:V2idx+22], fittedline2, linewidth=1, color = 'black')  
            
            #finding where the two fitted lines intercept
            
            V_fulldepletion = (b2 - b1)/(m1 - m2)   #derived manually
            #plot vertical line on full depletion voltage
            plt.axvline(x = V_fulldepletion, linewidth = '1.5', linestyle = 'dashed', color = 'grey', label = f'PiN Full Depletion Voltage = {round(V_fulldepletion, 2)}V')
        
        
        plt.legend(loc = 'lower right', fontsize = 18)
        
def smooth(y, box_pts):
    box = np.ones(box_pts)/box_pts
    y_smooth = np.convolve(y, box, mode='same')
    return y_smooth      
        
def doping(sensorlist):
    
    fig, ax = plt.subplots()
    plt.rcParams["figure.figsize"] = [12,9]
    plt.ylabel('Doping Concentration [cm^-3]', fontsize = 20)   #change to cm^-3
    plt.xlabel('Depth [$\mu$m]', fontsize = 20)
    plt.yscale('log')
    plt.ylim(11e10, 10e16)
    plt.xlim(0, 50)
    ax.minorticks_on()
    ax.grid(which='major', linestyle='-', linewidth='0.5', color='grey')
    ax.grid(which='minor', linestyle=':', linewidth='0.5', color='grey')
    plt.title('Doping Profiles', fontsize=22)
    plt.xticks(fontsize = 20)
    plt.yticks(fontsize = 20)
    
    for sensor in sensorlist:
        V_plot, C_plot = getdata(sensor)
        
        
        gradient = []
        for i in range(1, len(V_plot) - 1):
            dy = C_plot[i+1] - C_plot[i-1]
            dx = V_plot[i+1] - V_plot[i-1]
            gradient.append((dy/dx))
            
            
        
        #reclaim C from 1/C^2
        C = []
        for i in range(0, len(C_plot)):
            C.append(1/(C_plot[i]**0.5))
        
        area = ((float(sensor.size[0]))*10**-3)**2  #area size in m
        q = 1.6*10**-19
        
        N = []          #dopng conc
        x = []
        x_plot = []     #mapped capacitance
        
        
        #if, by chance, there is a gradient of zero, remove it
        while 0 in gradient:
            del gradient[gradient.index(0)]
        
        for i in range(0, len(gradient)):
            N.append(((2/gradient[i])*(1/(((11.68*8.85*10**-12)*1.6*10**-19)*area**2)))*1e-6)
            x.append(11.68*8.85*10**-12*(area/C[i]))
            x_plot.append(x[i]*10**6)   #x in $\mu$m
            #use silicons epsilon_r = 11.68
            
            #max doping x:
            if x_plot[i] < 10:
                maxdopingdepthidx = np.argmax(N)
        
        #can do this to write the data to a list.txt
        """
        file = open("list.txt", "w")
        for index in range(len(x_plot)):
            file.write(str(x_plot[index]) + " " + str(N[index]) + "\n")
        file.close()
        """
            
        
        if sensor.type == 'LGAD':
            #plt.axvline(x = x_plot[maxdopingdepthidx], linewidth = 1.5, linestyle = '--', color = 'black', label = f'LGAD Peak Doping Depth: {round(x[maxdopingdepthidx]*10e5, 2)}$\mu$m')
            #plt.axhline(y = N[maxdopingdepthidx], linewidth = 1.5, linestyle = '--', color = 'black', label = f'LGAD Peak Doping Value: {"{:.2e}".format(round(N[maxdopingdepthidx], 2))}cm^-3')
            
            #plt.scatter(x_plot[maxdopingdepthidx], N[maxdopingdepthidx], marker = 'x', s = 100, color = 'green', label = f'LGAD Peak Doping Depth = {round(x[maxdopingdepthidx]*10e5, 2)}$\mu$m \nLGAD Peak Doping Value = {"{:.2e}".format(round(N[maxdopingdepthidx], 2))}cm^-3')
            
            #FIRST FIT:
            x1idx = (np.abs(np.array(x_plot) - 2.9)).argmin() #these values can be changed on a sensor-by-sensor basis
            x2idx = (np.abs(np.array(x_plot) - 4)).argmin() #these are the start and end points to the first, steeper fit
            #plt.axvline(x = x_plot[x1idx], color = 'green')
            #plt.axvline(x = x_plot[x2idx], color = 'red')
            
            #plt.axvline(x_plot[20])
            x_fitplotrange = np.arange(2, 4.5, 0.1)#just the range at which i want my fitting lines to appear
            m1, b1 = np.polyfit(x_plot[x1idx:x2idx], np.log10(N[x1idx:x2idx]), 1)
            fittedline1 = []
                
            #creating the fitted line y values
            for x in x_fitplotrange:
                fittedline1.append(10**(m1*x + b1))
            
            plt.plot(x_fitplotrange, fittedline1, linewidth=1, color = 'magenta')   #plotting the fitted y values within x_fitplotrange
            
            #SECOND FIT:
            x1idx = (np.abs(np.array(x_plot) - 10)).argmin() #fits between the closest values of x = 10 -> 30, can change depending on sensor
            x2idx = (np.abs(np.array(x_plot) - 30)).argmin() #'epi'fit
            #to help decide where to define these, the vertical lines below help
            #plt.axvline(x = x_plot[x1idx], color = 'purple')
            #plt.axvline(x = x_plot[x2idx], color = 'orange')
            
            x_fitplotrange = np.arange(2, 35, 0.1)
            m2, b2 = np.polyfit(x_plot[x1idx:x2idx], np.log10(N[x1idx:x2idx]), 1)
            fittedline2 = []
                
            #creating the fitted line y values
            for x in x_fitplotrange:
                fittedline2.append(10**(m2*x + b2))
            
            plt.plot(x_fitplotrange, fittedline2, linewidth=1, color = 'magenta')
            
            #where fits intersect? == implant depth
            x_intersect = (b2 - b1)/(m1 - m2)
            plt.scatter(x_intersect, 10**(m2*x_intersect + b2), marker = 'x', s = 100,  color = 'purple', label = f'LGAD Implant Depth = {round(x_intersect, 2)}$\mu m$')
            implantdepth = x_intersect
            
            #epidoping defined at depth = 20um. find the point at which this occurs,
            differencelist = []
            for i in x_plot:
                differencelist.append(abs(i - 20))
            
            epiidx = np.array(differencelist).argmin()  #idx of x_plot at which the depth is 20
            epidoping = N[epiidx]
            plt.scatter(x_plot[epiidx], epidoping, label = f'LGAD Epitaxial Doping Concentration = {"{:.2e}".format(round(epidoping), 2)}cm^-3', marker = 's', color = 'rebeccapurple')
            
            
            #attempt to fit the doping peak
            """
            #gaussian fit:
            #below are two ways to get idx1 and idx2, depending on how you want to do the fit
            ##################################################################
            #the first part of this is finding the indices to fit between,
            #for the gaussian fit, fit up to the mininum point of the peak
            idx1 = 0
             #cut N to first 'i' indexes below 20um as we're not messing with the tail here
            N_cut = N[:(np.abs(np.array(x_plot) - 20)).argmin()]
            
            idx2 = np.array(N_cut).argmin()
            #print(idx2)
            plt.axvline(x = x_plot[idx2], color = 'orange')
            ##################################################################
            #the first part of this is finding the indices to fit between,
            #which are the first index of x and the symmetric equivilent on the RHS of the peak
            idx1 = 0
            N_cut = N[:100]  #cut N to first 50 indexes as we're not messing with the tail here
            N_cutcut = []   #list that cuts from the max value of doping peak onwards
            for n in N_cut[np.argmax(np.array(N_cut))::]:
                N_cutcut.append(n)
            idx2 = (np.abs(np.array(N_cutcut) - N[0])).argmin()     #idx2 is closest value to in N_cutcut
            #now need to find which index this in the main N list
            idx2 = N.index(N_cutcut[idx2])
            #idx1, idx2 are now the generalised fitting region for the doping peak
            #can check the fitting region here:
            #plt.axvline(x = x_plot[idx1])
            #plt.axvline(x = x_plot[idx2])
            plt.axvline(x = x_plot[idx2], color = 'orange')
            ##################################################################
            def gauss(x, H, A, x0, sigma):
                return H + A * np.exp(-(x - x0) ** 2 / (2 * sigma ** 2))
            
            def gauss_fit(x, y):
                mean = sum(np.array(x) * np.array(y)) / sum(np.array(y))
                sigma = np.sqrt(sum(y * (x - mean) ** 2) / sum(y))
                popt, pcov = curve_fit(gauss, x, y, p0=[min(y), max(y), mean, sigma])
                return popt
            #print(N[idx1:idx2])
            H, A, x0, sigma = gauss_fit(x_plot[idx1:idx2], N[idx1:idx2])
            #print(x0)
            x_fitplotrange = np.arange(x_plot[idx1], x_plot[idx2], 0.01)
            x_fitplotrange = x_plot[idx1:idx2]
            plt.plot(x_fitplotrange, gauss(x_fitplotrange, H, A, x0, sigma), color = 'purple')
            plt.scatter(x0, max(gauss(x_fitplotrange, H, A, x0, sigma)), marker = 'x', color = 'orange', s = 100, label = f'Fitted Peak Doping Depth {round(x0, 2)}$\mu$m \nFitted Peak Doping Value {"{:.2e}".format(round(H + A), 2)}cm^-3')
            
            #print(gauss(x_plot[idx1:idx2], H, A, x0, sigma))
            #chi squared of this fit
            chisum = 0
            for i in range(0, len(x_plot[idx1:idx2])):
                print(chisum)
                print(N[i])
                print(gauss(x_plot[idx1:idx2], H, A, x0, sigma)[i])
                chisum += ((N[i] - gauss(x_plot[idx1:idx2], H, A, x0, sigma)[i])**2)/((gauss(x_plot[idx1:idx2], H, A, x0, sigma)[i]))
            print(chisum/(idx2-idx1))
            #2nd order polynomial fit~
            """
            
            
            #the first part of this is finding the indices to fit between,
            #which are the first index of x and the symmetric equivilent on the RHS of the peak
            idx1 = 0
            N_cut = N[:50]  #cut N to first 50 indexes as we're not messing with the tail here
            N_cutcut = []   #list that cuts from the max value of doping peak onwards
            for n in N_cut[np.argmax(np.array(N_cut))::]:
                N_cutcut.append(n)
            idx2 = (np.abs(np.array(N_cutcut) - N[0])).argmin()     #idx2 is closest value to in N_cutcut
            #now need to find which index this in the main N list
            idx2 = N.index(N_cutcut[idx2])
            #idx1, idx2 are now the generalised fitting region for the doping peak
            #can check the fitting region here:
            #plt.axvline(x = x_plot[idx1])
            #plt.axvline(x = x_plot[idx2])
            
            peakfit = []
            a, b, c = np.polyfit(x_plot[idx1:idx2], np.log10(N[idx1:idx2]), 2)
            #ax^2 + b^x + c fit
            
            #x_fitplotrange = np.arange(x_plot[idx1]-0.5, x_plot[idx2]+0.5, 0.01)   #range of fit plot
            x_fitplotrange = x_plot[idx1:idx2]  #choose if want the fit to be smooth or on x_plot point
            for x in x_fitplotrange:
                peakfit.append(10**(a*x**2 + b*x + c))
            plt.plot(x_fitplotrange, peakfit, linewidth=1, color = 'purple')
            
            
            #now find depth and peak value of this fitted peak (done in-line of plotting)
            plt.scatter(x_fitplotrange[np.array(peakfit).argmax()], max(peakfit), marker = 'x', color = 'orange', s = 100, label = f'Fitted LGAD Peak Doping Value = {"{:.2e}".format(round(max(peakfit)), 2)}cm^-3 \nFitted LGAD Peak Doping Depth = {round(x_fitplotrange[np.array(peakfit).argmax()], 2)}')
            
            #chi squared of this fit
            chisum = 0
            for i in range(0, idx2):
                chisum += ((N[i] - peakfit[i])**2)/(peakfit[i])
            #chisum is correct
            #print(stats.chisquare(N[idx1:idx2], peakfit))
            
            #now try and integrate this peak (not the fit)
            idx1 = 0
            #cut N to first 'i' indexes below 20um as we're not messing with the tail here
            #want idx2 to be the implant depth
            N_cut = N[:(np.abs(np.array(x_plot) - 20)).argmin()]
            idx2 = np.array(N_cut).argmin() #seconf index is mininum point of plot
            idx2 = (np.abs(np.array(x_plot) - implantdepth)).argmin()
            
            #plt.axvline(x = x_plot[idx1])
            #plt.axvline(x = x_plot[idx2])
            integral = integrate.simpson(N[idx1:idx2], x = x_plot[idx1:idx2], dx = 0.01)
            
            plt.fill_between(x_plot[idx1:idx2+1], 0, N[idx1:idx2+1], color = 'grey', alpha = 0.2, label = f'Total Dopants in Gain Layer {"{:.2e}".format(round(integral), 2)}')
            
            #print(f'{sensor.type}{sensor.size}{sensor.location}_{sensor.wafer}, {"{:.2e}".format(round(integral), 2)}')
            
        elif sensor.type == 'PiN':
            differencelist = []
            for i in x_plot:
                differencelist.append(abs(i - 20))
            
            epiidx = np.array(differencelist).argmin()  #idx of x_plot at which the depth is 20
            epidoping = N[epiidx]
            plt.scatter(x_plot[epiidx], epidoping, label = f'PiN Epitaxial Doping Concentration = {"{:.2e}".format(round(epidoping), 2)}cm^-3', marker = 's', color = 'rebeccapurple')
        
        #actual plot of doping conc line
        plt.plot(x_plot, N, linewidth = 1.5, color = colourgrabber(sensor), label = f'Doping Profile of {sensor.type} {sensor.size} on Wafer {sensor.wafer} Location {sensor.location}', linestyle = linestylegrabber(sensor))
        
        plt.legend(fontsize = 16.5, loc = 'upper center')
        #plt.savefig(f'{sensor.type}{sensor.size}{sensor.location}_{sensor.wafer}_fits')
    

def depcompare(sensorsize):
    """
    Depletion comparison
    """
    #WAFER COMPARISON
    if sensorsize == '4mm':
        fig, ax = plt.subplots()
        plt.rcParams["figure.figsize"] = [12,9]
        plt.ylabel('Bias Voltage [V]', fontsize = 18)
        plt.xlabel('Wafer', fontsize = 18)
        #plt.yscale('log')
        #plt.xlim(0, 800)
        plt.ylim(0, 50)
        ax.minorticks_on()
        ax.grid(which='major', linestyle='-', linewidth='0.5', color='grey')
        ax.grid(which='minor', linestyle=':', linewidth='0.5', color='grey')
        plt.title('4mm Sensor Depletion Voltages', fontsize=18)
        plt.xticks(fontsize = 16)
        plt.yticks(fontsize = 16)
        
        plt.plot(['wafer 6', 'wafer 11', 'wafer 16', 'wafer 20', 'wafer 3'], [23.56, 24.49, 18.94, 19.86, 29.04], label = 'LGAD Loc. 1 GLD', color = 'green', marker = 'x')
        plt.plot(['wafer 6', 'wafer 11', 'wafer 16', 'wafer 20', 'wafer 3'], [32.55, 32.38, 26.89, 27.78, 38.7], label = 'LGAD Loc. 1 FD', color = 'red', marker = 'x')
        plt.plot(['wafer 6', 'wafer 11', 'wafer 16', 'wafer 20', 'wafer 3'], [23.85, 24.51, 19.49, 20.26, 28.92], label = 'LGAD Loc. 3 GLD', color = 'orange', marker = 'x')
        plt.plot(['wafer 6', 'wafer 11', 'wafer 16', 'wafer 20', 'wafer 3'], [32.9, 32.6, 27.79, 27.63, 37.68], label = 'LGAD Loc. 3 FD', color = 'grey', marker = 'x')
        plt.plot(['wafer 6', 'wafer 11', 'wafer 16', 'wafer 20', 'wafer 3'], [23.96, 24.35, 19.16, 20.09, 28.96], label = 'LGAD Loc. 5 GLD', color = 'magenta', marker = 'x')
        plt.plot(['wafer 6', 'wafer 11', 'wafer 16', 'wafer 20', 'wafer 3'], [32.92, 32.34, 28.01, 27.51, 38.98], label = 'LGAD Loc. 5 FD', color = 'purple', marker = 'x')
        
        plt.plot(['wafer 6', 'wafer 11', 'wafer 16', 'wafer 20', 'wafer 3'], [9.06, 7.11, 7.49, 7.83, 8.49], label = 'PiN Loc. 1 FD', color = 'green', marker = 'x', linestyle = '--')
        plt.legend(fontsize = 16)
    
        #DOSE COMPARISON
        #ACROSS ALL WAFERS
        
        fig, ax = plt.subplots()
        plt.rcParams["figure.figsize"] = [12,9]
        plt.ylabel('Bias Voltage [V]', fontsize = 18)
        plt.xlabel('Normalised Dose', fontsize = 18)
        #plt.yscale('log')
        #plt.xlim(0, 800)
        plt.ylim(0, 50)
        ax.minorticks_on()
        ax.grid(which='major', linestyle='-', linewidth='0.5', color='grey')
        ax.grid(which='minor', linestyle=':', linewidth='0.5', color='grey')
        plt.title('4mm Sensor Depletion Voltages', fontsize=18)
        plt.xticks([0.92, 1.00, 1.00, 1.07, 1.07], fontsize = 16)
        plt.yticks(fontsize = 16)
        #ax.set_xticks
        
        def doseswapper(waferlist):
            """
            takes in the list of vales in the wafer order: 6, 11, 16, 20, 3
            and returns a list of them in normalised dose order
            """
            mylist = []
            mylist.append(waferlist[2])
            mylist.append(waferlist[3])
            mylist.append(waferlist[0])
            mylist.append(waferlist[1])
            mylist.append(waferlist[4])
            return mylist
        
        plt.plot([0.92, 1.00, 1.00, 1.07, 1.07], doseswapper([23.56, 24.49, 18.94, 19.86, 29.04]), label = 'LGAD Loc. 1 GLD', color = 'green', marker = 'x')
        plt.plot([0.92, 1.00, 1.00, 1.07, 1.07], doseswapper([32.55, 32.38, 26.89, 27.78, 38.7]), label = 'LGAD Loc. 1 FD', color = 'red', marker = 'x')
        plt.plot([0.92, 1.00, 1.00, 1.07, 1.07], doseswapper([23.85, 24.51, 19.49, 20.26, 28.92]), label = 'LGAD Loc. 3 GLD', color = 'orange', marker = 'x')
        plt.plot([0.92, 1.00, 1.00, 1.07, 1.07], doseswapper([32.9, 32.6, 27.79, 27.63, 37.68]), label = 'LGAD Loc. 3 FD', color = 'grey', marker = 'x')
        plt.plot([0.92, 1.00, 1.00, 1.07, 1.07], doseswapper([23.96, 24.35, 19.16, 20.09, 28.96]), label = 'LGAD Loc. 5 GLD', color = 'magenta', marker = 'x')
        plt.plot([0.92, 1.00, 1.00, 1.07, 1.07], doseswapper([32.92, 32.34, 28.01, 27.51, 38.98]), label = 'LGAD Loc. 5 FD', color = 'purple', marker = 'x')
        
        plt.plot([0.92, 1.00, 1.00, 1.07, 1.07], doseswapper([9.06, 7.11, 7.49, 7.83, 8.49]), label = 'PiN Loc. 1 FD', color = 'green', marker = 'x', linestyle = '--')
        plt.legend(fontsize = 16)
        
        #ENERGY COMPARISON
        
        fig, ax = plt.subplots()
        plt.rcParams["figure.figsize"] = [12,9]
        plt.ylabel('Bias Voltage [V]', fontsize = 18)
        plt.xlabel('Normalised Energy', fontsize = 18)
        #plt.yscale('log')
        #plt.xlim(0, 800)
        plt.ylim(0, 50)
        ax.minorticks_on()
        ax.grid(which='major', linestyle='-', linewidth='0.5', color='grey')
        ax.grid(which='minor', linestyle=':', linewidth='0.5', color='grey')
        plt.title('4mm Sensor Depletion Voltages', fontsize=18)
        plt.xticks([1.00, 1.05, 1.05, 1.11, 1.11], fontsize = 16)
        plt.yticks(fontsize = 16)
        #ax.set_xticks
        
        def energyswapper(waferlist):
            """
            takes in the list of vales in the wafer order: 6, 11, 16, 20, 3
            and returns a list of them in normalised dose order
            """
            mylist = []
            mylist.append(waferlist[3])
            mylist.append(waferlist[2])
            mylist.append(waferlist[1])
            mylist.append(waferlist[0])
            mylist.append(waferlist[4])
            return mylist
        
        plt.plot([1.00, 1.05, 1.05, 1.11, 1.11], energyswapper([23.56, 24.49, 18.94, 19.86, 29.04]), label = 'LGAD Loc. 1 GLD', color = 'green', marker = 'x')
        plt.plot([1.00, 1.05, 1.05, 1.11, 1.11], energyswapper([32.55, 32.38, 26.89, 27.78, 38.7]), label = 'LGAD Loc. 1 FD', color = 'red', marker = 'x')
        plt.plot([1.00, 1.05, 1.05, 1.11, 1.11], energyswapper([23.85, 24.51, 19.49, 20.26, 28.92]), label = 'LGAD Loc. 3 GLD', color = 'orange', marker = 'x')
        plt.plot([1.00, 1.05, 1.05, 1.11, 1.11], energyswapper([32.9, 32.6, 27.79, 27.63, 37.68]), label = 'LGAD Loc. 3 FD', color = 'grey', marker = 'x')
        plt.plot([1.00, 1.05, 1.05, 1.11, 1.11], energyswapper([23.96, 24.35, 19.16, 20.09, 28.96]), label = 'LGAD Loc. 5 GLD', color = 'magenta', marker = 'x')
        plt.plot([1.00, 1.05, 1.05, 1.11, 1.11], energyswapper([32.92, 32.34, 28.01, 27.51, 38.98]), label = 'LGAD Loc. 5 FD', color = 'purple', marker = 'x')
        
        plt.plot([1.00, 1.05, 1.05, 1.11, 1.11], energyswapper([9.06, 7.11, 7.49, 7.83, 8.49]), label = 'PiN Loc. 1 FD', color = 'green', marker = 'x', linestyle = '--')
        plt.legend(fontsize = 16)
        
        
        #okay, now want to compare across wafers that have a constant between them
        
        #first, wafer 16/11 that both have E=1.05 and dose = 0.92/1.07
        fig, ax = plt.subplots()
        plt.rcParams["figure.figsize"] = [12,9]
        plt.ylabel('Bias Voltage [V]', fontsize = 18)
        plt.xlabel('Normalised Dose', fontsize = 18)
        #plt.yscale('log')
        plt.xlim(0.89, 1.14)
        plt.ylim(0, 50)
        ax.minorticks_on()
        ax.grid(which='major', linestyle='-', linewidth='0.5', color='grey')
        ax.grid(which='minor', linestyle=':', linewidth='0.5', color='grey')
        plt.title('4mm Sensor Depletion Voltages', fontsize=18)
        plt.xticks([0.92, 1.07], fontsize = 16)
        plt.yticks(fontsize = 16)
        plt.text(0.97, 41, 'Normalised Implant Energy = 1.05', fontsize = 18)
        plt.text(1.072, 32, 'LGAD Full Depletion', fontsize = 16)
        plt.text(1.072, 23, 'LGAD Gain Layer \nDepletion', fontsize = 16)
        plt.text(1.072, 8.5, 'PiN Full Depletion', fontsize = 16)
        
        plt.plot([0.92, 1.07], [18.94, 24.49], label = 'LGAD Loc. 1 GLD', color = 'green', marker = 'x')
        plt.plot([0.92, 1.07], [26.89, 32.38], label = 'LGAD Loc. 1 FD', color = 'red', marker = 'x')
        plt.plot([0.92, 1.07], [19.49, 24.51], label = 'LGAD Loc. 3 GLD', color = 'orange', marker = 'x')
        plt.plot([0.92, 1.07], [27.79, 32.60], label = 'LGAD Loc. 3 FD', color = 'grey', marker = 'x')
        plt.plot([0.92, 1.07], [19.16, 24.34], label = 'LGAD Loc. 5 GLD', color = 'magenta', marker = 'x')
        plt.plot([0.92, 1.07], [28.01, 32.34], label = 'LGAD Loc. 5 FD', color = 'purple', marker = 'x')
        
        plt.plot([0.92, 1.07], [7.49, 9.06], label = 'PiN Loc. 1 FD', color = 'green', marker = 'x', linestyle = '--')
        plt.legend(fontsize = 16)
        
        #secondly, wafer 6/3 that both have E=1.11 and dose = 1.00, 1.07
        fig, ax = plt.subplots()
        plt.rcParams["figure.figsize"] = [12,9]
        plt.ylabel('Bias Voltage [V]', fontsize = 18)
        plt.xlabel('Normalised Dose', fontsize = 18)
        #plt.yscale('log')
        plt.xlim(0.98, 1.1)
        plt.ylim(0, 50)
        ax.minorticks_on()
        ax.grid(which='major', linestyle='-', linewidth='0.5', color='grey')
        ax.grid(which='minor', linestyle=':', linewidth='0.5', color='grey')
        plt.title('4mm Sensor Depletion Voltages', fontsize=18)
        plt.xticks([1.00, 1.07], fontsize = 16)
        plt.yticks(fontsize = 16)
        plt.text(1.03, 44, 'Normalised Implant Energy = 1.11', fontsize = 18)
        plt.text(1.071, 38, 'LGAD Full Depletion', fontsize = 16)
        plt.text(1.071, 27, 'LGAD Gain Layer \nDepletion', fontsize = 16)
        plt.text(1.071, 8, 'PiN Full Depletion', fontsize = 16)
        
        plt.plot([1.00, 1.07], [23.56, 29.04], label = 'LGAD Loc. 1 GLD', color = 'green', marker = 'x')
        plt.plot([1.00, 1.07], [32.55, 38.70], label = 'LGAD Loc. 1 FD', color = 'red', marker = 'x')
        plt.plot([1.00, 1.07], [23.85, 28.92], label = 'LGAD Loc. 3 GLD', color = 'orange', marker = 'x')
        plt.plot([1.00, 1.07], [32.90, 37.68], label = 'LGAD Loc. 3 FD', color = 'grey', marker = 'x')
        plt.plot([1.00, 1.07], [23.96, 28.96], label = 'LGAD Loc. 5 GLD', color = 'magenta', marker = 'x')
        plt.plot([1.00, 1.07], [32.92, 38.98], label = 'LGAD Loc. 5 FD', color = 'purple', marker = 'x')
        
        plt.plot([1.00, 1.07], [9.06, 8.49], label = 'PiN Loc. 1 FD', color = 'green', marker = 'x', linestyle = '--')
        plt.legend(fontsize = 16, loc = 'upper left')
        
        #finally, wafer 20/6 that both have dose = 1.00 and E = 1.00/1.11
        fig, ax = plt.subplots()
        plt.rcParams["figure.figsize"] = [12,9]
        plt.ylabel('Bias Voltage [V]', fontsize = 18)
        plt.xlabel('Normalised Energy', fontsize = 18)
        #plt.yscale('log')
        plt.xlim(0.98, 1.155)
        plt.ylim(0, 50)
        ax.minorticks_on()
        ax.grid(which='major', linestyle='-', linewidth='0.5', color='grey')
        ax.grid(which='minor', linestyle=':', linewidth='0.5', color='grey')
        plt.title('4mm Sensor Depletion Voltages', fontsize=18)
        plt.xticks([1.00, 1.11], fontsize = 16)
        plt.yticks(fontsize = 16)
        plt.text(1.06, 42, 'Normalised Implant Dose = 1.00', fontsize = 18)
        plt.text(1.112, 32, 'LGAD Full Depletion', fontsize = 16)
        plt.text(1.112, 22.5, 'LGAD Gain Layer \nDepletion', fontsize = 16)
        plt.text(1.112, 8.5, 'PiN Full Depletion', fontsize = 16)
        
        plt.plot([1.00, 1.11], [19.86, 23.56], label = 'LGAD Loc. 1 GLD', color = 'green', marker = 'x')
        plt.plot([1.00, 1.11], [27.78, 32.55], label = 'LGAD Loc. 1 FD', color = 'red', marker = 'x')
        plt.plot([1.00, 1.11], [20.26, 23.85], label = 'LGAD Loc. 3 GLD', color = 'orange', marker = 'x')
        plt.plot([1.00, 1.11], [27.63, 32.90], label = 'LGAD Loc. 3 FD', color = 'grey', marker = 'x')
        plt.plot([1.00, 1.11], [20.09, 23.96], label = 'LGAD Loc. 5 GLD', color = 'magenta', marker = 'x')
        plt.plot([1.00, 1.11], [27.51, 32.92], label = 'LGAD Loc. 5 FD', color = 'purple', marker = 'x')
        
        plt.plot([1.00, 1.11], [7.83, 9.06], label = 'PiN Loc. 1 FD', color = 'green', marker = 'x', linestyle = '--')
        plt.legend(fontsize = 16, loc = 'upper left')
        
        #now i've put the dictionary in, we can plot absolutely everything against against wafer dose/energy
        
        #second finally, wafer 11/3 that both have dose = 1.07 and E = 1.05/1.11
        fig, ax = plt.subplots()
        plt.rcParams["figure.figsize"] = [12,9]
        plt.ylabel('Bias Voltage [V]', fontsize = 22)
        plt.xlabel('Normalised Energy', fontsize = 22)
        #plt.yscale('log')
        plt.xlim(1.02, 1.14)
        plt.ylim(0, 50)
        ax.minorticks_on()
        ax.grid(which='major', linestyle='-', linewidth='0.5', color='grey')
        ax.grid(which='minor', linestyle=':', linewidth='0.5', color='grey')
        plt.title('4mm Sensor Depletion Voltages', fontsize=22)
        plt.xticks([1.05, 1.11], fontsize = 20)
        plt.yticks(fontsize = 20)
        plt.text(1.06, 45, 'Normalised Implant Dose = 1.07', fontsize = 22)
        plt.text(1.111, 37.5, 'LGAD Full Depletion', fontsize = 16)
        plt.text(1.112, 28, 'LGAD Gain Layer \nDepletion', fontsize = 16)
        plt.text(1.112, 7.5, 'PiN Full Depletion', fontsize = 16)
        plt.text(1.05, 0.4, 'Wafer 11', fontsize = 20, horizontalalignment='center')
        plt.text(1.11, 0.4, 'Wafer 3', fontsize = 20, horizontalalignment='center')
        
        plt.plot([1.05, 1.11], [LGAD4mm1_11_dic['GLD'], LGAD4mm1_3_dic['GLD']], label = 'LGAD Loc. 1', color = 'green', marker = 'x')
        plt.plot([1.05, 1.11], [LGAD4mm1_11_dic['FD'], LGAD4mm1_3_dic['FD']], label = 'LGAD Loc. 1', color = 'red', marker = 'x')
        plt.plot([1.05, 1.11], [LGAD4mm3_11_dic['GLD'], LGAD4mm3_3_dic['GLD']], label = 'LGAD Loc. 3', color = 'orange', marker = 'x')
        plt.plot([1.05, 1.11], [LGAD4mm3_11_dic['FD'], LGAD4mm3_3_dic['FD']], label = 'LGAD Loc. 3', color = 'grey', marker = 'x')
        plt.plot([1.05, 1.11], [LGAD4mm5_11_dic['GLD'], LGAD4mm5_3_dic['GLD']], label = 'LGAD Loc. 5', color = 'magenta', marker = 'x')
        plt.plot([1.05, 1.11], [LGAD4mm5_11_dic['FD'], LGAD4mm5_3_dic['FD']], label = 'LGAD Loc. 5', color = 'purple', marker = 'x')
        
        plt.plot([1.05, 1.11], [PiN4mm1_11_dic['FD'], PiN4mm1_3_dic['FD']], label = 'PiN Loc. 1', color = 'green', marker = 'x', linestyle = '--')
        plt.legend(fontsize = 16, loc = 'upper left')
        
    elif sensorsize == '1mm':
        fig, ax = plt.subplots()
        plt.rcParams["figure.figsize"] = [12,9]
        plt.ylabel('Bias Voltage [V]', fontsize = 18)
        plt.xlabel('Wafer', fontsize = 18)
        #plt.yscale('log')
        #plt.xlim(0, 800)
        plt.ylim(0, 50)
        ax.minorticks_on()
        ax.grid(which='major', linestyle='-', linewidth='0.5', color='grey')
        ax.grid(which='minor', linestyle=':', linewidth='0.5', color='grey')
        plt.title('1mm Sensor Depletion Voltages', fontsize=18)
        plt.xticks(fontsize = 16)
        plt.yticks(fontsize = 16)
        
        plt.plot(['wafer 6', 'wafer 11', 'wafer 16', 'wafer 20', 'wafer 3'], [23.44, 23.7, 18.23, 19.44, 28.14], label = 'LGAD Loc. 1 GLD', color = 'green', marker = 'x')
        plt.plot(['wafer 6', 'wafer 11', 'wafer 16', 'wafer 20', 'wafer 3'], [31.9, 31.64, 26.36, 27.19, 37.57], label = 'LGAD Loc. 1 FD', color = 'red', marker = 'x')
        plt.plot(['wafer 6', 'wafer 11', 'wafer 16', 'wafer 20', 'wafer 3'], [24.28, 24.47, 19.53, 20.28, 28.84], label = 'LGAD Loc. 3 GLD', color = 'orange', marker = 'x')
        plt.plot(['wafer 6', 'wafer 11', 'wafer 16', 'wafer 20', 'wafer 3'], [32.27, 32.11, 26.89, 28.27, 37.39], label = 'LGAD Loc. 3 FD', color = 'grey', marker = 'x')
        plt.plot(['wafer 6', 'wafer 11', 'wafer 16', 'wafer 20', 'wafer 3'], [24.04, 24.54, 19.6, 19.86, 28.54], label = 'LGAD Loc. 5 GLD', color = 'magenta', marker = 'x')
        plt.plot(['wafer 6', 'wafer 11', 'wafer 16', 'wafer 20', 'wafer 3'], [31.97, 31.39, 26.94, 28.02, 37.59], label = 'LGAD Loc. 5 FD', color = 'purple', marker = 'x')
        
        plt.plot(['wafer 6', 'wafer 11', 'wafer 16', 'wafer 20', 'wafer 3'], [9.49, 8.12, 7.51, 7.75, 8.03], label = 'PiN Loc. 1 FD', color = 'green', marker = 'x', linestyle = '--')
        plt.legend(fontsize = 16)
        
        #DOSE COMPARISON
        
        fig, ax = plt.subplots()
        plt.rcParams["figure.figsize"] = [12,9]
        plt.ylabel('Bias Voltage [V]', fontsize = 18)
        plt.xlabel('Normalised Dose', fontsize = 18)
        #plt.yscale('log')
        #plt.xlim(0, 800)
        plt.ylim(0, 50)
        ax.minorticks_on()
        ax.grid(which='major', linestyle='-', linewidth='0.5', color='grey')
        ax.grid(which='minor', linestyle=':', linewidth='0.5', color='grey')
        plt.title('1mm Sensor Depletion Voltages', fontsize=18)
        plt.xticks([0.92, 1.00, 1.00, 1.07, 1.07], fontsize = 16)
        plt.yticks(fontsize = 16)
        #ax.set_xticks
        
        def doseswapper(waferlist):
            """
            takes in the list of vales in the wafer order: 6, 11, 16, 20, 3
            and returns a list of them in normalised dose order
            """
            mylist = []
            mylist.append(waferlist[2])
            mylist.append(waferlist[3])
            mylist.append(waferlist[0])
            mylist.append(waferlist[1])
            mylist.append(waferlist[4])
            return mylist
        
        plt.plot([0.92, 1.00, 1.00, 1.07, 1.07], doseswapper([23.44, 23.7, 18.23, 19.44, 28.14]), label = 'LGAD Loc. 1 GLD', color = 'green', marker = 'x')
        plt.plot([0.92, 1.00, 1.00, 1.07, 1.07], doseswapper([31.9, 31.64, 26.36, 27.19, 37.57]), label = 'LGAD Loc. 1 FD', color = 'red', marker = 'x')
        plt.plot([0.92, 1.00, 1.00, 1.07, 1.07], doseswapper([24.28, 24.47, 19.53, 20.28, 28.84]), label = 'LGAD Loc. 3 GLD', color = 'orange', marker = 'x')
        plt.plot([0.92, 1.00, 1.00, 1.07, 1.07], doseswapper([32.27, 32.11, 26.89, 28.27, 37.39]), label = 'LGAD Loc. 3 FD', color = 'grey', marker = 'x')
        plt.plot([0.92, 1.00, 1.00, 1.07, 1.07], doseswapper([24.04, 24.54, 19.6, 19.86, 28.54]), label = 'LGAD Loc. 5 GLD', color = 'magenta', marker = 'x')
        plt.plot([0.92, 1.00, 1.00, 1.07, 1.07], doseswapper([31.97, 31.39, 26.94, 28.02, 37.59]), label = 'LGAD Loc. 5 FD', color = 'purple', marker = 'x')
        
        plt.plot([0.92, 1.00, 1.00, 1.07, 1.07], doseswapper([9.49, 8.12, 7.51, 7.75, 8.03]), label = 'PiN Loc. 1 FD', color = 'green', marker = 'x', linestyle = '--')
        plt.legend(fontsize = 16)
        
        #ENERGY COMPARISON
        
        fig, ax = plt.subplots()
        plt.rcParams["figure.figsize"] = [12,9]
        plt.ylabel('Bias Voltage [V]', fontsize = 18)
        plt.xlabel('Normalised Energy', fontsize = 18)
        #plt.yscale('log')
        #plt.xlim(0, 800)
        plt.ylim(0, 50)
        ax.minorticks_on()
        ax.grid(which='major', linestyle='-', linewidth='0.5', color='grey')
        ax.grid(which='minor', linestyle=':', linewidth='0.5', color='grey')
        plt.title('1mm Sensor Depletion Voltages', fontsize=18)
        plt.xticks([1.00, 1.05, 1.05, 1.11, 1.11], fontsize = 16)
        plt.yticks(fontsize = 16)
        #ax.set_xticks
        
        def energyswapper(waferlist):
            """
            takes in the list of vales in the wafer order: 6, 11, 16, 20, 3
            and returns a list of them in normalised dose order
            """
            mylist = []
            mylist.append(waferlist[3])
            mylist.append(waferlist[2])
            mylist.append(waferlist[1])
            mylist.append(waferlist[0])
            mylist.append(waferlist[4])
            return mylist
        
        plt.plot([1.00, 1.05, 1.05, 1.11, 1.11], energyswapper([23.44, 23.7, 18.23, 19.44, 28.14]), label = 'LGAD Loc. 1 GLD', color = 'green', marker = 'x')
        plt.plot([1.00, 1.05, 1.05, 1.11, 1.11], energyswapper([31.9, 31.64, 26.36, 27.19, 37.57]), label = 'LGAD Loc. 1 FD', color = 'red', marker = 'x')
        plt.plot([1.00, 1.05, 1.05, 1.11, 1.11], energyswapper([24.28, 24.47, 19.53, 20.28, 28.84]), label = 'LGAD Loc. 3 GLD', color = 'orange', marker = 'x')
        plt.plot([1.00, 1.05, 1.05, 1.11, 1.11], energyswapper([32.27, 32.11, 26.89, 28.27, 37.39]), label = 'LGAD Loc. 3 FD', color = 'grey', marker = 'x')
        plt.plot([1.00, 1.05, 1.05, 1.11, 1.11], energyswapper([24.04, 24.54, 19.6, 19.86, 28.54]), label = 'LGAD Loc. 5 GLD', color = 'magenta', marker = 'x')
        plt.plot([1.00, 1.05, 1.05, 1.11, 1.11], energyswapper([31.97, 31.39, 26.94, 28.02, 37.59]), label = 'LGAD Loc. 5 FD', color = 'purple', marker = 'x')
        
        plt.plot([1.00, 1.05, 1.05, 1.11, 1.11], energyswapper([9.49, 8.12, 7.51, 7.75, 8.03]), label = 'PiN Loc. 1 FD', color = 'green', marker = 'x', linestyle = '--')
        plt.legend(fontsize = 16)
        
        #okay, now want to compare across wafers that have a constant between them
        
        #first, wafer 16/11 that both have E=1.05 and dose = 0.92/1.07
        fig, ax = plt.subplots()
        plt.rcParams["figure.figsize"] = [12,9]
        plt.ylabel('Bias Voltage [V]', fontsize = 18)
        plt.xlabel('Normalised Dose', fontsize = 18)
        #plt.yscale('log')
        plt.xlim(0.89, 1.14)
        plt.ylim(0, 50)
        ax.minorticks_on()
        ax.grid(which='major', linestyle='-', linewidth='0.5', color='grey')
        ax.grid(which='minor', linestyle=':', linewidth='0.5', color='grey')
        plt.title('1mm Sensor Depletion Voltages', fontsize=18)
        plt.xticks([0.92, 1.07], fontsize = 16)
        plt.yticks(fontsize = 16)
        plt.text(0.97, 41, 'Normalised Implant Energy = 1.05', fontsize = 18)
        plt.text(1.072, 31, 'LGAD Full Depletion', fontsize = 16)
        plt.text(1.072, 23, 'LGAD Gain Layer \nDepletion', fontsize = 16)
        plt.text(1.072, 7.5, 'PiN Full Depletion', fontsize = 16)
        
        plt.plot([0.92, 1.07], [18.23, 23.70], label = 'LGAD Loc. 1 GLD', color = 'green', marker = 'x')
        plt.plot([0.92, 1.07], [26.36, 31.64], label = 'LGAD Loc. 1 FD', color = 'red', marker = 'x')
        plt.plot([0.92, 1.07], [19.53, 24.47], label = 'LGAD Loc. 3 GLD', color = 'orange', marker = 'x')
        plt.plot([0.92, 1.07], [26.89, 32.11], label = 'LGAD Loc. 3 FD', color = 'grey', marker = 'x')
        plt.plot([0.92, 1.07], [19.60, 24.54], label = 'LGAD Loc. 5 GLD', color = 'magenta', marker = 'x')
        plt.plot([0.92, 1.07], [26.94, 31.39], label = 'LGAD Loc. 5 FD', color = 'purple', marker = 'x')
        
        plt.plot([0.92, 1.07], [7.51, 8.12], label = 'PiN Loc. 1 FD', color = 'green', marker = 'x', linestyle = '--')
        plt.legend(fontsize = 16, loc = 'upper left')
        
        #secondly, wafer 6/3 that both have E=1.11 and dose = 1.00, 1.07
        fig, ax = plt.subplots()
        plt.rcParams["figure.figsize"] = [12,9]
        plt.ylabel('Bias Voltage [V]', fontsize = 22)
        plt.xlabel('Normalised Dose', fontsize = 22)
        #plt.yscale('log')
        plt.xlim(0.98, 1.1)
        plt.ylim(0, 50)
        ax.minorticks_on()
        ax.grid(which='major', linestyle='-', linewidth='0.5', color='grey')
        ax.grid(which='minor', linestyle=':', linewidth='0.5', color='grey')
        plt.title('1mm Sensor Depletion Voltages', fontsize=22)
        plt.xticks([1.00, 1.07], fontsize = 20)
        plt.yticks(fontsize = 20)
        plt.text(1.02, 44, 'Normalised Implant Energy = 1.11', fontsize = 22)
        plt.text(1.071, 37, 'LGAD Full Depletion', fontsize = 16)
        plt.text(1.071, 27, 'LGAD Gain Layer \nDepletion', fontsize = 16)
        plt.text(1.071, 7.5, 'PiN Full Depletion', fontsize = 16)
        plt.text(1, 0.4, 'Wafer 6', fontsize = 20, horizontalalignment='center')
        plt.text(1.07, 0.4, 'Wafer 3', fontsize = 20, horizontalalignment='center')
        
        plt.plot([1.00, 1.07], [23.44, 28.14], label = 'LGAD Loc. 1 GLD', color = 'green', marker = 'x')
        plt.plot([1.00, 1.07], [31.90, 37.57], label = 'LGAD Loc. 1 FD', color = 'red', marker = 'x')
        plt.plot([1.00, 1.07], [24.28, 28.84], label = 'LGAD Loc. 3 GLD', color = 'orange', marker = 'x')
        plt.plot([1.00, 1.07], [32.27, 37.39], label = 'LGAD Loc. 3 FD', color = 'grey', marker = 'x')
        plt.plot([1.00, 1.07], [24.04, 28.54], label = 'LGAD Loc. 5 GLD', color = 'magenta', marker = 'x')
        plt.plot([1.00, 1.07], [31.49, 37.59], label = 'LGAD Loc. 5 FD', color = 'purple', marker = 'x')
        
        plt.plot([1.00, 1.07], [9.49, 8.03], label = 'PiN Loc. 1 FD', color = 'green', marker = 'x', linestyle = '--')
        plt.legend(fontsize = 16, loc = 'upper left')
        
        #finally, wafer 20/6 that both have dose = 1.00 and E = 1.00/1.11
        fig, ax = plt.subplots()
        plt.rcParams["figure.figsize"] = [12,9]
        plt.ylabel('Bias Voltage [V]', fontsize = 18)
        plt.xlabel('Normalised Energy', fontsize = 18)
        #plt.yscale('log')
        plt.xlim(0.98, 1.155)
        plt.ylim(0, 50)
        ax.minorticks_on()
        ax.grid(which='major', linestyle='-', linewidth='0.5', color='grey')
        ax.grid(which='minor', linestyle=':', linewidth='0.5', color='grey')
        plt.title('1mm Sensor Depletion Voltages', fontsize=18)
        plt.xticks([1.00, 1.11], fontsize = 16)
        plt.yticks(fontsize = 16)
        plt.text(1.06, 42, 'Normalised Implant Dose = 1.00', fontsize = 18)
        plt.text(1.112, 32, 'LGAD Full Depletion', fontsize = 16)
        plt.text(1.112, 22.5, 'LGAD Gain Layer \nDepletion', fontsize = 16)
        plt.text(1.112, 8.5, 'PiN Full Depletion', fontsize = 16)
        
        plt.plot([1.00, 1.11], [19.44, 23.44], label = 'LGAD Loc. 1 GLD', color = 'green', marker = 'x')
        plt.plot([1.00, 1.11], [27.19, 31.90], label = 'LGAD Loc. 1 FD', color = 'red', marker = 'x')
        plt.plot([1.00, 1.11], [20.28, 24.28], label = 'LGAD Loc. 3 GLD', color = 'orange', marker = 'x')
        plt.plot([1.00, 1.11], [28.27, 32.27], label = 'LGAD Loc. 3 FD', color = 'grey', marker = 'x')
        plt.plot([1.00, 1.11], [19.86, 24.02], label = 'LGAD Loc. 5 GLD', color = 'magenta', marker = 'x')
        plt.plot([1.00, 1.11], [28.02, 31.97], label = 'LGAD Loc. 5 FD', color = 'purple', marker = 'x')
        
        plt.plot([1.00, 1.11], [7.83, 9.06], label = 'PiN Loc. 1 FD', color = 'green', marker = 'x', linestyle = '--')
        plt.legend(fontsize = 16, loc = 'upper left')
        
        #second finally, wafer 11/3 that both have dose = 1.07 and E = 1.05/1.11
        fig, ax = plt.subplots()
        plt.rcParams["figure.figsize"] = [12,9]
        plt.ylabel('Bias Voltage [V]', fontsize = 22)
        plt.xlabel('Normalised Energy', fontsize = 22)
        #plt.yscale('log')
        plt.xlim(1.02, 1.14)
        plt.ylim(0, 50)
        ax.minorticks_on()
        ax.grid(which='major', linestyle='-', linewidth='0.5', color='grey')
        ax.grid(which='minor', linestyle=':', linewidth='0.5', color='grey')
        plt.title('1mm Sensor Depletion Voltages', fontsize=22)
        plt.xticks([1.05, 1.11], fontsize = 20)
        plt.yticks(fontsize = 20)
        plt.text(1.06, 45, 'Normalised Implant Dose = 1.07', fontsize = 22)
        plt.text(1.111, 37.5, 'LGAD Full Depletion', fontsize = 16)
        plt.text(1.112, 28, 'LGAD Gain Layer \nDepletion', fontsize = 16)
        plt.text(1.112, 7.5, 'PiN Full Depletion', fontsize = 16)
        plt.text(1.05, 0.4, 'Wafer 11', fontsize = 20, horizontalalignment='center')
        plt.text(1.11, 0.4, 'Wafer 3', fontsize = 20, horizontalalignment='center')
        
        plt.plot([1.05, 1.11], [LGAD1mm1_11_dic['GLD'], LGAD1mm1_3_dic['GLD']], label = 'LGAD Loc. 1', color = 'green', marker = 'x')
        plt.plot([1.05, 1.11], [LGAD1mm1_11_dic['FD'], LGAD1mm1_3_dic['FD']], label = 'LGAD Loc. 1', color = 'red', marker = 'x')
        plt.plot([1.05, 1.11], [LGAD1mm3_11_dic['GLD'], LGAD1mm3_3_dic['GLD']], label = 'LGAD Loc. 3', color = 'orange', marker = 'x')
        plt.plot([1.05, 1.11], [LGAD1mm3_11_dic['FD'], LGAD1mm3_3_dic['FD']], label = 'LGAD Loc. 3', color = 'grey', marker = 'x')
        plt.plot([1.05, 1.11], [LGAD1mm5_11_dic['GLD'], LGAD1mm5_3_dic['GLD']], label = 'LGAD Loc. 5', color = 'magenta', marker = 'x')
        plt.plot([1.05, 1.11], [LGAD1mm5_11_dic['FD'], LGAD1mm5_3_dic['FD']], label = 'LGAD Loc. 5', color = 'purple', marker = 'x')
        
        plt.plot([1.05, 1.11], [PiN1mm1_11_dic['FD'], PiN1mm1_3_dic['FD']], label = 'PiN Loc. 1', color = 'green', marker = 'x', linestyle = '--')
        plt.legend(fontsize = 16, loc = 'upper left')
    
def dopeconccompare():
    
    fig, ax = plt.subplots()
    plt.rcParams["figure.figsize"] = [12,9]
    plt.ylabel('Peak Doping Concentration [cm^-3]', fontsize = 18)
    plt.xlabel('Wafer', fontsize = 18)
    #plt.yscale('log')
    #plt.xlim(0, 800)
    #plt.ylim(0, 800)
    ax.minorticks_on()
    ax.grid(which='major', linestyle='-', linewidth='0.5', color='grey')
    ax.grid(which='minor', linestyle=':', linewidth='0.5', color='grey')
    plt.title('4mm LGAD Peak Doping Concentrations', fontsize=18)
    plt.xticks(fontsize = 16)
    plt.yticks(fontsize = 16)
    
    plt.plot(['wafer 6', 'wafer 11', 'wafer 16', 'wafer 20', 'wafer 3'], [7.97*10**15, 8.66*10**15, 6.05*10**15, 6.55*10**15, 9.37*10**15], label = 'LGAD Loc. 1', color = 'green', marker = 'x')
    plt.plot(['wafer 6', 'wafer 11', 'wafer 16', 'wafer 20', 'wafer 3'], [8.71*10**15, 8.5*10**15, 6.02*10**15, 6.13*10**15, 8.48*10**15], label = 'LGAD Loc. 3', color = 'red', marker = 'x')
    plt.plot(['wafer 6', 'wafer 11', 'wafer 16', 'wafer 20', 'wafer 3'], [8.86*10**15, 8.39*10**15, 5.95*10**15, 6.2*10**15, 8.66*10**15], label = 'LGAD Loc. 5', color = 'blue', marker = 'x')
    
    plt.legend(fontsize = 16)
    
    #DOSE COMPARISON
    
    fig, ax = plt.subplots()
    plt.rcParams["figure.figsize"] = [12,9]
    plt.ylabel('Peak Doping Concentration [cm^-3]', fontsize = 18)
    plt.xlabel('Normalised Dose', fontsize = 18)
    #plt.yscale('log')
    #plt.xlim(0, 800)
    #plt.ylim(0, 800)
    ax.minorticks_on()
    ax.grid(which='major', linestyle='-', linewidth='0.5', color='grey')
    ax.grid(which='minor', linestyle=':', linewidth='0.5', color='grey')
    plt.title('4mm LGAD Peak Doping Concentrations', fontsize=18)
    plt.xticks([0.92, 1.00, 1.00, 1.07, 1.07], fontsize = 16)
    plt.yticks(fontsize = 16)
    
    def doseswapper(waferlist):
            """
            takes in the list of vales in the wafer order: 6, 11, 16, 20, 3
            and returns a list of them in normalised dose order: 0.92, 1.00, 1.00, 1.07, 1.07
            which is equivilent to: 16, 20, 6, 11, 3
            """
            mylist = []
            mylist.append(waferlist[2])
            mylist.append(waferlist[3])
            mylist.append(waferlist[0])
            mylist.append(waferlist[1])
            mylist.append(waferlist[4])
            return mylist
    
    plt.plot([0.92, 1.00, 1.00, 1.07, 1.07], doseswapper([7.97*10**15, 8.66*10**15, 6.05*10**15, 6.55*10**15, 9.37*10**15]), label = 'LGAD Loc. 1', color = 'green', marker = 'x')
    plt.plot([0.92, 1.00, 1.00, 1.07, 1.07], doseswapper([8.71*10**15, 8.5*10**15, 6.02*10**15, 6.13*10**15, 8.48*10**15]), label = 'LGAD Loc. 3', color = 'red', marker = 'x')
    plt.plot([0.92, 1.00, 1.00, 1.07, 1.07], doseswapper([8.86*10**15, 8.39*10**15, 5.95*10**15, 6.2*10**15, 8.66*10**15]), label = 'LGAD Loc. 5', color = 'blue', marker = 'x')
    
    plt.legend(fontsize = 16)
    
    #ENERGY COMPARISON
    
    fig, ax = plt.subplots()
    plt.rcParams["figure.figsize"] = [12,9]
    plt.ylabel('Peak Doping Concentration [cm^-3]', fontsize = 18)
    plt.xlabel('Normalised Implant Energy', fontsize = 18)
    #plt.yscale('log')
    #plt.xlim(0, 800)
    #plt.ylim(0, 800)
    ax.minorticks_on()
    ax.grid(which='major', linestyle='-', linewidth='0.5', color='grey')
    ax.grid(which='minor', linestyle=':', linewidth='0.5', color='grey')
    plt.title('4mm LGAD Peak Doping Concentrations', fontsize=18)
    plt.xticks([1.00, 1.05, 1.05, 1.11, 1.11], fontsize = 16)
    plt.yticks(fontsize = 16)
    
    def energyswapper(waferlist):
            """
            takes in the list of vales in the wafer order: 6, 11, 16, 20, 3
            and returns a list of them in normalised dose order: 1.00, 1.05, 1.05, 1.11, 1.11
            which is equivilent to: 20, 16, 11, 6, 3
            """
            mylist = []
            mylist.append(waferlist[3])
            mylist.append(waferlist[2])
            mylist.append(waferlist[1])
            mylist.append(waferlist[0])
            mylist.append(waferlist[4])
            return mylist
    
    plt.plot([1.00, 1.05, 1.05, 1.11, 1.11], energyswapper([7.97*10**15, 8.66*10**15, 6.05*10**15, 6.55*10**15, 9.37*10**15]), label = 'LGAD Loc. 1', color = 'green', marker = 'x')
    plt.plot([1.00, 1.05, 1.05, 1.11, 1.11], energyswapper([8.71*10**15, 8.5*10**15, 6.02*10**15, 6.13*10**15, 8.48*10**15]), label = 'LGAD Loc. 3', color = 'red', marker = 'x')
    plt.plot([1.00, 1.05, 1.05, 1.11, 1.11], energyswapper([8.86*10**15, 8.39*10**15, 5.95*10**15, 6.2*10**15, 8.66*10**15]), label = 'LGAD Loc. 5', color = 'blue', marker = 'x')
    
    plt.legend(fontsize = 16)
    
    #okay, now want to compare across wafers that have a constant between them
    
    #first, wafer 16/11 that both have E=1.05 and dose = 0.92/1.07
    fig, ax = plt.subplots()
    plt.rcParams["figure.figsize"] = [12,9]
    plt.ylabel('Peak Doping Concentration [cm^-3]', fontsize = 18)
    plt.xlabel('Normalised Dose', fontsize = 18)
    #plt.yscale('log')
    plt.xlim(0.89, 1.11)
    plt.ylim(5*10**15, 12*10**15)
    ax.minorticks_on()
    ax.grid(which='major', linestyle='-', linewidth='0.5', color='grey')
    ax.grid(which='minor', linestyle=':', linewidth='0.5', color='grey')
    plt.title('LGAD 4mm Peak Doping Concentrations', fontsize=18)
    plt.xticks([0.92, 1.07], fontsize = 16)
    plt.yticks(fontsize = 16)
    plt.text(0.96, 11.5*10**15, 'Normalised Implant Energy = 1.05', fontsize = 18)
    
    plt.plot([0.92, 1.07], [LGAD4mm1_16_dic['FittedPeakDope']*10**15, LGAD4mm1_11_dic['FittedPeakDope']*10**15], label = 'LGAD Loc. 1', color = 'green', marker = 'x')
    plt.plot([0.92, 1.07], [LGAD4mm3_16_dic['FittedPeakDope']*10**15, LGAD4mm3_11_dic['FittedPeakDope']*10**15], label = 'LGAD Loc. 3', color = 'red', marker = 'x')
    plt.plot([0.92, 1.07], [LGAD4mm3_16_dic['FittedPeakDope']*10**15, LGAD4mm3_11_dic['FittedPeakDope']*10**15], label = 'LGAD Loc. 5', color = 'blue', marker = 'x')
    plt.legend(fontsize = 16, loc = 'upper left')
    
    #secondly, wafer 6/3 that both have E=1.11 and dose = 1.00/1.07
    fig, ax = plt.subplots()
    plt.rcParams["figure.figsize"] = [12,9]
    plt.ylabel('Peak Doping Concentration [cm^-3]', fontsize = 18)
    plt.xlabel('Normalised Dose', fontsize = 18)
    #plt.yscale('log')
    plt.xlim(0.98, 1.10)
    plt.ylim(5*10**15, 12*10**15)
    ax.minorticks_on()
    ax.grid(which='major', linestyle='-', linewidth='0.5', color='grey')
    ax.grid(which='minor', linestyle=':', linewidth='0.5', color='grey')
    plt.title('LGAD 4mm Peak Doping Concentrations', fontsize=18)
    plt.xticks([1.00, 1.07], fontsize = 16)
    plt.yticks(fontsize = 16)
    plt.text(1.03, 11.5*10**15, 'Normalised Implant Energy = 1.11', fontsize = 18)
    
    plt.plot([1, 1.07], [LGAD4mm1_6_dic['FittedPeakDope']*10**15, LGAD4mm1_3_dic['FittedPeakDope']*10**15], label = 'LGAD Loc. 1', color = 'green', marker = 'x')
    plt.plot([1, 1.07], [LGAD4mm3_6_dic['FittedPeakDope']*10**15, LGAD4mm3_3_dic['FittedPeakDope']*10**15], label = 'LGAD Loc. 3', color = 'red', marker = 'x')
    plt.plot([1, 1.07], [LGAD4mm5_6_dic['FittedPeakDope']*10**15, LGAD4mm5_3_dic['FittedPeakDope']*10**15], label = 'LGAD Loc. 5', color = 'blue', marker = 'x')
    plt.legend(fontsize = 16, loc = 'upper left')
    
    #finally, wafer 20/6 that both have dose = 1.00 and energy = 1.00/1.11
    fig, ax = plt.subplots()
    plt.rcParams["figure.figsize"] = [12,9]
    plt.ylabel('Peak Doping Concentration [cm^-3]', fontsize = 18)
    plt.xlabel('Normalised Energy', fontsize = 18)
    #plt.yscale('log')
    plt.xlim(0.97, 1.15)
    plt.ylim(5*10**15, 12*10**15)
    ax.minorticks_on()
    ax.grid(which='major', linestyle='-', linewidth='0.5', color='grey')
    ax.grid(which='minor', linestyle=':', linewidth='0.5', color='grey')
    plt.title('LGAD 4mm Peak Doping Concentrations', fontsize=18)
    plt.xticks([1.00, 1.11], fontsize = 16)
    plt.yticks(fontsize = 16)
    plt.text(1.03, 11.5*10**15, 'Normalised Implant Dose = 1.00', fontsize = 18)
    
    plt.plot([1, 1.11], [LGAD4mm1_20_dic['FittedPeakDope']*10**15, LGAD4mm1_6_dic['FittedPeakDope']*10**15], label = 'LGAD Loc. 1', color = 'green', marker = 'x')
    plt.plot([1, 1.11], [LGAD4mm3_20_dic['FittedPeakDope']*10**15, LGAD4mm3_6_dic['FittedPeakDope']*10**15], label = 'LGAD Loc. 3', color = 'red', marker = 'x')
    plt.plot([1, 1.11], [LGAD4mm5_20_dic['FittedPeakDope']*10**15, LGAD4mm5_6_dic['FittedPeakDope']*10**15], label = 'LGAD Loc. 5', color = 'blue', marker = 'x')
    plt.legend(fontsize = 16, loc = 'upper left')
    
    #finally, wafer 11/3 that both have dose = 1.07 and energy = 1.05/1.11
    fig, ax = plt.subplots()
    plt.rcParams["figure.figsize"] = [12,9]
    plt.ylabel('Peak Doping Concentration [cm^-3]', fontsize = 18)
    plt.xlabel('Normalised Energy', fontsize = 18)
    #plt.yscale('log')
    plt.xlim(1.03, 1.14)
    plt.ylim(5*10**15, 12*10**15)
    ax.minorticks_on()
    ax.grid(which='major', linestyle='-', linewidth='0.5', color='grey')
    ax.grid(which='minor', linestyle=':', linewidth='0.5', color='grey')
    plt.title('LGAD 4mm Peak Doping Concentrations', fontsize=18)
    plt.xticks([1.05, 1.11], fontsize = 16)
    plt.yticks(fontsize = 16)
    plt.text(1.07, 11.5*10**15, 'Normalised Implant Dose = 1.07', fontsize = 18)
    
    plt.plot([1.05, 1.11], [LGAD4mm1_11_dic['FittedPeakDope']*10**15, LGAD4mm1_3_dic['FittedPeakDope']*10**15], label = 'LGAD Loc. 1', color = 'green', marker = 'x')
    plt.plot([1.05, 1.11], [LGAD4mm3_11_dic['FittedPeakDope']*10**15, LGAD4mm3_3_dic['FittedPeakDope']*10**15], label = 'LGAD Loc. 3', color = 'red', marker = 'x')
    plt.plot([1.05, 1.11], [LGAD4mm5_11_dic['FittedPeakDope']*10**15, LGAD4mm5_3_dic['FittedPeakDope']*10**15], label = 'LGAD Loc. 5', color = 'blue', marker = 'x')
    plt.legend(fontsize = 16, loc = 'upper left')
    
    #doping depth comparison across constant values now
    
def dopedepthcompare():
    
    #still need to do full across wafer comparison as a function of ernergy and then dose
    
    fig, ax = plt.subplots()
    plt.rcParams["figure.figsize"] = [12,9]
    plt.ylabel('Peak Doping Depth [$\mu m$]', fontsize = 18)
    plt.xlabel('Wafer', fontsize = 18)
    #plt.yscale('log')
    #plt.xlim(0, 800)
    plt.ylim(1.7, 2)
    ax.minorticks_on()
    ax.grid(which='major', linestyle='-', linewidth='0.5', color='grey')
    ax.grid(which='minor', linestyle=':', linewidth='0.5', color='grey')
    plt.title('4mm LGAD Peak Doping Depths', fontsize=18)
    plt.xticks(fontsize = 16)
    plt.yticks(fontsize = 16)
    
    plt.plot(['wafer 6', 'wafer 11', 'wafer 16', 'wafer 20', 'wafer 3'], [1.73, 1.78, 1.81, 1.87, 1.78], label = 'LGAD Loc. 1', color = 'green', marker = 'x')
    plt.plot(['wafer 6', 'wafer 11', 'wafer 16', 'wafer 20', 'wafer 3'], [1.75, 1.82, 1.82, 1.98, 1.94], label = 'LGAD Loc. 3', color = 'red', marker = 'x')
    plt.plot(['wafer 6', 'wafer 11', 'wafer 16', 'wafer 20', 'wafer 3'], [1.73, 1.71, 1.89, 1.96, 1.92], label = 'LGAD Loc. 5', color = 'blue', marker = 'x')
    
    plt.legend(fontsize = 16, loc = 'upper left')
    
    #okay, now want to compare across wafers that have a constant between them
    
    #first, wafer 16/11 that both have E=1.05 and dose = 0.92/1.07
    fig, ax = plt.subplots()
    plt.rcParams["figure.figsize"] = [12,9]
    plt.ylabel('Peak Doping Depth [$\mu m$]', fontsize = 18)
    plt.xlabel('Normalised Implant Dose', fontsize = 18)
    #plt.yscale('log')
    #plt.xlim(0, 800)
    plt.ylim(2, 2.2)
    ax.minorticks_on()
    ax.grid(which='major', linestyle='-', linewidth='0.5', color='grey')
    ax.grid(which='minor', linestyle=':', linewidth='0.5', color='grey')
    plt.title('4mm LGAD Peak Doping Depths', fontsize=18)
    plt.xticks([0.92, 1.07], fontsize = 16)
    plt.yticks(fontsize = 16)
    plt.text(0.97, 1.97, 'Normalised Implant Energy = 1.05', fontsize = 18)
    
    plt.plot([0.92, 1.07], [LGAD1mm1_16_dic['FittedPeakDopeDepth'], LGAD1mm1_11_dic['FittedPeakDopeDepth']], label = 'LGAD Loc. 1', color = 'green', marker = 'x')
    plt.plot([0.92, 1.07], [LGAD1mm3_16_dic['FittedPeakDopeDepth'], LGAD1mm3_11_dic['FittedPeakDopeDepth']], label = 'LGAD Loc. 3', color = 'red', marker = 'x')
    plt.plot([0.92, 1.07], [LGAD1mm5_16_dic['FittedPeakDopeDepth'], LGAD1mm5_11_dic['FittedPeakDopeDepth']], label = 'LGAD Loc. 5', color = 'blue', marker = 'x')
    plt.legend(loc = 'upper left', fontsize = 16)
    
    #secondly, wafer 6/3 that both have E=1.11 and dose = 1.00/1.07
    fig, ax = plt.subplots()
    plt.rcParams["figure.figsize"] = [12,9]
    plt.ylabel('Peak Doping Depth [$\mu m$]', fontsize = 18)
    plt.xlabel('Normalised Implant Dose', fontsize = 18)
    #plt.yscale('log')
    #plt.xlim(0, 800)
    plt.ylim(2, 2.2)
    ax.minorticks_on()
    ax.grid(which='major', linestyle='-', linewidth='0.5', color='grey')
    ax.grid(which='minor', linestyle=':', linewidth='0.5', color='grey')
    plt.title('4mm LGAD Peak Doping Depths', fontsize=18)
    plt.xticks([1.00, 1.07], fontsize = 16)
    plt.yticks(fontsize = 16)
    plt.text(1.028, 1.97, 'Normalised Implant Energy = 1.11', fontsize = 18)
    
    plt.plot([1.00, 1.07], [LGAD1mm1_6_dic['FittedPeakDopeDepth'], LGAD1mm1_3_dic['FittedPeakDopeDepth']], label = 'LGAD Loc. 1', color = 'green', marker = 'x')
    plt.plot([1.00, 1.07], [LGAD1mm3_6_dic['FittedPeakDopeDepth'], LGAD1mm3_3_dic['FittedPeakDopeDepth']], label = 'LGAD Loc. 3', color = 'red', marker = 'x')
    plt.plot([1.00, 1.07], [LGAD1mm5_6_dic['FittedPeakDopeDepth'], LGAD1mm5_3_dic['FittedPeakDopeDepth']], label = 'LGAD Loc. 5', color = 'blue', marker = 'x')
    plt.legend(loc = 'upper left', fontsize = 16)
    
    #finally, wafer 20/6 that both have dose = 1.00 and energy = 1.00/1.11
    fig, ax = plt.subplots()
    plt.rcParams["figure.figsize"] = [12,9]
    plt.ylabel('Peak Doping Depth [$\mu m$]', fontsize = 18)
    plt.xlabel('Normalised Implant Energy', fontsize = 18)
    #plt.yscale('log')
    plt.xlim(0.97, 1.14)
    plt.ylim(2, 2.2)
    ax.minorticks_on()
    ax.grid(which='major', linestyle='-', linewidth='0.5', color='grey')
    ax.grid(which='minor', linestyle=':', linewidth='0.5', color='grey')
    plt.title('4mm LGAD Peak Doping Depths', fontsize=18)
    plt.xticks([1.00, 1.11], fontsize = 16)
    plt.yticks(fontsize = 16)
    plt.text(1.028, 1.97, 'Normalised Implant Dose = 1.00', fontsize = 18)
    
    plt.plot([1.00, 1.11], [LGAD1mm1_20_dic['FittedPeakDopeDepth'], LGAD1mm1_6_dic['FittedPeakDopeDepth']], label = 'LGAD Loc. 1', color = 'green', marker = 'x')
    plt.plot([1.00, 1.11], [LGAD1mm3_20_dic['FittedPeakDopeDepth'], LGAD1mm3_6_dic['FittedPeakDopeDepth']], label = 'LGAD Loc. 3', color = 'red', marker = 'x')
    plt.plot([1.00, 1.11], [LGAD1mm5_20_dic['FittedPeakDopeDepth'], LGAD1mm5_6_dic['FittedPeakDopeDepth']], label = 'LGAD Loc. 5', color = 'blue', marker = 'x')
    plt.legend(loc = 'upper left', fontsize = 16)
    
    
    #Fitted peak dope depth comparison^
      
def implantdepthcompare():
    
    
    #ENERGY COMPARISON ACROSS ALL WAFERS
    
    fig, ax = plt.subplots()
    plt.rcParams["figure.figsize"] = [12,9]
    plt.ylabel('Implant Depth [$\mu$m]', fontsize = 18)
    plt.xlabel('Normalised Implant Energy', fontsize = 18)
    #plt.yscale('log')
    #plt.xlim(0, 800)
    #plt.ylim(0, 800)
    ax.minorticks_on()
    ax.grid(which='major', linestyle='-', linewidth='0.5', color='grey')
    ax.grid(which='minor', linestyle=':', linewidth='0.5', color='grey')
    plt.title('4mm LGAD Implant Depths', fontsize=18)
    #energy order: 20, 16, 11, 6, 3
    plt.xticks([1.00, 1.05, 1.05, 1.11, 1.11], fontsize = 16)
    plt.yticks(fontsize = 16)
    
    
    plt.plot([1.00, 1.05, 1.05, 1.11, 1.11], [LGAD1mm1_20_dic['ImplantDepth'], LGAD1mm1_16_dic['ImplantDepth'], LGAD1mm1_11_dic['ImplantDepth'], LGAD1mm1_6_dic['ImplantDepth'], LGAD1mm1_3_dic['ImplantDepth']], label = 'LGAD Loc. 1', color = 'green', marker = 'x')
    plt.plot([1.00, 1.05, 1.05, 1.11, 1.11], [LGAD1mm3_20_dic['ImplantDepth'], LGAD1mm3_16_dic['ImplantDepth'], LGAD1mm3_11_dic['ImplantDepth'], LGAD1mm3_6_dic['ImplantDepth'], LGAD1mm3_3_dic['ImplantDepth']], label = 'LGAD Loc. 3', color = 'red', marker = 'x')
    plt.plot([1.00, 1.05, 1.05, 1.11, 1.11], [LGAD1mm5_20_dic['ImplantDepth'], LGAD1mm5_16_dic['ImplantDepth'], LGAD1mm5_11_dic['ImplantDepth'], LGAD1mm5_6_dic['ImplantDepth'], LGAD1mm5_3_dic['ImplantDepth']], label = 'LGAD Loc. 5', color = 'blue', marker = 'x')
    plt.legend(fontsize = 16)
    
    
    #wafer 20/6 that both have dose = 1.00 and energy = 1.00/1.11
    fig, ax = plt.subplots()
    plt.rcParams["figure.figsize"] = [12,9]
    plt.ylabel('Implant Depth [$\mu m$]', fontsize = 18)
    plt.xlabel('Normalised Implant Energy', fontsize = 18)
    #plt.yscale('log')
    plt.xlim(0.97, 1.14)
    plt.ylim(3, 5)
    ax.minorticks_on()
    ax.grid(which='major', linestyle='-', linewidth='0.5', color='grey')
    ax.grid(which='minor', linestyle=':', linewidth='0.5', color='grey')
    plt.title('1mm LGAD Implant Depth', fontsize=18)
    plt.xticks([1.00, 1.11], fontsize = 16)
    plt.yticks(fontsize = 16)
    plt.text(1.03, 4.85, 'Normalised Implant Dose = 1.00', fontsize = 18)
    
    plt.plot([1.00, 1.11], [LGAD1mm1_20_dic['ImplantDepth'], LGAD1mm1_6_dic['ImplantDepth']], label = 'LGAD Loc. 1', color = 'green', marker = 'x')
    plt.plot([1.00, 1.11], [LGAD1mm3_20_dic['ImplantDepth'], LGAD1mm3_6_dic['ImplantDepth']], label = 'LGAD Loc. 3', color = 'red', marker = 'x')
    plt.plot([1.00, 1.11], [LGAD1mm5_20_dic['ImplantDepth'], LGAD1mm5_6_dic['ImplantDepth']], label = 'LGAD Loc. 5', color = 'blue', marker = 'x')
    plt.legend(loc = 'upper left', fontsize = 16)
    
    
    #wafer 11/3 that both have dose = 1.07 and energy = 1.05/1.11
    fig, ax = plt.subplots()
    plt.rcParams["figure.figsize"] = [12,9]
    plt.ylabel('Implant Depth [$\mu m$]', fontsize = 22)
    plt.xlabel('Normalised Implant Energy', fontsize = 22)
    #plt.yscale('log')
    plt.xlim(1.03, 1.13)
    plt.ylim(3, 5)
    ax.minorticks_on()
    ax.grid(which='major', linestyle='-', linewidth='0.5', color='grey')
    ax.grid(which='minor', linestyle=':', linewidth='0.5', color='grey')
    plt.title('1mm LGAD Implant Depth', fontsize=22)
    plt.xticks([1.05, 1.11], fontsize = 20)
    plt.yticks(fontsize = 20)
    plt.text(1.07, 4.85, 'Normalised Implant Dose = 1.07', fontsize = 22)
    plt.text(1.05, 3.05, 'Wafer 11', fontsize = 22, horizontalalignment='center')
    plt.text(1.11, 3.05, 'Wafer 3', fontsize = 22, horizontalalignment='center')
    
    plt.plot([1.05, 1.11], [LGAD1mm1_11_dic['ImplantDepth'], LGAD1mm1_3_dic['ImplantDepth']], label = 'LGAD Loc. 1', color = 'green', marker = 'x')
    plt.plot([1.05, 1.11], [LGAD1mm3_11_dic['ImplantDepth'], LGAD1mm3_3_dic['ImplantDepth']], label = 'LGAD Loc. 3', color = 'red', marker = 'x')
    plt.plot([1.05, 1.11], [LGAD1mm5_11_dic['ImplantDepth'], LGAD1mm5_3_dic['ImplantDepth']], label = 'LGAD Loc. 5', color = 'blue', marker = 'x')
    plt.legend(loc = 'upper left', fontsize = 18)
    
    #wafer 6/3 that both have E=1.11 and dose = 1.00/1.07
    fig, ax = plt.subplots()
    plt.rcParams["figure.figsize"] = [12,9]
    plt.ylabel('Implant Depth [$\mu m$]', fontsize = 22)
    plt.xlabel('Normalised Dose', fontsize = 22)
    #plt.yscale('log')
    plt.xlim(0.98, 1.10)
    plt.ylim(3, 5)
    ax.minorticks_on()
    ax.grid(which='major', linestyle='-', linewidth='0.5', color='grey')
    ax.grid(which='minor', linestyle=':', linewidth='0.5', color='grey')
    plt.title('1mm LGAD Implant Depth', fontsize=22)
    plt.xticks([1.00, 1.07], fontsize = 20)
    plt.yticks(fontsize = 20)
    plt.text(1.02, 4.85, 'Normalised Implant Energy = 1.11', fontsize = 22)
    plt.text(1., 3.05, 'Wafer 6', fontsize = 22, horizontalalignment='center')
    plt.text(1.07, 3.05, 'Wafer 3', fontsize = 22, horizontalalignment='center')
    
    plt.plot([1, 1.07], [LGAD1mm1_6_dic['ImplantDepth'], LGAD1mm1_3_dic['ImplantDepth']], label = 'LGAD Loc. 1', color = 'green', marker = 'x')
    plt.plot([1, 1.07], [LGAD1mm3_6_dic['ImplantDepth'], LGAD1mm3_3_dic['ImplantDepth']], label = 'LGAD Loc. 3', color = 'red', marker = 'x')
    plt.plot([1, 1.07], [LGAD1mm5_6_dic['ImplantDepth'], LGAD1mm5_3_dic['ImplantDepth']], label = 'LGAD Loc. 5', color = 'blue', marker = 'x')
    plt.legend(fontsize = 18, loc = 'upper left')
    
    

def totaldopecompare():
    """
    compares the integrated peak values
    """
    #first, wafer 16/11 that both have E=1.05 and dose = 0.92/1.07
    fig, ax = plt.subplots()
    plt.rcParams["figure.figsize"] = [12,9]
    plt.ylabel('Total Number of Dopants [cm^-2]', fontsize = 18)
    plt.xlabel('Normalised Dose', fontsize = 18)
    #plt.yscale('log')
    plt.xlim(0.89, 1.11)
    plt.ylim(4*10**15, 10*10**15)
    ax.minorticks_on()
    ax.grid(which='major', linestyle='-', linewidth='0.5', color='grey')
    ax.grid(which='minor', linestyle=':', linewidth='0.5', color='grey')
    plt.title('LGAD 1mm Total Dopant Comparison', fontsize=18)
    plt.xticks([0.92, 1.07], fontsize = 16)
    plt.yticks(fontsize = 16)
    plt.text(0.96, 9.7*10**15, 'Normalised Implant Energy = 1.05', fontsize = 18)
    plt.text(0.92, 4.1*10**15, 'Wafer 16', fontsize = 16, horizontalalignment='center')
    plt.text(1.07, 4.1*10**15, 'Wafer 11', fontsize = 16, horizontalalignment='center')
    
    plt.plot([0.92, 1.07], [LGAD1mm1_16_dic['TotalDope']*10**15, LGAD1mm1_11_dic['TotalDope']*10**15], label = 'LGAD Loc. 1', color = 'green', marker = 'x')
    plt.plot([0.92, 1.07], [LGAD1mm3_16_dic['TotalDope']*10**15, LGAD1mm3_11_dic['TotalDope']*10**15], label = 'LGAD Loc. 3', color = 'red', marker = 'x')
    plt.plot([0.92, 1.07], [LGAD1mm3_16_dic['TotalDope']*10**15, LGAD1mm3_11_dic['TotalDope']*10**15], label = 'LGAD Loc. 5', color = 'blue', marker = 'x')
    plt.legend(fontsize = 16, loc = 'upper left')
    
    #secondly, wafer 6/3 that both have E=1.11 and dose = 1.00/1.07
    fig, ax = plt.subplots()
    plt.rcParams["figure.figsize"] = [12,9]
    plt.ylabel('Total Number of Dopants [cm^-2]', fontsize = 22)
    plt.xlabel('Normalised Dose', fontsize = 22)
    #plt.yscale('log')
    plt.xlim(0.98, 1.10)
    plt.ylim(4*10**15, 10*10**15)
    ax.minorticks_on()
    ax.grid(which='major', linestyle='-', linewidth='0.5', color='grey')
    ax.grid(which='minor', linestyle=':', linewidth='0.5', color='grey')
    plt.title('LGAD 1mm Total Dopant Comparison', fontsize=22)
    plt.xticks([1.00, 1.07], fontsize = 20)
    plt.yticks(fontsize = 20)
    plt.text(1.02, 9.7*10**15, 'Normalised Implant Energy = 1.11', fontsize = 22)
    plt.text(1, 4.1*10**15, 'Wafer 6', fontsize = 20, horizontalalignment='center')
    plt.text(1.07, 4.1*10**15, 'Wafer 3', fontsize = 20, horizontalalignment='center')
    
    plt.plot([1, 1.07], [LGAD1mm1_6_dic['TotalDope']*10**15, LGAD1mm1_3_dic['TotalDope']*10**15], label = 'LGAD Loc. 1', color = 'green', marker = 'x')
    plt.plot([1, 1.07], [LGAD1mm3_6_dic['TotalDope']*10**15, LGAD1mm3_3_dic['TotalDope']*10**15], label = 'LGAD Loc. 3', color = 'red', marker = 'x')
    plt.plot([1, 1.07], [LGAD1mm5_6_dic['TotalDope']*10**15, LGAD1mm5_3_dic['TotalDope']*10**15], label = 'LGAD Loc. 5', color = 'blue', marker = 'x')
    plt.legend(fontsize = 18, loc = 'upper left')
    
    #finally, wafer 20/6 that both have dose = 1.00 and energy = 1.00/1.11
    fig, ax = plt.subplots()
    plt.rcParams["figure.figsize"] = [12,9]
    plt.ylabel('Total Number of Dopants [cm^-2]', fontsize = 18)
    plt.xlabel('Normalised Energy', fontsize = 18)
    #plt.yscale('log')
    plt.xlim(0.97, 1.15)
    plt.ylim(4*10**15, 10*10**15)
    ax.minorticks_on()
    ax.grid(which='major', linestyle='-', linewidth='0.5', color='grey')
    ax.grid(which='minor', linestyle=':', linewidth='0.5', color='grey')
    plt.title('LGAD 1mm Total Dopant Comparison', fontsize=18)
    plt.xticks([1.00, 1.11], fontsize = 16)
    plt.yticks(fontsize = 16)
    plt.text(1.03, 9.7*10**15, 'Normalised Implant Dose = 1.00', fontsize = 18)
    plt.text(1, 4.1*10**15, 'Wafer 20', fontsize = 16, horizontalalignment='center')
    plt.text(1.11, 4.1*10**15, 'Wafer 6', fontsize = 16, horizontalalignment='center')
    
    plt.plot([1, 1.11], [LGAD1mm1_20_dic['TotalDope']*10**15, LGAD1mm1_6_dic['TotalDope']*10**15], label = 'LGAD Loc. 1', color = 'green', marker = 'x')
    plt.plot([1, 1.11], [LGAD1mm3_20_dic['TotalDope']*10**15, LGAD1mm3_6_dic['TotalDope']*10**15], label = 'LGAD Loc. 3', color = 'red', marker = 'x')
    plt.plot([1, 1.11], [LGAD1mm5_20_dic['TotalDope']*10**15, LGAD1mm5_6_dic['TotalDope']*10**15], label = 'LGAD Loc. 5', color = 'blue', marker = 'x')
    plt.legend(fontsize = 16, loc = 'upper left')
    
    #finally, wafer 11/3 that both have dose = 1.07 and energy = 1.05/1.11
    fig, ax = plt.subplots()
    plt.rcParams["figure.figsize"] = [12,9]
    plt.ylabel('Total Number of Dopants [cm^-2]', fontsize = 22)
    plt.xlabel('Normalised Energy', fontsize = 22)
    #plt.yscale('log')
    plt.xlim(1.03, 1.14)
    plt.ylim(4*10**15, 10*10**15)
    ax.minorticks_on()
    ax.grid(which='major', linestyle='-', linewidth='0.5', color='grey')
    ax.grid(which='minor', linestyle=':', linewidth='0.5', color='grey')
    plt.title('LGAD 1mm Total Dopant Comparison', fontsize=22)
    plt.xticks([1.05, 1.11], fontsize = 20)
    plt.yticks(fontsize = 20)
    plt.text(1.07, 9.7*10**15, 'Normalised Implant Dose = 1.07', fontsize = 22)
    plt.text(1.05, 4.1*10**15, 'Wafer 11', fontsize = 22, horizontalalignment='center')
    plt.text(1.11, 4.1*10**15, 'Wafer 3', fontsize = 22, horizontalalignment='center')
    
    plt.plot([1.05, 1.11], [LGAD1mm1_11_dic['TotalDope']*10**15, LGAD1mm1_3_dic['TotalDope']*10**15], label = 'LGAD Loc. 1', color = 'green', marker = 'x')
    plt.plot([1.05, 1.11], [LGAD1mm3_11_dic['TotalDope']*10**15, LGAD1mm3_3_dic['TotalDope']*10**15], label = 'LGAD Loc. 3', color = 'red', marker = 'x')
    plt.plot([1.05, 1.11], [LGAD1mm5_11_dic['TotalDope']*10**15, LGAD1mm5_3_dic['TotalDope']*10**15], label = 'LGAD Loc. 5', color = 'blue', marker = 'x')
    plt.legend(fontsize = 18, loc = 'upper left')


#CV([PiN4mm1_11], [[0, 6], [20, 40], [0, 15]])
#CV([LGAD4mm3_11, PiN4mm1_11], [])
#CV([LGAD4mm3_11], [[25, 30], [35, 48], [2, 15]])
#CV([LGAD4mm1_11, LGAD4mm3_11, LGAD4mm5_11, LGAD1mm1_11, LGAD1mm3_11, LGAD1mm5_11, PiN4mm1_11, PiN1mm1_11], [])
#KEY:
#[[fit1V1, fit1V2], [fit2V1, fit2V2], [fit3V1, fit3V2]]
#fit1=bigslope, fit2=tail off high V, fit3 = gain layer depletion part (LGAD only)

#doping([LGAD1mm1_3])
#depcompare('1mm')
#dopeconccompare()
#dopedepthcompare()
#implantdepthcompare()
#totaldopecompare()

#CV([LGAD1mm5_6_diced, LGAD1mm5_6, LGAD1mm1_6_diced, LGAD1mm1_6], [])
#CV([LGAD1mm1_6], [])
#doping([LGAD1mm1_6])
    
    
    
    
    

    
