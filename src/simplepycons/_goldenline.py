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


class GoldenlineIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "goldenline"

    @property
    def original_file_name(self) -> "str":
        return "goldenline.svg"

    @property
    def title(self) -> "str":
        return "GoldenLine"

    @property
    def primary_color(self) -> "str":
        return "#FFE005"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>GoldenLine</title>
     <path d="M11.997 24a11.995 11.995 0 0 0
 11.949-13.04h-6.781v2.943h1.226a6.667 6.667 0 1
 1-.114-4.156h5.509A11.995 11.995 0 1 0 12 23.991z" />
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
