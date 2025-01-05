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


class WesternUnionIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "westernunion"

    @property
    def original_file_name(self) -> "str":
        return "westernunion.svg"

    @property
    def title(self) -> "str":
        return "Western Union"

    @property
    def primary_color(self) -> "str":
        return "#FFDD00"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Western Union</title>
     <path d="M15.799 5.188h5.916L24 9.155l-4.643 8.043c-1.246
 2.153-3.28 2.153-4.526 0L7.893 5.188h5.919l4.273 7.39a1.127 1.127 0 0
 0 1.981.002l-4.267-7.392ZM0 5.188h5.921l6.237 10.802-.697
 1.204c-1.246 2.153-3.285 2.153-4.531 0L0 5.188Z" />
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
