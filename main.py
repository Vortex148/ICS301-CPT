import aircraft
import tools

# tools.printDanger("DANGER")
# tools.printWarning("WARN")
# tools.printBlue("Blue")

test = aircraft.player()
npc = aircraft.npc(aircraft.npc.Types.SU57)
test.adjustOrdinance()

test.promotionProgress()
test.testAtBase()
