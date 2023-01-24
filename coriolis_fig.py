import numpy as np
import sys
import matplotlib.pyplot as plt

default_omega = 7.29e-05                # radians / sec

latitude = np.arange(-90, 90, 0.5)      # an array of latitude values, pole to pole

def value_of_f(latitude=latitude, omega=default_omega):

    f_ = 2 * omega * np.sin(np.deg2rad(latitude))

    fig, ax = plt.subplots()

    ax.plot(f_, latitude, label='24 hour rotation period')

    ax.hlines(0, f_[0], f_[len(f_)-1], linestyles='--', alpha=0.6)
    ax.vlines(0, latitude[0], latitude[len(f_)-1], linestyles='--', alpha=0.6)

    ax.set_xlim((f_[0], f_[len(f_)-1]))
    ax.set_ylim((latitude[0], latitude[len(f_)-1]))

    ax.set_xlabel('Value of $f$ ($\mathregular{s^{-1}}$)')
    ax.set_ylabel('Latitude (Degrees)')
    plt.show()

    return fig
