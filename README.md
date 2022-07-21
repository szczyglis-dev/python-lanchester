
**Python 3+**, current release: **1.0.0** build 2022-07-21

# Python Lanchester's laws

**A Python module, a Jupyter notebook and a sample application for predicting the result of a battle using Lanchester differential equations. The module can predict the result with 3 different models: `linear law`, `square law` and `modernized model`. An example included in the repository allows you to predict the result using one of these 3 models and display the result and a plot with the course of the battle over time. The module can be easily used in any Python application.**

## What are Lanchester's laws?
from: https://en.wikipedia.org/wiki/Lanchester%27s_laws
> Lanchester's laws are mathematical formulae for calculating the relative strengths of military forces. The Lanchester equations are differential equations describing the time dependence of two armies' strengths A and B as a function of time, with the function depending only on A and B.
In 1915 and 1916, during World War I, M. Osipov and Frederick Lanchester independently devised a series of differential equations to demonstrate the power relationships between opposing forces. Among these are what is known as Lanchester's linear law (for ancient combat) and Lanchester's square law (for modern combat with long-range weapons such as firearms).

**Screenshot from Matplotlib:**

![lanchester](https://user-images.githubusercontent.com/61396542/180256468-4fec137e-121a-416b-86ce-ed96f4a27ad2.png)

## Repository contents:

- `lanchester.py` - Python module with functions that solve the Lanchester equations in time
- `app.py` - example application that uses the module
- `notebook.ipynb` - Jupyter notebook with an example of how it works in real-time


### Example of use:

The module can predict the result using 3 different models: `linear law`, `square law` and `modernized model`.

**Required libraries**

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

**Result:**

![lanchester](https://user-images.githubusercontent.com/61396542/180256468-4fec137e-121a-416b-86ce-ed96f4a27ad2.png)


## Changelog
**- 1.0.0** - published first release (2022-07-21)

## Credits
 
### Python Lanchester is free to use but if you liked then you can donate project via BTC: 

**14X6zSCbkU5wojcXZMgT9a4EnJNcieTrcr**

or by PayPal:
 **[https://www.paypal.me/szczyglinski](https://www.paypal.me/szczyglinski)**


**Enjoy!**

MIT License | 2022 Marcin 'szczyglis' Szczygliński

https://github.com/szczyglis-dev/python-lanchester

Contact: szczyglis@protonmail.com
