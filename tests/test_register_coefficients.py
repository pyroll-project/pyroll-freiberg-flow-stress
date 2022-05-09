from pyroll_freiberg_flow_stress import FreibergFlowStressCoefficients
from pyroll import RollPass, Roll, Profile, RoundGroove


def test_register_coefficients():
    c = FreibergFlowStressCoefficients(42)
    c.register("test_material")

    p = RollPass.Profile(RollPass(strain_rate=1, roll=Roll(RoundGroove(1, 10, 5))),
                         Profile.round(10, strain=1, temperature=1200, material="test_material"))

    assert p.flow_stress == 42
