from hardware import(
    ReoLab_SerialCommands as rsc)

import time

from datetime import datetime

import users

def main():

    # demand that a valid authorized user enter their initials
    while(1):
        primary_user = str(input("Input your initials: "))
        if primary_user in users.USERS["Initials"].values:
            break
        else:
            print("Invalid user initials. "
                  "Please select intials from \n{}.".format(users.USERS))
            continue

    # initialize the system prior to the assay
    print('Initialization Devices')
    print('IMI 8 Channel Syringe Pump Initialization')
    rsc.initialize_pump()
    time.sleep(0.1)
    print('Magnet Mover USB-1024LS Check')
    rsc.engage_both()
    time.sleep(0.1)
    rsc.release_both()
    time.sleep(0.1)
    print('Initialization Completed')

    # enter the name of the experiment
    name_test()
    filename_body = datetime.now().strftime("{}_{}_%Y-%m-%d--"
                                            "%H-%M".format(
                                                testname, primary_user))

    # block the reactor by swishing buffer in and out 5 times from inlet
    proceed_query("Load XXX volume of blocking buffer.")
    for i in range(5):
        rsc.fast_fill()
        time.sleep(0.1)
        # collect data for the baseline
        if i == 4:
            rsc.image_capture(fname = filename_body + "_baseline")
            time.sleep(0.1)
        # clear with air
        rsc.shift_to_syringe()
        time.sleep(0.1)
        i += 1

    # load beads
    proceed_query("Load XXX volume of bead solution.")
    rsc.shift_to_trapping()
    time.sleep(0.1)
    rsc.engage_both()
    time.sleep(0.1)
    rsc.shift_to_syringe()
    time.sleep(0.1)

    # wash with 5 reactor volume
    proceed_query("Load XXX volume of wash buffer.")
    for i in range(5):
        rsc.fill()
        time.sleep(0.1)
        # incubate for t sec
        rsc.incubate(t = 60)
        time.sleep(0.1)
        rsc.shift_to_syringe()
        time.sleep(0.1)
        i += 1

    # expose to detection ligand
    proceed_query("Load XXX volume of analyte.")
    rsc.shift_to_trapping()
    time.sleep(0.1)
    rsc.incubate(t = 60)
    time.sleep(0.1)
    rsc.shift_to_syringe()
    time.sleep(0.1)

    # wash with 5 reactor volume
    proceed_query("Load XXX volume of wash buffer.")
    for i in range(5):
        rsc.fill()
        time.sleep(0.1)
        # incubate for t sec
        rsc.incubate(t = 60)
        time.sleep(0.1)
        rsc.shift_to_syringe()
        time.sleep(0.1)
        i += 1

    #indicate
    proceed_query("Load XXX volume of TMB.")
    rsc.shift_to_trapping()
    time.sleep(0.1)
    rsc.incubate(t = 60)
    time.sleep(0.1)
    rsc.shift_to_detection()
    time.sleep(0.1)
    rsc.image_capture(fname = filename_body + "_indication")
    rsc.shift_to_syringe()

    # wash out the beads and clean the channel
    proceed_query("Release the beads in the traps")
    rsc.release_both()
    # clean with phosphate acid solution
    proceed_query("Load XXX volume of acid")
    for i in range(4):
        rsc.fast_fill()
        time.sleep(0.1)
        rsc.shift_to_syringe()
        time.sleep(0.1)
        i += 1
    # clean with 5% Contrad
    proceed_query("Load XXX volume of 5% Contrad")
    for i in range(4):
        rsc.fast_fill()
        time.sleep(0.1)
        rsc.shift_to_syringe()
        time.sleep(0.1)
        i += 1
    # clean with deionized water
    proceed_query("Load XXX volume of deionized water")
    for i in range(4):
        rsc.fast_fill()
        time.sleep(0.1)
        rsc.shift_to_syringe()
        time.sleep(0.1)
        i += 1

    # empty the syringe
    proceed_query("Dump the waste")
    rsc.empty_syringe()
    time.sleep(0.1)
    print('Syringe Empty')
    Print('-Test Complete-')

def name_test():
    """Function allows for the user to name each test and apply the name on
    the indication image.
    """
    print("Enter the name of the test:")
    global testname
    testname = str(input())
    while(1):
        print("{}? type \"y\" to confirm or \"n\" to retype".format(testname))
        answer = str(input())
        if answer not in ["y", "n"]:
            print("Invalid answer")
            continue
        elif answer is "y":
            break
        elif answer is "n":
            return name_test()

def proceed_query(custom_message = None):
    """Function allows for the protocol to be stopped and a message to be
    asked of the user. Demands the user acts to exit or proceed with the
    test.
    """
    while(1):
        print(custom_message)
        print("Type \"proceed\" to continue, or \"exit\" to abort test.")
        answer = str(input())
        if answer not in ["proceed", "PROCEED", "p", "exit", "EXIT", "e"]:
            print("Invalid answer.")
            continue
        elif answer in ["proceed", "PROCEED", "p"]:
            print("User elected to proceed.")
            break
        elif answer in ["exit", "EXIT", "e"]:
            print("User elected to abort the test.")
            exit()

if __name__ == "__main__":
    
    main()












