class Colors:
    background = "#1c1c22"
    object = "#2a2a34"
    #accent = "#0e74bb"
    accent = '#c8da2b'
    text = "WHITE"

class Spacer:
    source = 100
    source_buttons = 0
    exercise = 40
    display = 20

class Text:
    font = "Arial"
    size = 25
    format = "bold"
    text = [font, size, format]

class Padding:
    source = 0
    source_buttons = 0
    exercise = 10
    display = 0

class Styles:
    source_button = {
        "font": Text.text,
        "background": Colors.object,
        "foreground": Colors.text,
        "activebackground": Colors.object,
        "activeforeground": Colors.accent,
        "highlightthickness": 2,
        "highlightbackground": Colors.accent,
        "highlightcolor": "WHITE",
        "width": 23,
        "height": 2,
        "border": 0,
    }
    button_frame = {
        "highlightbackground": Colors.accent,
        "highlightthickness": 5,
        "background": Colors.accent,
        "border": 0,
    }
    optionmenu = {
        "font": Text.text,
        "background": Colors.object,
        "foreground": Colors.text,
        "activebackground": Colors.object,
        "activeforeground": Colors.accent,
        "highlightthickness": 5,
        "highlightbackground": Colors.accent,
        "highlightcolor": "WHITE",
        "width": 24,
        "border": 0,
    }