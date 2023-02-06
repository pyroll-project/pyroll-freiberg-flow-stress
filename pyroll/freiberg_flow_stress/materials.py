from pyroll.core import Profile

from .freiberg_flow_stress import FreibergFlowStressCoefficients


def is_material(profile: Profile, materials: set[str]):
    if isinstance(profile.material, str):
        return profile.material.lower() in materials
    return materials.intersection([m.lower() for m in profile.material])


@Profile.freiberg_flow_stress_coefficients
def c20(self: Profile):
    if is_material(self, {"c20", "c22"}):
        return FreibergFlowStressCoefficients(
            a=3304.39 * 1e6,
            m1=-0.00281,
            m2=0.34766,
            m4=0.00002,
            m5=-0.00130,
            m7=0.07632,
            m8=0.000148,
            baseStrain=0.1,
            baseStrainRate=0.1
        )


@Profile.freiberg_flow_stress_coefficients
def c45(self: Profile):
    if is_material(self, {"c45"}):
        return FreibergFlowStressCoefficients(
            a=3268.49 * 1e6,
            m1=-0.00267855,
            m2=0.34446,
            m4=0.000551814,
            m5=-0.00132042,
            m7=0.0166334,
            m8=0.000149907,
            baseStrain=0.1,
            baseStrainRate=0.1
        )


@Profile.freiberg_flow_stress_coefficients
def s355j2(self: Profile):
    if is_material(self, {"s355j2"}):
        return FreibergFlowStressCoefficients(
            a=2852.66 * 1e6,
            m1=-0.00244,
            m2=0.41934,
            m4=0.00088,
            m5=-0.00149,
            m7=0.12169,
            m8=0.000127,
            baseStrain=0.1,
            baseStrainRate=0.1
        )
