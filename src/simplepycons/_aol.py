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


class AolIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "aol"

    @property
    def original_file_name(self) -> "str":
        return "aol.svg"

    @property
    def title(self) -> "str":
        return "AOL"

    @property
    def primary_color(self) -> "str":
        return "#3399FF"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>AOL</title>
     <path d="M13.07 9.334c2.526 0 3.74 1.997 3.74 3.706 0 1.709-1.214
 3.706-3.74 3.706-2.527 0-3.74-1.997-3.74-3.706 0-1.709 1.213-3.706
 3.74-3.706m0 5.465c.9 0 1.663-.741 1.663-1.759
 0-1.018-.763-1.759-1.663-1.759s-1.664.741-1.664 1.759c0 1.018.764
 1.76 1.664 1.76m4.913-7.546h2.104v9.298h-2.104zm4.618 6.567a1.398
 1.398 0 1 0 .002 2.796 1.398 1.398 0 0 0-.002-2.796M5.536
 7.254H3.662L0 16.55h2.482l.49-1.343h3.23l.452 1.343H9.16zm-1.91
 6.068L4.6 10.08l.974 3.242H3.626z" />
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
