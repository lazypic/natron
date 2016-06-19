#coding:utf8
import NatronEngine
import NatronGui

def scan2grey():
	inum = NatronEngine.natron.getNumInstances() #최초 1을 반환한다.
	app = NatronGui.natron.getGuiInstance(inum-1)
	t = app.createNode("fr.inria.openfx.ReadOIIO")
