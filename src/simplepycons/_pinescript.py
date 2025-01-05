#
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2025 Carsten Igel.
#
# This file is part of simplepycons
# (see https://github.com/carstencodes/simplepycons).
#
# This file is published using the MIT license.
# Refer to LICENSE for more information
#
""""""
# pylint: disable=C0302
# Justification: Code is generated

from typing import TYPE_CHECKING

from .base_icon import Icon

if TYPE_CHECKING:
    from collections.abc import Iterable


class PineScriptIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "pinescript"

    @property
    def original_file_name(self) -> "str":
        return "pinescript.svg"

    @property
    def title(self) -> "str":
        return "Pine Script"

    @property
    def primary_color(self) -> "str":
        return "#00B453"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Pine Script</title>
     <path d="M3.785 16.14.124 21.287c-.311.437 0 1.044.536
 1.044h22.681c.535 0 .846-.608.536-1.045l-4.2-5.927-1.979 1.161c-.037
 1.063-.907 1.913-1.976 1.913-1.092 0-1.977-.887-1.977-1.982
 0-.055.003-.11.007-.165l-3.173-2.328c-.341.278-.775.445-1.249.445-.56
 0-1.065-.234-1.425-.609l-4.12 2.346Zm7.693-14.194L3.813
 12.732c-.222.314-.132.751.197.95l.691.417 2.66-1.515a1.747 1.747 0 0
 1-.007-.163c0-1.095.885-1.982 1.977-1.982 1.091 0 1.976.887 1.976
 1.982 0 .138-.014.273-.041.403l3.047 2.237c.359-.366.858-.592
 1.409-.592.634 0 1.198.299
 1.56.764l2.831-1.66c.219-.222.258-.581.068-.849L12.553
 1.948c-.262-.371-.812-.373-1.075-.002Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/tradingview/documentation-
guidelines/blob/0d7a2d014818ebdd03540c5fd7b97fe493cd056c/images/pine/P'''

    @property
    def license(self) -> "tuple[str | None, str | None]":
        _type: "str | None" = ''''''
        _url: "str | None" = ''''''

        if _type is not None and len(_type) == 0:
            _type = None

        if _url is not None and len(_url) == 0:
            _url = None

        return _type, _url

    @property
    def aliases(self) -> "Iterable[str]":
        yield from []
