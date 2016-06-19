
import NatronEngine
import NatronGui

def scan2grey():
	app = NatronGui.natron.getGuiInstance(0)
	t = app.createNode("fr.inria.openfx.ReadOIIO")
