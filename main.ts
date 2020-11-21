// startLight = input.light_level()
//  step = 0
// ########Testing 1 show leds##########
while (true) {
    basic.showLeds(`
    # . . . #
    . # . # .
    . . # . .
    . # . # .
    # . . . #
    `)
    basic.pause(500)
    basic.clearScreen()
    basic.pause(500)
}
