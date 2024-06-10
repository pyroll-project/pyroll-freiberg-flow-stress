import pytest
import logging
import importlib
import webbrowser

import pyroll.core
import pyroll.pillar_model
import pyroll.freiberg_flow_stress
import pyroll.local_velocity

from pathlib import Path
from pyroll.core import Profile, PassSequence, RollPass, Roll, CircularOvalGroove, Transport, RoundGroove


@RollPass.DiskElement.pillar_spreads
def pillar_spreads(self: RollPass.DiskElement):
    return self.pillar_draughts ** -0.5


DISK_ELEMENT_COUNT = 30
pyroll.pillar_model.Config.PILLAR_COUNT = 100


@pytest.mark.skipif(not pyroll.freiberg_flow_stress.PILLAR_MODEL_INSTALLED, reason="Pillar model is not installed.")
def test_solve_pillars_flow_stress(tmp_path: Path, caplog):
    caplog.set_level(logging.INFO, logger="pyroll")
    pyroll.pillar_model.Config.PILLAR_TYPE = "EQUIDISTANT"

    in_profile = Profile.round(
        diameter=19.5e-3,
        temperature=1200 + 273.15,
        strain=0,
        material=["C45", "steel"],
        density=7.5e3,
        specific_heat_capcity=690,
    )

    sequence = PassSequence(
        [
            RollPass(
                label="Oval",
                roll=Roll(
                    groove=CircularOvalGroove(
                        depth=5e-3,
                        r1=0.2e-3,
                        r2=16e-3,
                    ),
                    nominal_radius=160e-3,
                    rotational_frequency=1,
                    neutral_point=-20e-3
                ),
                gap=4e-3,
                disk_element_count=DISK_ELEMENT_COUNT,
            ),

        ]
    )

    try:
        sequence.solve(in_profile)
    finally:
        print("\nLog:")
        print(caplog.text)

    try:
        from pyroll.report import report

        report = report(sequence)
        f = tmp_path / "report.html"
        f.write_text(report)
        webbrowser.open(f.as_uri())

    except ImportError:
        pass
