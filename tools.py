import os
import keyboard


def clearTerminal():
    os.system('cls' if os.name == 'nt' else 'clear')


def printWarning(message):
    print('\033[93m' + message + '\033[0m')


def printDanger(message):
    print('\033[91m' + message + '\033[0m')


def printBlue(message):
    print('\033[94m' + message + '\033[0m')


def update_selector_vertical(content, selector_pos, last_print):
    clearTerminal()
    print(last_print)
    for i in range(len(content)):
        if selector_pos == i:
            last_print += "\n" + content[i] + "\t<--"
            print(content[i] + "\t<--")
        else:
            last_print += "\n" + content[i]
            print(content[i])


def generateSelectorDict(display_content, drop_down_content):
    last_print = ""
    doublepress = False
    selector_open = False
    pos = [0, 0]
    string_ordinance = ""

    for i in display_content:
        string_ordinance += display_content[i] + "\t"

    while True:
        if keyboard.is_pressed("left") or keyboard.is_pressed("right") and not doublepress:

            offset = ""
            clearTerminal()
            if keyboard.is_pressed("left") and not doublepress:
                pos[0] = (pos[0] - 1) % 6

            elif keyboard.is_pressed("right") and not doublepress:
                pos[0] = (pos[0] + 1) % 6

            for i in range(pos[0]):
                offset = offset + len(display_content[i]) * " " + "\t"
            print(string_ordinance)
            print(offset + len(display_content[pos[0]]) // 2 * " " + "^")
            last_print = string_ordinance + "\n" + offset + len(display_content[pos[0]]) // 2 * " " + "^"

            doublepress = True

        elif keyboard.is_pressed("up") or keyboard.is_pressed("down") and not doublepress:
            if keyboard.is_pressed("up") and not doublepress:
                pos[1] = (pos[1] - 1) % len(drop_down_content)
            elif keyboard.is_pressed("down") and not doublepress:
                pos[1] = (pos[1] + 1) % len(drop_down_content)
            update_selector_vertical(drop_down_content, pos[1], last_print)
            doublepress = True
            selector_open = True


        elif keyboard.is_pressed("enter") and not doublepress and not selector_open:
            input()
            clearTerminal()
            print(last_print)
            for i in range(len(drop_down_content)):
                if pos[1] == i:

                    print(drop_down_content[i] + "\t<--")
                else:

                    print(drop_down_content[i])
            doublepress = True
            selector_open = True

        elif keyboard.is_pressed("enter") and not doublepress and selector_open:
            input("Confirm?")
            display_content[pos[0]] = drop_down_content[pos[1]]
            string_ordinance = ""
            for i in display_content:
                string_ordinance += display_content[i] + "\t"
            selector_open = False
            doublepress = True

        elif keyboard.is_pressed("esc"):
            return string_ordinance.strip().split("\t")

        elif not keyboard.is_pressed("left") and not keyboard.is_pressed("right") and not keyboard.is_pressed(
                "enter") and not keyboard.is_pressed("up") and not keyboard.is_pressed("down"):
            doublepress = False


