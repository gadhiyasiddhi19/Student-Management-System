import os
import time
import random

# ---------------- COLORS ----------------
RESET = "\033[0m"
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
WHITE = "\033[97m"

# Windows Terminal color support
os.system("")

def clear():
    os.system("cls" if os.name == "nt" else "clear")


# ---------------- GANESHJI ----------------
ganesh = [
    MAGENTA + "                 .-=========-." + RESET,
    MAGENTA + "              .-'             '-." + RESET,
    YELLOW  + "            .'      👑 👑 👑      '." + RESET,
    YELLOW  + "           /      ███████████      \\" + RESET,
    RED     + "          /     ███           ███     \\" + RESET,
    RED     + "         |    ███    ●     ●    ███    |" + RESET,
    WHITE   + "         |   ███        ^        ███   |" + RESET,
    WHITE   + "         |   ███      \\___/      ███   |" + RESET,
    YELLOW  + "          \\    ███      |      ███    /" + RESET,
    YELLOW  + "           \\    █████████████████    /" + RESET,
    RED     + "            '._       ███       _.'" + RESET,
    RED     + "               '-----█████-----'" + RESET,
    CYAN    + "                    █████" + RESET,
    CYAN    + "                 ███████████" + RESET,
    GREEN   + "              █████████████████" + RESET,
    GREEN   + "            █████████████████████" + RESET,
    YELLOW  + "                ███████████" + RESET,
]


# ---------------- DECORATION ----------------
def decorations(frame):

    sparkle = [
        "✨", "🌟", "✦", "✧", "❖"
    ]

    s1 = sparkle[frame % len(sparkle)]
    s2 = sparkle[(frame + 2) % len(sparkle)]

    print()
    print(MAGENTA + "╔══════════════════════════════════════════════════════════╗" + RESET)
    print(MAGENTA + "║" + RESET +
          f"       {s1}  {YELLOW}GANESH CHATURTHI{RESET}  {s2}       " +
          MAGENTA + "║" + RESET)
    print(MAGENTA + "╚══════════════════════════════════════════════════════════╝" + RESET)

    print()
    print(RED + "       🌺       🪔       🌸       🪔       🌺" + RESET)
    print()


# ---------------- MODAK ----------------
def show_modak():

    print()
    print(YELLOW + "              🍬 MODAK        🍬 MODAK" + RESET)
    print()
    print(YELLOW + "                 /\\              /\\" + RESET)
    print(YELLOW + "                /  \\            /  \\" + RESET)
    print(YELLOW + "               /    \\          /    \\" + RESET)
    print(YELLOW + "              /______\\        /______\\" + RESET)
    print(YELLOW + "              \\______/        \\______/" + RESET)


# ---------------- DIYAS ----------------
def show_diyas(frame):

    flame = ["🔥", "🕯️", "🔥", "🕯️"][frame % 4]

    print()
    print(
        RED + "        🪔" + RESET +
        "          " + YELLOW + flame + RESET +
        "          " + RED + "🪔" + RESET
    )


# ---------------- MAIN ANIMATION ----------------
for frame in range(12):

    clear()

    decorations(frame)

    # Ganeshji
    for line in ganesh:
        print(" " * 10 + line)

    show_modak()
    show_diyas(frame)

    print()
    print(CYAN + "     🌸  🌸  🌸  🌸  🌸  🌸  🌸" + RESET)

    print()
    print(YELLOW + "          🙏 GANPATI BAPPA MORYA 🙏" + RESET)

    print(GREEN + "             MANGAL MURTI MORYA" + RESET)

    print()
    print(MAGENTA + "        Created with Python 🐍" + RESET)

    time.sleep(0.6)


# ---------------- FINAL SCREEN ----------------
clear()

print()
print(MAGENTA + "╔══════════════════════════════════════════════════════════╗" + RESET)
print()
print(YELLOW + "             🌺  GANESH CHATURTHI  🌺" + RESET)
print()

for line in ganesh:
    print(" " * 10 + line)

print()
show_modak()
show_diyas(0)

print()
print(RED + "       🌸 🪔 🌸 🪔 🌸 🪔 🌸 🪔 🌸" + RESET)
print()

print(YELLOW + "          🙏 GANPATI BAPPA MORYA 🙏" + RESET)
print(GREEN + "             MANGAL MURTI MORYA" + RESET)

print()
print(MAGENTA + "╚══════════════════════════════════════════════════════════╝" + RESET)