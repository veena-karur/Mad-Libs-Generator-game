from tkinter import *

cap = Tk()
cap.geometry('500x500')
cap.title('DataFlair-*****MAD LIBS Generator*****')
Label(cap, text= '^^^MAD LIBS Generator ^^^\n Have FUN!!!!' , font = 'arial 20 bold').pack()
Label(cap, text = '****CHOSE YOUR INTEREST**** ' , font = 'arial 15 bold').place(x=150, y=80)

def story1():
    relation= input("CHOSE SISTER OR BROTHER :")
    friend = input("ENTER THE NAME OF  YOUR FRIEND :")
    emotion = input("ENTER THE TYPE OF EMOTION : ")
    expression= input("ENTER THE TYPE OF EXPRESSION :")
    thing= input("ENTER THE NAME OF THING :")
    place = input("CHOSE TERRACE OR BALCONY :")
    verb = input("ENTER THE VERB WITH ING FORM :")
    
    print("As I reached home, I realised that I had forgotten the "+thing+". There was still an hour for my "+relation+" to turn up ."
          "So I decided  to go to "+place+" to enjoy the cool breeze . Just as I reached the "+place+", I received a call on my mobile phone from "+friend +
          ". I started walking on the "+place+" while discussing the day's happenings with him/her. After some time , it started getting dark but that didn't deter "
          "as I don't get scared easily . I continued talking on the phone and was "+expression+" at my friend's joke when I heard some footsteps behind me. I immediately "
          "turned around to see who it was. On finding nobody on the "+place+", I discarded the whole thing as a figment of my imagination and resumed talking on phone"
          "I heard footsteps behind me again and I could feel my hair standing on end . With a lot "+emotion+", turned around and just then the "+place+
          " door closed with a loud sound . The phone fell from my "+verb+" hand and I screamed at the top of my voice. Just then I heard my "+relation+"'s loud laughter."
          "I had lost track of time while talking on the phone and my "+relation+" had taken advantage of the situation to play a practical joke on me .")


def story2():
   
    adjective1 = input("ENTER ADJECTIVE NAME : ")
    person = input("ENTER A RELATION NAME  : ")
    thing =input("ENTER A OBJECT NAME TO SIT ON  :")
    room = input("ENTER A ROOM NAME   : ")
    expression= input("ENTER THE TYPE OF EXPRESSION  : ")
    adjective2=input("ENTER THE TYPE OF FEELING :")
    noun= input("ENTER NOUN  :")
    verb = input("ENTER VERB NAME :")
    important=input("ENTER IMPORTANT THING  :")
    emotion=input("ENTER AN EMOTION NAME  :")
    print("I was "+adjective1+" and scared . I heard someone call out my name . I ran out of my "+room+" and saw my "+person+
          " sitting on "+thing+" doing his/her office work . I asked if he/she needed something . He/She did not reply. I came to know that he/she is "
          +expression+" at me . I could feel myself "+adjective2+" . I was afraid of being scolded ."
          "suddendly the doorbell rang and I went to open the door . It was my mother . I thanked God upon seeing her as I knew she was my "+noun+" . "+person+
          " didn't speak to me till dinner . It was at the dinner table when I gathered my courage to "+verb+" to him/her, because I wasn't feeling good to see him/her upset. "
          " As soon as I was about to say something, she/he said to be careful from now on . I heaved a sigh of relief and apologised for misplacing his "+important+
          " due to my carelessness.")
          

def story3():
    person = input("ENTER THE PERSON'S NAME :")
    vehicle = input("ENTER THE VEHICLE NAME  :")
    adverb = input("ENTER AN ADVERB  :")
    adjective = input("ENTER AN ADJECTIVE  :")
    bird = input("ENTER BIRD NAME :")
    sound = input("ENTER THE SOUND NAME :")
    place = input("ENTER A PLACE NAME IN JUNGLE  :")
    number = input("ENTER NUMBER IN WORDS :")
    noun = input("ENTER NOUN  :")
    emotion = input("ENTER EMOTION NAME :")
   
    print("It was dark and lonely night . I was returning from "+person+"'s place and missed the last "+vehicle+" going towards my home . Now , I had to walk through "
          "the jungle . I was "+adjective+" , but the thought of reaching home on time persuaded me ."
          "There was something odd about the jungle in night .  It was very "+adverb+" and the silence made me shiver . Horrifically , I realised that I was lost . I was "+emotion+
          " with panic. I cried for help but there was no respose . I was terified to hear the sounds of owls and "+bird+". It was scary and I had lost all hopes of survival ."
          " suddenly , I heard the sound of "+sound+". I suspected whether I was alone . I followed the sound of these "+sound+". It was like light at the end of a "+place+
          ". After "+number+" minutes, I reached near a lonely house . I hid behind the trees to see whether it would be safe to go near the house. "
          "Finally, I decided to take shelter in the lonely house , but to my "+noun+" it was full of dancing SKELETONS . I fainted with fear. When I opened my eyes my dog Jack"
          " came to rescue me .")


Button(cap, text= "^^PRIDE COMES AFTER PREJUDICE^^", font ='algerian 16', command= story1, bg = 'orange').place(x=100, y=150)
Button(cap, text= "AWAKENING!!!", font ='algerian 16', command = story2 , bg = 'yellow').place(x=190, y=220)
Button(cap, text= "***THE HAUNTED JUNGLE*** ", font ='algerian 16', command = story3, bg = 'red').place(x=70, y=290)
cap.mainloop()



