"""
Produces MOCHImodel tree structure.

Initialized Mon Oct 21 15:31:15 2013

Author: A. Card
"""
import MDSplus as mds
import Functions as func
reload(func)

proto = mds.Tree(tree='proto_tree', shot=-1, mode='New')

DAQcard = 3
DAQchannel = 8
RIOcard = 3
RIOchannel = 32
TimeCard = 2
TCardChannel = 8

"""Initialize TOP node parent structure."""
func.TreeInit(proto)

"""Build Timing child branch."""
for i in xrange(TimeCard):
    func.TIMEcards(proto, i)
    for j in xrange(TCardChannel):
        func.TIMEchannels(proto, i, j)

"""Build DAQ card child branch."""
for i in xrange(DAQcard):
    func.DAQcards(proto, i)
    for j in xrange(DAQchannel):
        func.DAQchannels(proto, i, j)
        
"""Build RIO card child branch."""
for i in xrange(RIOcard):
    func.RIOcards(proto, i)
    for j in xrange(RIOchannel):
        func.RIOchannels(proto, i, j)

"""Build DAQ voltage measurements child branch."""
for i in xrange(DAQcard):
    for j in xrange(DAQchannel):
        func.VOLTchannels_D(proto, i, j)
        
"""Build RIO voltage measurements child branch."""
for i in xrange(RIOcard):
    for j in xrange(RIOchannel):
        func.VOLTchannels_R(proto, i, j)

proto.write()
proto.quit()
