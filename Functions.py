"""
Functions utilized in "master" tree construction file.

Initialized Mon Oct 21 14:20:36 2013

Author: A. Card
"""


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
    tree.addNode('.SETTINGS.EXPERIMENT:SHOT_DATE', usage='TEXT')
    tree.addNode('.SETTINGS.EXPERIMENT:SHOT_NOTES', usage='TEXT')
    tree.addNode('.SETTINGS.EXPERIMENT:SYS_MESSAGE', usage='TEXT')
    tree.addNode('.SETTINGS.EXPERIMENT:SHOT_FLAVOR', usage='TEXT')
    tree.addNode('.SETTINGS.EXPERIMENT:SHOT_NUMBER', usage='TEXT')


def TIMEcards(tree, TIMEnum):
    """
    Builds the node structure for the timing cards.
    """
    tree.addNode('.SETTINGS.NI.TIMING.TCARD_' + str(TIMEnum))
    tree.addNode('.SETTINGS.NI.TIMING.TCARD_' + str(TIMEnum) +
                 '.TCARD_GLOBAL')
    tree.addNode('.SETTINGS.NI.TIMING.TCARD_' + str(TIMEnum) +
                 '.TCARD_GLOBAL:SLOT_NUMBER', usage='TEXT')


def TIMEchannels(tree, TIMEnum, CHnum):
    """
    Builds the node structure for the timing cards' channels.
    """
    tree.addNode('.SETTINGS.NI.TIMING.TCARD_'
                 + str(TIMEnum) + '.CHANNEL_' + str(CHnum))
    tree.addNode('.SETTINGS.NI.TIMING.TCARD_'
                 + str(TIMEnum) + '.CHANNEL_' + str(CHnum) + ':ACTIVE',
                 usage='NUMERIC')
    tree.addNode('.SETTINGS.NI.TIMING.TCARD_'
                 + str(TIMEnum) + '.CHANNEL_' + str(CHnum) + ':CHANNEL_NAME',
                 usage='TEXT')
    tree.addNode('.SETTINGS.NI.TIMING.TCARD_'
                 + str(TIMEnum) + '.CHANNEL_' + str(CHnum) + ':DELAY',
                 usage='NUMERIC')
    tree.addNode('.SETTINGS.NI.TIMING.TCARD_'
                 + str(TIMEnum) + '.CHANNEL_' + str(CHnum) + ':PULSE_WIDTH',
                 usage='NUMERIC')
    tree.addNode('.SETTINGS.NI.TIMING.TCARD_'
                 + str(TIMEnum) + '.CHANNEL_' + str(CHnum) + ':NI_NAME',
                 usage='TEXT')


def DAQcards(tree, DAQnum):
    """
    This function creates the tree structure for all DAQ cards.
    """
    tree.addNode('.NI_DAQ.DAQ_' + str(DAQnum))
    tree.addNode('.NI_DAQ.DAQ_' + str(DAQnum) + '.DCARD_GLOBAL')
    tree.addNode('.NI_DAQ.DAQ_' + str(DAQnum) +
                 '.DCARD_GLOBAL:START_T', usage='NUMERIC')
    tree.addNode('.NI_DAQ.DAQ_' + str(DAQnum) +
                 '.DCARD_GLOBAL:END_T', usage='NUMERIC')
    tree.addNode('.NI_DAQ.DAQ_' + str(DAQnum) +
                 '.DCARD_GLOBAL:SAMPLE_RATE', usage='NUMERIC')
    tree.addNode('.NI_DAQ.DAQ_' + str(DAQnum) +
                 '.DCARD_GLOBAL:DELTA_T', usage='NUMERIC')
    tree.addNode('.NI_DAQ.DAQ_' + str(DAQnum) +
                 '.DCARD_GLOBAL:N_PRE_SAMP', usage='NUMERIC')
    tree.addNode('.NI_DAQ.DAQ_' + str(DAQnum) +
                 '.DCARD_GLOBAL:N_SAMPLES', usage='NUMERIC')
    tree.addNode('.NI_DAQ.DAQ_' + str(DAQnum) +
                 '.DCARD_GLOBAL:SLOT_NUMBER', usage='TEXT')


def DAQchannels(tree, DAQnum, CHnum):
    """
    This function creates the tree structure for a given
    DAQ channel by reading the variable DAQnum.
    """
    tree.addNode('.NI_DAQ.DAQ_' + str(DAQnum) + '.CHANNEL_' + str(CHnum))
    tree.addNode('.NI_DAQ.DAQ_' + str(DAQnum) + '.CHANNEL_' + str(CHnum)
                 + '.CHAN_SETTING')
    tree.addNode('.NI_DAQ.DAQ_' + str(DAQnum) + '.CHANNEL_' + str(CHnum)
                 + '.CHAN_SETTING:ACTIVE', usage='NUMERIC')
    tree.addNode('.NI_DAQ.DAQ_' + str(DAQnum) + '.CHANNEL_' + str(CHnum)
                 + '.CHAN_SETTING:CHANNEL_NAME', usage='TEXT')
    tree.addNode('.NI_DAQ.DAQ_' + str(DAQnum) + '.CHANNEL_' + str(CHnum)
                 + '.CHAN_SETTING:VOLT_RANGE', usage='NUMERIC')
    tree.addNode('.NI_DAQ.DAQ_' + str(DAQnum) + '.CHANNEL_' + str(CHnum)
                 + '.CHAN_SETTING:NI_NAME', usage='TEXT')


def VOLTcards(tree, DAQnum):
    """
    This function creates the tree structure for all DAQ cards. INCOMPLETE!
    """
    tree.addNode('.NI_DAQ.DAQ_' + str(DAQnum))


def VOLTchannels(tree, DAQnum, CHnum):
    """
    This function creates the tree structure for all DAQ cards.
    """
    tree.addNode('.NI_DAQ.DAQ_' + str(DAQnum) + '.CHANNEL_' + str(CHnum)
                 + '.DATA')
    tree.addNode('.NI_DAQ.DAQ_' + str(DAQnum) + '.CHANNEL_' + str(CHnum)
                 + '.DATA:WAVEFORM', usage='SIGNAL')
    tree.addNode('.NI_DAQ.DAQ_' + str(DAQnum) + '.CHANNEL_' + str(CHnum)
                 + '.DATA:TIME_VALUES', usage='NUMERIC')
    tree.addNode('.NI_DAQ.DAQ_' + str(DAQnum) + '.CHANNEL_' + str(CHnum)
                 + '.DATA:DATA_VALUES', usage='NUMERIC')
    tree.addNode('.NI_DAQ.DAQ_' + str(DAQnum) + '.CHANNEL_' + str(CHnum)
                 + '.DATA:DELTA_T', usage='NUMERIC')
