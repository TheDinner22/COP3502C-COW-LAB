# joe goodman
# 03/07/23
# cowsay, a driver file with a main method

import sys
from heifer_generator import HeiferGenerator

def error(msg):
    raise Exception(msg)

def main():
    # create the cow objects
    cows = HeiferGenerator.get_cows()
    file_cows = HeiferGenerator.get_file_cows()

    # make sure argc > 1
    if not len(sys.argv) > 1:
        error("no args!")

    first_argv = sys.argv[1]

    # check for -l
    if first_argv == "-l":
        # this is fancy
        cow_names = " ".join(map(lambda cow: cow.name, cows))
        print(f"Cows available: {cow_names}")

    # check for -n or -f
    elif first_argv == "-n" or first_argv == "-f":
        # make sure argc > 3
        # (otherwise the next three lines would index error)
        if not len(sys.argv) > 3:
            error("no args!")

        maybe_a_cow_name = sys.argv[2]
        msg = " ".join(sys.argv[3:])

        # determine if it is cows or file cows that we are working with
        list_of_cows_or_file_cows = cows if first_argv == "-n" else file_cows

        # loop through every cow
        for cow in list_of_cows_or_file_cows:
            # if the names match, print the message and break
            if cow.name == maybe_a_cow_name:
                cow.print(msg)
                break
        else: # I love this feature so much
              # if the loop does not break, this else block
              # runs
            print(f"Could not find {maybe_a_cow_name} cow!")

    # print sys.argv[0] as the msg
    else:
        # this just takes argv, ignores the filename, and combines the rest
        # into a string (each element is seperated with a space
                      # ------------------ #
        cows[0].print(" ".join(sys.argv[1:]))

if __name__ == "__main__":
    main()
