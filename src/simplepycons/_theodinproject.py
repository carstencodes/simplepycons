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


class TheOdinProjectIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "theodinproject"

    @property
    def original_file_name(self) -> "str":
        return "theodinproject.svg"

    @property
    def title(self) -> "str":
        return "The Odin Project"

    @property
    def primary_color(self) -> "str":
        return "#A9792B"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>The Odin Project</title>
     <path d="m3.002 0 1.9902 7.3867L6.5684 8.963v.5762l.9746
 1.9238c.806-1.53 2.8445-2.0638
 4.3125-.9688l.2011.1504.2012-.1504c1.469-1.095 3.5075-.5612
 4.3145.9688l.9746-1.9258v-.6894l1.461-1.461L20.998 0l-3.6328
 1.8594v3.2578c-.655-.395-2.9816-1.6914-5.3086-1.6914-2.494 0-4.9868
 1.4887-5.4218 1.7617V1.8594L3.002 0zm6.1113 10.2285c-.18
 0-.3262.1443-.3262.3223v.998c0 .267.2192.4844.4902.4844h.5606c.304 0
 .5936-.12.8086-.332a1.115 1.115 0 0 0
 .336-.7969v-.3535c0-.178-.1472-.3223-.3282-.3223h-1.541zm5.291.3926c-.285
 0-.5176.2278-.5176.5098 0 .281.2326.5097.5176.5097.286 0
 .5176-.2287.5176-.5097
 0-.282-.2316-.5098-.5176-.5098zm-7.836.0234-1.4648 5.414 1.4961
 2.9513 1.375-5.1035.1973-.0977-1.6035-3.164zm10.9786 0-1.6035
 3.164.1972.0977 1.375 5.1036 1.4961-2.9512-1.4648-5.414zm-5.4903
 1.8047-1.828.9024L8.58 22.1953 12.0566
 24l3.4766-1.8047-1.6465-8.8437-1.83-.9024zM9.668
 13.629l-1.2696.625-1.6543 6.1367 1.4688 1.0489 1.455-7.8106zm4.7793 0
 1.455 7.8106
 1.4668-1.0489-1.6523-6.1367-1.2695-.625zm-3.0157.084h1.2813v.4512a.623.623
 0 0 1-.1875.4453.6434.6434 0 0 1-.4531.1855.6451.6451 0 0
 1-.4532-.1855.623.623 0 0 1-.1875-.4453v-.4512z" />
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
