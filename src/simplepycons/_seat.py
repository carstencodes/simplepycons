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


class SeatIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "seat"

    @property
    def original_file_name(self) -> "str":
        return "seat.svg"

    @property
    def title(self) -> "str":
        return "SEAT"

    @property
    def primary_color(self) -> "str":
        return "#33302E"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>SEAT</title>
     <path d="M0 10.325l23.98 4.46c-.021.657-.062 2.712-.103
 3.903-.041 1.418-.35 2.281-.925 2.815-.801.72-1.747.884-4.007
 1.007-5.219.288-10.54.247-17.219-.226-.699-.04-.966-.185-1.089-.267-.288-.205-.329-.431-.411-1.603-.062-.801-.164-3.123-.205-3.904
 3.102.206 7.849.37 11.712.37.966 0 3.493.02 4.171.02.534 0 1.233-.143
 1.582-.698L0
 13.222zm.02-1.253c.021-.76.062-2.65.103-3.76.041-1.418.35-2.281.925-2.815.801-.72
 1.747-.884 4.007-1.007 5.219-.288 10.54-.247
 17.219.226.699.04.966.185 1.089.267.288.205.329.431.411
 1.603.041.678.144 2.486.185
 3.472-2.301-.123-6.206-.308-9.596-.35-3.39-.04-6.452.021-6.822.063-.74.102-1.089.452-1.192.595L24
 10.634v2.568Z" />
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
