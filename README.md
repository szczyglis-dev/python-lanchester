Release: **1.0.1** | build: **2024.08.26** | Python: **>=3.7**

# Python Lanchester's laws

**A Python module, Jupyter notebook, and sample application for predicting the outcome of battles using Lanchester's differential equations. The module can forecast results using three different models: the `linear law`, the `square law`, and a `modernized model`. An example included in the repository demonstrates how to predict outcomes using any of these three models and display both the result and a plot showing the progress of the battle over time. The module can be easily integrated into any Python application.**

## What are Lanchester's laws?

from: https://en.wikipedia.org/wiki/Lanchester%27s_laws
> Lanchester's laws are mathematical formulae for calculating the relative strengths of military forces. The Lanchester equations are differential equations describing the time dependence of two armies' strengths A and B as a function of time, with the function depending only on A and B.
In 1915 and 1916, during World War I, M. Osipov and Frederick Lanchester independently devised a series of differential equations to demonstrate the power relationships between opposing forces. Among these are what is known as Lanchester's linear law (for ancient combat) and Lanchester's square law (for modern combat with long-range weapons such as firearms).

**Screenshot from included example application**

![lanchester](https://user-images.githubusercontent.com/61396542/180256468-4fec137e-121a-416b-86ce-ed96f4a27ad2.png)

## Repository contents

- `lanchester.py` - A Python module containing functions that solve the Lanchester equations over time.
- `app.py` - An example application demonstrating the use of the module.
- `notebook.ipynb` - A Jupyter notebook showcasing an example of how the module works in real time.


### Example of Use

The module can predict outcomes using three different models: the `linear law`, the `square law`, and a `modernized model`.

**Required packages**

- `numpy`
- `matplotlib`


**Method #1: linear law**

```python
# app.py

import numpy as np
import matplotlib.pyplot as plt
import lanchester

# base parameters:
R0 = 8000 # number of RED units
B0 = 10000 # number of BLUE units
T = 100 # total number of steps in the simulation
dt = 1 # time interval 


# parameters for "linear" and "modernized" models:
r_l = 0.00001 # combat efficiency of RED units
b_l = 0.00002 # combat efficiency of BLUE units

R, B = lanchester.linear(R0, B0, r_l, b_l, T, dt) # result

```

**Method #2: square law**

```python
# app.py

import numpy as np
import matplotlib.pyplot as plt
import lanchester

# base parameters:
R0 = 8000 # number of RED units
B0 = 10000 # number of BLUE units
T = 100 # total number of steps in the simulation
dt = 1 # time interval 

# parameters for "square" and "modernized"  models:
r_s = 0.2 # average number of RED units that damage each other per unit of time
b_s = 0.1 # average number of BLUE units that damage each other per unit of time

R, B = lanchester.square(R0, B0, r_s, b_s, T, dt) # result

```

**Method #3: modernized model**

```python
# app.py

import numpy as np
import matplotlib.pyplot as plt
import lanchester

# base parameters:
R0 = 8000 # number of RED units
B0 = 10000 # number of BLUE units
T = 100 # total number of steps in the simulation
dt = 1 # time interval 

# parameters for "linear" and "modernized" models:
r_l = 0.00001 # combat efficiency of RED units
b_l = 0.00002 # combat efficiency of BLUE units


# parameters for "square" and "modernized"  models:
r_s = 0.2 # average number of RED units that damage each other per unit of time
b_s = 0.1 # average number of BLUE units that damage each other per unit of time


# parameters for "modernized" model only:
r_f = 0.6 # RED units camouflage ability factor
b_f = 0.2 # BLUE units camouflage ability factor

r_a = 0.6 # RED units ability to recognize
b_a = 0.2 # BLUE units ability to recognize

r_i = 4 # RED units information warfare ability coefficient
b_i = 4 # BLUE units information warfare ability coefficient

R, B = lanchester.modernized(R0, B0, r_l, b_l, r_s, b_s, r_f, r_a, b_f, b_a, r_i, b_i, T, dt) # result
```

**Displaying result and plot from obtained predictions**

```python

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
plt.plot(t, R, '--r', label='RED units')
plt.plot(t, B, 'b', label='BLUE units')
plt.xlabel("Time (round)")
plt.ylabel("Number of units")
plt.title("Lanchester's model simulation")
plt.legend()
plt.show()
```

**Result of the battle**

![lanchester](https://user-images.githubusercontent.com/61396542/180256468-4fec137e-121a-416b-86ce-ed96f4a27ad2.png)


## Changelog

**1.0.0** - Initial release (2022-07-21)

**1.0.1** - Updated documentation (2024-08-26)

--- 
**Python Lanchester is free to use, but if you like it, you can support my work by buying me a coffee ;)**

https://www.buymeacoffee.com/szczyglis

**Enjoy!**

MIT License | 2022 Marcin 'szczyglis' Szczygliński

https://github.com/szczyglis-dev/python-lanchester

Contact: szczyglis@protonmail.com
