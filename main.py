#startLight = input.light_level()
# step = 0
#########Testing 1 show leds##########
while True:
    basic.show_leds("""
    # . . . #
    . # . # .
    . . # . .
    . # . # .
    # . . . #
    """)
    basic.pause(500)
    basic.clear_screen()
    basic.pause(500)
###### IfElse button testing#########
# while True:
#     if input.button_is_pressed(Button.A):
#         basic.show_icon(IconNames.SAD)
#     elif input.button_is_pressed(Button.B):
#         basic.show_icon(IconNames.HAPPY)
#     else:
#         basic.show_icon(IconNames.CONFUSED)
##########Light Sensor##################
#While True:
    #Light_intensity=input.light_level()
    #led.plot_bar_graph(Light_intensity, 255)
    #if(startLight>input.light_level()):
    #   music.play_melody("C5 C5 C5", 150)
    #   basic.show_icon(IconNames.ANGRY)
    #else:
    #    basic.show_icon(IconNames.HAPPY)
##########Temperature##################
#While True:
    # currenttemp=input.temperature()
    # basic.show_number(currenttemp)
    # pause(500)
    # if(currenttemp>25):
    #     music.play_melody("C5 C5 C5", 120)
    #     basic.show_icon(IconNames.ANGRY)
        
    # else:
    #     basic.show_icon(IconNames.HAPPY)

##########Acceleration Testing##################    
    # if(input.acceleration(Dimension.STRENGTH)>1300):
    #     step+=1
    # basic.show_number(step)
    # degree = input.compass_heading()
    # if(degree>45 and degree<135):
    #     basic.show_arrow(ArrowNames.EAST)
    # elif(degree<45 and degree>0 or degree>315 and degree<360):
    #     basic.show_arrow(ArrowNames.NORTH)
    # elif(degree>225 and degree<315):
    #     basic.show_arrow(ArrowNames.WEST)
    # else:
    #     basic.show_arrow(ArrowNames.SOUTH)
#######Gesture Test################################
# radio.set_group(1)
# def on_gesture_tilt_left():
#     radio.send_string("L")
# input.on_gesture(Gesture.TILT_LEFT,on_gesture_tilt_left)

# def on_gesture_tilt_right():
#     radio.send_string("R")
# input.on_gesture(Gesture.TILT_RIGHT,on_gesture_tilt_right)

# def on_gesture_tilt_forward():
#     radio.send_string("U")
# input.on_gesture(Gesture.LOGO_UP,on_gesture_tilt_forward)

# def on_gesture_tilt_backward():
#     radio.send_string("D")
# input.on_gesture(Gesture.LOGO_DOWN,on_gesture_tilt_backward)

# def on_received_string(receivedString):
#     if(receivedString=="L"):
#         basic.show_arrow(ArrowNames.EAST)
#     elif(receivedString=="R"):
#         basic.show_arrow(ArrowNames.WEST)
#     elif(receivedString=="U"):
#         basic.show_arrow(ArrowNames.NORTH)
#     elif(receivedString=="D"):
#         basic.show_arrow(ArrowNames.SOUTH)
#     else:
#         basic.clear_screen()
        
# radio.on_received_string(on_received_string)


            
       
