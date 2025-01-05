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


class EightSleepIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "eightsleep"

    @property
    def original_file_name(self) -> "str":
        return "eightsleep.svg"

    @property
    def title(self) -> "str":
        return "Eight Sleep"

    @property
    def primary_color(self) -> "str":
        return "#262729"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Eight Sleep</title>
     <path d="M19.847 7.28V4.105A4.104 4.104 0 0 0 15.745
 0H8.258a4.104 4.104 0 0 0-4.105 4.102v3.183a4.092 4.092 0 0 0 2.415
 3.738v.588a4.102 4.102 0 0 0-2.415 3.738v4.546A4.104 4.104 0 0 0
 8.255 24h7.488a4.104 4.104 0 0 0 4.104-4.104v-4.553a4.102 4.102 0 0
 0-2.415-3.738v-.587a4.102 4.102 0 0 0 2.415-3.738zM8.451
 5.126c0-.818.662-1.482 1.48-1.483h4.133c.819 0 1.483.663 1.483
 1.482v1.991c0 .819-.664 1.482-1.483 1.482H9.93a1.482 1.482 0 0
 1-1.482-1.482l.003-1.99zm7.1 13.732c0 .818-.664 1.482-1.483
 1.482H9.93a1.482 1.482 0 0 1-1.482-1.482v-2.752c0-.819.664-1.483
 1.482-1.483h4.134c.819 0 1.483.664 1.483 1.483l.003 2.752z" />
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
