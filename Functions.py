"""
Functions utilized in master tree construction file.

Created on Mon Oct 21 14:20:36 2013

@author: A. Card
"""


def TreeInit(tree):
    """
    Initializes the TOP node structure.
    """
    tree.addNode('.TIMING_CARDS')
    tree.addNode('.DAQ_CARDS')
    tree.addNode('.VOLT_DATA')
    tree.addNode(':SHOT_DATE', usage='TEXT')
    tree.addNode(':SHOT_NOTES', usage='TEXT')
    tree.addNode(':SYS_MESSAGE', usage='TEXT')


def TIMEcards(tree, TIMEnum):
    """
    Builds the node structure for the timing cards.
    """
    tree.addNode('.TIMING_CARDS.TCARD_' + str(TIMEnum))
    tree.addNode('.TIMING_CARDS.TCARD_' + str(TIMEnum) + '.SETTINGS')
    tree.addNode('.TIMING_CARDS.TCARD_' + str(TIMEnum) +
                 '.SETTINGS:SLOT_NUMBER', usage='TEXT')


def TIMEchannels(tree, TIMEnum, CHnum):
    """
    Builds the node structure for the timing cards' channels.
    """
    tree.addNode('.TIMING_CARDS.TCARD_'
                 + str(TIMEnum) + '.CHANNEL_' + str(CHnum))
    tree.addNode('.TIMING_CARDS.TCARD_'
                 + str(TIMEnum) + '.CHANNEL_' + str(CHnum) + ':ACTIVE',
                 usage='NUMERIC')
    tree.addNode('.TIMING_CARDS.TCARD_'
                 + str(TIMEnum) + '.CHANNEL_' + str(CHnum) + ':CHANNEL_NAME',
                 usage='TEXT')
    tree.addNode('.TIMING_CARDS.TCARD_'
                 + str(TIMEnum) + '.CHANNEL_' + str(CHnum) + ':DELAY',
                 usage='NUMERIC')
    tree.addNode('.TIMING_CARDS.TCARD_'
                 + str(TIMEnum) + '.CHANNEL_' + str(CHnum) + ':PULSE_WIDTH',
                 usage='NUMERIC')
    tree.addNode('.TIMING_CARDS.TCARD_'
                 + str(TIMEnum) + '.CHANNEL_' + str(CHnum) + ':NI_NAME',
                 usage='TEXT')


def DAQcards(tree, DAQnum):
    """
    This function creates the tree structure for all DAQ cards.
    """
    tree.addNode('.DAQ_CARDS.DAQ_' + str(DAQnum))
    tree.addNode('.DAQ_CARDS.DAQ_' + str(DAQnum) + '.SETTINGS')
    tree.addNode('.DAQ_CARDS.DAQ_' + str(DAQnum) +
                 '.SETTINGS:START_T', usage='NUMERIC')
    tree.addNode('.DAQ_CARDS.DAQ_' + str(DAQnum) +
                 '.SETTINGS:END_T', usage='NUMERIC')
    tree.addNode('.DAQ_CARDS.DAQ_' + str(DAQnum) +
                 '.SETTINGS:SAMPLE_RATE', usage='NUMERIC')
    tree.addNode('.DAQ_CARDS.DAQ_' + str(DAQnum) +
                 '.SETTINGS:DELTA_T', usage='NUMERIC')
    tree.addNode('.DAQ_CARDS.DAQ_' + str(DAQnum) +
                 '.SETTINGS:N_PRE_SAMP', usage='NUMERIC')
    tree.addNode('.DAQ_CARDS.DAQ_' + str(DAQnum) +
                 '.SETTINGS:N_SAMPLES', usage='NUMERIC')
    tree.addNode('.DAQ_CARDS.DAQ_' + str(DAQnum) +
                 '.SETTINGS:SLOT_NUMBER', usage='TEXT')


def DAQchannels(tree, DAQnum, CHnum):
    """
    This function creates the tree structure for a given
    DAQ channel by reading the variable DAQnum.
    """
    tree.addNode('.DAQ_CARDS.DAQ_'
                 + str(DAQnum) + '.CHANNEL_' + str(CHnum))
    tree.addNode('.DAQ_CARDS.DAQ_'
                 + str(DAQnum) + '.CHANNEL_' + str(CHnum) + ':ACTIVE',
                 usage='NUMERIC')
    tree.addNode('.DAQ_CARDS.DAQ_'
                 + str(DAQnum) + '.CHANNEL_' + str(CHnum) + ':CHANNEL_NAME',
                 usage='TEXT')
    tree.addNode('.DAQ_CARDS.DAQ_'
                 + str(DAQnum) + '.CHANNEL_' + str(CHnum) + ':VOLT_RANGE',
                 usage='NUMERIC')
    tree.addNode('.DAQ_CARDS.DAQ_'
                 + str(DAQnum) + '.CHANNEL_' + str(CHnum) + ':NI_NAME',
                 usage='TEXT')


def VOLTcards(tree, DAQnum):
    """
    This function creates the tree structure for all DAQ cards.
    """
    tree.addNode('.VOLT_DATA.DAQ_' + str(DAQnum))


def VOLTchannels(tree, DAQnum, CHnum):
    """
    This function creates the tree structure for all DAQ cards.
    """
    tree.addNode('.VOLT_DATA.DAQ_' + str(DAQnum) + '.CHANNEL_' + str(CHnum))
    tree.addNode('.VOLT_DATA.DAQ_'
                 + str(DAQnum) + '.CHANNEL_' + str(CHnum) + ':WAVEFORM',
                 usage='SIGNAL')
    tree.addNode('.VOLT_DATA.DAQ_'
                 + str(DAQnum) + '.CHANNEL_' + str(CHnum) + ':TIME_VALUES',
                 usage='NUMERIC')
    tree.addNode('.VOLT_DATA.DAQ_'
                 + str(DAQnum) + '.CHANNEL_' + str(CHnum) + ':DATA_VALUES',
                 usage='NUMERIC')
    tree.addNode('.VOLT_DATA.DAQ_'
                 + str(DAQnum) + '.CHANNEL_' + str(CHnum) + ':DELTA_T',
                 usage='NUMERIC')
