#Sound Levels
Jackhammer = 130
Gas_Lawnmower = 106 
Alarm_Clock = 70 
Quiet_Room = 40 
sound = int(input("Enter a sound level in decibels: "))
if(sound >= Quiet_Room and sound <= Jackhammer):
    if(sound >= Quiet_Room and sound < Alarm_Clock):
        if(sound == Quiet_Room):
            value = "like a quiet room"
        else:
            value = "beetwen a quiet room and an alarm clock"
    elif(sound >= Alarm_Clock and sound < Gas_Lawnmower):
        if(sound == Alarm_Clock):
            value = "like an alarm clock"
        else:
            value = "beetwen an Alarm clock and a gas lawnmower"
    elif(sound >= Gas_Lawnmower and sound < Jackhammer):
        if(sound == Gas_Lawnmower):
            value = "like a gas lawnmower"
        else:
            value = "beetwen a quiet room and an alarm clock"
    else:
        value = "like a Jackhammer"
    print("The sound level is", value) 
elif(sound < Quiet_Room):
    print("Your sound level is inferior of a quiet room")
else:
    print("Your sound level is superior of a Jackammer")
    
        