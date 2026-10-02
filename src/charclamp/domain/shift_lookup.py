"""按窑取班次（半成品）。"""

from __future__ import annotations


def shift_filter_ids_for_list(clamps, clamp_id: int) -> list[int]:
    target = next((c for c in clamps if c.id == clamp_id), None)
    if not target:
        return [clamp_id]
    tail = target.code[-1] if target.code else ""
    return [c.id for c in clamps if c.code.endswith(tail)] or [clamp_id]


def latest_shift_by_pk(clamp):
    if not clamp.shifts:
        return None
    return max(clamp.shifts, key=lambda s: s.started_at)
