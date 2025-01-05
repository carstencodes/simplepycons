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


class DotenvIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "dotenv"

    @property
    def original_file_name(self) -> "str":
        return "dotenv.svg"

    @property
    def title(self) -> "str":
        return ".ENV"

    @property
    def primary_color(self) -> "str":
        return "#ECD53F"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>.ENV</title>
     <path d="M24 0v24H0V0h24ZM10.933
 15.89H6.84v5.52h4.198v-.93H7.955v-1.503h2.77v-.93h-2.77v-1.224h2.978v-.934Zm2.146
 0h-1.084v5.52h1.035v-3.6l2.226
 3.6h1.118v-5.52h-1.036v3.686l-2.259-3.687Zm5.117 0h-1.208l1.973
 5.52h1.19l1.976-5.52h-1.182l-1.352 4.085-1.397-4.086ZM5.4
 19.68H3.72v1.68H5.4v-1.68Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/motdotla/dotenv/blob/40e75'''

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
        yield from [
            "Dotenv",
        ]
