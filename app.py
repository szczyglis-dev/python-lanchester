# (c) 2022 Marcin "szczyglis" Szczygliński
# GitHub page: https://github.com/szczyglis-dev/python-lanchester
# Email: szczyglis@protonmail.com
# Version: 1.0.0
# This package is licensed under the MIT License.
# License text available at https://opensource.org/licenses/MIT

import numpy as np
import matplotlib.pyplot as plt
import lanchester

model = "square"

# base parameters:
R0 = 8000  # number of RED units
B0 = 10000  # number of BLUE units
T = 100  # total number of steps in the simulation
dt = 1  # time interval

# parameters for "linear" and "modernized" models:
r_l = 0.00001  # combat efficiency of RED units
b_l = 0.00002  # combat efficiency of BLUE units

# parameters for "square" and "modernized"  models:
r_s = 0.2  # average number of RED units that damage each other per unit of time
b_s = 0.1  # average number of BLUE units that damage each other per unit of time

# parameters for "modernized" model only:
r_f = 0.6  # RED units camouflage ability factor
b_f = 0.2  # BLUE units camouflage ability factor

r_a = 0.6  # RED units ability to recognize
b_a = 0.2  # BLUE units ability to recognize

r_i = 4  # RED units information warfare ability coefficient
b_i = 4  # BLUE units information warfare ability coefficient

# model select
def select_model():
    global model
    n = int(
        input(
            "Select model (type number 1-3 and press Enter):\n\n"
            "1 - square law\n2 - linear law\n3 - modernized model\n"
        )
        or 0
    )
    if n == 1:
        model = "square"
    elif n == 2:
        model = "linear"
    elif n == 3:
        model = "modernized"
    else:
        print("\nInvalid value. Please try again:\n")
        select_model()


# get integer input
def get_int(msg, current):
    n = int(input("\nEnter {}: [current: {}]\n".format(msg, current)) or current)
    print("Current value: {}\n".format(n))
    return n


# get float input
def get_float(msg, current):
    n = float(input("\nEnter {}: [current: {}]\n".format(msg, current)) or current)
    print("Current value: {}\n".format(n))
    return n


# get input params
def get_params():
    global R0, B0, T, dt, r_l, b_l, r_f, r_s, b_s, b_f, r_a, b_a, r_i, b_i

    # base parameters:
    R0 = get_int("number of RED units", R0)
    B0 = get_int("number of BLUE units", B0)
    T = get_int("total number of steps in the simulation", T)
    dt = get_int("time interval", dt)

    # parameters for "linear" and "modernized" models:
    if model == "linear" or model == "modernized":
        r_l = get_float("combat efficiency of RED units", r_l)
        b_l = get_float("combat efficiency of BLUE units", b_l)

    # parameters for "square" and "modernized"  models:
    if model == "square" or model == "modernized":
        r_s = get_float(
            "average number of RED units that damage each other per unit of time", r_s
        )
        b_s = get_float(
            "average number of BLUE units that damage each other per unit of time", b_s
        )

    # parameters for "modernized" model only:
    if model == "modernized":
        r_f = get_float("RED units camouflage ability factor", r_f)
        b_f = get_float("BLUE units camouflage ability factor", b_f)

        r_a = get_float("RED units ability to recognize", r_a)
        b_a = get_float("BLUE units ability to recognize", b_a)

        r_i = get_float("RED units information warfare ability coefficient", r_i)
        b_i = get_float("BLUE units information warfare ability coefficient", b_i)

    # try again or continue
    c = input(
        "[OK] All parameters are collected.\nDo you want to predict battle result now?\n\n"
        "Type any key to continue and predict or 'N' to come back and correct input parameters\n"
    )
    if c == "N" or c == "n" or c == "no":
        get_input()


# initialize
def get_input():
    select_model()
    get_params()


# main app
def main():
    print("Lanchester's laws simulation, v.{}".format(lanchester.__version__))
    print("GitHub page: https://github.com/szczyglis-dev/python-lanchester\n")

    get_input()

    if model == "square":
        R, B = lanchester.square(R0, B0, r_s, b_s, T, dt)
    elif model == "linear":
        R, B = lanchester.linear(R0, B0, r_l, b_l, T, dt)
    elif model == "modernized":
        R, B = lanchester.modernized(
            R0, B0, r_l, b_l, r_s, b_s, r_f, r_a, b_f, b_a, r_i, b_i, T, dt
        )

    # display result
    print("Predicted result of the battle：\n")
    if R[-1] > B[-1]:
        print("Winner: RED")
    else:
        print("Winner: BLUE")

    # display remaining units info
    print("Remaining RED units [", R[-1], "]")
    print("Remaining BLUE units [", B[-1], "]")

    # display result on plot
    t = np.arange(0, len(R) * dt, dt)
    plt.figure(1)
    plt.plot(t, R, "--r", label="RED units")
    plt.plot(t, B, "b", label="BLUE units")
    plt.xlabel("Time (round)")
    plt.ylabel("Number of units")
    plt.title("Lanchester model simulation")
    plt.legend()
    plt.show()

    c = input(
        "\n\n[FINISHED] Do you want to try again?\n\nType 'Y' to try again or any other key to exit\n"
    )
    if c == "Y" or c == "y" or c == "yes":
        get_input()


if __name__ == "__main__":
    main()
