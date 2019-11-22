# gebaseerd op code van Python Advanced Course Topics: https://www.python-course.eu/finite_state_machine.php
from StateMachine.Statemachine import StateMachine
import random

def beneden_l_transitions(txt):
    splitted_txt = txt.split(None, 1)
    word, txt = splitted_txt if len(splitted_txt) > 1 else (txt, "")
    if word in "l":
        newState = "beneden_l"
    elif word in "v":
        newState = "beneden_v"
    elif word == "k":
        newState = "boven_l"
    else:
        newState = "error_state"

    return newState, txt


def beneden_v_transitions(txt):
    splitted_txt = txt.split(None, 1)
    word, txt = splitted_txt if len(splitted_txt) > 1 else (txt, "")
    if word in "l":
        newState = "beneden_l"
    elif word in "v":
        newState = "beneden_v"
    elif word == "k":
        newState = "boven_v"
    else:
        newState = "error_state"

    return newState, txt


def boven_l_transitions(txt):
    splitted_txt = txt.split(None, 1)
    word, txt = splitted_txt if len(splitted_txt) > 1 else (txt, "")
    if word in "l":
        newState = "boven_l"
    elif word in "v":
        newState = "boven_v"
    elif word == "k":
        newState = "beneden_l"
    else:
        newState = "error_state"

    return newState, txt


def boven_v_transitions(txt):
    splitted_txt = txt.split(None, 1)
    word, txt = splitted_txt if len(splitted_txt) > 1 else (txt, "")
    if word in "l":
        newState = "boven_l"
    elif word in "v":
        newState = "boven_v"
    elif word == "k":
        newState = "beneden_v"
    else:
        newState = "error_state"

    return newState, txt


def randomPicker(lst):
    # returns random item from list
    return random.choice(lst)


def createWachtrij(taal, num):
    i = 0
    wachtrij = []
    while num >= i:
        wachtrij.append(randomPicker(taal))
        i += 1
    print("wachtrij setup klaar...")
    return wachtrij


def simulation(num0, num1):
    """"Simulatie van invalide lift: input = aantal mensen per verdieping"""
    m = StateMachine()
    m.add_state("beneden_l", beneden_l_transitions)
    m.add_state("beneden_v", beneden_v_transitions)
    m.add_state("boven_l", boven_l_transitions)
    m.add_state("boven_v", boven_v_transitions)
    m.add_state("beneden_l", beneden_l_transitions, end_state=1)
    m.add_state("boven_l", boven_l_transitions, end_state=1)
    m.add_state("error_state", None, end_state=1)
    newstate = "beneden_l"
    m.set_start(newstate)

    # v staat voor er gaat iemand in de lift
    # l staat voor, er gaat iemand uit de lift
    # k staat voor, de lift gaat naar boven of beneden
    # als er meer dan twee verdiepingen zijn kan de k woden vervangen voor specefieke verdiepingen

    taal_0 = ["v k l"] # de taal kan ook meerdere commands bevatten. (zolang ze niet op "v" eindigen)
    taal_1 = ["v k l"]
    wachtrij_0 = createWachtrij(taal_0, num0)
    wachtrij_1 = createWachtrij(taal_1, num1)

    while len(wachtrij_0) > 0 or len(wachtrij_1) > 0:
        print("wachtrij verdieping 0: ", len(wachtrij_0))
        print("wachtrij verdieping 1: ", len(wachtrij_1))
        if newstate == "beneden_l":
            if len(wachtrij_0) <= 0:
                newstate = m.run("k")
                m.set_start(newstate)
            else:
                string = wachtrij_0[0]
                del wachtrij_0[0]
                newstate = m.run(string)
                m.set_start(newstate)
        else:
            if len(wachtrij_1) <= 0:
                newstate = m.run("k")
                m.set_start(newstate)
            else:
                string = wachtrij_1[0]
                del wachtrij_1[0]
                newstate = m.run(string)
                m.set_start(newstate)
    print("Simulatie is klaar!")



if __name__== "__main__":
    rij_v0 = 20
    rij_v1 = 15
    simulation(rij_v0, rij_v1)
