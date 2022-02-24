# The Freiberg Flow Stress Model

The Freiberg Flow Stress Model is a flexible empirical flow stress model approach. It features several terms and
coefficients to model common shapes of flow stress curves in cold and hot forming. The flow stress is here assumed to be
only dependent on strain, strain rate and temperature, thus all other influences are included in the empirical
coefficients.

The model includes several exponential and power terms. The material dependent coefficients are $`A`$ and the $`m_i`$.
One has not to use everytime all coefficients, if a term is not needed the corresponding coefficient can be set to zero.

```math
    k_\mathrm{f} \left( \varphi, \dot{\varphi}, \vartheta \right) =
    A\exp\left(m_1 \vartheta\right) \vartheta^{m_9} 
    \varphi^{m_2} \exp\left( \frac{m_4}{\varphi} \right) 
    \left(1 + \varphi \right)^{m_5\vartheta+m_6} \exp\left(m_7 \varphi\right)
    \dot{\varphi}^{m_3 + m_8 \vartheta}
```

The temperature is commonly used in °C, conversion is done internally, since PyRoll uses temperatures in K. The function
shows results to 0 at $`\varphi = 0`$ and $`\dot{\varphi} = 0`$, so commonly small base values are added to the
variables (about 0.01 to 0.1). These influence the model fitting, so one should receive those used in fitting together
with the coefficients.

For model fitting one needs several flow stress curves, determined from compression, torsion or tension tests, at
several temperatures and strain rates. A common thumb rule for hot forming is to take temperatures every $`50`$ or
$`100 \mathrm{K}`$ in the desired range and strain rates of $`0.1`$, $`1`$ and $`10 s^{-1}`$. The model should not be
used across major structural transitions of the material.

## References

- Landolt-Börnstein - Group VIII Advanced Materials and Technologies - 2 Flow Stress of Steel,
  DOI: [10.1007/978-3-540-44760-3_3](https://doi.org/10.1007/978-3-540-44760-3_3)
- Hensel, Spittel: Kraft- und Arbeitsbedarf bildsamer Formgebungsverfahren, Deutscher Verlag für Grundstoffindustrie,
  Leipzig, 1978
- Hensel, Poluchin: Technologie der Metallformung, Deutscher Verlag für Grundstoffindustrie, Leipzig, 1990, ISBN:
  3-342-00311-1