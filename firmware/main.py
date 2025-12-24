import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC

keyboard = KMKKeyboard()

PINS = [board.D0, board.D1, board.D2, board.D3, board.D4, board.D5, board.D6, board.D7, board.D8]

keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

keyboard.keymap = [
    [KC.Z, KC.S, KC.X, KC.D, KC.C, KC.F, KC.V, KC.G, KC.B]
]

#Start!
if __name__ == '__main__':
    keyboard.go()
