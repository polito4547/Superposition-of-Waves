# -*- coding: utf-8 -*-
"""
Created on Wed Mar 2 17:49:12 2022
@author: Leo Gomez
"""

import numpy as np
import matplotlib.pyplot as plotter

amplitudes = [2, -1, 1]

print(amplitudes[0], amplitudes[1], amplitudes[2])

time = np.linspace(0, 1, 100)

# Frequency values are in Hz
frequency = 1

waves = [amp * np.sin(2 * np.pi * frequency * time) for amp in amplitudes]

print(waves[0], waves[1], waves[2])

plotter.plot(time, waves[1], color = 'r', label = 'wave 1')
plotter.show()
