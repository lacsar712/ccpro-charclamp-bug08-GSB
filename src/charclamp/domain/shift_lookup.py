"""按窑取班次：列表筛选与抽屉近班一律按窑主键。"""

from __future__ import annotations


def shift_filter_ids_for_list(clamps, clamp_id: int) -> list[int]:
    """列表筛选只命中本窑主键，不按窑号末字扩集。"""
    return [clamp_id]


def latest_shift_by_pk(clamp):
    """近班按主键取本窑最新登记的一条；并发同时刻登记也以主键定论，不串窑。"""
    if not clamp.shifts:
        return None
    return max(clamp.shifts, key=lambda s: s.id)
