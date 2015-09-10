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
    All except for tree are strings.
    """
    tree.addNode(nodepath, usage=nodetype)
    tempnode = tree.getNode(nodepath)
    tempnode.addTag(tag)


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
    AddNodeWithTag(tree, '.CAMERAS.PIMAX3.CAM_SETTING:NUMERFRAMES', 
                   'NUMERIC', 'NUMBER_PFRAMES')
    AddNodeWithTag(tree, '.CAMERAS.PIMAX3.CAM_SETTING:INTENS_ON',
                   'TEXT', 'PIMAX_INTENSIFIER_STATE')
    AddNodeWithTag(tree, '.CAMERAS.PIMAX3.CAM_SETTING.INTENS_ON:GAIN', 
                   'NUMERIC', 'PIMAX_INTENSIFIER_GAIN')


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
    AddNodeWithTag(tree, chanpath + ':TRIG_TIME', 'NUMERIC', 'TRIGGERTIME_CARD'
                   + str(TIMEnum) + 'CH' + str(CHnum))
    AddNodeWithTag(tree, chanpath + ':PULSE_WIDTH', 'NUMERIC',
                   'PWM_CARD' + str(TIMEnum) + 'CH' + str(CHnum))
    AddNodeWithTag(tree, chanpath + ':NI_NAME', 'TEXT', 'TIMENINAME_CARD' +
                   str(TIMEnum) + 'CH' + str(CHnum))


def DAQcards(tree, DAQnum):
    """
    This function creates the tree structure for all DAQ cards.
    """
    cardpath = ('.NI_DAQ.DAQ_' + str(DAQnum) + '.DCARD_GLOBAL')
    tree.addNode('.NI_DAQ.DAQ_' + str(DAQnum))
    tree.addNode(cardpath)
    AddNodeWithTag(tree, cardpath + ':START_T', 'NUMERIC', 'START_DCARD' +
                   str(DAQnum))
    AddNodeWithTag(tree, cardpath + ':END_T', 'NUMERIC', 'END_DCARD' +
                   str(DAQnum))
    AddNodeWithTag(tree, cardpath + ':SAMPLE_RATE', 'NUMERIC', 
                   'SAMPLERATE_DCARD' + str(DAQnum))
    AddNodeWithTag(tree, cardpath + ':DELTA_T', 'NUMERIC', 'DELTAT_DCARD' +
                   str(DAQnum))
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
    AddNodeWithTag(tree, chanpath + ':VOLT_RANGE', 'NUMERIC', 'VOLTRANGE_DCARD' 
                   + str(DAQnum) + 'CH' + str(CHnum))
    AddNodeWithTag(tree, chanpath + ':NI_NAME', 'TEXT', 'NINAME_DCARD' 
                   + str(DAQnum) + 'CH' + str(CHnum))
                   

def RIOcards(tree, RIOnum):
    """
    This function creates the tree structure for all RIO cards.
    """
    cardpath = ('.NI_RIO.RIO_' + str(RIOnum) + '.RCARD_GLOBAL')
    tree.addNode('.NI_RIO.RIO_' + str(RIOnum))
    tree.addNode(cardpath)
    AddNodeWithTag(tree, cardpath + ':START_T', 'NUMERIC', 'START_RCARD' +
                   str(RIOnum))
    AddNodeWithTag(tree, cardpath + ':END_T', 'NUMERIC', 'END_RCARD' +
                   str(RIOnum))
    AddNodeWithTag(tree, cardpath + ':SAMPLE_RATE', 'NUMERIC', 
                   'SAMPLERATE_RCARD' + str(RIOnum))
    AddNodeWithTag(tree, cardpath + ':DELTA_T', 'NUMERIC', 'DELTAT_RCARD' +
                   str(RIOnum))
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
    AddNodeWithTag(tree, chanpath + ':VOLT_RANGE', 'NUMERIC', 'VOLTRANGE_RCARD' 
                   + str(RIOnum) + 'CH' + str(CHnum))
    AddNodeWithTag(tree, chanpath + ':NI_NAME', 'TEXT', 'NINAME_RCARD' 
                   + str(RIOnum) + 'CH' + str(CHnum))
    AddNodeWithTag(tree, chanpath + ':LPFILT_FREQ', 'NUMERIC',
                   'LP_FILT_FREQ_RCARD' + str(RIOnum) + 'CH' + str(CHnum))
    AddNodeWithTag(tree, chanpath + ':HPFILT_FREQ', 'NUMERIC',
                   'HP_FILT_FREQ_RCARD' + str(RIOnum) + 'CH' + str(CHnum))
    AddNodeWithTag(tree, chanpath + ':GAIN', 'NUMERIC', 'GAIN_RCARD' 
                   + str(RIOnum) + 'CH' + str(CHnum))


def DATAcards(tree, DAQnum):
    """
    This function creates the tree structure for all DAQ cards. INCOMPLETE!
    """
    tree.addNode('.NI_DAQ.DAQ_' + str(DAQnum))


def DATAchannels_D(tree, DAQnum, CHnum):
    """
    This function creates the tree structure for all DAQ cards.
    """
    datapath = ('.NI_DAQ.DAQ_' + str(DAQnum) + '.CHANNEL_' + str(CHnum))
    AddNodeWithTag(tree, datapath + ':DATA', 'SIGNAL', 'NIRAWDATA_DCARD' 
                   + str(DAQnum) + 'CH' + str(CHnum))
    AddNodeWithTag(tree, datapath + '.DATA:TIME_VALUES', 'NUMERIC', 
                   'NITIMEVALUES_DCARD' + str(DAQnum) + 'CH' + str(CHnum))
    AddNodeWithTag(tree, datapath + '.DATA:DATA_VALUES', 'NUMERIC', 
                   'NIDATAVALUES_DCARD' + str(DAQnum) + 'CH' + str(CHnum))
    AddNodeWithTag(tree, datapath + '.DATA:DELTA_T', 'NUMERIC', 
                   'NIDELTAT_DCARD' + str(DAQnum) + 'CH' + str(CHnum))
                   
def DATAchannels_R(tree, RIOnum, CHnum):
    """
    This function creates the tree structure for all DAQ card data streams.
    """
    datapath = ('.NI_RIO.RIO_' + str(RIOnum) + '.CHANNEL_' + str(CHnum))
    AddNodeWithTag(tree, datapath + ':VOLTAGE', 'SIGNAL', 'NIRAWDATA_RCARD' 
                   + str(RIOnum) + 'CH' + str(CHnum))
    AddNodeWithTag(tree, datapath + ':COUNTS', 'SIGNAL', 'NIRAWCOUNTS_RCARD' 
                   + str(RIOnum) + 'CH' + str(CHnum))

    AddNodeWithTag(tree, datapath + '.VOLTAGE:TIME_VALUES', 'NUMERIC', 
                   'VTIMEVALUES_RCARD' + str(RIOnum) + 'CH' + str(CHnum))
    AddNodeWithTag(tree, datapath + '.VOLTAGE:DATA_VALUES', 'NUMERIC', 
                   'VDATAVALUES_RCARD' + str(RIOnum) + 'CH' + str(CHnum))
    AddNodeWithTag(tree, datapath + '.VOLTAGE:DELTA_T', 'NUMERIC', 
                   'VDELTAT_RCARD' + str(RIOnum) + 'CH' + str(CHnum))

    AddNodeWithTag(tree, datapath + '.COUNTS:TIME_VALUES', 'NUMERIC', 
                   'CTIMEVALUES_RCARD' + str(RIOnum) + 'CH' + str(CHnum))
    AddNodeWithTag(tree, datapath + '.COUNTS:DATA_VALUES', 'NUMERIC', 
                   'CDATAVALUES_RCARD' + str(RIOnum) + 'CH' + str(CHnum))
    AddNodeWithTag(tree, datapath + '.COUNTS:DELTA_T', 'NUMERIC', 
                   'CDELTAT_RCARD' + str(RIOnum) + 'CH' + str(CHnum))

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
    AddNodeWithTag(tree, datapath + ':TIME', 'NUMERIC', 'TIMEVALUES_TEKCH' +
                   str(scope_chnum))
    AddNodeWithTag(tree, datapath + ':VOLTAGE', 'NUMERIC',
                   'VOLTAGEVALUES_TEKCH' + str(scope_chnum))
    AddNodeWithTag(tree, settingpath + ':N_SAMPLES', 'NUMERIC',
                   'NSAMPLES_TEKCH' + str(scope_chnum))
    AddNodeWithTag(tree, settingpath + ':DELTA_T', 'NUMERIC', 'DT_TEKCH' +
                   str(scope_chnum))
    AddNodeWithTag(tree, settingpath + ':N_PRE_SAMP', 'NUMERIC',
                   'NPRESAMP_TEKCH' + str(scope_chnum))
    AddNodeWithTag(tree, settingpath + ':TIME_DIV', 'NUMERIC',
                   'TIMEPERDIV_TEKCH' + str(scope_chnum))
    AddNodeWithTag(tree, settingpath + ':VOLT_DIV', 'NUMERIC',
                   'VOLTSPERDIV_TEKCH' + str(scope_chnum))
    AddNodeWithTag(tree, settingpath + ':PROBE_ATTEN', 'NUMERIC',
                   'PROBEATTENUATION_TEKCH' + str(scope_chnum))


def camframes(tree, cam_frame):
    """
    This function builds the storage nodes for the images produced by the
    PI-MAX3 camera.
    """
    campath = '.CAMERAS.PIMAX3'
    settingspath = '.CAMERAS.PIMAX3.CAM_SETTING'
    cam_frame = cam_frame + 1
    AddNodeWithTag(tree, campath + ':FRAME_' + str(cam_frame), 'NUMERIC',
                   'PIMAX_FRAME' + str(cam_frame))
    AddNodeWithTag(tree, campath + '.FRAME_' + str(cam_frame) + ':EXPOSURE', 
                   'NUMERIC', 'EXPOSURE_PFRAME' + str(cam_frame))
    AddNodeWithTag(tree, campath + '.FRAME_' + str(cam_frame) + ':DELAY', 
                   'NUMERIC', 'GATEDELAY_PFRAME' + str(cam_frame)) 
    
