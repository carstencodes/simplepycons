#
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2026 Carsten Igel.
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


class RolldownIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "rolldown"

    @property
    def original_file_name(self) -> "str":
        return "rolldown.svg"

    @property
    def title(self) -> "str":
        return "Rolldown"

    @property
    def primary_color(self) -> "str":
        return "#FF4100"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Rolldown</title>
     <path d="M21.652 0c.514 0 .796.6.466.998l-5.616
 6.74c-.662.793-.098 1.997.934 1.997h5.433c.516 0
 .797.6.467.998L12.467 23.775a.6.6 0 0 1-.468.225.6.6 0 0
 1-.468-.225L.661 10.733a.609.609 0 0 1 .468-.998H6.56c1.032 0
 1.595-1.204.937-1.997L1.88.998A.608.608 0 0 1 2.346 0Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/voidzero-dev/community-des
ign-resources/blob/55902097229cf01cf2a4ceb376f992f5cf306756/brand-asse'''

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
