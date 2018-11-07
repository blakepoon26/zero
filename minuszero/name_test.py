def name_test():

    print("enter the experiment name")
    global name
    name = str(input())
    while(1):
        print("{}? type y to confirm or n to reenter".format(name))
        answer = str(input())
        if answer not in ["y", "n"]:
            print("Invalid answer")
            continue
        elif answer is "y":
            break
        elif answer is "n":
            return name_test()
    print("done")

name_test()

filename_body = datetime.now().strftime("{}-{}--%Y-%m-%d--"
                                        "%H-%M-%S-%p".format(
                                            primary_user, protocol_name))

print(filename)