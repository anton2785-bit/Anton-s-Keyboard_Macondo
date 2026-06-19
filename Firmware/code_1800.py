# code.py — 1800 Compact Keyboard (96-key)
# Firmware: KMK (CircuitPython)
# Matrix: 6 rows × 18 columns = 108 positions (12 unused/empty)
#
# Flash instructions:
#   1. Install CircuitPython on your MCU
#   2. Copy the KMK folder to CIRCUITPY/
#      (download from https://github.com/KMKfw/kmk_firmware)
#   3. Save this file as code.py on CIRCUITPY/
#
# ─────────────────────────────────────────────────────────────────

import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.layers import Layers
from kmk.extensions.media_keys import MediaKeys

keyboard = KMKKeyboard()

keyboard.modules.append(Layers())
keyboard.extensions.append(MediaKeys())

# ── Pin mapping ───────────────────────────────────────────────────
# Update these to match your MCU and wiring.
# Run `import board; print(dir(board))` to list available pins.

keyboard.col_pins = (
    board.D0,  board.D1,  board.D2,  board.D3,
    board.D4,  board.D5,  board.D6,  board.D7,
    board.D8,  board.D9,  board.D10, board.D11,
    board.D12, board.D13, board.D14, board.D15,
    board.D16, board.D17,
)  # 18 columns

keyboard.row_pins = (
    board.A0,  # Row 1 — Function row
    board.A1,  # Row 2 — Number row
    board.A2,  # Row 3 — QWERTY row
    board.A3,  # Row 4 — Home row
    board.A4,  # Row 5 — Bottom row
    board.A5,  # Row 6 — Space row
)  # 6 rows

keyboard.diode_orientation = DiodeOrientation.COL2ROW

# ── Keymap ────────────────────────────────────────────────────────
# 96-key 1800 compact layout — 6 rows × 18 columns.
# KC.TRNS marks unused matrix positions (no switch).
#
# Physical layout (standard 1800 compact):
#
# Row 1 — Function row (16 keys + 2 nav)
# ┌────┬────┬────┬────┬────┬────┬────┬────┬────┬────┬────┬────┬────┬────────┬────┬────┬────┬────┐
# │ESC │ F1 │ F2 │ F3 │ F4 │ F5 │ F6 │ F7 │ F8 │ F9 │F10 │F11 │F12 │  DEL   │PSCR│SCRL│PAUS│    │
# └────┴────┴────┴────┴────┴────┴────┴────┴────┴────┴────┴────┴────┴────────┴────┴────┴────┴────┘
#
# Row 2 — Number row (14 keys + numpad top)
# ┌────┬────┬────┬────┬────┬────┬────┬────┬────┬────┬────┬────┬────┬────────┬────┬────┬────┬────┐
# │ `  │ 1  │ 2  │ 3  │ 4  │ 5  │ 6  │ 7  │ 8  │ 9  │ 0  │ -  │ =  │ BSPC   │INS │HOME│PGUP│NLCK│
# └────┴────┴────┴────┴────┴────┴────┴────┴────┴────┴────┴────┴────┴────────┴────┴────┴────┴────┘
#
# Row 3 — QWERTY row
# ┌──────┬────┬────┬────┬────┬────┬────┬────┬────┬────┬────┬────┬────┬──────┬────┬────┬────┬────┐
# │ TAB  │ Q  │ W  │ E  │ R  │ T  │ Y  │ U  │ I  │ O  │ P  │ [  │ ]  │  \   │DEL │END │PGDN│ /  │
# └──────┴────┴────┴────┴────┴────┴────┴────┴────┴────┴────┴────┴────┴──────┴────┴────┴────┴────┘
#
# Row 4 — Home row
# ┌───────┬────┬────┬────┬────┬────┬────┬────┬────┬────┬────┬────┬───────────┬────┬────┬────┬────┐
# │ CAPS  │ A  │ S  │ D  │ F  │ G  │ H  │ J  │ K  │ L  │ ;  │ '  │   ENTER   │ 7  │ 8  │ 9  │ -  │
# └───────┴────┴────┴────┴────┴────┴────┴────┴────┴────┴────┴────┴───────────┴────┴────┴────┴────┘
#
# Row 5 — Shift row
# ┌─────────┬────┬────┬────┬────┬────┬────┬────┬────┬────┬────┬─────────┬────┬────┬────┬────┬────┐
# │  LSFT   │ Z  │ X  │ C  │ V  │ B  │ N  │ M  │ ,  │ .  │ /  │  RSFT   │ ↑  │ 1  │ 2  │ 3  │ +  │
# └─────────┴────┴────┴────┴────┴────┴────┴────┴────┴────┴────┴─────────┴────┴────┴────┴────┴────┘
#
# Row 6 — Bottom row
# ┌─────┬─────┬─────┬──────────────────────────────┬─────┬─────┬─────┬────┬────┬────┬────┬────┐
# │LCTL │LGUI │LALT │            SPACE              │RALT │RGUI │RCTL │ ←  │ ↓  │ →  │ 0  │ENT │
# └─────┴─────┴─────┴──────────────────────────────┴─────┴─────┴─────┴────┴────┴────┴────┴────┘

keyboard.keymap = [
    [
        # Row 1 — Function row (18 keys, last position unused)
        KC.ESC,  KC.F1,   KC.F2,   KC.F3,   KC.F4,   KC.F5,   KC.F6,   KC.F7,
        KC.F8,   KC.F9,   KC.F10,  KC.F11,  KC.F12,  KC.DEL,  KC.PSCR, KC.SCRL,
        KC.PAUS, KC.TRNS,

        # Row 2 — Number row + right cluster top + numlock
        KC.GRV,  KC.N1,   KC.N2,   KC.N3,   KC.N4,   KC.N5,   KC.N6,   KC.N7,
        KC.N8,   KC.N9,   KC.N0,   KC.MINS, KC.EQL,  KC.BSPC, KC.INS,  KC.HOME,
        KC.PGUP, KC.NLCK,

        # Row 3 — QWERTY row + right cluster mid + numpad top
        KC.TAB,  KC.Q,    KC.W,    KC.E,    KC.R,    KC.T,    KC.Y,    KC.U,
        KC.I,    KC.O,    KC.P,    KC.LBRC, KC.RBRC, KC.BSLS, KC.DEL,  KC.END,
        KC.PGDN, KC.PSLS,

        # Row 4 — Home row + numpad middle
        KC.CAPS, KC.A,    KC.S,    KC.D,    KC.F,    KC.G,    KC.H,    KC.J,
        KC.K,    KC.L,    KC.SCLN, KC.QUOT, KC.ENT,  KC.TRNS, KC.P7,   KC.P8,
        KC.P9,   KC.PMNS,

        # Row 5 — Shift row + arrows + numpad bottom
        KC.LSFT, KC.Z,    KC.X,    KC.C,    KC.V,    KC.B,    KC.N,    KC.M,
        KC.COMM, KC.DOT,  KC.SLSH, KC.RSFT, KC.UP,   KC.TRNS, KC.P1,   KC.P2,
        KC.P3,   KC.PPLS,

        # Row 6 — Bottom row + arrows + numpad 0 + numpad enter
        KC.LCTL, KC.LGUI, KC.LALT, KC.SPC,  KC.TRNS, KC.TRNS, KC.TRNS, KC.RALT,
        KC.RGUI, KC.RCTL, KC.LEFT, KC.DOWN, KC.RGHT, KC.TRNS, KC.P0,   KC.TRNS,
        KC.PDOT, KC.PENT,
    ]
]

# ── Start! ────────────────────────────────────────────────────────
if __name__ == '__main__':
    keyboard.go()
