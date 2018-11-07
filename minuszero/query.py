import logging

# g

"""Function allows for the protocol to be stopped and a message to be
asked of the user. Demands the user acts to exit or proceed with the
test.
"""
def proceed_query(custom_message=None):

    print(custom_message)

    while(1):
        answer = str(input())
        if answer not in ["proceed", "PROCEED", "p", "exit", "EXIT", "e"]:
            continue
        elif answer in ["proceed", "PROCEED", "p"]:
            break
        elif answer in ["exit", "EXIT", "e"]:
            exit()

        


proceed_query("AAA")
proceed_query("BBB")
proceed_query("CCC")