from __future__ import annotations

from dataclasses import dataclass

import numpy as np

EHR_BLOCKS: dict[str, tuple[int, int]] = {
    "demographics": (0, 4),
    "labtrend": (4, 12),
    "autonomic": (12, 16),
    "medhx": (16, 22),
    "scifeat": (22, 28),
    "vitals": (28, 32),
}


@dataclass(frozen=True)
class Cohort:
    ehr: np.ndarray
    delta: np.ndarray
    bio: np.ndarray
    bio_mask: np.ndarray
    prev_tier: np.ndarray
    tier_label: np.ndarray
    visit_mask: np.ndarray
