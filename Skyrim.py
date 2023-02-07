import os
import random
## Defined Classes/Objects
class player:
    name = ""
    health = random.randint(58,101)
    strength = random.randint(1,10)
    pick = False

    def __init__(self, name) -> None:
        self.name = name
    
    def pickLock(self, difficulty):
        tries = 0
        lock = random.randint(0,difficulty+1)
        while(self.pick == True):
            guess = input("Attempt:{}\nAttempt to pick lock(0-{}): ".format(tries+1, difficulty))
            
            if guess == lock:
                input("Lock pick successful.")
                return True
            elif tries > 3:
                input("Lock pick broke.")
                self.pick=False
                return False
            elif guess > lock:
                print("<-")
            elif guess > lock:
                print("->")
        if self.pick == False:
            print("You do not have a lock pick.")
            return False


class npc:
    name=''
    disposition=0
    godMode = False

    def __init__(self, name, disposition) -> None:
        self.name = name
        self.disposition = disposition


## Functions

def playerinput(prompt, min, max):
    ans = input(prompt)
    if int(ans) not in range(min, max+1):
        print("Please enter one of the available options.")
        playerinput(prompt, min, max)
    else:
        return ans




os.system('cls')
## Opening Section
print("Skyrim")

input("\nNote:Press \"Enter\" to advance story")

os.system('cls')
nord = npc("Bruce", 0)
input("Nord: Hey, you. You’re finally awake. You were trying to cross the border, right? Walked right into that Imperial ambush, same as us.")

choice = playerinput("\nDo you want to: \n1. FUS RO DA .\n2. Stare at the horse\nChoice (1-2): ", 1, 2)

if choice == 1:
    input("*You scream giberish, but unfortunatly you have no knowledge of the dragon languate. Everyone on the cart looks at you stranglely. No one seems interested in continueing the conversation, and you sit in silence for the rest of the ride.*.\n")
else:
    input("Nord: That's alright, this must be hard for you. You had nothing to do with the ambush. Wrong time wrong place.")
    choice = playerinput("1. Damn you, I would be free now if if wasn't for you.\n2. It's not your fault. Everything happens for a reason.\nChoice (1-2): " ,1, 2)
    if int(choice) == 1:
        input("*Nord nods. He understands your frustration, but the converstaion stops.*")
    else:
        input("Nord: Yeah, maybe you're right.")
        nord.disposition = nord.disposition + 5
        input("*You see a castle come into view. The cart slowly rolls into it's walls and comes to a halt.*")

guard = npc("Tom", -1)
name = input("Guard: Prisoner, exit the cart and tell me your name.\n Enter Name:")
player1 = player(name)
if name.lower == "talos":
    player1.godmode = True
input("Ok {}, I've been informed that you were actually arrested by mistake during the clash. That being said, letting you go at this point could make us look bad. It'll be easier for everyone if we just pretend you were with them. Go wait to get your head cut off".format(player1.name))
choice = playerinput("1. You submit to his request.\n2. You argue with him.\n3. You yell there is a prisoner trying to escape behind him. You then try to run for it.(Luck)\nChoice (1-3): " ,1, 3)
if int(choice) == 1:
    input("*You walk over to the block. Guard is slightly perplexed with your lack of self preservation, but is ultimatly indifferent.*")
if int(choice) == 2:
    input("*You try reasoning with the guard. He glares at you and tells a guard to escort you to the block.*")
    guard.disposition = guard.disposition-10
else:
    luck = random.randint(1, 10)
    if luck > 9:
        input("*The guard checks over his sholder and a bug flies in his mouth just as he turns. He starts choking and gagging, and in the commotion you make a run for it. Arrows fly to your left and right, but due to what can only be called a miricle, you manage to make it to the woods and run off into the forest.*")
        input("\nYou escaped. Enjoy your freedom. (Speedrun Ending)")
        quit()
    else:
        input("*Guard continues to stare at you. You attempt to run, but immediatly, you get punched in the jaw and land on your back. You are dragged over to the block.*")
        guard.disposition = guard.disposition-100
        player1.health-random.ranndint(30, 40)

if guard.disposition <= -100:
    if player1.godmode == False:
        input("*You are immediatly called to the block. It seems you scored a fast pass with that little move you pulled, as several other people were ahead of you in line. Your head is quickly removed.*")
        input("\nYou Died.")
        quit()
    else:
        input("*You are immediatly called to the block. It seems you scored a fast pass with that little move you pulled, as several other people were ahead of you in line. You kneel and close your eyes. You can hear the whoosh of the axe coming down, and then a loud metalic clang. You open one eye to see what happened, and everyone around you is gaping in astonishment. Your neck was undamaged, but the axe's blad was badly damaged. You stand up and break your bounds. Suddenly a realization floods into your mind of who you are and you Scream 'OD AH VIING'. A dragon suddenly appears over the peak of a mountain and delievers a horendous blast of fire consuming everyone in the courtyard in fire. The Dragon lands and you climb on board. You pat it's neck and you both take off into the sky.*\n{}: Let's go buddy. I've heard that some elves need a sign of my existance.".format(player1.name))
        input("\nYou go and wreak havoc on the entriety of the elven race. Your return beckons a new golden age for the Nords, and the absoulte distruction of every other race. Not sure this is the good ending, but hey you survived.")
        quit()
else:
    input("*You wait in line, seeing several people being beheaded before you. Suddenly, the ground shakes. The momentary loss of stability causes the exicutioner to slip and sprain his wrist. Due to OSHA regualations, the exicutioner is immediatly required to stop working and go to an in network hospital to get a check up. All further exicutions are rescheduled for the next day.*")

input("*Your group is taken to the dungeons*")


escape=False
if guard.disposition < -10: ## Guards are annoyed with you due to you aruging earlier. You're sent out to clean out one of two possible stables
    input("Guard: You there. We need someone to clean out the stables. Get a shovel and go clean them out.")
    luck = random.randint(1,10)
    if luck > 6: ## You're assigned to the stables close to the gate, which have horses. 
        input("*You are taken to the stables situated next to the gate. You notice that they are slightly agar, and it seems that no one in intent to close them. You are taken into the stables which have several horses, and a lot to clean up.*")
        choice = playerinput("1. You start cleaning.\n2. You pick up the shovel, pick up some horse dung, and quickly throw it at your guards face. (Luck)\n3. You grab the shovel, and begin pretending to clean. Once the guards back is turned, you attempt to hit them on the head with the shovel. (Strength)\nChoice (1-3): " ,1, 3)
        if int(choice) == 1:
            input("*After many grueling hours, you finish cleaning the stall. You shuffle back into the prison, and colapse with exhaustion. You quickly lose pass out*")
            guard.disposition = guard.disposition+20
            player1.health= player1.health-5
            if player1.health<0:
                input("\nYou Died. Too bad you managed to survive long enough to finish cleaning out the stable.")
                quit()
        elif int(choice) == 2:
            luck = random.randint(1,10)
            if luck > 7:
                input("*You manage to hit the guard in the face. Immediatly you jump on the nearest horse, and you are making your way out the open gate you noticed earlier.*")
                input("You were able to escape into the forest. You survived! (The guard who let you escape unfortunatly took your spot on the block the next day)")
                quit()
            elif luck > 3:
                input("You completely miss. The guard looks angry, but only yells at you to get back to work. You complete the rest of the stable, and go back to the prison exhausted")
                player1.health= player1.health-5
                if player1.health<0:
                    input("\nYou Died. Too bad you managed to survive long enough to finish cleaning out the stable.")
                    quit()
                guard.disposition = guard.disposition-20
            else: 
                input("You manage to hit the guard squarely in his chest. He is irate, snatches the shovel fro you, and proceeds to beat you within an inch of your life with it. You are then required to continue cleaning until you are dragged back to the cell.")
                player1.health-45
                if player1.health<0:
                    input("\nYou Died. Too bad you managed to survive long enough to finish cleaning out the stable.")
                    quit()
                guard.disposition = guard.disposition-50
        else:
            luck = random.randint(1,10)
            if player1.strength > 5:
                if luck == 1:
                    input("Your shovel strikes a wooden beam above the guard that you hadn't noticed. The guard jumps and spins around. Seeing what you just attempted, he proceeds to beat you within an inch of your life. You are then required to continue cleaning until you are dragged back to the cell.")
                    player1.health-45
                    if player1.health<0:
                        input("\nYou Died. Too bad you managed to survive long enough to finish cleaning out the stable.")
                        quit()
                    guard.disposition = guard.disposition-50
                else:
                    input("You strike him on the head with the shovel. He immediatly crumbles and is motionless on the ground. You quitely hide his body, and replace your clothing with his own. You then take a horse, and confidently stroll out of the open gate you noticed ealier.")
                    input("You were able to escape into the forest. You survived! (The guard who let you escape unfortunatly took your spot on the block the next day)")
                    quit()
            else :
                input("Your shovel strikes the guard, but with such little force that he is unaffected. The guard jumps and spins around. Seeing what you just attempted, he proceeds to beat you within an inch of your life. You are then required to continue cleaning until you are dragged back to the cell.")
                player1.health-45
                if player1.health<0:
                    input("\nYou Died. Too bad you managed to survive long enough to finish cleaning out the stable.")
                    quit()
                guard.disposition = guard.disposition-50
    else: ## You're assigned to the stables deep inside of the hold. There are no horses here, but they do have mules.
        input("*You are taken to the stables situated next to the the edge of the back wall. As you enter the stables, you notice there are several donkeys and mules, and a lot to clean up.*")
        choice = playerinput("1. You start cleaning.\n2. You pick up the shovel, pick up some horse dung, and quickly throw it at your guards face. (Luck)\n3. You grab the shovel, and begin pretending to clean. Once the guards back is turned, you attempt to hit them on the head with the shovel. (Strength)\nChoice (1-3): " ,1, 3)
        if int(choice) == 1:
            input("*After many grueling hours, you finish cleaning the stall. You shuffle back into the prison, and colapse with exhaustion. You quickly pass out*")
            guard.disposition = guard.disposition+20
            player1.health= player1.health-5
            if player1.health<0:
                input("\nYou Died. Too bad you managed to survive long enough to finish cleaning out the stable.")
                quit()
        elif int(choice) == 2:
            luck = random.randint(1,10)
            if luck > 7:
                input("*You manage to hit the guard in the face. Immediatly you attempt to jump on a mule to escape, but are quickly bucked off and kicked in the face by the mule. Everything goes black*")
                player1.health-random.ranndint(30, 60)
                guard.disposition = guard.disposition-100
                if player1.health<0:
                    input("\nYou Died. If it brings you any solice, the guard would have killed you had the mule not done the job.")
                    quit()
                input("*You wake up back in the prison. You look outside of the bars of your cell and notice a very angry looking guard staring at you. You pretend to continue sleeping.*")
                quit()
            elif luck > 3:
                input("You completely miss. The guard looks angry, but only yells at you to get back to work. You complete the rest of the stable, and go back to the prison exhausted")
                player1.health= player1.health-5
                guard.disposition = guard.disposition-20
                if player1.health<0:
                    input("\nYou Died. Too bad you managed to survive long enough to finish cleaning out the stable.")
                    quit()
            else: 
                input("You manage to hit the guard squarely in his chest. He is irate, snatches the shovel fro you, and proceeds to beat you within an inch of your life with it. You are then required to continue cleaning until you are dragged back to the cell.")
                player1.health-45
                guard.disposition = guard.disposition-50
                if player1.health<0:
                    input("\nYou Died. Too bad you managed to survive long enough to finish cleaning out the stable.")
                    quit()
        else:
            luck = random.randint(1,10)
            if player1.strength > 5:
                if luck == 1:
                    input("Your shovel strikes a wooden beam above the guard that you hadn't noticed. The guard jumps and spins around. Seeing what you just attempted, he proceeds to beat you within an inch of your life. You are then required to continue cleaning until you are dragged back to the cell.")
                    guard.disposition = guard.disposition-50
                    player1.health-45
                    if player1.health<0:
                        input("\nYou Died. Too bad you managed to survive long enough to finish cleaning out the stable.")
                        quit()
                else:
                    input("You strike him on the head with the shovel. He immediatly crumbles and is motionless on the ground. You quitely hide his body, and replace your clothing with his own. You then take a mule, and head for the gate from which you entered. You notice that they are slightly ajar, and you are able to walk out.")
                    input("You were able to escape into the forest. You survived! (The guard who let you escape unfortunatly took your spot on the block the next day)")
                    quit()
            else :
                input("Your shovel strikes the guard, but with such little force that he is unaffected. The guard jumps and spins around. Seeing what you just attempted, he proceeds to beat you within an inch of your life. You are then required to continue cleaning until you are dragged back to the cell.")
                guard.disposition = guard.disposition-50
                player1.health-45
                if player1.health<0:
                    input("\nYou Died. Too bad you managed to survive long enough to finish cleaning out the stable.")
                    quit()
else:
    if nord.disposition > 0:
        input("Nord: Hey, it looks like we both get another day. How would you like to make sure we're still alive tomorrow?")
        choice = playerinput("1. I'm interested. What were you thinking?\n2. Are you crazy, you're going to get us killed talking like that!\n3. Tell me your plan and I'll tell you if I'm interested. (Luck)\nChoice (1-3): " ,1, 3)
        if choice == 3:
            luck = random.randint(1,10)
            if luck > 5:
                input("Nord: Fair enough. I'm thinking with the two of us, we may be able to overpower the guard over there.")
                choice = playerinput("1. I'm interested. What are the specifics?\n2. Are you crazy, you're going to get us killed talking like that!\nChoice (1-2): " ,1, 2)
            else:
                input("Nord: No, I need to know if you in first. I don't want you going over there and turning me in.")
                choice = playerinput("1. I'm interested. What's' the plan?\n2. Well then have fun dieing then, but I'm not interested.\nChoice (1-2): " ,1, 2)
        if choice == 2:
           input("Nord: Your loss. Don't expect any favors from me if I managed to escape.")
           nord.disposition = nord.disposition - 20
        if choice == 1:
            input("Nord: Ok good. So in order for this to work, we'll need a distraction. That'll be your job. Once the guard is distracted, I'll hit him with this stick I managed to grab while everyone was focusing on the exicutioner. Go over and get started and I'll jump in when your ready.")
            input("*You walk over and get the guards attention.*")
            choice = playerinput("1. Ask guard if they are descendant of pigs.\n2. Ask guard if you could go assist other prissoners who were sent to clean out stables.\nChoice (1-2): " ,1, 2)
            if int(choice) == 1:
                luck = random.randint(1,10)
                if luck > 5:
                    input("*Guard scowls and walks over to the cell. You back up forcing the guard to unlock the door and enter the cell. He starts beating you, but doesn't notice your friend creap up from behind. Within a moment the stick connects with his skull, and he's out cold. You are hurting, but still alive*")
                    escape=True
                    player1.health = player1.health - 20
                    guard.disposition = guard.disposition-100
                    nord.disposition = nord.disposition + 10
                    if player1.health<0:
                        input("\nYou attempt to get up, but wince in pain. You leg was broken during the beating. Your friend looks at you for a moment, and then appologizes and dashes out of the open cell door. Guards enter shortly after and kill everyone left in the cell. You died.")
                        quit()
                    input("Nord: That was pretty bold... Well I guess pretty stupid. Either way it worked. Let's get out of here.")
                    
                else:
                    input("*Guard grunts and throws a rock at you.*")
                    player1.health = player1.health - 5
                    guard.disposition = guard.disposition - 20
                    nord.disposition = nord.disposition - 10
                    if player1.health<0:
                        input("\nYou Died. Kinda a stupid way to go out don't you think?")
                        quit()
                    input("Nord: That's all you got? Maybe I should have asked someone else.")
                    
            elif int(choice) == 2:
                luck = random.randint(1,10)
                if luck > 7:
                    input("*Guard grins, and accepts. He walks over and enters the cell. He begins to walk over to you to escort you to the stables, but doesn't notice your friend creap up from behind. Within a moment the stick connects with his skull, and he's out cold.*")
                    input("Nord: Good idea! Let's get out of here.")
                    escape=True
                    guard.disposition = guard.disposition-100
                    nord.disposition = nord.disposition + 10
                else:
                    input("*Guard grunts and throws a rock at you.*")
                    player1.health = player1.health - 5
                    guard.disposition = guard.disposition - 20
                    nord.disposition = nord.disposition - 10
                    if player1.health<0:
                        input("\nYou Died. Kinda a stupid way to go out don't you think?")
                        quit()
                    input("Nord: That's all you got? Maybe I should have asked someone else.")
    else:
        input("You slowly pass out. Nothing for you to do until tomorrow.")
                    
if escape == False: ## You wake up in your cell. It's exicution day.
    input("*You wake up. Today is suposed to be your exicution day. A set of guards enters the room and unlocks the cell door.*")
    input("Guard: Ok lets go, back to the block with all of you.")
    input("*Suddenly, the ground shakes again. Just like last time, but this time you hear a mighty roar. The guards are shocked and turn towards the door.*")
    choice = playerinput("1. Do Nothing\n2. Charge the guards (Strength)\n" ,1, 2)
    if int(choice) == 1:
        input("The guards whisper together and yell for everyone to stay where they are. They proceed to re-lock the cage and rush back outside to see what had happened. You notice in the ground there is now a small object that the guards must have dropped. You take a closer look, and you find a pin.")
        player1.pick = True
        choice = playerinput("1. Attempt to pick cell lock\n2. Place in pocket\nChoice(1-2): " ,1, 2)
        if int(choice) == 1:
            success = player1.pickLock(20)
            if success == True:
                nord.disposition = nord.disposition + 50
                input("*The cell lock clicks open and the door swings open. The room is empty outside of you and your fellow cell mates. The nord you spoke to on the cart steps forward.*")
                choice = 3
            else:
                choice = 2
        elif choice ==2 :
            input("*No Luck. You and your cell mates sit in the cell. The shaking continues, and you start to smell smoke, and it begins to fill the room.*")
            input("Nord: I found a grate! Quick someone help me lift it up!")
            input("*You and the nord you spoke to on the cart attempt to pry the grate up. It's at this point that you notice a small key hold in the grate.*")
            input("Nord: Damn, looks like it's locked shut. Does anyone have anything to pick the lock?")
            success = player1.pickLock(5)
            if success == True:
                input("*You hear the lock click into place. You and your friend are now able to lift the grate. Your group crawls in one by one, and crawl through the wet vent. Eventually it empties into a tunnel. Your group continues on and stubles through the dark tunnel. Eventually, you turn around a bend, and see sunlight. You group rushes towards the exit and are in the forest. The shouting and crashing is still audible, but you can't see what's happening from where your group came out of. Frankly, you don't want to be involved, and make a run for it.*")
                input("You Escaped! You don't know what happened, but you're glad to have your life.")
                quit()
            else:
                input("*The room falls to silence. One by one everyone in the room accepts the inevitable. The smoke continues to grow thicker, and the air begins heating up. What ever happened outside seems to have caught the building on fire. You begin to cough and it your eyelids start getting heavy. Your lungs burn and can feel the life draining from you.*")
                input("You died, better luck next time.")
                quit()
        
    elif int(choice) == 2:
        if player1.strength > 6:
            input("*You lurch at the guard closest to you in the cell, shoving him face first into the cell bars. His skull connects with the metal, and he crumbles to the floor. The other guard turns back around but is struck by another inmate with a stick and crubles as well. The door is ajar, and no other guards are visable.*")
            input("*You exit the cell, and notice a lock pick sitting on the guard table. you grab it and put it in your pocket.*")
            nord.disposition = nord.disposition + 50
            guard.disposition = guard.disposition - 100
            choice = 3

        else: 
            input("You lurch at the guard closest to you, but your small build ment there was not enough to knock him over. He turns around, and thrusts his sword through your chest. As you tumble to the ground the other prisoners try fighting back as well and are cut down by the guards. As you vision fades to black, you can see the guards rushing out of the room with their blood stained swords.")
            input("You died. At least you died fighting. Even if it was a pretty lame attempt.")
            quit()
    elif int(choice) == 3:
        input("Nord: This is our chance. We need to get out of here now.")
        input("*You agree, and all the prisoners empty out of the cell. As you move through the halls, the building shakes again. You can hear shouting outside, but it's impossible to make anything out. One of the prisoners which had been assigned a job of cleaning the barracks speaks up, and say they've heard that there is a tunnel that leads outside the walls, but you need a key to get through.*")
        choice = playerinput("1. Go out the dungeon door to enter the couryard\n2. Try to unlock the door to go through the tunnel (Pick)\nChoice(1-2): " ,1, 2)
        if int(choice) == 2:
            input("*You agree to try the Tunnel, and the prisoner guides the group to the door he mentioned.*")
            success = player1.pickLock(30)
            if success == True:
                input("*You hear the lock click into place, and you are able to push the door open. Your group enters the tunnel, and stuble through the dark space. Eventually, you turn around a bend, and see sunlight. You group rushes towards the exit and are in the forest. The shouting and crashing is still audible, but you can't see what's happening from where your group came out of. Frankly, you don't want to be involved, and make a run for it.*")
                input("You Escaped! You don't know what happened, but you're glad to have your life.")
                quit()
            else:
                input("*You try your best, but are unable to pick the lock to the door. Unfortunatly at this point you have no choice but to try and exit through the courtyard.*")
                choice = 1
        if int(choice) == 1:
            input("*Your group makes their way to the main entrance. You can tell that just outside the door is a large commotion, but you have no choice.*")
else:
    input("*Your group pours out of the dungeon. the light is blinding, but as soon as your eyes adjust, your greated with a terifiying sight. An enourmous creature is flying overhead, quickly approuching the castle. Fire pours out of it's mouth and engulfs a group of archers stationed on the wall.*")
    input("Nord: By the nine, it's a dragon!")
    input("*Your group is in shock, but you don't have time to wait around.*")
    choice = playerinput("1. Yell for your group to snap out of it and follow you\n2. Back away, and duck behind some rubble. You see a path leading towards the gate.\nChoice (1-2): " ,1, 2)
    if int(choice) == 1:
        luck = random.randint(1,10)
        if luck > 5:
            input("*The group agrees, and starts following you. Somehow, you manage to avoid the dragons fire, and any guards which spot you decide to igonre you in favor of addressing the dragon. Finally, you rush through the gate and continue running until you can no longer hear the carnage.*")
            input("You survived! You'll never be able to forget what you witnessed, but maybe one day you'll be able to fully understand what you witnessed.")
            quit()
        else:
            input("*The group agrees, and starts following you. Any guards which spot you decide to igonre you in favor of addressing the dragon. You see the gate come into view.*")
            input("*The group runs faster*")
            input("*You are so close*")
            input("*Your breath is short, but you can make it*")
            input("*A shadow covers your group*")
            input("*You glace behind you, just in time to see it*")
            input("*The dragon flying just behind your group, mouth ajard. Fire pours out and and you scream.*")
            input("You died. Nothing you could have done about that unfortunatly. How could have expected it would have been a dragon after all.")   
            quit() 
    else:
        if guard.disposition > 0:
            input("*You rush through the courtyard keeping just out of sight. Suddnely, a guard steps directly into you. Confused for a moment, he recognizes you. For a moment he looks conflicted on what to do, but proceeds to nod to you and contines on his way. You are taken aback yet again, but have not time to dwell on his kindness. You continue on your way, and make it to the gate. The guards have already left to try and defend against the dragon. You turn around one last time, just in time to see the group of prisoners being consumed by fire int the courtyard. You feel guity for abandoing them, but you turn back towards freedom, and run for your life.*")
            input("You survived! Best of luck being haunted by the people you abondoned to be free.")     
            quit()   
        else:
            input("*You rush through the courtyard keeping just out of sight. Suddnely, a guard steps directly into you. Confused for a moment, he recognizes you. Sword already in hand, he runs you through, and kicks you back off his sword. you're dead before you hit the ground.*")
            input("You died. Guess it may have been a good idea to stick with the others.")     
            quit()   





## input("")
## print("")
## choice = playerinput("" ,1, 2)