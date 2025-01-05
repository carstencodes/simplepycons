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


class RockstarGamesIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "rockstargames"

    @property
    def original_file_name(self) -> "str":
        return "rockstargames.svg"

    @property
    def title(self) -> "str":
        return "Rockstar Games"

    @property
    def primary_color(self) -> "str":
        return "#FCAF17"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Rockstar Games</title>
     <path d="M5.971 6.816h3.241c1.469 0 2.741-.448 2.741-2.084
 0-1.3-1.117-1.576-2.19-1.576H6.748l-.777 3.66Zm12.834
 8.753h5.168l-4.664 3.228.755 5.087-4.041-3.07L10.599
 24l2.536-5.392s-2.95-3.075-2.947-3.075c-.198-.262-.265-.936-.265-1.226
 0-.367.024-.739.049-1.134.028-.451.058-.933.058-1.476
 0-1.338-.59-2.038-2.036-2.038H5.283l-1.18 5.525H.026L3.269
 0h7.672c2.852 0 5.027.702 5.027 3.936 0 2.276-1.12 3.894-3.592
 4.233v.045c1.162.276 1.598 1.062 1.598 2.527 0 .585-.018 1.098-.034
 1.581-.015.428-.03.834-.03 1.243 0 .525.137 1.382.48
 1.968h.567l3.028-5.06.82 5.096Zm-1.233-2.948-2.187 3.654h-3.457l2.103
 2.189-1.73 3.672 3.777-2.218 2.976 2.263-.553-3.731
 3.093-2.139h-3.43l-.592-3.69Z" />
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
