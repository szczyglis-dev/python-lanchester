# (c) 2022 Marcin "szczyglis" Szczygliński
# GitHub page: https://github.com/szczyglis-dev/python-lanchester
# Email: szczyglis@protonmail.com
# Version: 1.0.0
# This package is licensed under the MIT License.
# License text available at https://opensource.org/licenses/MIT

import numpy as np

__version__ = "1.0.0"


def calc_square(R, B, r_s, b_s, t):
    R.append(R[t] - b_s * B[t])
    B.append(B[t] - r_s * R[t])
    return R, B


def calc_linear(R, B, r_l, b_l, t):
    R.append(R[t] - b_l * B[t] * R[t])
    B.append(B[t] - r_l * B[t] * R[t])
    return R, B


def calc_modernized(R, B, r_s, b_s, r_l, b_l, r_f, s_r, b_f, s_b, r_i, b_i, t):
    rValue = (
        R[t]
        - (1 - r_f) * s_b * r_s * B[t] * b_i
        - (1 - (1 - r_f) * s_b) * r_l * B[t] * R[t] * b_i
    )
    bValue = (
        B[t]
        - (1 - b_f) * s_r * b_s * R[t] * r_i
        - (1 - (1 - b_f) * s_r) * b_l * B[t] * R[t] * r_i
    )
    R.append(rValue)
    B.append(bValue)
    return R, B


# square law
def square(R0, B0, r_s, b_s, T, dt):
    R = [R0,]
    B = [B0,]
    for t in np.arange(0, T, dt):
        calc_square(R, B, r_s, b_s, t)
        if R[-1] < 1e-6 or B[-1] < 1e-6:
            break
    return R, B


# linear law
def linear(R0, B0, r_l, b_l, T, dt):
    R = [R0,]
    B = [B0,]
    for t in np.arange(0, T, dt):
        calc_linear(R, B, r_l, b_l, t)
        if R[-1] < 1e-6 or B[-1] < 1e-6:
            break
    return R, B


# modernized model
def modernized(R0, B0, r_l, b_l, r_s, b_s, r_f, s_r, b_f, s_b, r_i, b_i, T, dt):
    R = [R0,]
    B = [B0,]
    for t in np.arange(0, T, dt):
        calc_modernized(R, B, r_s, b_s, r_l, b_l, r_f, s_r, b_f, s_b, r_i, b_i, t)
        if R[-1] < 1e-6 or B[-1] < 1e-6:
            break
    return R, B
