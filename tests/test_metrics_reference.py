from __future__ import annotations

import numpy as np

from chronorisk.soundingcheck.calibration import expected_calibration_error


def test_ece_extreme_cases() -> None:
    confident_wrong = np.full(100, 0.9)
    labels = np.zeros(100)
    assert abs(expected_calibration_error(confident_wrong, labels) - 0.9) < 1e-6
    calibrated = np.concatenate([np.zeros(50), np.ones(50)])
    perfect_labels = np.concatenate([np.zeros(50), np.ones(50)])
    assert expected_calibration_error(calibrated, perfect_labels) < 1e-9
