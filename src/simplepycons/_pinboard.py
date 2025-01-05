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


class PinboardIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "pinboard"

    @property
    def original_file_name(self) -> "str":
        return "pinboard.svg"

    @property
    def title(self) -> "str":
        return "Pinboard"

    @property
    def primary_color(self) -> "str":
        return "#0000FF"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Pinboard</title>
     <path d="M13.352 14.585l-4.509 4.614.72-4.062L3.428 7.57 0 7.753
 7.58 0v2.953l7.214 6.646 4.513-1.105-4.689 4.982L24
 24l-10.648-9.415z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://commons.wikimedia.org/wiki/File:Feedb'''

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
