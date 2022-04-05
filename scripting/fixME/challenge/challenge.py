#!/usr/bin/python3

import time
import os

NB_TRIES = 10
FLAG = "shellmates{d0N'7_y0u_7H1NK_7H47_pwn700lS_4R3_C0o0L??}"

passwords = list(set(['SayHelloToMyLittleFriend'
    ,'HastaLaVistaBaby'
    ,'IllBeBack'
    ,'ThereIsNoSpoon'
    ,'FranklyMyDear'
    ,'HappyBirthdayMrPresident'
    ,'WellAlwaysHaveParis'
    ,'GoAheadMakeMyDay'
    ,'NotInKansasAnymore'
    ,'TheForceIsStrongInThisOne'
    ,'ElementaryMyDearWatson'
    ,'MyPreciousssPasssword'
    ,'HoustonWeHaveAProblem'
    ,'LifeIsLikeABoxOfChocolates'
    ,'YouCantHandleThePassword'
    ,'NobodyPutsBabyInACorner'
    ,'YouHadMeAtPassword'
    ,'InternetTheFinalFrontier'
    ,'PasswordKarmaChameleon'
    ,'ChewieWereHome'
    ,'ImNoMan'
    ,'ThereCanOnlyBeOneImmortal'
    ,'HulkLikeRagingFireThorLikeSmolderingFire '
    ,'DontWorryBeHappy'
    ,'ForTheHorde'
    ,'IAmMrRobot'
    ,'WinterIsComing'
    ,'SpaceTrooper'
    ,'BeamMeUpScotty'
    ,'ISolemnlySwearImUpToNoGood']))

def welcome():
	print('''I found some passwords online but they are scrambaled!!!\nCan help me to fix them so I can build my own wordlist and learn ethical hacking!!!''')

def scramble(s):
    return list(set(enumerate(s)))

def challenge():
    welcome()
    for i in range(NB_TRIES):
        scrambaled = scramble(passwords[i])
        if i > 0:
            print('Correct Answer, you can continue')
            print('_________________________________')
        print(scrambaled)
        start_time = time.time()
        answer = input('write here your answer:')
        if answer != passwords[i]:
            print('Oh oh! your answer is wrong')
            exit()
        if time.time()-start_time > 4:
            print('You should hurry up, I need my password list ASAP')
            exit()
    print(FLAG)
    exit()

if __name__ == '__main__':
	challenge()
