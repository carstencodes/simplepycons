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


class EdgeImpulseIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "edgeimpulse"

    @property
    def original_file_name(self) -> "str":
        return "edgeimpulse.svg"

    @property
    def title(self) -> "str":
        return "Edge Impulse"

    @property
    def primary_color(self) -> "str":
        return "#3B47C2"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Edge Impulse</title>
     <path d="M16.008 10.287h4.51l1.348 3.53h-5.858c-.979
 0-1.772-.79-1.772-1.766s.793-1.766 1.772-1.766v.002ZM.677 12.049a1.77
 1.77 0 0 1 1.773-1.766h8.597a1.77 1.77 0 0 1 1.772 1.766c0 .976-.793
 1.766-1.772 1.766H2.45c-.98 0-1.773-.79-1.773-1.766ZM24
 19.613H4.448a2.515 2.515 0 0 1-1.93.899A2.514 2.514 0 0 1 0
 18.002a2.514 2.514 0 0 1 2.518-2.509c.775 0 1.467.351
 1.93.899h18.321L24 19.613ZM19.594 7.655H4.404a2.51 2.51 0 0
 1-1.886.852A2.514 2.514 0 0 1 0 5.998a2.514 2.514 0 0 1
 2.518-2.51c.797 0 1.506.371 1.967.946h13.878l1.231 3.221Z" />
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
