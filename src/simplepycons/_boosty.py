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


class BoostyIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "boosty"

    @property
    def original_file_name(self) -> "str":
        return "boosty.svg"

    @property
    def title(self) -> "str":
        return "Boosty"

    @property
    def primary_color(self) -> "str":
        return "#F15F2C"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Boosty</title>
     <path d="M2.661 14.337 6.801 0h6.362L11.88 4.444l-.038.077-3.378
 11.733h3.15c-1.321 3.289-2.35 5.867-3.086
 7.733-5.816-.063-7.442-4.228-6.02-9.155M8.554
 24l7.67-11.035h-3.25l2.83-7.073c4.852.508 7.137 4.33 5.791
 8.952C20.16 19.81 14.344 24 8.68 24h-.127z" />
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
