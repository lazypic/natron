#gui mode

import NatronEngine
import scan2grey
NatronEngine.natron.appendToNatronPath("~/natronset/python")


NatronGui.natron.addMenuCommand("lazypic/Scripts/Scan2grey","scan2grey.scan2grey")
