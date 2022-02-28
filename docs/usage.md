# Usage of the Plugin

Load the plugin with the module name `pyroll_freiberg_flow_stress`.

## The `RollPassProfile.freiberg_flow_stress_coefficients` hook

The plugin specifies the `RollPassProfile.freiberg_flow_stress_coefficients` hook to deliver material coefficients to
the flow stress function. The hook function must return an instance of the `FreibergFlowStressCoefficients` class.

    FreibergFlowStressCoefficients(
        A, m1, m2, m3, m4, m5, m6, m7, m8, m9,
        baseStrain, baseStrainRate
    )

The constructor takes in addition to the coefficients the base values for strain and strain rate to prevent zero flow
stress.

> The unit of the returned flow stress depends solely on the value of $`A`$. 
> Choose the unit of $`A`$ in that way, that the function returns flow stress in Pa (SI unit).
> Coefficient sets found in literature often return flow stress in MPa, fix that by multiplying $`A`$ by `1e6`.

For a few common materials hooks delivering coefficients are implemented. Those implementations ask for a `material`
attribute on the profile, being a string for material identification. The following materials are implemented (
case-insensitive):

- C20
- C45
- S355J2

Implement your own hook function to extend this. As with all hooks, to use custom coefficients one could simply give a
keyword argument `freiberg_flow_stress_coefficients` to the initial profile to use a constant coefficient set.

## The `RollPassProfile.flow_stress` hook

The plugin implements a function for the `RollPassProfile.flow_stress` hook, calculating flow stress according to
the [model](model.md).
This hook function asks for `freiberg_flow_stress_coefficients` on the profile.
If no coefficients are available the function returns `None`.
It also asks for `strain` and `temperature` on the profile, as well as for `strain_rate` on the roll pass.
If those are not available an error will occur.
