"""
Produces NIRAWDATA tree structure.

Created on Mon Oct 21 15:31:15 2013

@author: A. Card
"""
import MDSplus as mds
import Functions as func

"""
surya = '192.168.0.194'
mds.Connection(surya)
"""

proto = mds.Tree(tree='proto_tree', shot=-1, mode='New')

DAQcard = 3
DAQchannel = 8
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

"""Build voltage measurements child branch."""
for i in xrange(DAQcard):
    func.VOLTcards(proto, i)
    for j in xrange(DAQchannel):
        func.VOLTchannels(proto, i, j)

proto.write()
proto.quit()
