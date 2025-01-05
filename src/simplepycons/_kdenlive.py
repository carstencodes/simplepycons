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


class KdenliveIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "kdenlive"

    @property
    def original_file_name(self) -> "str":
        return "kdenlive.svg"

    @property
    def title(self) -> "str":
        return "Kdenlive"

    @property
    def primary_color(self) -> "str":
        return "#527EB2"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Kdenlive</title>
     <path d="m8.727 1.554 2.727
 4.334v16.558h1.091V5.889l2.728-4.335zm-6 4.948V9.8h7.091c.003-.83
 0-1.672-.006-2.498
 0-.383-.356-.732-.718-.8H2.727zm12.303.001c-.402.024-.835.41-.834.837l-.014
 12.619c0 .57.767 1.065 1.207.727l8.28-6.331c.441-.335.44-1.12
 0-1.455l-8.265-6.287a.553.553 0 0 0-.374-.11zM-.001
 12v3.299h9.818V12zm4.363 5.497v3.3h5.455v-3.3z" />
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
