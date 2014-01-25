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
    """ Single-valued member nodes """
    AddNodeWithTag(tree,'.SETTINGS.EXPERIMENT:SHOT_DATE','TEXT',
                   'SHOTDATEANDTIME')
    AddNodeWithTag(tree,'.SETTINGS.EXPERIMENT:SHOT_NOTES','TEXT','SHOTNOTES')
    AddNodeWithTag(tree,'.SETTINGS.EXPERIMENT:SYS_MESSAGE','TEXT','SYSMESSAGE')
    AddNodeWithTag(tree,'.SETTINGS.EXPERIMENT:SHOT_QUALITY','TEXT',
                   'SHOTQUALITY')
    AddNodeWithTag(tree,'.SETTINGS.EXPERIMENT:SHOT_NUMBER','TEXT',
                   'SHOTNUMBER')


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
    AddNodeWithTag(tree, chanpath + ':DELAY', 'NUMERIC', 'DELAYTIME_CARD' +
                   str(TIMEnum) + 'CH' + str(CHnum))
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
    AddNodeWithTag(tree, cardpath + ':START_T', 'NUMERIC', 'START_CARD' +
                   str(DAQnum))
    AddNodeWithTag(tree, cardpath + ':END_T', 'NUMERIC', 'END_CARD' +
                   str(DAQnum))
    AddNodeWithTag(tree, cardpath + ':SAMPLE_RATE', 'NUMERIC', 
                   'SAMPLERATE_CARD' + str(DAQnum))
    AddNodeWithTag(tree, cardpath + ':DELTA_T', 'NUMERIC', 'DELTAT_CARD' +
                   str(DAQnum))
    AddNodeWithTag(tree, cardpath + ':N_PRE_SAMP', 'NUMERIC', 'N_PRESAMP_CARD' +
                   str(DAQnum))
    AddNodeWithTag(tree, cardpath + ':N_SAMPLES', 'NUMERIC',
                   'NUMBERSAMPLES_CARD' + str(DAQnum))
    AddNodeWithTag(tree, cardpath + ':SLOT_NUMBER', 'TEXT', 'DAQSLOTNUM_CARD' +
                   str(DAQnum))


def DAQchannels(tree, DAQnum, CHnum):
    """
    This function creates the tree structure for a given
    DAQ channel by reading the variable DAQnum.
    """
    tree.addNode('.NI_DAQ.DAQ_' + str(DAQnum) + '.CHANNEL_' + str(CHnum))
    chanpath = ('.NI_DAQ.DAQ_' + str(DAQnum) + '.CHANNEL_' + str(CHnum)
                 + '.CHAN_SETTING')
    tree.addNode(chanpath)
    AddNodeWithTag(tree, chanpath + ':ACTIVE', 'NUMERIC', 'DAQTIVE_CARD' +
                   str(DAQnum) + 'CH' + str(CHnum))
    AddNodeWithTag(tree, chanpath + ':CHANNEL_NAME', 'TEXT', 'CHANNELNAME_CARD' 
                   + str(DAQnum) + 'CH' + str(CHnum))
    AddNodeWithTag(tree, chanpath + ':VOLT_RANGE', 'NUMERIC', 'VOLTRANGE_CARD' 
                   + str(DAQnum) + 'CH' + str(CHnum))
    AddNodeWithTag(tree, chanpath + ':NI_NAME', 'TEXT', 'DAQNINAME_CARD' 
                   + str(DAQnum) + 'CH' + str(CHnum))


def VOLTcards(tree, DAQnum):
    """
    This function creates the tree structure for all DAQ cards. INCOMPLETE!
    """
    tree.addNode('.NI_DAQ.DAQ_' + str(DAQnum))


def VOLTchannels(tree, DAQnum, CHnum):
    """
    This function creates the tree structure for all DAQ cards.
    """
    datapath = ('.NI_DAQ.DAQ_' + str(DAQnum) + '.CHANNEL_' + str(CHnum))
    AddNodeWithTag(tree, datapath + ':DATA', 'SIGNAL', 'NIRAWDATA_CARD' 
                   + str(DAQnum) + 'CH' + str(CHnum))
    AddNodeWithTag(tree, datapath + '.DATA:TIME_VALUES', 'NUMERIC', 
                   'NITIMEVALUES_CARD' + str(DAQnum) + 'CH' + str(CHnum))
    AddNodeWithTag(tree, datapath + '.DATA:DATA_VALUES', 'NUMERIC', 
                   'NIDATAVALUES_CARD' + str(DAQnum) + 'CH' + str(CHnum))
    AddNodeWithTag(tree, datapath + '.DATA:DELTA_T', 'NUMERIC', 
                   'NIDELTAT_CARD' + str(DAQnum) + 'CH' + str(CHnum))

