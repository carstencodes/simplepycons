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


class VeedIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "veed"

    @property
    def original_file_name(self) -> "str":
        return "veed.svg"

    @property
    def title(self) -> "str":
        return "VEED"

    @property
    def primary_color(self) -> "str":
        return "#B6FF60"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>VEED</title>
     <path d="m23.9847 3.44845-6.4707 15.8711a2.41415 2.41415 0 0
 1-2.23542 1.50241H8.73883a2.4138 2.4138 0 0 1-2.23388-1.5005L.01467
 3.44846a.196.196 0 0 1 .18143-.27042h6.5505a.3923.3923 0 0 1
 .36707.25392l4.90577 13.08297
 4.8655-13.08144c.05678-.15342.20368-.25545.36708-.25545h6.55164c.13924
 0 .23398.14115.18181.26965z" />
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
