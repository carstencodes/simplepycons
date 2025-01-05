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


class ZerodhaIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "zerodha"

    @property
    def original_file_name(self) -> "str":
        return "zerodha.svg"

    @property
    def title(self) -> "str":
        return "Zerodha"

    @property
    def primary_color(self) -> "str":
        return "#387ED1"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Zerodha</title>
     <path d="M20.378 5.835A27.267 27.267 0 0124 12.169V0H13.666c2.486
 1.343 4.763 3.308 6.712 5.835zM5.48 1.297c-1.914 0-3.755.409-5.48
 1.166V24h22.944C22.766 11.44 15 1.297 5.48 1.297z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return ''''''

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
