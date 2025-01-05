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


class LinearIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "linear"

    @property
    def original_file_name(self) -> "str":
        return "linear.svg"

    @property
    def title(self) -> "str":
        return "Linear"

    @property
    def primary_color(self) -> "str":
        return "#5E6AD2"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Linear</title>
     <path d="M2.886 4.18A11.982 11.982 0 0 1 11.99 0C18.624 0 24
 5.376 24 12.009c0 3.64-1.62 6.903-4.18 9.105L2.887 4.18ZM1.817
 5.626l16.556 16.556c-.524.33-1.075.62-1.65.866L.951
 7.277c.247-.575.537-1.126.866-1.65ZM.322 9.163l14.515
 14.515c-.71.172-1.443.282-2.195.322L0 11.358a12 12 0 0 1
 .322-2.195Zm-.17 4.862 9.823 9.824a12.02 12.02 0 0 1-9.824-9.824Z" />
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
