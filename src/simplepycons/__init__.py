# type: ignore
#
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2024 Carsten Igel.
#
# This file is part of simplepycons
# (see https://github.com/carstencodes/simplepycons).
#
# This file is published using the MIT license.
# Refer to LICENSE for more information
#
""""""

from .all import *  # noqa: F403
from .base_icon import Icon
from .icons import IconFactory
from .registry import ICONS as _ICONS

all_icons = _ICONS

__all__ = ALL_ICONS  # noqa: F405
__all__ += [
      Icon.__name__,
      IconFactory.__name__,
]
