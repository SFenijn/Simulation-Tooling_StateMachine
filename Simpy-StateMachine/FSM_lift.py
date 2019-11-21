from Statemachine import StateMachine

def beneden_l_transitions(txt,time):
    splitted_txt = txt.split(None, 1)
    word, txt = splitted_txt if len(splitted_txt) > 1 else (txt, "")
    if word in "l":
        newState = "beneden_l"
    elif word in "v":
        newState = "beneden_v"
        time = transport_human(time,newState)
    elif word == "k":
        newState = "boven_l"
        time=transport_lift(time,newState)
    else:
        newState = "error_state"

    return newState, txt, time


def beneden_v_transitions(txt,time):
    splitted_txt = txt.split(None, 1)
    word, txt = splitted_txt if len(splitted_txt) > 1 else (txt, "")
    if word in "l":
        newState = "beneden_l"
        time = transport_human(time,newState)
    elif word in "v":
        newState = "beneden_v"
    elif word == "k":
        newState = "boven_v"
        time = transport_lift(time,newState)
    else:
        newState = "error_state"

    return newState, txt, time


def boven_l_transitions(txt,time):
    splitted_txt = txt.split(None, 1)
    word, txt = splitted_txt if len(splitted_txt) > 1 else (txt, "")
    if word in "l":
        newState = "boven_l"
    elif word in "v":
        newState = "boven_v"
        time = transport_human(time,newState)
    elif word == "k":
        newState = "beneden_l"
        time = transport_lift(time,newState)
    else:
        newState = "error_state"

    return newState, txt, time


def boven_v_transitions(txt,time):
    splitted_txt = txt.split(None, 1)
    word, txt = splitted_txt if len(splitted_txt) > 1 else (txt, "")
    if word in "l":
        newState = "boven_l"
        time = transport_human(time,newState)
    elif word in "v":
        newState = "boven_v"
    elif word == "k":
        newState = "beneden_v"
        time = transport_lift(time,newState)
    else:
        newState = "error_state"

    return newState, txt, time

def transport_lift(time,newState):
    if "boven" in newState:
        print("De lift gaat naar boven",end=". ")
    else:
        print("de lift gaat naar boven",end=". ")
    time+=10
    print("De tijd is nu: ",time)
    return time

def transport_human(time,newState):
    if "_v" in newState:
        print("Er gaat iemand in de lift",end=". ")
    else:
        print("Er gaat iemand uit de lift",end=". ")
    time+=5
    print("De tijd is nu: ",time)
    return time

if __name__== "__main__":
    m = StateMachine()
    m.add_state("beneden_l", beneden_l_transitions)
    m.add_state("beneden_v", beneden_v_transitions)
    m.add_state("boven_l", boven_l_transitions)
    m.add_state("boven_v", boven_v_transitions)
    m.add_state("beneden_l", beneden_l_transitions, end_state=1)
    m.add_state("boven_l", boven_l_transitions, end_state=1)
    m.add_state("error_state", None, end_state=1)
    m.add_state("end_state", None, end_state=1)
    m.set_start("beneden_l")

    m.run("l l l  l v v v k l")
    m.run("v k k l")
    m.run("k v v v  l v")
    m.run("l")
    m.run("v k k k k l v k k k l")