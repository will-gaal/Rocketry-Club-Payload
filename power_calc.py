#calculate power, determine necessary dimensions, determine temp difference.

import scipy.integrate
from scipy.integrat import quad
import math


flywheel_period = 1 #arbitary
flywheel_angle = 1 #arbitary
tao = flywheel_period #[seconds]
theta = flywheel_angle #[radians]
CR = 1.5 #[], dimensionless
R = 8.3145 #[J / mol / Kelvin]
Tc = 279.234 #[Kelvin], based on atmospheric temperature at 14,000 ft, 95F on ground
Th = 323 #[Kelvin], estimation
time = 250 #[seconds]
volume = 1 #arbitary
dV = 1 #arbitary
mass_fluid_Helium = volume * 4.00 * 0.000164 #[g], use mL for volume
pressure = 1 #arbitary
number_cycles = 1 #arbitary

###################################################
#Algorithm 1
#from https://aapt.scitation.org/doi/10.1119/10.0000832

non_dim_power = (1/tao)*integral(from 0 to 2pi)*(pressure*dV/dtheta)dtheta

def integrand(x, a, b):
    return pressure*dV/dtheta
integrand =
non_dim_power = (1/tao) * quad()

###################################################
#Algorithm 2
#from https://www.mide.com/ideal-stirling-cycle-calculator

total_work = Tc*R*(math.log(1/CR)) + R*Th*(math.log(CR))
power_eqn_2 = total_work * mass_fluid_Helium * number_cycles * time





