#one tailed test
# Using Python package - statsmodels - to solve for sample size in a Z Test. 

from statsmodels.stats.proportion import proportion_effectsize
from statsmodels.stats.power import zt_ind_solve_power

std_effect = proportion_effectsize(.073, .0876)
alpha=.05
power = 0.8
effect_size = std_effect
alternative= "smaller"

zt_ind_solve_power(effect_size=effect_size, nobs1=None, alpha=alpha, power=power, alternative=alternative)








#two tailed test
# Using Python package - statsmodels - to solve for sample size in a Z Test. 

from statsmodels.stats.proportion import proportion_effectsize
from statsmodels.stats.power import zt_ind_solve_power

std_effect = proportion_effectsize(.073, .0876)
alpha=.05
power = 0.8
effect_size = std_effect

zt_ind_solve_power(effect_size=effect_size, nobs1=None, alpha=alpha, power=power)



# if the difference in the effect size is small, you need a larger sample size to prove the dif is sig
