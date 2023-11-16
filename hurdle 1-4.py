#hurdle 1
#function dengan nama jalan
def jalan():
    move()
    turn_left()
    move()
    turn_left()
    turn_left()
    turn_left()
    move()
    turn_left()
    turn_left()
    turn_left()
    move()
    turn_left()
    
#function dengan nama jump    
def jump():
    jalan()
    jalan()
    jalan()
    jalan()
    jalan()
    jalan()

#perintah /memanggil fungsi
jump()

#cetak output
print (output)

#hurdle 2
def jalan():
    move()
    turn_left()
    move()
    turn_left()
    turn_left()
    turn_left()
    move()
    turn_left()
    turn_left()
    turn_left()
    move()
    turn_left()
    
def jump():
    jalan()
    jalan()
    
       
while at_goal()==False:
      jump()

#cetak output
print (output)



#hurdle 3
def lompat():
    while not wall_in_front():
        move()
        if at_goal():
            done()
     turn_left()
    while wall_on_right():
        move()
        turn_left()
        turn_left()
        turn_left()
        move()
        turn_left()
        turn_left()
        turn_left()
    while not wall_in_front():
        move()
    turn_left()
 
while not at_goal():
    lompat()

#cetak output
print (output)


#hurdle 4
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def lompat():
    while not wall_in_front():
        move()
        if at_goal():
            done()
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while not wall_in_front():
        move()
    turn_left()
 
while not at_goal():
    lompat()

#cetak output
print (output)

    
