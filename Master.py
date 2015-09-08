"""
Produces MOCHImodel tree structure.

Initialized Mon Oct 21 15:31:15 2013

Author: A. Card
"""
import MDSplus as mds
import Functions as func
reload(func)

treename = mds.Tree(tree='test_tree', shot=-1, mode='New')

DAQcard = 3
DAQchannel = 8
RIOcard = 3
RIOchannel = 32
TimeCard = 2
TCardChannel = 8
DIOchannel = 8
scope_chan = 4

"""Initialize TOP node parent structure"""
func.TreeInit(treename)

"""Build Timing child branch"""
for i in xrange(TimeCard):
    func.TIMEcards(treename, i)
    for j in xrange(TCardChannel):
        func.TIMEchannels(treename, i, j)

"""Build DAQ card child branch"""
for i in xrange(DAQcard):
    func.DAQcards(treename, i)
    for j in xrange(DAQchannel):
        func.DAQchannels(treename, i, j)
        
"""Build RIO card child branch"""
for i in xrange(RIOcard):
    func.RIOcards(treename, i)
    for j in xrange(RIOchannel):
        func.RIOchannels(treename, i, j)

"""Build DAQ voltage data measurements child branch"""
for i in xrange(DAQcard):
    for j in xrange(DAQchannel):
        func.DATAchannels_D(treename, i, j)
        
"""Build RIO voltage data measurements child branch"""
for i in xrange(RIOcard):
    for j in xrange(RIOchannel):
        func.DATAchannels_R(treename, i, j)
        
"""Build DIO relay control branch."""
for i in range(DIOchannel):
    func.DIOchannels(treename, i)
    
"""Build oscilloscope storage branch"""
for i in range(scope_chan):
    func.scopechannels(treename, i)

treename.write()
treename.quit()
