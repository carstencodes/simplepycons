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


class DolphinIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "dolphin"

    @property
    def original_file_name(self) -> "str":
        return "dolphin.svg"

    @property
    def title(self) -> "str":
        return "Dolphin"

    @property
    def primary_color(self) -> "str":
        return "#00AAFF"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Dolphin</title>
     <path d="M17.195 5.308a6.61 6.61 0 0
 0-.804.026c-1.223.108-1.834.504-2.135.691-.135.083-.344.1-.518.062-3.518-1.08-6.743-.62-8.363-.142-3.228.951-3.893
 2.885-4.098 3.978-.07.295-.093.532-.13.67-.115.443-1.565 1.225-1.029
 1.78.517.534 1.423.478 2.08.216 1.494-.592 2.652-.809
 4.599-.882h.021c.181-.003.338-.034.475.091.16.149.708 1.308 1.927
 2.16 1.363.953 2.772.913
 2.86.768v-.002h.002l.002-.002v-.002c.036-.12-.315-.2-1.063-1.13-.646-.804-.592-1.645.036-1.49a.591.591
 0 0 0 .04.007c3.447.901 5.748 2.922 5.868
 2.947v.002h.002l.002-.002.002-.002v-.008c.166-.229-.958-2.957-3.871-4.586-3.297-1.843-6.389-.971-7.061-.693-.162-.272.967-1.383
 3.377-1.476 5.4-.209 8.744 2.753 10.578 4.56 2.25 2.217 3.923 5.853
 3.973
 5.846l.002-.002h.002v-.004h.004c.12-.125-.2-2.393-.885-4.045-.881-2.126-1.966-3.69-3.525-5.148a15.572
 15.572 0 0 0-2.153-1.69c-.114-.079-.254-.183-.337-.328.434-1.003
 2.046-1.04
 2.213-1.13l.007-.005.002-.002v-.002l.002-.004c.085-.183-.424-.966-2.107-1.023z"
 />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/dolphin-emu/dolphin/blob/6'''

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
