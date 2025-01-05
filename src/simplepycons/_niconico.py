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


class NiconicoIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "niconico"

    @property
    def original_file_name(self) -> "str":
        return "niconico.svg"

    @property
    def title(self) -> "str":
        return "niconico"

    @property
    def primary_color(self) -> "str":
        return "#231815"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>niconico</title>
     <path d="M.4787 7.534v12.1279A2.0213 2.0213 0 0 0 2.5
 21.6832h2.3888l1.323 2.0948a.4778.4778 0 0 0 .4043.2205.4778.4778 0 0
 0 .441-.2205l1.323-2.0948h6.9828l1.323 2.0948a.4778.4778 0 0 0
 .441.2205c.1838 0 .3308-.0735.4043-.2205l1.323-2.0948h2.6462a2.0213
 2.0213 0 0 0 2.0213-2.0213V7.5339a2.0213 2.0213 0 0
 0-2.0213-1.9845h-7.681l4.4468-4.4469L17.1637 0l-5.1452 5.1452L6.8 0
 5.6973 1.1025l4.4102 4.4102H2.5367a2.0213 2.0213 0 0 0-2.058 2.058z"
 />
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
