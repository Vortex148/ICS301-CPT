import json
import time
from enum import Enum
import keyboard
import tools


class genericAircraft:
    aircraftProperties = json.loads(open("aircraftProperties.json").read())
    name = None

    components = {
        "Wings": 0,
        "Fuselage": 0,
        "Cockpit": 0,
        "Electrical": 0,
        "Tail": 0
    }

    def __init__(self, name="null"):
        self.name = name


class npc(genericAircraft):
    class Types(Enum):
        SU57 = "SU57"
        F14 = "F14"
        F15 = "F15"
        F16 = "F16"
        F18 = "F18"

    def __init__(self, type: Types):
        genericAircraft.name = type.name
        for i in genericAircraft.components:
            genericAircraft.components[i] = genericAircraft.aircraftProperties[type.name]["DefaultComponents"][i]


class player(genericAircraft):
    class states(Enum):
        InBattle = "InBattle"
        AtBase = "AtBase"

    currentState = states.AtBase

    ordinance = {
        0: "9X",
        1: "AMRAAM",
        2: "9X",
        3: "9X",
        4: "AMRAAM",
        5: "9X"

    }

    unlockedOrdinance = ["9X", "AMRAAM", "9M"]

    levels = {0: 0,
              1: 100,
              2: 1000,
              3: 2000}
    level = 0
    level_points = 10

    def __init__(self):
        super().__init__("player")
        for i in genericAircraft.components:
            genericAircraft.components[i] = genericAircraft.aircraftProperties["player"]["DefaultComponents"][i]

    def generateOrdinance(self):
        ordinance = json.loads(open("munitions.json").read())
        ordinance = ordinance["missle"]
        return ordinance

    def analyzeAircraft(self, target: genericAircraft):
        print("After observing the aircraft, you gather this information:")
        for i in target.components:
            print(f"\t{i} -- {target.components[i]}")
            time.sleep(1)

        input("Press any key to continue...")
        tools.clearTerminal()

    def promotionProgress(self):
        tools.clearTerminal()
        progress = self.level_points / self.levels[self.level + 1] * 10

        print(f"You are currently level {self.level}. Your next promotion is to {self.level + 1}")
        print("|| " + "*" * int(progress) + "=" * int(
            10 - progress) + " ||" + f"" + f" \t{self.level_points} / {self.levels[self.level + 1]}")

        time.sleep(2)
        input("Press any key to continue...")
        tools.clearTerminal()

    def adjustOrdinance(self):
        adjusted_ordinance = tools.generateSelectorDict(self.ordinance, self.unlockedOrdinance)
        for i in range(len(adjusted_ordinance)):
            self.ordinance[i] = adjusted_ordinance[i]
        print(self.ordinance)

    def devValues(self):
        adjustedPoints = int(input("Enter number of points you would like to adjust: "))
        self.level_points = adjustedPoints

    def updateValues(self):

        for i in range(len(self.levels)):
            if self.level_points >= self.levels[i]:
                self.level = i



    def testAttack(self, target: npc):
        self.currentState = self.states.InBattle
        print("ATTACKING " + target.name)
        time.sleep(1)
        while (self.currentState == self.states.InBattle):
            operation = int(input("ENTER YOUR DESIRED OPERATION:"
                                  "\n 1: Analyze"
                                  "\n 2: Attack"
                                  "\n 3: Return to Base"
                                  "\n "))

            if operation == 1:
                self.analyzeAircraft(target)

    def testAtBase(self):

        self.currentState = self.states.AtBase
        print("AT BASE")
        time.sleep(1)
        print("WELCOME HOME PILOT")
        time.sleep(0.5)
        print(f"YOUR PILOT LEVEL IS {self.level}")
        while (self.currentState == self.states.AtBase):
            self.updateValues()
            operation = input("WHAT WOULD YOU LIKE TO DO PILOT:"
                                  "\n 1: Sortie"
                                  "\n 2: Adjust Ordinance"
                                  "\n 3: Request Acquisitions"
                                  "\n 4: View Promotion Progress"
                                  "\n 5: Dev Console"
                                  "\n")

            match(operation):
                case "1":
                    self.adjustOrdinance()

                case "2":
                    pass

                case "3":
                    pass

                case "4":
                    self.promotionProgress()

                case "5":
                    self.devValues()

