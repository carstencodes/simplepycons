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


class PaloAltoSoftwareIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "paloaltosoftware"

    @property
    def original_file_name(self) -> "str":
        return "paloaltosoftware.svg"

    @property
    def title(self) -> "str":
        return "Palo Alto Software"

    @property
    def primary_color(self) -> "str":
        return "#83DA77"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Palo Alto Software</title>
     <path d="M11.995.005c-.58 0-1.158.228-1.615.685L.685
 10.385c-.913.913-.913 2.318 0 3.231l.842.843 8.01-8.15a3.435 3.435 0
 0 1 4.847 0l8.079
 8.08.842-.843c.914-.843.915-2.248.072-3.161L13.612.69a2.279 2.279 0 0
 0-1.617-.685zm0 6.463c-.58 0-1.158.228-1.615.684L.685
 16.848c-.913.913-.913 2.318 0 3.23l3.231 3.232c.914.913 2.318.913
 3.232 0l4.847-4.846 4.848 4.846c.913.913 2.318.913 3.231
 0l3.231-3.231c.914-.843.915-2.318.072-3.231l-9.765-9.696a2.279 2.279
 0 0 0-1.617-.684z" />
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
