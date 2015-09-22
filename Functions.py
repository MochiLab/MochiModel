"""
Functions utilized in "master" tree construction file.

Initialized Mon Oct 21 14:20:36 2013

Author: A. Card
"""
def AddNodeWithTag(tree, nodepath, nodetype, tag):
    """
    Adds the desired node w/type to a given tree with a user-defined tag.
    Note
    ----
    All except for 'tree' are strings.
    """
    tree.addNode(nodepath, usage=nodetype)
    tempnode = tree.getNode(nodepath)
    tempnode.addTag(tag)

    
def AddUnit(tree, parentnodepath, unit):
    """
    Adds a child node to parent node that stores the parent node's unit.
    """
    tree.addNode(parentnodepath + ':UNIT', usage='Text').putData(unit)
    

def AddNumericWithUnit(tree, nodepath, tag, unit):
    """
    Adds a NUMERIC node, adds a tag, and also adds a :UNIT child node into
    which one can store the value's unit.
    Note    
    ----
    All except for 'tree' are strings.
    """
    tree.addNode(nodepath, usage='NUMERIC')
    tempnode = tree.getNode(nodepath)
    tempnode.addTag(tag)
    AddUnit(tree, nodepath, unit)
    
    
def TreeInit(tree):
    """
    Initializes the TOP node structure. Two branches: SETTINGS and NI_DAQ
    """
    """ Settings/NI_DAQ """
    tree.addNode('.SETTINGS')
    tree.addNode('.SETTINGS.EXPERIMENT')
    tree.addNode('.SETTINGS.NI')
    tree.addNode('.SETTINGS.NI.TIMING')
    tree.addNode('.SETTINGS.NI.DAQ')
    tree.addNode('.NI_DAQ')
    tree.addNode('.NI_RIO')
    tree.addNode('.SETTINGS.NI.DIO')
    tree.addNode('.TEK_SCOPE')
    tree.addNode('.CAMERAS')
    tree.addNode('.CAMERAS.PIMAX3')
    tree.addNode('.CAMERAS.PIMAX3.RAW')
    tree.addNode('.CAMERAS.PIMAX3.CAM_SETTING')
    tree.addNode('.CAMERAS.IMACON')
    """ Single-valued member nodes """
    AddNodeWithTag(tree,'.SETTINGS.EXPERIMENT:SHOT_DATE','TEXT',
                   'SHOTDATEANDTIME')
    AddNodeWithTag(tree,'.SETTINGS.EXPERIMENT:SHOT_NOTES','TEXT','SHOTNOTES')
    AddNodeWithTag(tree,'.SETTINGS.EXPERIMENT:SYS_MESSAGE','TEXT','SYSMESSAGE')
    AddNodeWithTag(tree,'.SETTINGS.EXPERIMENT:SHOT_QUALITY','TEXT',
                   'SHOTQUALITY')
    AddNodeWithTag(tree,'.SETTINGS.EXPERIMENT:SHOT_NUMBER','TEXT',
                   'SHOTNUMBER')
    AddNodeWithTag(tree,'.SETTINGS.EXPERIMENT:PROG_VERSION','TEXT',
                   'PROGRAM_VERSION')
    AddNodeWithTag(tree, '.TEK_SCOPE:RAW', 'TEXT', 'RAWTEKSCOPE')
    

def TIMEcards(tree, TIMEnum):
    """
    Builds the node structure for the timing cards.
    """
    tree.addNode('.SETTINGS.NI.TIMING.TCARD_' + str(TIMEnum))
    tree.addNode('.SETTINGS.NI.TIMING.TCARD_' + str(TIMEnum) +
                 '.TCARD_GLOBAL')
    AddNodeWithTag(tree, '.SETTINGS.NI.TIMING.TCARD_' + str(TIMEnum) +
                 '.TCARD_GLOBAL:SLOT_NUMBER', 'TEXT', 'TIMESLOTNUM_CARD' +
                 str(TIMEnum))


def TIMEchannels(tree, TIMEnum, CHnum):
    """
    Builds the node structure for the timing cards' channels.
    """
    chanpath = ('.SETTINGS.NI.TIMING.TCARD_'
                 + str(TIMEnum) + '.CHANNEL_' + str(CHnum))
    tree.addNode(chanpath)
    AddNodeWithTag(tree, chanpath + ':ACTIVE', 'NUMERIC', 'TIMACTIVE_CARD' +
                   str(TIMEnum) + 'CH' + str(CHnum))
    AddNodeWithTag(tree, chanpath + ':CHANNEL_NAME', 'TEXT', 
                   'TIMEUSERNAME_CARD' + str(TIMEnum) + 'CH' + str(CHnum))
    AddNumericWithUnit(tree, chanpath + ':TRIG_TIME', 'TRIGGERTIME_CARD' +
                       str(TIMEnum) + 'CH' + str(CHnum), 's')
    AddNumericWithUnit(tree, chanpath + ':PULSE_WIDTH', 'PWM_CARD' +
                       str(TIMEnum) + 'CH' + str(CHnum), 's')
    AddNodeWithTag(tree, chanpath + ':NI_NAME', 'TEXT', 'TIMENINAME_CARD' +
                   str(TIMEnum) + 'CH' + str(CHnum))


def DAQcards(tree, DAQnum):
    """
    This function creates the tree structure for all DAQ cards.
    """
    cardpath = ('.NI_DAQ.DAQ_' + str(DAQnum) + '.DCARD_GLOBAL')
    tree.addNode('.NI_DAQ.DAQ_' + str(DAQnum))
    tree.addNode(cardpath)
    AddNumericWithUnit(tree, cardpath + ':START_T', 'START_DCARD' +
                       str(DAQnum), 's')
    AddNumericWithUnit(tree, cardpath + ':END_T', 'END_DCARD' + str(DAQnum),
                       's')
    AddNumericWithUnit(tree, cardpath + ':SAMPLE_RATE', 'SAMPLERATE_DCARD' +
                       str(DAQnum), 's^-1')
    AddNumericWithUnit(tree, cardpath + ':DELTA_T', 'DELTAT_DCARD' +
                   str(DAQnum), 's')
    AddNodeWithTag(tree, cardpath + ':N_PRE_SAMP', 'NUMERIC', 'N_PRESAMP_DCARD'
                   + str(DAQnum))
    AddNodeWithTag(tree, cardpath + ':N_SAMPLES', 'NUMERIC',
                   'NUMBERSAMPLES_DCARD' + str(DAQnum))
    AddNodeWithTag(tree, cardpath + ':SLOT_NUMBER', 'TEXT', 'SLOTNUM_DCARD' +
                   str(DAQnum))
    AddNodeWithTag(tree, cardpath + ':PXISTARLINE', 'TEXT', 'PXISTARLINE_DCARD'
                   + str(DAQnum))


def DAQchannels(tree, DAQnum, CHnum):
    """
    This function creates the tree structure for a given
    DAQ channel by reading the variable DAQnum.
    """
    tree.addNode('.NI_DAQ.DAQ_' + str(DAQnum) + '.CHANNEL_' + str(CHnum))
    chanpath = ('.NI_DAQ.DAQ_' + str(DAQnum) + '.CHANNEL_' + str(CHnum)
                 + '.CHAN_SETTING')
    tree.addNode(chanpath)
    AddNodeWithTag(tree, chanpath + ':ACTIVE', 'NUMERIC', 'DAQTIVE_DCARD' +
                   str(DAQnum) + 'CH' + str(CHnum))
    AddNodeWithTag(tree, chanpath + ':CHANNEL_NAME', 'TEXT', 'USERNAME_DCARD' 
                   + str(DAQnum) + 'CH' + str(CHnum))
    AddNumericWithUnit(tree, chanpath + ':VOLT_RANGE', 'VOLTRANGE_DCARD' 
                   + str(DAQnum) + 'CH' + str(CHnum), 'V')
    AddNodeWithTag(tree, chanpath + ':NI_NAME', 'TEXT', 'NINAME_DCARD' 
                   + str(DAQnum) + 'CH' + str(CHnum))
                   

def RIOcards(tree, RIOnum):
    """
    This function creates the tree structure for all RIO cards.
    """
    cardpath = ('.NI_RIO.RIO_' + str(RIOnum) + '.RCARD_GLOBAL')
    tree.addNode('.NI_RIO.RIO_' + str(RIOnum))
    tree.addNode(cardpath)
    AddNumericWithUnit(tree, cardpath + ':START_T', 'START_RCARD' +
                   str(RIOnum), 's')
    AddNumericWithUnit(tree, cardpath + ':END_T', 'END_RCARD' + str(RIOnum),
                       's')
    AddNumericWithUnit(tree, cardpath + ':SAMPLE_RATE', 'SAMPLERATE_RCARD' +
                       str(RIOnum), 's^-1')
    AddNumericWithUnit(tree, cardpath + ':DELTA_T', 'DELTAT_RCARD' +
                   str(RIOnum), 's')
    AddNodeWithTag(tree, cardpath + ':N_SAMPLES', 'NUMERIC',
                   'NUMBERSAMPLES_RCARD' + str(RIOnum))
    AddNodeWithTag(tree, cardpath + ':FPGA_NAME', 'TEXT', 'FPGANAME_RCARD' +
                   str(RIOnum))
    AddNodeWithTag(tree, cardpath + ':PXISTARLINE', 'TEXT', 'PXISTARLINE_RCARD'
                   + str(RIOnum))
    AddNodeWithTag(tree, cardpath + ':DELAYCYCLES', 'NUMERIC',
                   'DELAYCYCLES_RCARD' + str(RIOnum))
    AddNodeWithTag(tree, cardpath + ':FPGA_RAW', 'NUMERIC',
                   'FPGA_RAW_RCARD' + str(RIOnum))


def RIOchannels(tree, RIOnum, CHnum):
    """
    This function creates the tree structure for a given RIO channel by
    reading the variable RIOnum.
    """
    tree.addNode('.NI_RIO.RIO_' + str(RIOnum) + '.CHANNEL_' + str(CHnum))
    chanpath = ('.NI_RIO.RIO_' + str(RIOnum) + '.CHANNEL_' + str(CHnum)
                 + '.CHAN_SETTING')
    tree.addNode(chanpath)
    AddNodeWithTag(tree, chanpath + ':ACTIVE', 'NUMERIC', 'RIAQTIVE_RCARD' +
                   str(RIOnum) + 'CH' + str(CHnum))
    AddNodeWithTag(tree, chanpath + ':CHANNEL_NAME', 'TEXT', 'USERNAME_RCARD' 
                   + str(RIOnum) + 'CH' + str(CHnum))
    AddNumericWithUnit(tree, chanpath + ':VOLT_RANGE', 'VOLTRANGE_RCARD' 
                   + str(RIOnum) + 'CH' + str(CHnum), 'V')
    AddNodeWithTag(tree, chanpath + ':NI_NAME', 'TEXT', 'NINAME_RCARD' 
                   + str(RIOnum) + 'CH' + str(CHnum))
    AddNumericWithUnit(tree, chanpath + ':LPFILT_FREQ', 'LP_FILT_FREQ_RCARD' +
                       str(RIOnum) + 'CH' + str(CHnum), 's^-1')
    AddNumericWithUnit(tree, chanpath + ':HPFILT_FREQ', 'HP_FILT_FREQ_RCARD' +
                       str(RIOnum) + 'CH' + str(CHnum), 's^-1')
    AddNodeWithTag(tree, chanpath + ':GAIN', 'NUMERIC', 'GAIN_RCARD' 
                   + str(RIOnum) + 'CH' + str(CHnum))


def DATAchannels_D(tree, DAQnum, CHnum):
    """
    This function creates the tree structure for all DAQ cards.
    """
    datapath = ('.NI_DAQ.DAQ_' + str(DAQnum) + '.CHANNEL_' + str(CHnum))
    AddNodeWithTag(tree, datapath + ':DATA', 'SIGNAL', 'NIRAWDATA_DCARD' 
                   + str(DAQnum) + 'CH' + str(CHnum))
    AddNumericWithUnit(tree, datapath + '.DATA:TIME_VALUES', 
                   'NITIMEVALUES_DCARD' + str(DAQnum) + 'CH' + str(CHnum), 's')
    AddNumericWithUnit(tree, datapath + '.DATA:DATA_VALUES', 
                   'NIDATAVALUES_DCARD' + str(DAQnum) + 'CH' + str(CHnum), 'V')
    AddNumericWithUnit(tree, datapath + '.DATA:DELTA_T', 'NIDELTAT_DCARD' +
                       str(DAQnum) + 'CH' + str(CHnum), 's')
                       
                   
def DATAchannels_R(tree, RIOnum, CHnum):
    """
    This function creates the tree structure for all DAQ card data streams.
    """
    datapath = ('.NI_RIO.RIO_' + str(RIOnum) + '.CHANNEL_' + str(CHnum))
    AddNodeWithTag(tree, datapath + ':VOLTAGE', 'SIGNAL', 'NIRAWDATA_RCARD' 
                   + str(RIOnum) + 'CH' + str(CHnum))
    AddNodeWithTag(tree, datapath + ':COUNTS', 'SIGNAL', 'NIRAWCOUNTS_RCARD' 
                   + str(RIOnum) + 'CH' + str(CHnum))
    
    AddNumericWithUnit(tree, datapath + '.VOLTAGE:TIME_VALUES', 
                   'VTIMEVALUES_RCARD' + str(RIOnum) + 'CH' + str(CHnum), 's')
    AddNumericWithUnit(tree, datapath + '.VOLTAGE:DATA_VALUES',
                   'VDATAVALUES_RCARD' + str(RIOnum) + 'CH' + str(CHnum), 'V')
    AddNumericWithUnit(tree, datapath + '.VOLTAGE:DELTA_T', 'VDELTAT_RCARD' +
                       str(RIOnum) + 'CH' + str(CHnum), 's')

    AddNumericWithUnit(tree, datapath + '.COUNTS:TIME_VALUES',  
                   'CTIMEVALUES_RCARD' + str(RIOnum) + 'CH' + str(CHnum), 's')
    AddNodeWithTag(tree, datapath + '.COUNTS:DATA_VALUES', 'NUMERIC', 
                   'CDATAVALUES_RCARD' + str(RIOnum) + 'CH' + str(CHnum))
    AddNumericWithUnit(tree, datapath + '.COUNTS:DELTA_T', 'CDELTAT_RCARD' +
                       str(RIOnum) + 'CH' + str(CHnum), 's')


def DIOchannels(tree, DIOnum):
    """
    This function creates the tree nodes necessary for storing DIO information.
    """
    tree.addNode('.SETTINGS.NI.DIO.CHANNEL_' + str(DIOnum))
    diopath = ('.SETTINGS.NI.DIO.CHANNEL_' + str(DIOnum))
    AddNodeWithTag(tree, diopath + ':CHANNEL_NAME', 'TEXT', 'USERNAME_DIOCH' 
                   + str(DIOnum))
    AddNodeWithTag(tree, diopath + ':NI_NAME', 'TEXT', 'NINAME_DIOCH' 
                   + str(DIOnum))
                   

def scopechannels(tree, scope_chan):
    """
    This function builds the Tektronix oscilloscope data/setting nodes.
    """
    scope_chnum = scope_chan + 1
    chanpath = '.TEK_SCOPE.CHANNEL_' + str(scope_chnum)
    datapath = chanpath + '.DATA'
    settingpath = chanpath + '.SETTINGS'
    tree.addNode(chanpath)
    AddNodeWithTag(tree, chanpath + ':STATE', 'TEXT', 'STATE_TEKCH' +
                   str(scope_chnum))
    AddNodeWithTag(tree, chanpath + ':DATA', 'SIGNAL', 'DATA_TEKCH' +
                   str(scope_chnum))
    tree.addNode(settingpath)
    AddNumericWithUnit(tree, datapath + ':TIME', 'TIMEVALUES_TEKCH' +
                   str(scope_chnum), 's')
    AddNumericWithUnit(tree, datapath + ':VOLTAGE', 'VOLTAGEVALUES_TEKCH' +
                       str(scope_chnum), 'V')
    AddNodeWithTag(tree, settingpath + ':CHANNEL_NAME', 'TEXT',
                   'CHANNEL_NAME_TEKCH' + str(scope_chnum))
    AddNodeWithTag(tree, settingpath + ':GROUND_STATE', 'TEXT',
                   'GROUND_STATE_TEKCH' + str(scope_chnum))
    AddNodeWithTag(tree, settingpath + ':N_SAMPLES', 'NUMERIC',
                   'NSAMPLES_TEKCH' + str(scope_chnum))
    AddNumericWithUnit(tree, settingpath + ':DELTA_T', 'DT_TEKCH' +
                   str(scope_chnum), 's')
    AddNodeWithTag(tree, settingpath + ':N_PRE_SAMP', 'NUMERIC',
                   'NPRESAMP_TEKCH' + str(scope_chnum))
    AddNumericWithUnit(tree, settingpath + ':TIME_DIV', 'TIMEPERDIV_TEKCH' +
                       str(scope_chnum), 's/div')
    AddNumericWithUnit(tree, settingpath + ':VOLT_DIV', 'VOLTSPERDIV_TEKCH' +
                       str(scope_chnum), 'V/div')
    AddNodeWithTag(tree, settingpath + ':PROBE_ATTEN', 'NUMERIC',
                   'PROBEATTENUATION_TEKCH' + str(scope_chnum))


def camsettings(tree):
    """
    This function builds the general settings for the PIMAX3 camera.
    """
    settingspath = '.CAMERAS.PIMAX3.CAM_SETTING'
    AddNodeWithTag(tree, '.CAMERAS.PIMAX3.RAW:HEADER', 'TEXT',
                   'PIMAX_RAWHEADER')
    AddNodeWithTag(tree, '.CAMERAS.PIMAX3.RAW:FOOTER', 'TEXT',
                   'PIMAX_RAWFOOTER')
    AddNodeWithTag(tree, settingspath + ':NUMERFRAMES', 'NUMERIC',
                   'NUMBER_PFRAMES')
    AddNodeWithTag(tree, settingspath + ':READOUT_MODE', 'TEXT',
                   'PIMAX_READOUT_MODE')
    AddNodeWithTag(tree, settingspath + ':INTENS_ON', 'TEXT',
                   'PIMAX_INTENSIFIER_STATE')
    AddNodeWithTag(tree, settingspath + '.INTENS_ON:GAIN', 'NUMERIC',
                   'PIMAX_INTENSIFIER_GAIN')
    tree.addNode(settingspath + '.PHOSDECAY')
    AddNodeWithTag(tree, settingspath + '.PHOSDECAY:FACTOR', 'NUMERIC',
                   'PHOSPHOR_DECAY_FACTOR')
    AddNumericWithUnit(tree, settingspath + '.PHOSDECAY:DELAY', 
                   'PHOSPHOR_DECAY_DELAY', 's')
    AddNumericWithUnit(tree, settingspath + '.PHOSDECAY:RES', 
                   'PHOSPHOR_DECAY_RES', 's')
    tree.addNode(settingspath + '.SENSOR_CLEAN')
    AddNodeWithTag(tree, settingspath + '.SENSOR_CLEAN:ENABLED', 'TEXT',
                   'PIMAX_SENSOR_CLEANING')
    AddNodeWithTag(tree, settingspath + '.SENSOR_CLEAN:UNTILTRIGGER', 'TEXT',
                   'PIMAX_CLEANUNTILTRIGGER')
    AddNodeWithTag(tree, settingspath + '.SENSOR_CLEAN:CYCLES', 'NUMERIC',
                   'PIMAX_CLEANCYCLES')
    AddNumericWithUnit(tree, settingspath + '.SENSOR_CLEAN:CYCLEHEIGHT', 
                   'PIMAX_CYCLEHEIGHT', 'rows')
    AddNumericWithUnit(tree, settingspath + '.SENSOR_CLEAN:SECTHEIGHT', 
                   'PIMAX_SECTIONHEIGHT', 'rows')
    AddNodeWithTag(tree, settingspath + '.SENSOR_CLEAN:SECTCOUNT', 'NUMERIC',
                   'PIMAX_SECTIONCOUNT')


def camframes(tree, cam_frame):
    """
    This function builds the storage nodes for the images produced by the
    PI-MAX3 camera.
    """
    campath = '.CAMERAS.PIMAX3'
    cam_frame = cam_frame + 1
    AddNodeWithTag(tree, campath + ':FRAME_' + str(cam_frame), 'NUMERIC',
                   'PIMAX_FRAME' + str(cam_frame))
    AddNumericWithUnit(tree, campath + '.FRAME_' + str(cam_frame) +
                       ':EXPOSURE', 'EXPOSURE_PFRAME' + str(cam_frame), 's')
    AddNumericWithUnit(tree, campath + '.FRAME_' + str(cam_frame) + ':DELAY', 
                       'GATEDELAY_PFRAME' + str(cam_frame), 's')
    

def globalsettings(tree):
    """
    This function builds the storage nodes for the global experimental
    settings.
    """
    globepath = '.SETTINGS.EXPERIMENT.GLOBAL'
    backpath = globepath + '.BACKGROUND'
    puffpath = globepath + '.GAS_PUFF'
    PSUpath = globepath + '.PSU_VOLTS'
    tree.addNode(globepath)
    tree.addNode(backpath)
    AddNodeWithTag(tree, backpath + ':REF_SHOTNUM', 'NUMERIC', 
                   'GLOBE_REFERENCE_SHOTNUM')
    AddNumericWithUnit(tree, backpath + ':PRESSURE','GLOBE_BACKGROUNDPRESSURE',
                       'torr')
    AddNumericWithUnit(tree, backpath + ':CRYOTEMP_V', 'GLOBE_CRYOTEMP_V', 'V')
    AddNumericWithUnit(tree, backpath + ':CRYOTEMP_K', 'GLOBE_CRYOTEMP_K', 'K')
        
    tree.addNode(puffpath)
    tree.addNode(puffpath + '.TYPE')
    AddNodeWithTag(tree, puffpath + '.TYPE:A', 'TEXT', 'GLOBE_GAS_A_TYPE')
    AddNodeWithTag(tree, puffpath + '.TYPE:B', 'TEXT', 'GLOBE_GAS_B_TYPE')
    AddNodeWithTag(tree, puffpath + '.TYPE:C', 'TEXT', 'GLOBE_GAS_C_TYPE')
    tree.addNode(puffpath + '.PRESSURE')
    AddNumericWithUnit(tree, puffpath + '.PRESSURE:A', 'GLOBE_GAS_A_PRESSURE',
                       'psi')
    AddNumericWithUnit(tree, puffpath + '.PRESSURE:B', 'GLOBE_GAS_B_PRESSURE',
                       'psi')
    AddNumericWithUnit(tree, puffpath + '.PRESSURE:C', 'GLOBE_GAS_C_PRESSURE',
                       'psi')
    tree.addNode(puffpath + '.BOTTLE_P')
    AddNumericWithUnit(tree, puffpath + '.BOTTLE_P:A', 'GLOBE_GAS_A_BOTTLE_P',
                       'psi')
    AddNumericWithUnit(tree, puffpath + '.BOTTLE_P:B', 'GLOBE_GAS_B_BOTTLE_P',
                       'psi')
    AddNumericWithUnit(tree, puffpath + '.BOTTLE_P:C', 'GLOBE_GAS_C_BOTTLE_P',
                       'psi')
    tree.addNode(puffpath + '.DISTRIBUTION')
    AddNodeWithTag(tree, puffpath + '.DISTRIBUTION:INNER', 'TEXT',
                   'GLOBE_INNER_DISTRIB')
    AddNodeWithTag(tree, puffpath + '.DISTRIBUTION:MIDDLE', 'TEXT',
                   'GLOBE_MIDDLE_DISTRIB')
    AddNodeWithTag(tree, puffpath + '.DISTRIBUTION:OUTER', 'TEXT',
                   'GLOBE_OUTER_DISTRIB')
    
    tree.addNode(PSUpath)
    tree.addNode(PSUpath + '.BANKS')
    AddNumericWithUnit(tree, PSUpath + '.BANKS:PSU1', 'GLOBE_BANKVOLT_PSU1',
                       'V')
    AddNumericWithUnit(tree, PSUpath + '.BANKS:PSU2', 'GLOBE_BANKVOLT_PSU2',
                       'V')
    AddNodeWithTag(tree, PSUpath + '.BANKS.PSU2:COUNTER', 'TEXT',
                   'TACH_PSU2_COUNTER')
    AddNumericWithUnit(tree, PSUpath + '.BANKS:PSU3', 'GLOBE_BANKVOLT_PSU3',
                       'V')
    AddNodeWithTag(tree, PSUpath + '.BANKS.PSU3:COUNTER', 'TEXT',
                   'TACH_PSU3_COUNTER')
    tree.addNode(PSUpath + '.BIAS')
    AddNumericWithUnit(tree, PSUpath + '.BIAS:BIAS1', 'GLOBE_BIASVOLT_BIAS1',
                       'V')
    AddNumericWithUnit(tree, PSUpath + '.BIAS:BIAS2', 'GLOBE_BIASVOLT_BIAS2',
                       'V')

    tree.addNode(PSUpath + '.PUFF_PSU')
    tree.addNode(PSUpath + '.PUFF_PSU.PUFF1')
    AddNumericWithUnit(tree, PSUpath + '.PUFF_PSU.PUFF1:CH1', 
                   'GLOBE_PUFF_PSU1_VOLT_CH1', 'V')
    AddNumericWithUnit(tree, PSUpath + '.PUFF_PSU.PUFF1:CH2', 
                   'GLOBE_PUFF_PSU1_VOLT_CH2', 'V')
    AddNumericWithUnit(tree, PSUpath + '.PUFF_PSU.PUFF1:CH3', 
                   'GLOBE_PUFF_PSU1_VOLT_CH3', 'V')
    
    