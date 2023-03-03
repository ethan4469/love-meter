def on_pin_pressed_p0():
    basic.show_number(randint(0, 100))
input.on_pin_pressed(TouchPin.P0, on_pin_pressed_p0)

basic.show_string("LOVE METER")

def on_forever():
    pass
basic.forever(on_forever)
