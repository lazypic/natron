#gui mode

import NatronEngine
NatronEngine.natron.appendToNatronPath("~/natronset/python")
import scan2grey
NatronGui.natron.addMenuCommand("lazypic/Scripts/Scan2grey","scan2grey.scan2grey")
