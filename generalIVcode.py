# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 14:20:12 2021

@author: Marcus
"""

class sensor():
    """
    Defines a sensor
    """
    def __init__(self, file, wafer, size, location, sensortype, datastyle, diced = False):
        self.file = file
        self.wafer = wafer
        self.size = size
        self.location = location
        self.type = sensortype
        self.datastyle = datastyle
        self.diced = diced
        

%matplotlib qt

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


LGAD4mm1_6 = sensor('IVdata\wafer6\Te2V_Batch1_Wafer6_LGAD_4mm_No1_pad_only_floating_002.txt', 6, '4mm', 1, 'LGAD', 'normal')
LGAD4mm2_6 = sensor('IVdata\wafer6\Te2V_Batch1_Wafer6_LGAD_4mm_No2_pad_only_floating.txt', 6, '4mm', 2, 'LGAD', 'normal')
LGAD4mm3_6 = sensor('IVdata\wafer6\Te2V_Batch1_Wafer6_LGAD_4mm_No3_pad_only_floating_retest.txt', 6, '4mm', 3, 'LGAD', 'normal')
LGAD4mm4_6 = sensor('IVdata\wafer6\Te2V_Batch1_Wafer6_LGAD_4mm_No4_pad_only_floating.txt', 6, '4mm', 4, 'LGAD', 'normal')
LGAD4mm5_6 = sensor('IVdata\wafer6\Te2V_Batch1_Wafer6_LGAD_4mm_No5_pad_only_floating.txt', 6, '4mm', 5, 'LGAD', 'normal')
PiN4mm1_6 = sensor('IVdata\wafer6\Te2V_Batch1_Wafer6_PiN_4mm_No1_pad_only_floating.txt', 6, '4mm', 1, 'PiN', 'normal') 
PiN2mm1_6 = sensor('IVdata\wafer6\Te2V_Batch1_Wafer6_PiN_2mm_No1_pad_only_floating.txt', 6, '2mm', 1, 'PiN', 'normal')
LGAD2mm1_6 = sensor('IVdata\wafer6\Te2V_Batch1_Wafer6_LGAD_2mm_No1_pad_only_floating.txt', 6, '2mm', 1, 'LGAD', 'normal')
LGAD2mm2_6 = sensor('IVdata\wafer6\Te2V_Batch1_Wafer6_LGAD_2mm_No2_pad_only_floating.txt', 6, '2mm', 2, 'LGAD', 'normal')
LGAD2mm3_6 = sensor('IVdata\wafer6\Te2V_Batch1_Wafer6_LGAD_2mm_No3_pad_only_floating.txt', 6, '2mm', 3, 'LGAD', 'normal')
LGAD2mm4_6 = sensor('IVdata\wafer6\Te2V_Batch1_Wafer6_LGAD_2mm_No4_pad_only_floating.txt', 6, '2mm', 4, 'LGAD', 'normal')
LGAD2mm5_6 = sensor('IVdata\wafer6\Te2V_Batch1_Wafer6_LGAD_2mm_No5_pad_only_floating.txt', 6, '2mm', 5, 'LGAD', 'normal')
LGAD1mm1_6 = sensor('IVdata\wafer6\Te2V_Batch1_Wafer6_LGAD_1mm_No1_pad_only_floating.txt', 6, '1mm', 1, 'LGAD', 'normal')
LGAD1mm2_6 = sensor('IVdata\wafer6\Te2V_Batch1_Wafer6_LGAD_1mm_No2_pad_only_floating.txt', 6, '1mm', 2, 'LGAD', 'normal')
LGAD1mm3_6 = sensor('IVdata\wafer6\Te2V_Batch1_Wafer6_LGAD_1mm_No3_pad_only_floating.txt', 6, '1mm', 3, 'LGAD', 'normal')
LGAD1mm4_6 = sensor('IVdata\wafer6\Te2V_Batch1_Wafer6_LGAD_1mm_No4_pad_only_floating_retest.txt', 6, '1mm', 4, 'LGAD', 'normal')
LGAD1mm5_6 = sensor('IVdata\wafer6\Te2V_Batch1_Wafer6_LGAD_1mm_No5_pad_only_floating.txt', 6, '1mm', 5, 'LGAD', 'normal')
PiN1mm1_6 = sensor('IVdata\wafer6\Te2V_Batch1_Wafer6_PiN_1mm_No1_pad_only_floating.txt', 6, '1mm', 1, 'PiN', 'normal')

LGAD4mm1_11 = sensor('IVdata\wafer11\Te2V_Batch1_Wafer11_LGAD_4mm_No1_pad_only_floating.txt', 11, '4mm', 1, 'LGAD', 'normal')
LGAD4mm2_11 = sensor('IVdata\wafer11\Te2V_Batch1_Wafer11_LGAD_4mm_No2_pad_only_floating.txt', 11, '4mm', 2, 'LGAD', 'normal')
LGAD4mm3_11 = sensor('IVdata\wafer11\Te2V_Batch1_Wafer11_LGAD_4mm_No3_pad_only_floating.txt', 11, '4mm', 3, 'LGAD', 'normal')
LGAD4mm4_11 = sensor('IVdata\wafer11\Te2V_Batch1_Wafer11_LGAD_4mm_No4_pad_only_floating.txt', 11, '4mm', 4, 'LGAD', 'normal')
LGAD4mm5_11 = sensor('IVdata\wafer11\Te2V_Batch1_Wafer11_LGAD_4mm_No5_pad_only_floating.txt', 11, '4mm', 5, 'LGAD', 'normal')
PiN4mm1_11 = sensor('IVdata\wafer11\Te2V_Batch1_Wafer11_PiN_4mm_No1_pad_only_floating.txt', 11, '4mm', 1, 'PiN', 'normal')
LGAD2mm1_11 = sensor('IVdata\wafer11\Te2V_Batch1_Wafer11_LGAD_2mm_No1_pad_only_floating.txt', 11, '2mm', 1, 'LGAD', 'normal')
LGAD2mm2_11 = sensor('IVdata\wafer11\Te2V_Batch1_Wafer11_LGAD_2mm_No2_pad_only_floating.txt', 11, '2mm', 2, 'LGAD', 'normal')
LGAD2mm3_11 = sensor('IVdata\wafer11\Te2V_Batch1_Wafer11_LGAD_2mm_No3_pad_only_floating.txt', 11, '2mm', 3, 'LGAD', 'normal')
LGAD2mm4_11 = sensor('IVdata\wafer11\Te2V_Batch1_Wafer11_LGAD_2mm_No4_pad_only_floating.txt', 11, '2mm', 4, 'LGAD', 'normal')
LGAD2mm5_11 = sensor('IVdata\wafer11\Te2V_Batch1_Wafer11_LGAD_2mm_No5_pad_only_floating.txt', 11, '2mm', 5, 'LGAD', 'normal')
PiN2mm1_11 = sensor('IVdata\wafer11\Te2V_Batch1_Wafer11_PiN_2mm_No1_pad_only_floating.txt', 11, '2mm', 1, 'PiN', 'normal')
LGAD1mm1_11 = sensor('IVdata\wafer11\Te2V_Batch1_Wafer11_LGAD_1mm_No1_pad_only_floating.txt', 11, '1mm', 1, 'LGAD', 'normal')
LGAD1mm2_11 = sensor('IVdata\wafer11\Te2V_Batch1_Wafer11_LGAD_1mm_No2_pad_only_floating.txt', 11, '1mm', 2, 'LGAD', 'normal')
LGAD1mm3_11 = sensor('IVdata\wafer11\Te2V_Batch1_Wafer11_LGAD_1mm_No3_pad_only_floating.txt', 11, '1mm', 3, 'LGAD', 'normal')
LGAD1mm4_11 = sensor('IVdata\wafer11\Te2V_Batch1_Wafer11_LGAD_1mm_No4_pad_only_floating.txt', 11, '1mm', 4, 'LGAD', 'normal')
LGAD1mm5_11 = sensor('IVdata\wafer11\Te2V_Batch1_Wafer11_LGAD_1mm_No5_pad_only_floating.txt', 11, '1mm', 5, 'LGAD', 'normal')
PiN1mm1_11 = sensor('IVdata\wafer11\Te2V_Batch1_Wafer11_PiN_1mm_No1_pad_only_floating.txt', 11, '1mm', 1, 'PiN', 'normal')

LGAD4mm1_3 = sensor('IVdata\wafer3\Te2V_Batch1_Wafer3_LGAD_4mm_No1_pad_only_floating', 3, '4mm', 1, 'LGAD', 'labview')
LGAD4mm3_3 = sensor('IVdata\wafer3\Te2V_Batch1_Wafer3_LGAD_4mm_No3_pad_only_floating', 3, '4mm', 3, 'LGAD', 'labview')
LGAD4mm5_3 = sensor('IVdata\wafer3\Te2V_Batch1_Wafer3_LGAD_4mm_No5_pad_only_floating', 3, '4mm', 5, 'LGAD', 'labview')
LGAD1mm1_3 = sensor('IVdata\wafer3\Te2V_Batch1_Wafer3_LGAD_1mm_No1_pad_only_grounded_fixedRange', 3, '1mm', 1, 'LGAD', 'labview')
LGAD1mm3_3 = sensor('IVdata\wafer3\Te2V_Batch1_Wafer3_LGAD_1mm_No3_pad_only_floating', 3, '1mm', 3, 'LGAD', 'labview')
LGAD1mm5_3 = sensor('IVdata\wafer3\Te2V_Batch1_Wafer3_LGAD_1mm_No5_pad_only_floating', 3, '1mm', 5, 'LGAD', 'labview')
PiN4mm1_3 = sensor('IVdata\wafer3\Te2V_Batch1_Wafer3_PiN_4mm_No1_pad_only_floating', 3, '4mm', 1, 'PiN', 'labview')
PiN4mm3_3 = sensor('IVdata\wafer3\Te2V_Batch1_Wafer3_PiN_4mm_No3_pad_only_floating', 3, '4mm', 3, 'PiN', 'labview')
PiN4mm5_3 = sensor('IVdata\wafer3\Te2V_Batch1_Wafer3_PiN_4mm_No5_pad_only_floating', 3, '4mm', 5, 'PiN', 'labview')
PiN1mm1_3 = sensor('IVdata\wafer3\Te2V_Batch1_Wafer3_PiN_1mm_No1_pad_only_floating', 3, '1mm', 1, 'PiN', 'labview')
PiN1mm3_3 = sensor('IVdata\wafer3\Te2V_Batch1_Wafer3_PiN_1mm_No3_pad_only_floating', 3, '1mm', 3, 'PiN', 'labview')
PiN1mm5_3 = sensor('IVdata\wafer3\Te2V_Batch1_Wafer3_PiN_1mm_No5_pad_only_floating', 3, '1mm', 5, 'PiN', 'labview')

LGAD4mm1_16 = sensor('IVdata\wafer16\Te2V_Batch1_Wafer16_LGAD_4mm_No1_pad_only_floating_fixedrange', 16, '4mm', 1, 'LGAD', 'labview')
LGAD4mm3_16 = sensor('IVdata\wafer16\Te2V_Batch1_Wafer16_LGAD_4mm_No3_pad_only_floating', 16, '4mm', 3, 'LGAD', 'labview')
LGAD4mm5_16 = sensor('IVdata\wafer16\Te2V_Batch1_Wafer16_LGAD_4mm_No5_pad_only_floating', 16, '4mm', 5, 'LGAD', 'labview')
LGAD1mm1_16 = sensor('IVdata\wafer16\Te2V_Batch1_Wafer16_LGAD_1mm_No1_pad_only_floating', 16, '1mm', 1, 'LGAD', 'labview')
LGAD1mm3_16 = sensor('IVdata\wafer16\Te2V_Batch1_Wafer16_LGAD_1mm_No3_pad_only_floating', 16, '1mm', 3, 'LGAD', 'labview')
LGAD1mm5_16 = sensor('IVdata\wafer16\Te2V_Batch1_Wafer16_LGAD_1mm_No5_pad_only_floating', 16, '1mm', 5, 'LGAD', 'labview')
PiN4mm1_16 = sensor('IVdata\wafer16\Te2V_Batch1_Wafer16_PiN_4mm_No1_pad_only_floating', 16, '4mm', 1, 'PiN', 'labview')
PiN4mm3_16 = sensor('IVdata\wafer16\Te2V_Batch1_Wafer16_PiN_4mm_No3_pad_only_floating', 16, '4mm', 3, 'PiN', 'labview')
PiN4mm5_16 = sensor('IVdata\wafer16\Te2V_Batch1_Wafer16_PiN_4mm_No5_pad_only_floating', 16, '4mm', 5, 'PiN', 'labview')
PiN1mm1_16 = sensor('IVdata\wafer16\Te2V_Batch1_Wafer16_PiN_1mm_No1_pad_only_floating', 16, '1mm', 1, 'PiN', 'labview')
PiN1mm3_16 = sensor('IVdata\wafer16\Te2V_Batch1_Wafer16_PiN_1mm_No3_pad_only_floating', 16, '1mm', 3, 'PiN', 'labview')
PiN1mm5_16 = sensor('IVdata\wafer16\Te2V_Batch1_Wafer16_PiN_1mm_No5_pad_only_floating', 16, '1mm', 5, 'PiN', 'labview')

LGAD4mm1_20 = sensor('IVdata\wafer20\Te2V_Batch1_Wafer20_LGAD_4mm_No1_pad_only', 20, '4mm', 1, 'LGAD', 'labview')
LGAD4mm2_20 = sensor('IVdata\wafer20\Te2V_Batch1_Wafer20_LGAD_4mm_No2_pad_only', 20, '4mm', 2, 'LGAD', 'labview')
LGAD4mm3_20 = sensor('IVdata\wafer20\Te2V_Batch1_Wafer20_LGAD_4mm_No3_pad_only', 20, '4mm', 3, 'LGAD', 'labview')
LGAD4mm4_20 = sensor('IVdata\wafer20\Te2V_Batch1_Wafer20_LGAD_4mm_No4_pad_only', 20, '4mm', 4, 'LGAD', 'labview')
LGAD4mm5_20 = sensor('IVdata\wafer20\Te2V_Batch1_Wafer20_LGAD_4mm_No5_pad_only', 20, '4mm', 5, 'LGAD', 'labview')
LGAD2mm1_20 = sensor('IVdata\wafer20\Te2V_Batch1_Wafer20_LGAD_2mm_No1_pad_only', 20, '2mm', 1, 'LGAD', 'labview')
LGAD2mm2_20 = sensor('IVdata\wafer20\Te2V_Batch1_Wafer20_LGAD_2mm_No2_pad_only', 20, '2mm', 2, 'LGAD', 'labview')
LGAD2mm3_20 = sensor('IVdata\wafer20\Te2V_Batch1_Wafer20_LGAD_2mm_No3_pad_only', 20, '2mm', 3, 'LGAD', 'labview')
LGAD2mm4_20 = sensor('IVdata\wafer20\Te2V_Batch1_Wafer20_LGAD_2mm_No4_pad_only', 20, '2mm', 4, 'LGAD', 'labview')
LGAD2mm5_20 = sensor('IVdata\wafer20\Te2V_Batch1_Wafer20_LGAD_2mm_No5_pad_only', 20, '2mm', 5, 'LGAD', 'labview')
LGAD1mm1_20 = sensor('IVdata\wafer20\Te2V_Batch1_Wafer20_LGAD_1mm_No1_pad_only', 20, '1mm', 1, 'LGAD', 'labview')
LGAD1mm2_20 = sensor('IVdata\wafer20\Te2V_Batch1_Wafer20_LGAD_1mm_No2_pad_only', 20, '1mm', 2, 'LGAD', 'labview')
LGAD1mm3_20 = sensor('IVdata\wafer20\Te2V_Batch1_Wafer20_LGAD_1mm_No3_pad_only', 20, '1mm', 3, 'LGAD', 'labview')
LGAD1mm4_20 = sensor('IVdata\wafer20\Te2V_Batch1_Wafer20_LGAD_1mm_No4_pad_only', 20, '1mm', 4, 'LGAD', 'labview')
LGAD1mm5_20 = sensor('IVdata\wafer20\Te2V_Batch1_Wafer20_LGAD_1mm_No5_pad_only', 20, '1mm', 5, 'LGAD', 'labview')
PiN4mm1_20 = sensor('IVdata\wafer20\Te2V_Batch1_Wafer20_PiN_4mm_No1_pad_only_new', 20, '4mm', 1, 'PiN', 'labview')
PiN4mm2_20 = sensor('IVdata\wafer20\Te2V_Batch1_Wafer20_PiN_4mm_No2_pad_only_new', 20, '4mm', 2, 'PiN', 'labview')
PiN4mm3_20 = sensor('IVdata\wafer20\Te2V_Batch1_Wafer20_PiN_4mm_No3_pad_only', 20, '4mm', 3, 'PiN', 'labview')
PiN4mm4_20 = sensor('IVdata\wafer20\Te2V_Batch1_Wafer20_PiN_4mm_No4_pad_only', 20, '4mm', 4, 'PiN', 'labview')
PiN4mm5_20 = sensor('IVdata\wafer20\Te2V_Batch1_Wafer20_PiN_4mm_No5_pad_only', 20, '4mm', 5, 'PiN', 'labview')
PiN2mm1_20 = sensor('IVdata\wafer20\Te2V_Batch1_Wafer20_PiN_2mm_No1_pad_only', 20, '2mm', 1, 'PiN', 'labview')
PiN2mm2_20 = sensor('IVdata\wafer20\Te2V_Batch1_Wafer20_PiN_2mm_No2_pad_only', 20, '2mm', 2, 'PiN', 'labview')
PiN2mm3_20 = sensor('IVdata\wafer20\Te2V_Batch1_Wafer20_PiN_2mm_No3_pad_only', 20, '2mm', 3, 'PiN', 'labview')
PiN2mm4_20 = sensor('IVdata\wafer20\Te2V_Batch1_Wafer20_PiN_2mm_No4_pad_only', 20, '2mm', 4, 'PiN', 'labview')
PiN2mm5_20 = sensor('IVdata\wafer20\Te2V_Batch1_Wafer20_PiN_2mm_No5_pad_only', 20, '2mm', 5, 'PiN', 'labview')
PiN1mm1_20 = sensor('IVdata\wafer20\Te2V_Batch1_Wafer20_PiN_1mm_No1_pad_only', 20, '1mm', 1, 'PiN', 'labview')
PiN1mm2_20 = sensor('IVdata\wafer20\Te2V_Batch1_Wafer20_PiN_1mm_No2_pad_only', 20, '1mm', 2, 'PiN', 'labview')
PiN1mm3_20 = sensor('IVdata\wafer20\Te2V_Batch1_Wafer20_PiN_1mm_No3_pad_only', 20, '1mm', 3, 'PiN', 'labview')
PiN1mm4_20 = sensor('IVdata\wafer20\Te2V_Batch1_Wafer20_PiN_1mm_No4_pad_only', 20, '1mm', 4, 'PiN', 'labview')
PiN1mm5_20 = sensor('IVdata\wafer20\Te2V_Batch1_Wafer20_PiN_1mm_No5_pad_only', 20, '1mm', 5, 'PiN', 'labview')

#diced wafers now

LGAD1mm1_6_diced = sensor('IVdata\diced\IV_wafer_6_LGAD_loc1_1mm_D2_plt.txt', 6, '1mm', 1, 'LGAD', 'normal', True)
LGAD1mm5_6_diced = sensor('IVdata\diced\IV_wafer_6_LGAD_loc5_1mm_D2_plt.txt', 6, '1mm', 5, 'LGAD', 'normal', True)
PiN1mm1_6_diced = sensor('IVdata\diced\IV_wafer_6_PiN_loc1_1mm_D2_plt.txt', 6, '1mm', 1, 'PiN', 'normal', True)

#get all values from excel table
edata = pd.read_csv('Sensor-Data-Table-Live.csv')   #can i change this to read_excel and keep .xlsx format?

LGAD4mm1_6_dic = {'Kbreakdown':edata['Breakdown Voltage (K=4) [V]'][0], 'ATLASbreakdown':float(edata['ALTLAS Breakdown [V]'][0]), 'GLD':edata['Gain Layer Depletion [V]'][0], 'FD':edata['Full Depletion [V]'][0], 'PeakDope':edata['Peak Doping Value [*10^15cm^-3]'][0], 'PeakDopeDepth':edata['Peak Doping Depth [um]'][0], 'FittedPeakDope':edata['Fitted Peak Doping Value [*10^15cm^-3]'][0], 'FittedPeakDopeDepth':edata['Fitted Peak Doping Depth [um]'][0], 'EpiDope':edata['Epitaxial Doping @ 20 um[*10^12cm^-3]'][0], 'ImplantDepth':edata['Implant Depth [um]'][0]}
LGAD4mm2_6_dic = {'Kbreakdown':edata['Breakdown Voltage (K=4) [V]'][1], 'ATLASbreakdown':float(edata['ALTLAS Breakdown [V]'][1])}
LGAD4mm3_6_dic = {'Kbreakdown':edata['Breakdown Voltage (K=4) [V]'][2], 'ATLASbreakdown':float(edata['ALTLAS Breakdown [V]'][2]), 'GLD':edata['Gain Layer Depletion [V]'][2], 'FD':edata['Full Depletion [V]'][2], 'PeakDope':edata['Peak Doping Value [*10^15cm^-3]'][2], 'PeakDopeDepth':edata['Peak Doping Depth [um]'][2], 'FittedPeakDope':edata['Fitted Peak Doping Value [*10^15cm^-3]'][2], 'FittedPeakDopeDepth':edata['Fitted Peak Doping Depth [um]'][2], 'EpiDope':edata['Epitaxial Doping @ 20 um[*10^12cm^-3]'][2], 'ImplantDepth':edata['Implant Depth [um]'][2]}
LGAD4mm4_6_dic = {'Kbreakdown':edata['Breakdown Voltage (K=4) [V]'][3], 'ATLASbreakdown':float(edata['ALTLAS Breakdown [V]'][3])}
LGAD4mm5_6_dic = {'Kbreakdown':edata['Breakdown Voltage (K=4) [V]'][4], 'ATLASbreakdown':float(edata['ALTLAS Breakdown [V]'][4]), 'GLD':edata['Gain Layer Depletion [V]'][4], 'FD':edata['Full Depletion [V]'][4], 'PeakDope':edata['Peak Doping Value [*10^15cm^-3]'][4], 'PeakDopeDepth':edata['Peak Doping Depth [um]'][4], 'FittedPeakDope':edata['Fitted Peak Doping Value [*10^15cm^-3]'][4], 'FittedPeakDopeDepth':edata['Fitted Peak Doping Depth [um]'][4], 'EpiDope':edata['Epitaxial Doping @ 20 um[*10^12cm^-3]'][4], 'ImplantDepth':edata['Implant Depth [um]'][4]}
PiN4mm1_6_dic = {'Kbreakdown':edata['Breakdown Voltage (K=4) [V]'][5], 'ATLASbreakdown':float(edata['ALTLAS Breakdown [V]'][5]), 'GLD':edata['Gain Layer Depletion [V]'][5], 'FD':edata['Full Depletion [V]'][5], 'PeakDope':edata['Peak Doping Value [*10^15cm^-3]'][5], 'PeakDopeDepth':edata['Peak Doping Depth [um]'][5], 'FittedPeakDope':edata['Fitted Peak Doping Value [*10^15cm^-3]'][5], 'FittedPeakDopeDepth':edata['Fitted Peak Doping Depth [um]'][5], 'EpiDope':edata['Epitaxial Doping @ 20 um[*10^12cm^-3]'][5], 'ImplantDepth':edata['Implant Depth [um]'][5]}
LGAD2mm1_6_dic = {'Kbreakdown':edata['Breakdown Voltage (K=4) [V]'][6], 'ATLASbreakdown':float(edata['ALTLAS Breakdown [V]'][6]), 'GLD':edata['Gain Layer Depletion [V]'][6], 'FD':edata['Full Depletion [V]'][6], 'PeakDope':edata['Peak Doping Value [*10^15cm^-3]'][6], 'PeakDopeDepth':edata['Peak Doping Depth [um]'][6], 'FittedPeakDope':edata['Fitted Peak Doping Value [*10^15cm^-3]'][6], 'FittedPeakDopeDepth':edata['Fitted Peak Doping Depth [um]'][6], 'EpiDope':edata['Epitaxial Doping @ 20 um[*10^12cm^-3]'][6], 'ImplantDepth':edata['Implant Depth [um]'][6]}
LGAD2mm2_6_dic = {'Kbreakdown':edata['Breakdown Voltage (K=4) [V]'][7], 'ATLASbreakdown':float(edata['ALTLAS Breakdown [V]'][7])}
LGAD2mm3_6_dic = {'Kbreakdown':edata['Breakdown Voltage (K=4) [V]'][8], 'ATLASbreakdown':float(edata['ALTLAS Breakdown [V]'][8]), 'GLD':edata['Gain Layer Depletion [V]'][8], 'FD':edata['Full Depletion [V]'][8], 'PeakDope':edata['Peak Doping Value [*10^15cm^-3]'][8], 'PeakDopeDepth':edata['Peak Doping Depth [um]'][8], 'FittedPeakDope':edata['Fitted Peak Doping Value [*10^15cm^-3]'][8], 'FittedPeakDopeDepth':edata['Fitted Peak Doping Depth [um]'][8], 'EpiDope':edata['Epitaxial Doping @ 20 um[*10^12cm^-3]'][8], 'ImplantDepth':edata['Implant Depth [um]'][8]}
LGAD2mm4_6_dic = {'Kbreakdown':edata['Breakdown Voltage (K=4) [V]'][9], 'ATLASbreakdown':float(edata['ALTLAS Breakdown [V]'][9])}
LGAD2mm5_6_dic = {'Kbreakdown':edata['Breakdown Voltage (K=4) [V]'][10], 'ATLASbreakdown':float(edata['ALTLAS Breakdown [V]'][10]), 'GLD':edata['Gain Layer Depletion [V]'][10], 'FD':edata['Full Depletion [V]'][10], 'PeakDope':edata['Peak Doping Value [*10^15cm^-3]'][10], 'PeakDopeDepth':edata['Peak Doping Depth [um]'][10], 'FittedPeakDope':edata['Fitted Peak Doping Value [*10^15cm^-3]'][10], 'FittedPeakDopeDepth':edata['Fitted Peak Doping Depth [um]'][10], 'EpiDope':edata['Epitaxial Doping @ 20 um[*10^12cm^-3]'][10], 'ImplantDepth':edata['Implant Depth [um]'][10]}
PiN2mm1_6_dic = {'Kbreakdown':edata['Breakdown Voltage (K=4) [V]'][11], 'ATLASbreakdown':float(edata['ALTLAS Breakdown [V]'][11]), 'GLD':edata['Gain Layer Depletion [V]'][11], 'FD':edata['Full Depletion [V]'][11], 'PeakDope':edata['Peak Doping Value [*10^15cm^-3]'][11], 'PeakDopeDepth':edata['Peak Doping Depth [um]'][11], 'FittedPeakDope':edata['Fitted Peak Doping Value [*10^15cm^-3]'][11], 'FittedPeakDopeDepth':edata['Fitted Peak Doping Depth [um]'][11], 'EpiDope':edata['Epitaxial Doping @ 20 um[*10^12cm^-3]'][11], 'ImplantDepth':edata['Implant Depth [um]'][11]}
LGAD1mm1_6_dic = {'Kbreakdown':edata['Breakdown Voltage (K=4) [V]'][12], 'ATLASbreakdown':float(edata['ALTLAS Breakdown [V]'][12]), 'GLD':edata['Gain Layer Depletion [V]'][12], 'FD':edata['Full Depletion [V]'][12], 'PeakDope':edata['Peak Doping Value [*10^15cm^-3]'][12], 'PeakDopeDepth':edata['Peak Doping Depth [um]'][12], 'FittedPeakDope':edata['Fitted Peak Doping Value [*10^15cm^-3]'][12], 'FittedPeakDopeDepth':edata['Fitted Peak Doping Depth [um]'][12], 'EpiDope':edata['Epitaxial Doping @ 20 um[*10^12cm^-3]'][12], 'ImplantDepth':edata['Implant Depth [um]'][12]}
LGAD1mm2_6_dic = {'Kbreakdown':edata['Breakdown Voltage (K=4) [V]'][13], 'ATLASbreakdown':float(edata['ALTLAS Breakdown [V]'][13]), 'GLD':edata['Gain Layer Depletion [V]'][13], 'FD':edata['Full Depletion [V]'][13], 'PeakDope':edata['Peak Doping Value [*10^15cm^-3]'][13], 'PeakDopeDepth':edata['Peak Doping Depth [um]'][13], 'FittedPeakDope':edata['Fitted Peak Doping Value [*10^15cm^-3]'][13], 'FittedPeakDopeDepth':edata['Fitted Peak Doping Depth [um]'][13], 'EpiDope':edata['Epitaxial Doping @ 20 um[*10^12cm^-3]'][13], 'ImplantDepth':edata['Implant Depth [um]'][13]}
LGAD1mm3_6_dic = {'Kbreakdown':edata['Breakdown Voltage (K=4) [V]'][14], 'ATLASbreakdown':float(edata['ALTLAS Breakdown [V]'][14]), 'GLD':edata['Gain Layer Depletion [V]'][14], 'FD':edata['Full Depletion [V]'][14], 'PeakDope':edata['Peak Doping Value [*10^15cm^-3]'][14], 'PeakDopeDepth':edata['Peak Doping Depth [um]'][14], 'FittedPeakDope':edata['Fitted Peak Doping Value [*10^15cm^-3]'][14], 'FittedPeakDopeDepth':edata['Fitted Peak Doping Depth [um]'][14], 'EpiDope':edata['Epitaxial Doping @ 20 um[*10^12cm^-3]'][14], 'ImplantDepth':edata['Implant Depth [um]'][14]}
LGAD1mm4_6_dic = {'Kbreakdown':edata['Breakdown Voltage (K=4) [V]'][15], 'ATLASbreakdown':float(edata['ALTLAS Breakdown [V]'][15]), 'GLD':edata['Gain Layer Depletion [V]'][15], 'FD':edata['Full Depletion [V]'][15], 'PeakDope':edata['Peak Doping Value [*10^15cm^-3]'][15], 'PeakDopeDepth':edata['Peak Doping Depth [um]'][15], 'FittedPeakDope':edata['Fitted Peak Doping Value [*10^15cm^-3]'][15], 'FittedPeakDopeDepth':edata['Fitted Peak Doping Depth [um]'][15], 'EpiDope':edata['Epitaxial Doping @ 20 um[*10^12cm^-3]'][15], 'ImplantDepth':edata['Implant Depth [um]'][15]}
LGAD1mm5_6_dic = {'Kbreakdown':edata['Breakdown Voltage (K=4) [V]'][16], 'ATLASbreakdown':float(edata['ALTLAS Breakdown [V]'][16]), 'GLD':edata['Gain Layer Depletion [V]'][16], 'FD':edata['Full Depletion [V]'][16], 'PeakDope':edata['Peak Doping Value [*10^15cm^-3]'][16], 'PeakDopeDepth':edata['Peak Doping Depth [um]'][16], 'FittedPeakDope':edata['Fitted Peak Doping Value [*10^15cm^-3]'][16], 'FittedPeakDopeDepth':edata['Fitted Peak Doping Depth [um]'][16], 'EpiDope':edata['Epitaxial Doping @ 20 um[*10^12cm^-3]'][16], 'ImplantDepth':edata['Implant Depth [um]'][16]}
PiN1mm1_6_dic = {'Kbreakdown':edata['Breakdown Voltage (K=4) [V]'][17], 'ATLASbreakdown':float(edata['ALTLAS Breakdown [V]'][17]), 'GLD':edata['Gain Layer Depletion [V]'][17], 'FD':edata['Full Depletion [V]'][17], 'PeakDope':edata['Peak Doping Value [*10^15cm^-3]'][17], 'PeakDopeDepth':edata['Peak Doping Depth [um]'][17], 'FittedPeakDope':edata['Fitted Peak Doping Value [*10^15cm^-3]'][17], 'FittedPeakDopeDepth':edata['Fitted Peak Doping Depth [um]'][17], 'EpiDope':edata['Epitaxial Doping @ 20 um[*10^12cm^-3]'][17], 'ImplantDepth':edata['Implant Depth [um]'][17]}

LGAD4mm1_11_dic = {'Kbreakdown':edata['Breakdown Voltage (K=4) [V]'][19], 'ATLASbreakdown':float(edata['ALTLAS Breakdown [V]'][19]), 'GLD':edata['Gain Layer Depletion [V]'][19], 'FD':edata['Full Depletion [V]'][19], 'PeakDope':edata['Peak Doping Value [*10^15cm^-3]'][19], 'PeakDopeDepth':edata['Peak Doping Depth [um]'][19], 'FittedPeakDope':edata['Fitted Peak Doping Value [*10^15cm^-3]'][19], 'FittedPeakDopeDepth':edata['Fitted Peak Doping Depth [um]'][19], 'EpiDope':edata['Epitaxial Doping @ 20 um[*10^12cm^-3]'][19], 'ImplantDepth':edata['Implant Depth [um]'][19]}
LGAD4mm2_11_dic = {'Kbreakdown':edata['Breakdown Voltage (K=4) [V]'][20], 'ATLASbreakdown':float(edata['ALTLAS Breakdown [V]'][20]), 'GLD':edata['Gain Layer Depletion [V]'][20], 'FD':edata['Full Depletion [V]'][20], 'PeakDope':edata['Peak Doping Value [*10^15cm^-3]'][20], 'PeakDopeDepth':edata['Peak Doping Depth [um]'][20], 'FittedPeakDope':edata['Fitted Peak Doping Value [*10^15cm^-3]'][20], 'FittedPeakDopeDepth':edata['Fitted Peak Doping Depth [um]'][20], 'EpiDope':edata['Epitaxial Doping @ 20 um[*10^12cm^-3]'][20], 'ImplantDepth':edata['Implant Depth [um]'][20]}
LGAD4mm3_11_dic = {'Kbreakdown':edata['Breakdown Voltage (K=4) [V]'][21], 'ATLASbreakdown':float(edata['ALTLAS Breakdown [V]'][21]), 'GLD':edata['Gain Layer Depletion [V]'][21], 'FD':edata['Full Depletion [V]'][21], 'PeakDope':edata['Peak Doping Value [*10^15cm^-3]'][21], 'PeakDopeDepth':edata['Peak Doping Depth [um]'][21], 'FittedPeakDope':edata['Fitted Peak Doping Value [*10^15cm^-3]'][21], 'FittedPeakDopeDepth':edata['Fitted Peak Doping Depth [um]'][21], 'EpiDope':edata['Epitaxial Doping @ 20 um[*10^12cm^-3]'][21], 'ImplantDepth':edata['Implant Depth [um]'][21]}
LGAD4mm4_11_dic = {'Kbreakdown':edata['Breakdown Voltage (K=4) [V]'][22], 'ATLASbreakdown':float(edata['ALTLAS Breakdown [V]'][22]), 'GLD':edata['Gain Layer Depletion [V]'][22], 'FD':edata['Full Depletion [V]'][22], 'PeakDope':edata['Peak Doping Value [*10^15cm^-3]'][22], 'PeakDopeDepth':edata['Peak Doping Depth [um]'][22], 'FittedPeakDope':edata['Fitted Peak Doping Value [*10^15cm^-3]'][22], 'FittedPeakDopeDepth':edata['Fitted Peak Doping Depth [um]'][22], 'EpiDope':edata['Epitaxial Doping @ 20 um[*10^12cm^-3]'][22], 'ImplantDepth':edata['Implant Depth [um]'][22]}
LGAD4mm5_11_dic = {'Kbreakdown':edata['Breakdown Voltage (K=4) [V]'][23], 'ATLASbreakdown':float(edata['ALTLAS Breakdown [V]'][23]), 'GLD':edata['Gain Layer Depletion [V]'][23], 'FD':edata['Full Depletion [V]'][23], 'PeakDope':edata['Peak Doping Value [*10^15cm^-3]'][23], 'PeakDopeDepth':edata['Peak Doping Depth [um]'][23], 'FittedPeakDope':edata['Fitted Peak Doping Value [*10^15cm^-3]'][23], 'FittedPeakDopeDepth':edata['Fitted Peak Doping Depth [um]'][23], 'EpiDope':edata['Epitaxial Doping @ 20 um[*10^12cm^-3]'][23], 'ImplantDepth':edata['Implant Depth [um]'][23]}
PiN4mm1_11_dic = {'Kbreakdown':edata['Breakdown Voltage (K=4) [V]'][24], 'ATLASbreakdown':float(edata['ALTLAS Breakdown [V]'][24]), 'GLD':edata['Gain Layer Depletion [V]'][24], 'FD':edata['Full Depletion [V]'][24], 'PeakDope':edata['Peak Doping Value [*10^15cm^-3]'][24], 'PeakDopeDepth':edata['Peak Doping Depth [um]'][24], 'FittedPeakDope':edata['Fitted Peak Doping Value [*10^15cm^-3]'][24], 'FittedPeakDopeDepth':edata['Fitted Peak Doping Depth [um]'][24], 'EpiDope':edata['Epitaxial Doping @ 20 um[*10^12cm^-3]'][24], 'ImplantDepth':edata['Implant Depth [um]'][24]}
LGAD2mm1_11_dic = {'Kbreakdown':edata['Breakdown Voltage (K=4) [V]'][25], 'ATLASbreakdown':float(edata['ALTLAS Breakdown [V]'][25]), 'GLD':edata['Gain Layer Depletion [V]'][25], 'FD':edata['Full Depletion [V]'][25], 'PeakDope':edata['Peak Doping Value [*10^15cm^-3]'][25], 'PeakDopeDepth':edata['Peak Doping Depth [um]'][25], 'FittedPeakDope':edata['Fitted Peak Doping Value [*10^15cm^-3]'][25], 'FittedPeakDopeDepth':edata['Fitted Peak Doping Depth [um]'][25], 'EpiDope':edata['Epitaxial Doping @ 20 um[*10^12cm^-3]'][25], 'ImplantDepth':edata['Implant Depth [um]'][25]}
LGAD2mm2_11_dic = {'Kbreakdown':edata['Breakdown Voltage (K=4) [V]'][26], 'ATLASbreakdown':float(edata['ALTLAS Breakdown [V]'][26]), 'GLD':edata['Gain Layer Depletion [V]'][26], 'FD':edata['Full Depletion [V]'][26], 'PeakDope':edata['Peak Doping Value [*10^15cm^-3]'][26], 'PeakDopeDepth':edata['Peak Doping Depth [um]'][26], 'FittedPeakDope':edata['Fitted Peak Doping Value [*10^15cm^-3]'][26], 'FittedPeakDopeDepth':edata['Fitted Peak Doping Depth [um]'][26], 'EpiDope':edata['Epitaxial Doping @ 20 um[*10^12cm^-3]'][26], 'ImplantDepth':edata['Implant Depth [um]'][26]}
LGAD2mm3_11_dic = {'Kbreakdown':edata['Breakdown Voltage (K=4) [V]'][27], 'ATLASbreakdown':float(edata['ALTLAS Breakdown [V]'][27]), 'GLD':edata['Gain Layer Depletion [V]'][27], 'FD':edata['Full Depletion [V]'][27], 'PeakDope':edata['Peak Doping Value [*10^15cm^-3]'][27], 'PeakDopeDepth':edata['Peak Doping Depth [um]'][27], 'FittedPeakDope':edata['Fitted Peak Doping Value [*10^15cm^-3]'][27], 'FittedPeakDopeDepth':edata['Fitted Peak Doping Depth [um]'][27], 'EpiDope':edata['Epitaxial Doping @ 20 um[*10^12cm^-3]'][27], 'ImplantDepth':edata['Implant Depth [um]'][27]}
LGAD2mm4_11_dic = {'Kbreakdown':edata['Breakdown Voltage (K=4) [V]'][28], 'ATLASbreakdown':float(edata['ALTLAS Breakdown [V]'][28]), 'GLD':edata['Gain Layer Depletion [V]'][28], 'FD':edata['Full Depletion [V]'][28], 'PeakDope':edata['Peak Doping Value [*10^15cm^-3]'][28], 'PeakDopeDepth':edata['Peak Doping Depth [um]'][28], 'FittedPeakDope':edata['Fitted Peak Doping Value [*10^15cm^-3]'][28], 'FittedPeakDopeDepth':edata['Fitted Peak Doping Depth [um]'][28], 'EpiDope':edata['Epitaxial Doping @ 20 um[*10^12cm^-3]'][28], 'ImplantDepth':edata['Implant Depth [um]'][28]}
LGAD2mm5_11_dic = {'Kbreakdown':edata['Breakdown Voltage (K=4) [V]'][29], 'ATLASbreakdown':float(edata['ALTLAS Breakdown [V]'][29]), 'GLD':edata['Gain Layer Depletion [V]'][29], 'FD':edata['Full Depletion [V]'][29], 'PeakDope':edata['Peak Doping Value [*10^15cm^-3]'][29], 'PeakDopeDepth':edata['Peak Doping Depth [um]'][29], 'FittedPeakDope':edata['Fitted Peak Doping Value [*10^15cm^-3]'][29], 'FittedPeakDopeDepth':edata['Fitted Peak Doping Depth [um]'][29], 'EpiDope':edata['Epitaxial Doping @ 20 um[*10^12cm^-3]'][29], 'ImplantDepth':edata['Implant Depth [um]'][29]}
PiN2mm1_11_dic = {'Kbreakdown':edata['Breakdown Voltage (K=4) [V]'][30], 'ATLASbreakdown':float(edata['ALTLAS Breakdown [V]'][30]), 'GLD':edata['Gain Layer Depletion [V]'][30], 'FD':edata['Full Depletion [V]'][30], 'PeakDope':edata['Peak Doping Value [*10^15cm^-3]'][30], 'PeakDopeDepth':edata['Peak Doping Depth [um]'][30], 'FittedPeakDope':edata['Fitted Peak Doping Value [*10^15cm^-3]'][30], 'FittedPeakDopeDepth':edata['Fitted Peak Doping Depth [um]'][30], 'EpiDope':edata['Epitaxial Doping @ 20 um[*10^12cm^-3]'][30], 'ImplantDepth':edata['Implant Depth [um]'][30]}
LGAD1mm1_11_dic = {'Kbreakdown':edata['Breakdown Voltage (K=4) [V]'][31], 'ATLASbreakdown':float(edata['ALTLAS Breakdown [V]'][31]), 'GLD':edata['Gain Layer Depletion [V]'][31], 'FD':edata['Full Depletion [V]'][31], 'PeakDope':edata['Peak Doping Value [*10^15cm^-3]'][31], 'PeakDopeDepth':edata['Peak Doping Depth [um]'][31], 'FittedPeakDope':edata['Fitted Peak Doping Value [*10^15cm^-3]'][31], 'FittedPeakDopeDepth':edata['Fitted Peak Doping Depth [um]'][31], 'EpiDope':edata['Epitaxial Doping @ 20 um[*10^12cm^-3]'][31], 'ImplantDepth':edata['Implant Depth [um]'][31]}
LGAD1mm2_11_dic = {'Kbreakdown':edata['Breakdown Voltage (K=4) [V]'][32], 'ATLASbreakdown':float(edata['ALTLAS Breakdown [V]'][32]), 'GLD':edata['Gain Layer Depletion [V]'][32], 'FD':edata['Full Depletion [V]'][32], 'PeakDope':edata['Peak Doping Value [*10^15cm^-3]'][32], 'PeakDopeDepth':edata['Peak Doping Depth [um]'][32], 'FittedPeakDope':edata['Fitted Peak Doping Value [*10^15cm^-3]'][32], 'FittedPeakDopeDepth':edata['Fitted Peak Doping Depth [um]'][32], 'EpiDope':edata['Epitaxial Doping @ 20 um[*10^12cm^-3]'][32], 'ImplantDepth':edata['Implant Depth [um]'][32]}
LGAD1mm3_11_dic = {'Kbreakdown':edata['Breakdown Voltage (K=4) [V]'][33], 'ATLASbreakdown':float(edata['ALTLAS Breakdown [V]'][33]), 'GLD':edata['Gain Layer Depletion [V]'][33], 'FD':edata['Full Depletion [V]'][33], 'PeakDope':edata['Peak Doping Value [*10^15cm^-3]'][33], 'PeakDopeDepth':edata['Peak Doping Depth [um]'][33], 'FittedPeakDope':edata['Fitted Peak Doping Value [*10^15cm^-3]'][33], 'FittedPeakDopeDepth':edata['Fitted Peak Doping Depth [um]'][33], 'EpiDope':edata['Epitaxial Doping @ 20 um[*10^12cm^-3]'][33], 'ImplantDepth':edata['Implant Depth [um]'][33]}
LGAD1mm4_11_dic = {'Kbreakdown':edata['Breakdown Voltage (K=4) [V]'][34], 'ATLASbreakdown':float(edata['ALTLAS Breakdown [V]'][34]), 'GLD':edata['Gain Layer Depletion [V]'][34], 'FD':edata['Full Depletion [V]'][34], 'PeakDope':edata['Peak Doping Value [*10^15cm^-3]'][34], 'PeakDopeDepth':edata['Peak Doping Depth [um]'][34], 'FittedPeakDope':edata['Fitted Peak Doping Value [*10^15cm^-3]'][34], 'FittedPeakDopeDepth':edata['Fitted Peak Doping Depth [um]'][34], 'EpiDope':edata['Epitaxial Doping @ 20 um[*10^12cm^-3]'][34], 'ImplantDepth':edata['Implant Depth [um]'][34]}
LGAD1mm5_11_dic = {'Kbreakdown':edata['Breakdown Voltage (K=4) [V]'][35], 'ATLASbreakdown':float(edata['ALTLAS Breakdown [V]'][35]), 'GLD':edata['Gain Layer Depletion [V]'][35], 'FD':edata['Full Depletion [V]'][35], 'PeakDope':edata['Peak Doping Value [*10^15cm^-3]'][35], 'PeakDopeDepth':edata['Peak Doping Depth [um]'][35], 'FittedPeakDope':edata['Fitted Peak Doping Value [*10^15cm^-3]'][35], 'FittedPeakDopeDepth':edata['Fitted Peak Doping Depth [um]'][35], 'EpiDope':edata['Epitaxial Doping @ 20 um[*10^12cm^-3]'][35], 'ImplantDepth':edata['Implant Depth [um]'][35]}
PiN1mm1_11_dic = {'Kbreakdown':edata['Breakdown Voltage (K=4) [V]'][36], 'ATLASbreakdown':float(edata['ALTLAS Breakdown [V]'][36]), 'GLD':edata['Gain Layer Depletion [V]'][36], 'FD':edata['Full Depletion [V]'][36], 'PeakDope':edata['Peak Doping Value [*10^15cm^-3]'][36], 'PeakDopeDepth':edata['Peak Doping Depth [um]'][36], 'FittedPeakDope':edata['Fitted Peak Doping Value [*10^15cm^-3]'][36], 'FittedPeakDopeDepth':edata['Fitted Peak Doping Depth [um]'][36], 'EpiDope':edata['Epitaxial Doping @ 20 um[*10^12cm^-3]'][36], 'ImplantDepth':edata['Implant Depth [um]'][36]}

LGAD4mm1_16_dic = {'Kbreakdown':edata['Breakdown Voltage (K=4) [V]'][38], 'ATLASbreakdown':float(edata['ALTLAS Breakdown [V]'][38]), 'GLD':edata['Gain Layer Depletion [V]'][38], 'FD':edata['Full Depletion [V]'][38], 'PeakDope':edata['Peak Doping Value [*10^15cm^-3]'][38], 'PeakDopeDepth':edata['Peak Doping Depth [um]'][38], 'FittedPeakDope':edata['Fitted Peak Doping Value [*10^15cm^-3]'][38], 'FittedPeakDopeDepth':edata['Fitted Peak Doping Depth [um]'][38], 'EpiDope':edata['Epitaxial Doping @ 20 um[*10^12cm^-3]'][38], 'ImplantDepth':edata['Implant Depth [um]'][38]}
LGAD4mm3_16_dic = {'Kbreakdown':edata['Breakdown Voltage (K=4) [V]'][39], 'ATLASbreakdown':float(edata['ALTLAS Breakdown [V]'][39]), 'GLD':edata['Gain Layer Depletion [V]'][39], 'FD':edata['Full Depletion [V]'][39], 'PeakDope':edata['Peak Doping Value [*10^15cm^-3]'][39], 'PeakDopeDepth':edata['Peak Doping Depth [um]'][39], 'FittedPeakDope':edata['Fitted Peak Doping Value [*10^15cm^-3]'][39], 'FittedPeakDopeDepth':edata['Fitted Peak Doping Depth [um]'][39], 'EpiDope':edata['Epitaxial Doping @ 20 um[*10^12cm^-3]'][39], 'ImplantDepth':edata['Implant Depth [um]'][39]}
LGAD4mm5_16_dic = {'Kbreakdown':edata['Breakdown Voltage (K=4) [V]'][40], 'ATLASbreakdown':float(edata['ALTLAS Breakdown [V]'][40]), 'GLD':edata['Gain Layer Depletion [V]'][40], 'FD':edata['Full Depletion [V]'][40], 'PeakDope':edata['Peak Doping Value [*10^15cm^-3]'][40], 'PeakDopeDepth':edata['Peak Doping Depth [um]'][40], 'FittedPeakDope':edata['Fitted Peak Doping Value [*10^15cm^-3]'][40], 'FittedPeakDopeDepth':edata['Fitted Peak Doping Depth [um]'][40], 'EpiDope':edata['Epitaxial Doping @ 20 um[*10^12cm^-3]'][40], 'ImplantDepth':edata['Implant Depth [um]'][40]}
PiN4mm1_16_dic = {'Kbreakdown':edata['Breakdown Voltage (K=4) [V]'][41], 'ATLASbreakdown':float(edata['ALTLAS Breakdown [V]'][41]), 'GLD':edata['Gain Layer Depletion [V]'][41], 'FD':edata['Full Depletion [V]'][41], 'PeakDope':edata['Peak Doping Value [*10^15cm^-3]'][41], 'PeakDopeDepth':edata['Peak Doping Depth [um]'][41], 'FittedPeakDope':edata['Fitted Peak Doping Value [*10^15cm^-3]'][41], 'FittedPeakDopeDepth':edata['Fitted Peak Doping Depth [um]'][41], 'EpiDope':edata['Epitaxial Doping @ 20 um[*10^12cm^-3]'][41], 'ImplantDepth':edata['Implant Depth [um]'][41]}
PiN4mm3_16_dic = {'Kbreakdown':edata['Breakdown Voltage (K=4) [V]'][42], 'ATLASbreakdown':float(edata['ALTLAS Breakdown [V]'][42]), 'GLD':edata['Gain Layer Depletion [V]'][42], 'FD':edata['Full Depletion [V]'][42], 'PeakDope':edata['Peak Doping Value [*10^15cm^-3]'][42], 'PeakDopeDepth':edata['Peak Doping Depth [um]'][42], 'FittedPeakDope':edata['Fitted Peak Doping Value [*10^15cm^-3]'][42], 'FittedPeakDopeDepth':edata['Fitted Peak Doping Depth [um]'][42], 'EpiDope':edata['Epitaxial Doping @ 20 um[*10^12cm^-3]'][42], 'ImplantDepth':edata['Implant Depth [um]'][42]}
PiN4mm5_16_dic = {'Kbreakdown':edata['Breakdown Voltage (K=4) [V]'][43], 'ATLASbreakdown':float(edata['ALTLAS Breakdown [V]'][43]), 'GLD':edata['Gain Layer Depletion [V]'][43], 'FD':edata['Full Depletion [V]'][43], 'PeakDope':edata['Peak Doping Value [*10^15cm^-3]'][43], 'PeakDopeDepth':edata['Peak Doping Depth [um]'][43], 'FittedPeakDope':edata['Fitted Peak Doping Value [*10^15cm^-3]'][43], 'FittedPeakDopeDepth':edata['Fitted Peak Doping Depth [um]'][43], 'EpiDope':edata['Epitaxial Doping @ 20 um[*10^12cm^-3]'][43], 'ImplantDepth':edata['Implant Depth [um]'][43]}
LGAD1mm1_16_dic = {'Kbreakdown':edata['Breakdown Voltage (K=4) [V]'][44], 'ATLASbreakdown':float(edata['ALTLAS Breakdown [V]'][44]), 'GLD':edata['Gain Layer Depletion [V]'][44], 'FD':edata['Full Depletion [V]'][44], 'PeakDope':edata['Peak Doping Value [*10^15cm^-3]'][44], 'PeakDopeDepth':edata['Peak Doping Depth [um]'][44], 'FittedPeakDope':edata['Fitted Peak Doping Value [*10^15cm^-3]'][44], 'FittedPeakDopeDepth':edata['Fitted Peak Doping Depth [um]'][44], 'EpiDope':edata['Epitaxial Doping @ 20 um[*10^12cm^-3]'][44], 'ImplantDepth':edata['Implant Depth [um]'][44]}
LGAD1mm3_16_dic = {'Kbreakdown':edata['Breakdown Voltage (K=4) [V]'][45], 'ATLASbreakdown':float(edata['ALTLAS Breakdown [V]'][45]), 'GLD':edata['Gain Layer Depletion [V]'][45], 'FD':edata['Full Depletion [V]'][45], 'PeakDope':edata['Peak Doping Value [*10^15cm^-3]'][45], 'PeakDopeDepth':edata['Peak Doping Depth [um]'][45], 'FittedPeakDope':edata['Fitted Peak Doping Value [*10^15cm^-3]'][45], 'FittedPeakDopeDepth':edata['Fitted Peak Doping Depth [um]'][45], 'EpiDope':edata['Epitaxial Doping @ 20 um[*10^12cm^-3]'][45], 'ImplantDepth':edata['Implant Depth [um]'][45]}
LGAD1mm5_16_dic = {'Kbreakdown':edata['Breakdown Voltage (K=4) [V]'][46], 'ATLASbreakdown':float(edata['ALTLAS Breakdown [V]'][46]), 'GLD':edata['Gain Layer Depletion [V]'][46], 'FD':edata['Full Depletion [V]'][46], 'PeakDope':edata['Peak Doping Value [*10^15cm^-3]'][46], 'PeakDopeDepth':edata['Peak Doping Depth [um]'][46], 'FittedPeakDope':edata['Fitted Peak Doping Value [*10^15cm^-3]'][46], 'FittedPeakDopeDepth':edata['Fitted Peak Doping Depth [um]'][46], 'EpiDope':edata['Epitaxial Doping @ 20 um[*10^12cm^-3]'][46], 'ImplantDepth':edata['Implant Depth [um]'][46]}
PiN1mm1_16_dic = {'Kbreakdown':edata['Breakdown Voltage (K=4) [V]'][47], 'ATLASbreakdown':float(edata['ALTLAS Breakdown [V]'][47]), 'GLD':edata['Gain Layer Depletion [V]'][47], 'FD':edata['Full Depletion [V]'][47], 'PeakDope':edata['Peak Doping Value [*10^15cm^-3]'][47], 'PeakDopeDepth':edata['Peak Doping Depth [um]'][47], 'FittedPeakDope':edata['Fitted Peak Doping Value [*10^15cm^-3]'][47], 'FittedPeakDopeDepth':edata['Fitted Peak Doping Depth [um]'][47], 'EpiDope':edata['Epitaxial Doping @ 20 um[*10^12cm^-3]'][47], 'ImplantDepth':edata['Implant Depth [um]'][47]}
PiN1mm3_16_dic = {'Kbreakdown':edata['Breakdown Voltage (K=4) [V]'][48], 'ATLASbreakdown':float(edata['ALTLAS Breakdown [V]'][48]), 'GLD':edata['Gain Layer Depletion [V]'][48], 'FD':edata['Full Depletion [V]'][48], 'PeakDope':edata['Peak Doping Value [*10^15cm^-3]'][48], 'PeakDopeDepth':edata['Peak Doping Depth [um]'][48], 'FittedPeakDope':edata['Fitted Peak Doping Value [*10^15cm^-3]'][48], 'FittedPeakDopeDepth':edata['Fitted Peak Doping Depth [um]'][48], 'EpiDope':edata['Epitaxial Doping @ 20 um[*10^12cm^-3]'][48], 'ImplantDepth':edata['Implant Depth [um]'][48]}
PiN1mm5_16_dic = {'Kbreakdown':edata['Breakdown Voltage (K=4) [V]'][49], 'ATLASbreakdown':float(edata['ALTLAS Breakdown [V]'][49]), 'GLD':edata['Gain Layer Depletion [V]'][49], 'FD':edata['Full Depletion [V]'][49], 'PeakDope':edata['Peak Doping Value [*10^15cm^-3]'][49], 'PeakDopeDepth':edata['Peak Doping Depth [um]'][49], 'FittedPeakDope':edata['Fitted Peak Doping Value [*10^15cm^-3]'][49], 'FittedPeakDopeDepth':edata['Fitted Peak Doping Depth [um]'][49], 'EpiDope':edata['Epitaxial Doping @ 20 um[*10^12cm^-3]'][49], 'ImplantDepth':edata['Implant Depth [um]'][49]}

LGAD4mm1_20_dic = {'Kbreakdown':edata['Breakdown Voltage (K=4) [V]'][51], 'ATLASbreakdown':float(edata['ALTLAS Breakdown [V]'][51]), 'GLD':edata['Gain Layer Depletion [V]'][51], 'FD':edata['Full Depletion [V]'][51], 'PeakDope':edata['Peak Doping Value [*10^15cm^-3]'][51], 'PeakDopeDepth':edata['Peak Doping Depth [um]'][51], 'FittedPeakDope':edata['Fitted Peak Doping Value [*10^15cm^-3]'][51], 'FittedPeakDopeDepth':edata['Fitted Peak Doping Depth [um]'][51], 'EpiDope':edata['Epitaxial Doping @ 20 um[*10^12cm^-3]'][51], 'ImplantDepth':edata['Implant Depth [um]'][51]}
LGAD4mm3_20_dic = {'Kbreakdown':edata['Breakdown Voltage (K=4) [V]'][52], 'ATLASbreakdown':float(edata['ALTLAS Breakdown [V]'][52]), 'GLD':edata['Gain Layer Depletion [V]'][52], 'FD':edata['Full Depletion [V]'][52], 'PeakDope':edata['Peak Doping Value [*10^15cm^-3]'][52], 'PeakDopeDepth':edata['Peak Doping Depth [um]'][52], 'FittedPeakDope':edata['Fitted Peak Doping Value [*10^15cm^-3]'][52], 'FittedPeakDopeDepth':edata['Fitted Peak Doping Depth [um]'][52], 'EpiDope':edata['Epitaxial Doping @ 20 um[*10^12cm^-3]'][52], 'ImplantDepth':edata['Implant Depth [um]'][52]}
LGAD4mm5_20_dic = {'Kbreakdown':edata['Breakdown Voltage (K=4) [V]'][53], 'ATLASbreakdown':float(edata['ALTLAS Breakdown [V]'][53]), 'GLD':edata['Gain Layer Depletion [V]'][53], 'FD':edata['Full Depletion [V]'][53], 'PeakDope':edata['Peak Doping Value [*10^15cm^-3]'][53], 'PeakDopeDepth':edata['Peak Doping Depth [um]'][53], 'FittedPeakDope':edata['Fitted Peak Doping Value [*10^15cm^-3]'][53], 'FittedPeakDopeDepth':edata['Fitted Peak Doping Depth [um]'][53], 'EpiDope':edata['Epitaxial Doping @ 20 um[*10^12cm^-3]'][53], 'ImplantDepth':edata['Implant Depth [um]'][53]}
PiN4mm1_20_dic = {'Kbreakdown':edata['Breakdown Voltage (K=4) [V]'][54], 'ATLASbreakdown':float(edata['ALTLAS Breakdown [V]'][54]), 'GLD':edata['Gain Layer Depletion [V]'][54], 'FD':edata['Full Depletion [V]'][54], 'PeakDope':edata['Peak Doping Value [*10^15cm^-3]'][54], 'PeakDopeDepth':edata['Peak Doping Depth [um]'][54], 'FittedPeakDope':edata['Fitted Peak Doping Value [*10^15cm^-3]'][54], 'FittedPeakDopeDepth':edata['Fitted Peak Doping Depth [um]'][54], 'EpiDope':edata['Epitaxial Doping @ 20 um[*10^12cm^-3]'][54], 'ImplantDepth':edata['Implant Depth [um]'][54]}
PiN4mm3_20_dic = {'Kbreakdown':edata['Breakdown Voltage (K=4) [V]'][55], 'ATLASbreakdown':float(edata['ALTLAS Breakdown [V]'][55]), 'GLD':edata['Gain Layer Depletion [V]'][55], 'FD':edata['Full Depletion [V]'][55], 'PeakDope':edata['Peak Doping Value [*10^15cm^-3]'][55], 'PeakDopeDepth':edata['Peak Doping Depth [um]'][55], 'FittedPeakDope':edata['Fitted Peak Doping Value [*10^15cm^-3]'][55], 'FittedPeakDopeDepth':edata['Fitted Peak Doping Depth [um]'][55], 'EpiDope':edata['Epitaxial Doping @ 20 um[*10^12cm^-3]'][55], 'ImplantDepth':edata['Implant Depth [um]'][55]}
PiN4mm5_20_dic = {'Kbreakdown':edata['Breakdown Voltage (K=4) [V]'][56], 'ATLASbreakdown':float(edata['ALTLAS Breakdown [V]'][56]), 'GLD':edata['Gain Layer Depletion [V]'][56], 'FD':edata['Full Depletion [V]'][56], 'PeakDope':edata['Peak Doping Value [*10^15cm^-3]'][56], 'PeakDopeDepth':edata['Peak Doping Depth [um]'][56], 'FittedPeakDope':edata['Fitted Peak Doping Value [*10^15cm^-3]'][56], 'FittedPeakDopeDepth':edata['Fitted Peak Doping Depth [um]'][56], 'EpiDope':edata['Epitaxial Doping @ 20 um[*10^12cm^-3]'][56], 'ImplantDepth':edata['Implant Depth [um]'][56]}
LGAD2mm1_20_dic = {'Kbreakdown':edata['Breakdown Voltage (K=4) [V]'][57], 'ATLASbreakdown':float(edata['ALTLAS Breakdown [V]'][57]), 'GLD':edata['Gain Layer Depletion [V]'][57], 'FD':edata['Full Depletion [V]'][57], 'PeakDope':edata['Peak Doping Value [*10^15cm^-3]'][57], 'PeakDopeDepth':edata['Peak Doping Depth [um]'][57], 'FittedPeakDope':edata['Fitted Peak Doping Value [*10^15cm^-3]'][57], 'FittedPeakDopeDepth':edata['Fitted Peak Doping Depth [um]'][57], 'EpiDope':edata['Epitaxial Doping @ 20 um[*10^12cm^-3]'][57], 'ImplantDepth':edata['Implant Depth [um]'][57]}
PiN2mm1_20_dic = {'Kbreakdown':edata['Breakdown Voltage (K=4) [V]'][58], 'ATLASbreakdown':float(edata['ALTLAS Breakdown [V]'][58]), 'GLD':edata['Gain Layer Depletion [V]'][58], 'FD':edata['Full Depletion [V]'][58], 'PeakDope':edata['Peak Doping Value [*10^15cm^-3]'][58], 'PeakDopeDepth':edata['Peak Doping Depth [um]'][58], 'FittedPeakDope':edata['Fitted Peak Doping Value [*10^15cm^-3]'][58], 'FittedPeakDopeDepth':edata['Fitted Peak Doping Depth [um]'][58], 'EpiDope':edata['Epitaxial Doping @ 20 um[*10^12cm^-3]'][58], 'ImplantDepth':edata['Implant Depth [um]'][58]}
LGAD1mm1_20_dic = {'Kbreakdown':edata['Breakdown Voltage (K=4) [V]'][59], 'ATLASbreakdown':float(edata['ALTLAS Breakdown [V]'][59]), 'GLD':edata['Gain Layer Depletion [V]'][59], 'FD':edata['Full Depletion [V]'][59], 'PeakDope':edata['Peak Doping Value [*10^15cm^-3]'][59], 'PeakDopeDepth':edata['Peak Doping Depth [um]'][59], 'FittedPeakDope':edata['Fitted Peak Doping Value [*10^15cm^-3]'][59], 'FittedPeakDopeDepth':edata['Fitted Peak Doping Depth [um]'][59], 'EpiDope':edata['Epitaxial Doping @ 20 um[*10^12cm^-3]'][59], 'ImplantDepth':edata['Implant Depth [um]'][59]}
LGAD1mm3_20_dic = {'Kbreakdown':edata['Breakdown Voltage (K=4) [V]'][60], 'ATLASbreakdown':float(edata['ALTLAS Breakdown [V]'][60]), 'GLD':edata['Gain Layer Depletion [V]'][60], 'FD':edata['Full Depletion [V]'][60], 'PeakDope':edata['Peak Doping Value [*10^15cm^-3]'][60], 'PeakDopeDepth':edata['Peak Doping Depth [um]'][60], 'FittedPeakDope':edata['Fitted Peak Doping Value [*10^15cm^-3]'][60], 'FittedPeakDopeDepth':edata['Fitted Peak Doping Depth [um]'][60], 'EpiDope':edata['Epitaxial Doping @ 20 um[*10^12cm^-3]'][60], 'ImplantDepth':edata['Implant Depth [um]'][60]}
LGAD1mm5_20_dic = {'Kbreakdown':edata['Breakdown Voltage (K=4) [V]'][61], 'ATLASbreakdown':float(edata['ALTLAS Breakdown [V]'][61]), 'GLD':edata['Gain Layer Depletion [V]'][61], 'FD':edata['Full Depletion [V]'][61], 'PeakDope':edata['Peak Doping Value [*10^15cm^-3]'][61], 'PeakDopeDepth':edata['Peak Doping Depth [um]'][61], 'FittedPeakDope':edata['Fitted Peak Doping Value [*10^15cm^-3]'][61], 'FittedPeakDopeDepth':edata['Fitted Peak Doping Depth [um]'][61], 'EpiDope':edata['Epitaxial Doping @ 20 um[*10^12cm^-3]'][61], 'ImplantDepth':edata['Implant Depth [um]'][61]}
PiN1mm1_20_dic = {'Kbreakdown':edata['Breakdown Voltage (K=4) [V]'][62], 'ATLASbreakdown':float(edata['ALTLAS Breakdown [V]'][62]), 'GLD':edata['Gain Layer Depletion [V]'][62], 'FD':edata['Full Depletion [V]'][62], 'PeakDope':edata['Peak Doping Value [*10^15cm^-3]'][62], 'PeakDopeDepth':edata['Peak Doping Depth [um]'][62], 'FittedPeakDope':edata['Fitted Peak Doping Value [*10^15cm^-3]'][62], 'FittedPeakDopeDepth':edata['Fitted Peak Doping Depth [um]'][62], 'EpiDope':edata['Epitaxial Doping @ 20 um[*10^12cm^-3]'][62], 'ImplantDepth':edata['Implant Depth [um]'][62]}
PiN1mm3_20_dic = {'Kbreakdown':edata['Breakdown Voltage (K=4) [V]'][63], 'ATLASbreakdown':float(edata['ALTLAS Breakdown [V]'][63]), 'GLD':edata['Gain Layer Depletion [V]'][63], 'FD':edata['Full Depletion [V]'][63], 'PeakDope':edata['Peak Doping Value [*10^15cm^-3]'][63], 'PeakDopeDepth':edata['Peak Doping Depth [um]'][63], 'FittedPeakDope':edata['Fitted Peak Doping Value [*10^15cm^-3]'][63], 'FittedPeakDopeDepth':edata['Fitted Peak Doping Depth [um]'][63], 'EpiDope':edata['Epitaxial Doping @ 20 um[*10^12cm^-3]'][63], 'ImplantDepth':edata['Implant Depth [um]'][63]}
PiN1mm5_30_dic = {'Kbreakdown':edata['Breakdown Voltage (K=4) [V]'][64], 'ATLASbreakdown':float(edata['ALTLAS Breakdown [V]'][64]), 'GLD':edata['Gain Layer Depletion [V]'][64], 'FD':edata['Full Depletion [V]'][64], 'PeakDope':edata['Peak Doping Value [*10^15cm^-3]'][64], 'PeakDopeDepth':edata['Peak Doping Depth [um]'][64], 'FittedPeakDope':edata['Fitted Peak Doping Value [*10^15cm^-3]'][64], 'FittedPeakDopeDepth':edata['Fitted Peak Doping Depth [um]'][64], 'EpiDope':edata['Epitaxial Doping @ 20 um[*10^12cm^-3]'][64], 'ImplantDepth':edata['Implant Depth [um]'][64]}

LGAD4mm1_3_dic = {'Kbreakdown':edata['Breakdown Voltage (K=4) [V]'][66], 'ATLASbreakdown':float(edata['ALTLAS Breakdown [V]'][66]), 'GLD':edata['Gain Layer Depletion [V]'][66], 'FD':edata['Full Depletion [V]'][66], 'PeakDope':edata['Peak Doping Value [*10^15cm^-3]'][66], 'PeakDopeDepth':edata['Peak Doping Depth [um]'][66], 'FittedPeakDope':edata['Fitted Peak Doping Value [*10^15cm^-3]'][66], 'FittedPeakDopeDepth':edata['Fitted Peak Doping Depth [um]'][66], 'EpiDope':edata['Epitaxial Doping @ 20 um[*10^12cm^-3]'][66], 'ImplantDepth':edata['Implant Depth [um]'][66]}
LGAD4mm3_3_dic = {'Kbreakdown':edata['Breakdown Voltage (K=4) [V]'][67], 'ATLASbreakdown':float(edata['ALTLAS Breakdown [V]'][67]), 'GLD':edata['Gain Layer Depletion [V]'][67], 'FD':edata['Full Depletion [V]'][67], 'PeakDope':edata['Peak Doping Value [*10^15cm^-3]'][67], 'PeakDopeDepth':edata['Peak Doping Depth [um]'][67], 'FittedPeakDope':edata['Fitted Peak Doping Value [*10^15cm^-3]'][67], 'FittedPeakDopeDepth':edata['Fitted Peak Doping Depth [um]'][67], 'EpiDope':edata['Epitaxial Doping @ 20 um[*10^12cm^-3]'][67], 'ImplantDepth':edata['Implant Depth [um]'][67]}
LGAD4mm5_3_dic = {'Kbreakdown':edata['Breakdown Voltage (K=4) [V]'][68], 'ATLASbreakdown':float(edata['ALTLAS Breakdown [V]'][68]), 'GLD':edata['Gain Layer Depletion [V]'][68], 'FD':edata['Full Depletion [V]'][68], 'PeakDope':edata['Peak Doping Value [*10^15cm^-3]'][68], 'PeakDopeDepth':edata['Peak Doping Depth [um]'][68], 'FittedPeakDope':edata['Fitted Peak Doping Value [*10^15cm^-3]'][68], 'FittedPeakDopeDepth':edata['Fitted Peak Doping Depth [um]'][68], 'EpiDope':edata['Epitaxial Doping @ 20 um[*10^12cm^-3]'][68], 'ImplantDepth':edata['Implant Depth [um]'][68]}
PiN4mm1_3_dic = {'Kbreakdown':edata['Breakdown Voltage (K=4) [V]'][69], 'ATLASbreakdown':float(edata['ALTLAS Breakdown [V]'][69]), 'GLD':edata['Gain Layer Depletion [V]'][69], 'FD':edata['Full Depletion [V]'][69], 'PeakDope':edata['Peak Doping Value [*10^15cm^-3]'][69], 'PeakDopeDepth':edata['Peak Doping Depth [um]'][69], 'FittedPeakDope':edata['Fitted Peak Doping Value [*10^15cm^-3]'][69], 'FittedPeakDopeDepth':edata['Fitted Peak Doping Depth [um]'][69], 'EpiDope':edata['Epitaxial Doping @ 20 um[*10^12cm^-3]'][69], 'ImplantDepth':edata['Implant Depth [um]'][69]}
PiN4mm3_3_dic = {'Kbreakdown':edata['Breakdown Voltage (K=4) [V]'][70], 'ATLASbreakdown':float(edata['ALTLAS Breakdown [V]'][70]), 'GLD':edata['Gain Layer Depletion [V]'][70], 'FD':edata['Full Depletion [V]'][70], 'PeakDope':edata['Peak Doping Value [*10^15cm^-3]'][70], 'PeakDopeDepth':edata['Peak Doping Depth [um]'][70], 'FittedPeakDope':edata['Fitted Peak Doping Value [*10^15cm^-3]'][70], 'FittedPeakDopeDepth':edata['Fitted Peak Doping Depth [um]'][70], 'EpiDope':edata['Epitaxial Doping @ 20 um[*10^12cm^-3]'][70], 'ImplantDepth':edata['Implant Depth [um]'][70]}
PiN4mm5_3_dic = {'Kbreakdown':edata['Breakdown Voltage (K=4) [V]'][71], 'ATLASbreakdown':float(edata['ALTLAS Breakdown [V]'][71]), 'GLD':edata['Gain Layer Depletion [V]'][71], 'FD':edata['Full Depletion [V]'][71], 'PeakDope':edata['Peak Doping Value [*10^15cm^-3]'][71], 'PeakDopeDepth':edata['Peak Doping Depth [um]'][71], 'FittedPeakDope':edata['Fitted Peak Doping Value [*10^15cm^-3]'][71], 'FittedPeakDopeDepth':edata['Fitted Peak Doping Depth [um]'][71], 'EpiDope':edata['Epitaxial Doping @ 20 um[*10^12cm^-3]'][71], 'ImplantDepth':edata['Implant Depth [um]'][71]}
LGAD2mm1_3_dic = {'Kbreakdown':edata['Breakdown Voltage (K=4) [V]'][72], 'ATLASbreakdown':float(edata['ALTLAS Breakdown [V]'][72]), 'GLD':edata['Gain Layer Depletion [V]'][72], 'FD':edata['Full Depletion [V]'][72], 'PeakDope':edata['Peak Doping Value [*10^15cm^-3]'][72], 'PeakDopeDepth':edata['Peak Doping Depth [um]'][72], 'FittedPeakDope':edata['Fitted Peak Doping Value [*10^15cm^-3]'][72], 'FittedPeakDopeDepth':edata['Fitted Peak Doping Depth [um]'][72], 'EpiDope':edata['Epitaxial Doping @ 20 um[*10^12cm^-3]'][72], 'ImplantDepth':edata['Implant Depth [um]'][72]}
PiN2mm1_3_dic = {'Kbreakdown':edata['Breakdown Voltage (K=4) [V]'][73], 'ATLASbreakdown':float(edata['ALTLAS Breakdown [V]'][73]), 'GLD':edata['Gain Layer Depletion [V]'][73], 'FD':edata['Full Depletion [V]'][73], 'PeakDope':edata['Peak Doping Value [*10^15cm^-3]'][73], 'PeakDopeDepth':edata['Peak Doping Depth [um]'][73], 'FittedPeakDope':edata['Fitted Peak Doping Value [*10^15cm^-3]'][73], 'FittedPeakDopeDepth':edata['Fitted Peak Doping Depth [um]'][73], 'EpiDope':edata['Epitaxial Doping @ 20 um[*10^12cm^-3]'][73], 'ImplantDepth':edata['Implant Depth [um]'][73]}
LGAD1mm1_3_dic = {'Kbreakdown':edata['Breakdown Voltage (K=4) [V]'][74], 'ATLASbreakdown':float(edata['ALTLAS Breakdown [V]'][74]), 'GLD':edata['Gain Layer Depletion [V]'][74], 'FD':edata['Full Depletion [V]'][74], 'PeakDope':edata['Peak Doping Value [*10^15cm^-3]'][74], 'PeakDopeDepth':edata['Peak Doping Depth [um]'][74], 'FittedPeakDope':edata['Fitted Peak Doping Value [*10^15cm^-3]'][74], 'FittedPeakDopeDepth':edata['Fitted Peak Doping Depth [um]'][74], 'EpiDope':edata['Epitaxial Doping @ 20 um[*10^12cm^-3]'][74], 'ImplantDepth':edata['Implant Depth [um]'][74]}
LGAD1mm3_3_dic = {'Kbreakdown':edata['Breakdown Voltage (K=4) [V]'][75], 'ATLASbreakdown':float(edata['ALTLAS Breakdown [V]'][75]), 'GLD':edata['Gain Layer Depletion [V]'][75], 'FD':edata['Full Depletion [V]'][75], 'PeakDope':edata['Peak Doping Value [*10^15cm^-3]'][75], 'PeakDopeDepth':edata['Peak Doping Depth [um]'][75], 'FittedPeakDope':edata['Fitted Peak Doping Value [*10^15cm^-3]'][75], 'FittedPeakDopeDepth':edata['Fitted Peak Doping Depth [um]'][75], 'EpiDope':edata['Epitaxial Doping @ 20 um[*10^12cm^-3]'][75], 'ImplantDepth':edata['Implant Depth [um]'][75]}
LGAD1mm5_3_dic = {'Kbreakdown':edata['Breakdown Voltage (K=4) [V]'][76], 'ATLASbreakdown':float(edata['ALTLAS Breakdown [V]'][76]), 'GLD':edata['Gain Layer Depletion [V]'][76], 'FD':edata['Full Depletion [V]'][76], 'PeakDope':edata['Peak Doping Value [*10^15cm^-3]'][76], 'PeakDopeDepth':edata['Peak Doping Depth [um]'][76], 'FittedPeakDope':edata['Fitted Peak Doping Value [*10^15cm^-3]'][76], 'FittedPeakDopeDepth':edata['Fitted Peak Doping Depth [um]'][76], 'EpiDope':edata['Epitaxial Doping @ 20 um[*10^12cm^-3]'][76], 'ImplantDepth':edata['Implant Depth [um]'][76]}
PiN1mm1_3_dic = {'Kbreakdown':edata['Breakdown Voltage (K=4) [V]'][77], 'ATLASbreakdown':float(edata['ALTLAS Breakdown [V]'][77]), 'GLD':edata['Gain Layer Depletion [V]'][77], 'FD':edata['Full Depletion [V]'][77], 'PeakDope':edata['Peak Doping Value [*10^15cm^-3]'][77], 'PeakDopeDepth':edata['Peak Doping Depth [um]'][77], 'FittedPeakDope':edata['Fitted Peak Doping Value [*10^15cm^-3]'][77], 'FittedPeakDopeDepth':edata['Fitted Peak Doping Depth [um]'][77], 'EpiDope':edata['Epitaxial Doping @ 20 um[*10^12cm^-3]'][77], 'ImplantDepth':edata['Implant Depth [um]'][77]}
PiN1mm3_3_dic = {'Kbreakdown':edata['Breakdown Voltage (K=4) [V]'][78], 'ATLASbreakdown':float(edata['ALTLAS Breakdown [V]'][78]), 'GLD':edata['Gain Layer Depletion [V]'][78], 'FD':edata['Full Depletion [V]'][78], 'PeakDope':edata['Peak Doping Value [*10^15cm^-3]'][78], 'PeakDopeDepth':edata['Peak Doping Depth [um]'][78], 'FittedPeakDope':edata['Fitted Peak Doping Value [*10^15cm^-3]'][78], 'FittedPeakDopeDepth':edata['Fitted Peak Doping Depth [um]'][78], 'EpiDope':edata['Epitaxial Doping @ 20 um[*10^12cm^-3]'][78], 'ImplantDepth':edata['Implant Depth [um]'][78]}
PiN1mm5_3_dic = {'Kbreakdown':edata['Breakdown Voltage (K=4) [V]'][79], 'ATLASbreakdown':float(edata['ALTLAS Breakdown [V]'][79]), 'GLD':edata['Gain Layer Depletion [V]'][79], 'FD':edata['Full Depletion [V]'][79], 'PeakDope':edata['Peak Doping Value [*10^15cm^-3]'][79], 'PeakDopeDepth':edata['Peak Doping Depth [um]'][79], 'FittedPeakDope':edata['Fitted Peak Doping Value [*10^15cm^-3]'][79], 'FittedPeakDopeDepth':edata['Fitted Peak Doping Depth [um]'][79], 'EpiDope':edata['Epitaxial Doping @ 20 um[*10^12cm^-3]'][79], 'ImplantDepth':edata['Implant Depth [um]'][79]}


def getdata(sensor):

    if sensor.datastyle == 'normal':
        rawdata = []
        data = []
        V = []
        I = []
        dI = []
        
        with open(sensor.file, 'r') as filestream:
            for line in filestream:
                currentline = line.split(',')
                rawdata.append(currentline)
        rawdata = rawdata[12:-2]
        for i in range(0, len(rawdata)):
            data.append(rawdata[i][0:3])
            V.append(abs(float(data[i][0])))
            I.append(abs(float(data[i][1])))
            dI.append(abs(float(data[i][2])))
            
        return V, I, dI
    
    elif sensor.datastyle == 'labview':
        
        rawdata = []
        data = []
        V = []
        I = []
        dI = []
        startline = 0
        
        with open(sensor.file, 'r') as filestream:
            for line in filestream:
                currentline = line.split('\t')
                rawdata.append(currentline)
                
        #start reading from BEGIN in .txt
        for i in range(0, len(rawdata)):
            if 'BEGIN' in rawdata[i][0]:
                startline = i+1

        data = rawdata[startline:-2]
        
        #print(data[0])
        for i in range(0, len(data)):
            if i%2 == 0: #if i is even
                #sometimes the I values near the end are 9e+37, so need to not count them
                if abs(float(data[i][3])) < 1:
                    I.append(abs(float(data[i][3])))
                    V.append(abs(float(data[i][1])))

        return V, I, dI


def colourgrabber(sensor):
    """
    if sensor.size == '4mm':
        return 'red'
    elif sensor.size == '2mm':
        return 'green'
    elif sensor.size == '1mm':
        return 'blue'
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
        return 'green'
        
def linestylegrabber(sensor):
    if sensor.type == 'LGAD':
        return 'solid'
    elif sensor.type == 'PiN':
        return 'dashed'

def IV(sensorlist):
    """
    takes in a sensor file or a list of sensor files and plots them.
    """
    fig, ax = plt.subplots()
    plt.rcParams["figure.figsize"] = [12,9]
    plt.ylabel('Current [A]', fontsize = 22)
    plt.xlabel('Bias Voltage [V]', fontsize = 22)
    plt.yscale('log')
    #plt.ylim(10e-12, 10e-4)
    plt.xlim(-20, 800)
    ax.minorticks_on()
    ax.grid(which='major', linestyle='-', linewidth='0.5', color='grey')
    ax.grid(which='minor', linestyle=':', linewidth='0.5', color='grey')
    plt.title('IV Characteristics', fontsize=22)
    plt.xticks(fontsize = 20)
    plt.yticks(fontsize = 20)
    
    #plotted a few breakdowns for my seminar
    #plt.axvline(x = 378, linewidth = 1.5, linestyle = '-.', color = 'black', label = '$K = 4$ Breakdown of LGAD')
    #plt.axvline(x = 440, linewidth = 1.5, linestyle = '-.', color = 'purple', label = 'ATLAS Breakdown of LGAD')
    #plt.axvline(x = 396, linewidth = 1.5, linestyle = '-.', color = 'green', label = '$K = 4$ Breakdown of PiN')
    #plt.axvline(x = 590, linewidth = 1.5, linestyle = '-.', color = 'orange', label = 'ATLAS Breakdown of LGAD')
    
    if type(sensorlist) == list:
        for sensor in sensorlist:  
            V = getdata(sensor)[0]
            I = getdata(sensor)[1]
            dI = getdata(sensor)[2]
            
            #color = colourgrabber(sensor) is optional
            #if the sensors dice then include diced in the label
            if sensor.diced == True:
                plt.plot(V, I, linewidth=1.4, label = f'IV of {sensor.type} {sensor.size} on Wafer {sensor.wafer} Loc. {sensor.location} Diced', linestyle = linestylegrabber(sensor))
            else:
                plt.plot(V, I, linewidth=1.4, label = f'IV of {sensor.type} {sensor.size} on Wafer {sensor.wafer} Loc. {sensor.location}', linestyle = linestylegrabber(sensor))
            #plt.fill_between(V, (np.array(I) - np.array(dI)), (np.array(I) + np.array(dI)), color = 'grey' , alpha = 0.2)
            
            
            plt.legend(fontsize = 22)
            #plt.savefig(f'{sensor.type}{sensor.size}{sensor.location}_{sensor.wafer}')
    else:
        #if its just one sensor data to plot
        V = getdata(sensorlist)[0]
        I = getdata(sensorlist)[1]
        dI = getdata(sensorlist)[2]
        
        plt.plot(V, I , 'r', linewidth=1, label = f'IV Characteristic for {sensorlist.type} {sensorlist.size} on Wafer {sensorlist.location} {sensorlist.wafer}', linestyle = linestylegrabber(sensorlist))
        #plt.fill_between(V, (np.array(I) - np.array(dI)), (np.array(I) + np.array(dI)), color = 'grey', alpha = 0.2)
        
    plt.legend(fontsize = 16)

def Kfactor(sensorlist):
    
    fig, ax = plt.subplots()
    plt.rcParams["figure.figsize"] = [12,9]
    plt.ylabel('K Factor', fontsize = 22)
    plt.xlabel('Bias Voltage [V]',fontsize = 22)
    #plt.yscale('log')
    plt.xlim(-20, 800)
    plt.ylim(-5, 30)
    ax.minorticks_on()
    ax.grid(which='major', linestyle='-', linewidth='0.5', color='grey')
    ax.grid(which='minor', linestyle=':', linewidth='0.5', color='grey')
    plt.title('K Factor Characteristics', fontsize=22)
    plt.xticks(fontsize = 20)
    plt.yticks(fontsize = 20)
    
    if type(sensorlist) == list:
        for sensor in sensorlist:
            V = getdata(sensor)[0]
            I = getdata(sensor)[1]
            
            klist = []
            for i in range(1, len(V)-1):
                dy = I[i+1] - I[i-1]
                dx = V[i+1] - V[i-1]
                grad = dy/dx
                k = grad*V[i]/I[i]
                klist.append(k)
                
            plt.plot(V[1:-1], klist, label = f'K Factor of {sensor.type} {sensor.size} on Wafer {sensor.wafer} Loc. {sensor.location}', linestyle = linestylegrabber(sensor), color = colourgrabber(sensor))
            
            
            
            #calculating K = 4 breakdown voltage
            V_bd = 0
            for i in range(0, len(klist)):
                if V_bd == 0:
                    if klist[i] >= 4:
                        V_bd = V[i + 1] #to account for us truncating V(list)
            
            
            #breakdown with *2.511 at 2V higher
            V_bd2 = 0
            for i in range(100, len(V)-1):    #first 100V in 1V steps, the 2V steps but dm cus wont breakdown before 100V
                if V_bd2 == 0:
                    if I[i + 1] >= I[i]*(10**(2/5)):
                        V_bd2 = V[i]
            
            #proper definition of breakdown according to market study
            V_bd3 = 0
            for i in range(100, len(V)-3):    #first 100V in 1V steps, the 2V steps but dm cus wont breakdown before 100V
                if V_bd3 == 0:
                    if ((I[i+2]+I[i+3])/2) >= I[i]*10:
                        V_bd3 = V[i]
            orange = False 
            if V_bd3 == 0:  #if ATLAS breakdown isnt met, just take it as the final voltage value (see notes for as to why)
                V_bd3 = V[-1]
                orange = True   #true if ATLAS breakdown is just last voltage step
            
            plt.axvline(x = V_bd, linewidth = '1', linestyle = '--', color = 'b', label = f'K = 4 Breakdown of {sensor.type} = {V_bd}V')
            plt.axvline(x = V_bd3, linewidth = '1', linestyle = '--', color = 'purple', label = f'ATLAS Breakdown of {sensor.type}= {V_bd3}V')
            #plt.axvline(x = V_bd2, linewidth = '0.5', linestyle = '--', color = 'g')
            plt.legend(fontsize = 24)
            print(sensor.type, sensor.size, sensor.wafer, sensor.location, f'K = 4 breakdown = {V_bd}')
            print(sensor.type, sensor.size, sensor.wafer, sensor.location, f'ATLAS breakdown = {V_bd3} {orange}')
    else:   #if not a list (can probs delete tihs now as always input a list)
        V = getdata(sensorlist)[0]
        I = getdata(sensorlist)[1]
        
        klist = []
        for i in range(1, len(V)-1):
            dy = I[i+1] - I[i-1]
            dx = V[i+1] - V[i-1]
            grad = dy/dx
            k = grad*(V[i]/I[i])
            klist.append(k)
        
        #print(sensor, V_bd)
        plt.plot(V[1:-1], klist, label = f'K Factor of {sensorlist.type} {sensorlist.size} on Wafer {sensorlist.wafer} Location {sensorlist.location}', linestyle = linestylegrabber(sensor), color = colourgrabber(sensor))
        plt.axhline(y = 4, linewidth = '0.5', linestyle = '--', color = 'green')
        
        #K>4 breakdown
        V_bd = 0
        for i in range(0, len(klist)):
            if V_bd == 0:
                if klist[i] >= 4:
                    V_bd = V[i + 1] #to account for us truncating V(list)
        
        #breakdown with *2.511 at 2V higher
        V_bd2 = 0
        for i in range(100, len(V)):    #first 100V in 1V steps, the 2V steps but dm cus wont breakdown before 100V
            if V_bd2 == 0:
                if I[i + 2] >= I[i]*(10**(2/5)):
                    V_bd2 = V[i]
        
        #proper definition of breakdown according to market study
        V_bd3 = 0
        for i in range(100, len(V)):    #first 100V in 1V steps, the 2V steps but dm cus wont breakdown before 100V
            if V_bd3 == 0:
                if ((I[i+2]+I[i+3])/2) >= I[i]*10:
                    V_bd3 = V[i]
        
        #print(sensor, V_bd)
        plt.axvline(x = V_bd, linewidth = '0.5', linestyle = '--', color = 'r')
        #plt.axvline(x = V_bd2, linewidth = '0.5', linestyle = '--', color = 'g')
    plt.axhline(y = 4, linewidth = '1', linestyle = '--', color = 'green', label = 'K Factor = 4')    
    plt.legend(fontsize = 16)

def Ksweep(sensorlist):
    
    fig, ax = plt.subplots()
    plt.rcParams["figure.figsize"] = [12,9]
    plt.ylabel('Corresponding Breakdonwn Voltage [V]', fontsize = 18)
    plt.xlabel('K Factor Definition', fontsize = 18)
    #plt.yscale('log')
    #plt.xlim(0, 800)
    #plt.ylim(-5, 30)
    ax.minorticks_on()
    ax.grid(which='major', linestyle='-', linewidth='0.5', color='grey')
    ax.grid(which='minor', linestyle=':', linewidth='0.5', color='grey')
    plt.title('Varying K Factor and Corresponding Breakdown Voltages', fontsize=18)
    plt.xticks(fontsize = 16)
    plt.yticks(fontsize = 16)
    
    if type(sensorlist) == list:
        for sensor in sensorlist:
            V = getdata(sensor)[0]
            I = getdata(sensor)[1]
            
            klist = []
            for i in range(1, len(V)-1):
                dy = I[i+1] - I[i-1]
                dx = V[i+1] - V[i-1]
                grad = dy/dx
                k = grad*V[i]/I[i]
                klist.append(k)
                
                V_bdlist = []
                for k in range(0, len(np.arange(0, len(klist)/10, 0.1))):
                    V_bd = 0
                    for i in range(0, len(klist)):
                        if V_bd == 0:
                            if klist[i] >= k:
                                V_bd = V[i + 1]
                    V_bdlist.append(V_bd)
                    
            plt.plot(np.arange(0, len(klist)/10, 0.1), V_bdlist, label = f'K Factor Sweep of {sensor.type} {sensor.size} on Wafer {sensor.wafer} Location {sensor.location}', linestyle = linestylegrabber(sensor), color = colourgrabber(sensor))
        plt.axvline(x = 4, linewidth = '1.5', linestyle = 'dashed', color = 'blue', label = '$K$ = 4')
        
        #plt.legend(loc = 'right')
    
    else:
        V = getdata(sensorlist)[0]
        I = getdata(sensorlist)[1]
        
        klist = []
        for i in range(1, len(V)-1):
            dy = I[i+1] - I[i-1]
            dx = V[i+1] - V[i-1]
            grad = dy/dx
            k = grad*(V[i]/I[i])
            klist.append(k)
            
            V_bdlist = []
            for k in range(0, len(np.arange(0, len(klist)/10, 0.1))):
                V_bd = 0
                for i in range(0, len(klist)):
                    if V_bd == 0:
                        if klist[i] >= k:
                            V_bd = V[i + 1]
                V_bdlist.append(V_bd)
        
        
        
        plt.plot(np.arange(0, len(klist)/10, 0.1), V_bdlist, label = f'K Factor Sweep of {sensorlist.type} {sensorlist.size} on Wafer {sensorlist.wafer} Location {sensorlist.location}', linestyle = linestylegrabber(sensor), color = colourgrabber(sensor))
        plt.axvline(x = 4, linewidth = '0.5', linestyle = '--', color = 'r')
        
        
    plt.legend(loc = 'right', fontsize = 16)

def BKcompare():
    """
    fig, ax = plt.subplots()
    plt.rcParams["figure.figsize"] = [12,9]
    plt.ylabel('Bias Voltage [V]', fontsize = 18)
    plt.xlabel('Normalised Dose', fontsize = 18)
    #plt.yscale('log')
    #plt.xlim(0, 800)
    #plt.ylim(0, 50)
    ax.minorticks_on()
    ax.grid(which='major', linestyle='-', linewidth='0.5', color='grey')
    ax.grid(which='minor', linestyle=':', linewidth='0.5', color='grey')
    plt.title('4mm Sensor K = 4 Breakdowns', fontsize=18)
    plt.xticks([0.92, 1.00, 1.00, 1.07, 1.07], fontsize = 16)
    plt.yticks(fontsize = 16)
    
    #4mm K = 4 breakdowns
    #in dose order:
    #16, 20, 6, 11, 3
    #0.92, 1.00, 1.00, 1.07, 1.07
    
    plt.plot([0.92, 1.00, 1.00, 1.07, 1.07], [LGAD4mm1_16_dic['Kbreakdown'], LGAD4mm1_20_dic['Kbreakdown'], LGAD4mm1_6_dic['Kbreakdown'], LGAD4mm1_11_dic['Kbreakdown'], LGAD4mm1_3_dic['Kbreakdown']], label = 'LGAD Loc. 1', color = 'green', marker = 'x')
    plt.plot([0.92, 1.00, 1.00, 1.07, 1.07], [LGAD4mm3_16_dic['Kbreakdown'], LGAD4mm3_20_dic['Kbreakdown'], LGAD4mm3_6_dic['Kbreakdown'], LGAD4mm3_11_dic['Kbreakdown'], LGAD4mm3_3_dic['Kbreakdown']], label = 'LGAD Loc. 3', color = 'grey', marker = 'x')
    plt.plot([0.92, 1.00, 1.00, 1.07, 1.07], [LGAD4mm5_16_dic['Kbreakdown'], LGAD4mm5_20_dic['Kbreakdown'], LGAD4mm5_6_dic['Kbreakdown'], LGAD4mm5_11_dic['Kbreakdown'], LGAD4mm5_3_dic['Kbreakdown']], label = 'LGAD Loc. 5', color = 'blue', marker = 'x')
    plt.plot([0.92, 1.00, 1.00, 1.07, 1.07], [PiN4mm1_16_dic['Kbreakdown'], PiN4mm1_20_dic['Kbreakdown'], PiN4mm1_6_dic['Kbreakdown'], PiN4mm1_11_dic['Kbreakdown'], PiN4mm1_3_dic['Kbreakdown']], label = 'PiN Loc.1', color = 'orange', marker = 'x', linestyle = 'dashed')
    plt.legend(fontsize = 16)
    """
    
    #compare wafer 20/6. dose = 1.00. energy = 1.00/1.11.
    fig, ax = plt.subplots()
    plt.rcParams["figure.figsize"] = [12,9]
    plt.ylabel('Bias Voltage [V]', fontsize = 18)
    plt.xlabel('Normalised Energy', fontsize = 18)
    #plt.yscale('log')
    plt.ylim(0, 800)
    plt.xlim(0.97, 1.14)
    ax.minorticks_on()
    ax.grid(which='major', linestyle='-', linewidth='0.5', color='grey')
    ax.grid(which='minor', linestyle=':', linewidth='0.5', color='grey')
    plt.title('1mm Sensor ATLAS Breakdowns', fontsize=18)
    plt.xticks([1.00, 1.11], fontsize = 16)
    plt.yticks(fontsize = 16)
    plt.text(1.05, 750, 'Normalised Dose = 1.00', fontsize = 18)
    plt.text(1, 15, 'Wafer 20', fontsize = 16, horizontalalignment='center')
    plt.text(1.11, 15, 'Wafer 6', fontsize = 16, horizontalalignment='center')
    
    plt.plot([1.00, 1.11], [LGAD1mm1_20_dic['ATLASbreakdown'], LGAD1mm1_6_dic['ATLASbreakdown']], label = 'LGAD Loc. 1', color = 'green', marker = 'x')
    plt.plot([1.00, 1.11], [LGAD1mm3_20_dic['ATLASbreakdown'], LGAD1mm3_6_dic['ATLASbreakdown']], label = 'LGAD Loc. 3', color = 'grey', marker = 'x')
    plt.plot([1.00, 1.11], [LGAD1mm5_20_dic['ATLASbreakdown'], LGAD1mm5_6_dic['ATLASbreakdown']], label = 'LGAD Loc. 5', color = 'blue', marker = 'x')
    plt.plot([1.00, 1.11], [PiN1mm1_20_dic['ATLASbreakdown'], PiN1mm1_6_dic['ATLASbreakdown']], label = 'PiN Loc. 1', color = 'orange', marker = 'x', linestyle = 'dashed')
    plt.legend(fontsize = 16, loc = 'upper left')
    
    #compare wafer 11/3. dose = 1.07. energy = 1.05/1.11.
    fig, ax = plt.subplots()
    plt.rcParams["figure.figsize"] = [12,9]
    plt.ylabel('Bias Voltage [V]', fontsize = 22)
    plt.xlabel('Normalised Energy', fontsize = 22)
    #plt.yscale('log')
    plt.ylim(0, 800)
    plt.xlim(1.02, 1.14)
    ax.minorticks_on()
    ax.grid(which='major', linestyle='-', linewidth='0.5', color='grey')
    ax.grid(which='minor', linestyle=':', linewidth='0.5', color='grey')
    plt.title('4mm Sensor K = 4 Breakdowns', fontsize=22)
    plt.xticks([1.05, 1.11], fontsize = 20)
    plt.yticks(fontsize = 20)
    plt.text(1.08, 750, 'Normalised Dose = 1.07', fontsize = 22)
    plt.text(1.05, 15, 'Wafer 11', fontsize = 16, horizontalalignment='center')
    plt.text(1.11, 15, 'Wafer 3', fontsize = 16, horizontalalignment='center')
    
    plt.plot([1.05, 1.11], [LGAD4mm1_11_dic['Kbreakdown'], LGAD4mm1_3_dic['Kbreakdown']], label = 'LGAD Loc. 1', color = 'green', marker = 'x')
    plt.plot([1.05, 1.11], [LGAD4mm3_11_dic['Kbreakdown'], LGAD4mm3_3_dic['Kbreakdown']], label = 'LGAD Loc. 3', color = 'grey', marker = 'x')
    plt.plot([1.05, 1.11], [LGAD4mm5_11_dic['Kbreakdown'], LGAD4mm5_3_dic['Kbreakdown']], label = 'LGAD Loc. 5', color = 'blue', marker = 'x')
    plt.plot([1.05, 1.11], [PiN4mm1_11_dic['Kbreakdown'], PiN4mm1_3_dic['Kbreakdown']], label = 'PiN Loc. 1', color = 'orange', marker = 'x', linestyle = 'dashed')
    plt.legend(fontsize = 18, loc = 'upper left')
    
    #compare wafer 16/11. energy = 1.05. dose = 0.92/1.07.
    fig, ax = plt.subplots()
    plt.rcParams["figure.figsize"] = [12,9]
    plt.ylabel('Bias Voltage [V]', fontsize = 18)
    plt.xlabel('Normalised Dose', fontsize = 18)
    #plt.yscale('log')
    plt.ylim(0, 800)
    plt.xlim(0.89, 1.1)
    ax.minorticks_on()
    ax.grid(which='major', linestyle='-', linewidth='0.5', color='grey')
    ax.grid(which='minor', linestyle=':', linewidth='0.5', color='grey')
    plt.title('1mm Sensor ATLAS Breakdowns', fontsize=18)
    plt.xticks([0.92, 1.07], fontsize = 16)
    plt.yticks(fontsize = 16)
    plt.text(0.99, 750, 'Normalised Energy = 1.05', fontsize = 18)
    plt.text(0.92, 15, 'Wafer 16', fontsize = 16, horizontalalignment='center')
    plt.text(1.07, 15, 'Wafer 11', fontsize = 16, horizontalalignment='center')
    
    plt.plot([0.92, 1.07], [LGAD1mm1_16_dic['ATLASbreakdown'], LGAD1mm1_11_dic['ATLASbreakdown']], label = 'LGAD Loc. 1', color = 'green', marker = 'x')
    plt.plot([0.92, 1.07], [LGAD1mm3_16_dic['ATLASbreakdown'], LGAD1mm3_11_dic['ATLASbreakdown']], label = 'LGAD Loc. 3', color = 'grey', marker = 'x')
    plt.plot([0.92, 1.07], [LGAD1mm5_16_dic['ATLASbreakdown'], LGAD1mm5_11_dic['ATLASbreakdown']], label = 'LGAD Loc. 5', color = 'blue', marker = 'x')
    plt.plot([0.92, 1.07], [PiN1mm1_16_dic['ATLASbreakdown'], PiN1mm1_11_dic['ATLASbreakdown']], label = 'PiN Loc. 1', color = 'orange', marker = 'x', linestyle = 'dashed')
    plt.legend(fontsize = 16, loc = 'upper left')
    
    #compare wafer 6/3. energy = 1.11. dose = 1.00/1.07.
    fig, ax = plt.subplots()
    plt.rcParams["figure.figsize"] = [12,9]
    plt.ylabel('Bias Voltage [V]', fontsize = 22)
    plt.xlabel('Normalised Dose', fontsize = 22)
    #plt.yscale('log')
    plt.ylim(0, 800)
    plt.xlim(0.97, 1.10)
    ax.minorticks_on()
    ax.grid(which='major', linestyle='-', linewidth='0.5', color='grey')
    ax.grid(which='minor', linestyle=':', linewidth='0.5', color='grey')
    plt.title('4mm Sensor K = 4 Breakdowns', fontsize=22)
    plt.xticks([1.00, 1.07], fontsize = 20)
    plt.yticks(fontsize = 20)
    plt.text(1.04, 750, 'Normalised Energy = 1.11', fontsize = 22)
    plt.text(1, 15, 'Wafer 6', fontsize = 20, horizontalalignment='center')
    plt.text(1.07, 15, 'Wafer 3', fontsize = 20, horizontalalignment='center')
    
    plt.plot([1.00, 1.07], [LGAD4mm1_6_dic['Kbreakdown'], LGAD4mm1_3_dic['Kbreakdown']], label = 'LGAD Loc. 1', color = 'green', marker = 'x')
    plt.plot([1.00, 1.07], [LGAD4mm3_6_dic['Kbreakdown'], LGAD4mm3_3_dic['Kbreakdown']], label = 'LGAD Loc. 3', color = 'grey', marker = 'x')
    plt.plot([1.00, 1.07], [LGAD4mm5_6_dic['Kbreakdown'], LGAD4mm5_3_dic['Kbreakdown']], label = 'LGAD Loc. 5', color = 'blue', marker = 'x')
    plt.plot([1.00, 1.07], [PiN4mm1_6_dic['Kbreakdown'], PiN4mm1_3_dic['Kbreakdown']], label = 'PiN Loc. 1', color = 'orange', marker = 'x', linestyle = 'dashed')
    plt.legend(fontsize = 18, loc = 'upper left')
    
    

#print(LGAD1mm3_16_dic['ATLASbreakdown'])
#IV([LGAD1mm1_6, LGAD1mm3_6, LGAD1mm5_6])
#IV([LGAD1mm3_6, PiN1mm1_6])
#Kfactor([PiN1mm1_3, PiN1mm3_3, PiN1mm5_3])
#BKcompare()
#Ksweep([LGAD4mm1_6])

#IV([LGAD1mm5_6, LGAD1mm5_6_diced, LGAD1mm1_6, LGAD1mm1_6_diced])
#IV([LGAD1mm5_6])
Kfactor([LGAD4mm1_6, PiN4mm1_6])




