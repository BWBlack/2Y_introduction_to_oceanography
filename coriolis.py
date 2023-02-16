import numpy as np
import os
import matplotlib.pyplot as plt
from plotting import multiline

default_omega = (2*np.pi) / (24*3600)                                   # ~7.29e-05 radians / sec
latitude = np.arange(-90, 90, 0.5)                                      # an array of latitude values, pole to pole

def omegas(rotation_period):
    return (2 * np.pi) / (rotation_period * 3600)

def f_val(omega):
    return 2 * omega * np.sin(np.deg2rad(latitude))                     #

def f_plot(latitude=latitude, other_values=False, save=False):

    fig, ax = plt.subplots(figsize=(15,15))

    if other_values:
        
        print()
        start = input('Max rotation in hours (lowest number): ')
        stop = input('Min rotation in hours (largest number): ')
        # steps = input('Number of values between them (a whole number): ')

        rr_rng_ = np.arange(float(start), float(stop), 1)

        lats = np.repeat(latitude[np.newaxis,:], len(rr_rng_), axis=0)
        fs =   f_val(np.repeat(omegas(rr_rng_)[:,np.newaxis], len(latitude), axis=1))

        plot = multiline(fs, lats, rr_rng_, cmap='magma', lw=2, alpha=0.7)

        cb = fig.colorbar(plot)
        cb.set_label('Rotation period (hours)')

    f_ = f_val(default_omega)
    ax.plot(f_, latitude, color='black', label='24 hour rotation period')

    ax.hlines(0, 10*f_[0], 10*f_[len(f_)-1], linestyles='--', alpha=0.6)
    ax.vlines(0, latitude[0], latitude[len(f_)-1], linestyles='--', alpha=0.6)

    ax.relim(visible_only=True)
    ax.set_ylim(-90,90)
    ax.autoscale_view()

    ax.set_xlabel('Value of $f$ ($\mathregular{s^{-1}}$)')
    ax.set_ylabel('Latitude (Degrees)')
    ax.legend()

    plt.show()

    if save:
        id=np.random.rand().__round__(5)
        path=os.getcwd().replace('\\','/')
        fig.savefig(f'{path}/figures/coriolis_f_value_id{id}.png')
