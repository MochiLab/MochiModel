"""
Produces MOCHImodel tree structure.

Initialized Mon Oct 21 15:31:15 2013

Author: A. Card
"""
import MDSplus as mds
import Functions as func
reload(func)

tree = mds.Tree(tree='proto_tree', shot=-1, mode='New')

DAQcard = 3
DAQchannel = 8
RIOcard = 3
RIOchannel = 32
TimeCard = 2
TCardChannel = 8
DIOchannel = 8
scope_chan = 4
cam_frames = 2

"""Initialize TOP node parent structure"""
func.TreeInit(tree)

"""Build Global Settings branch"""
func.globalsettings(tree)

"""Build PSU LV panel interaction branch"""
func.PSUpanels(tree, 3)

"""Build Timing child branch"""
for i in xrange(TimeCard):
    func.TIMEcards(tree, i)
    for j in xrange(TCardChannel):
        func.TIMEchannels(tree, i, j)

"""Build DAQ card child branch"""
for i in xrange(DAQcard):
    func.DAQcards(tree, i)
    for j in xrange(DAQchannel):
        func.DAQchannels(tree, i, j)
        
"""Build RIO card child branch"""
for i in xrange(RIOcard):
    func.RIOcards(tree, i)
    for j in xrange(RIOchannel):
        func.RIOchannels(tree, i, j)

"""Build DAQ voltage data measurements child branch"""
for i in xrange(DAQcard):
    for j in xrange(DAQchannel):
        func.DATAchannels_D(tree, i, j)
        
"""Build RIO voltage data measurements child branch"""
for i in xrange(RIOcard):
    for j in xrange(RIOchannel):
        func.DATAchannels_R(tree, i, j)
        
"""Build DIO relay control branch"""
for i in range(DAQcard):
    func.DIOcards(tree, i)
    for j in range(DIOchannel):
        func.DIOchannels(tree, i, j)
    
"""Build oscilloscope storage branch"""
for i in range(scope_chan):
    func.scopechannels(tree, i)

"""Build camera storage branch"""
func.camsettings(tree)
for i in range(cam_frames):
    func.camframes(tree, i)

tree.write()
tree.quit()
