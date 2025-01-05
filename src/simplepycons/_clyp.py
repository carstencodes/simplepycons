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


class ClypIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "clyp"

    @property
    def original_file_name(self) -> "str":
        return "clyp.svg"

    @property
    def title(self) -> "str":
        return "Clyp"

    @property
    def primary_color(self) -> "str":
        return "#3CBDB1"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Clyp</title>
     <path d="M11.9995 17.9583a1.137 1.137 0
 01-1.137-1.136V7.2347a1.138 1.138 0 012.275 0v9.5896c0 .626-.51
 1.134-1.138 1.134m7.4397 2.4398a1.137 1.137 0
 01-1.14-1.1379V4.7958a1.138 1.138 0 012.276 0v14.4654c0 .627-.51
 1.136-1.138 1.136M15.7193 24a1.137 1.137 0 01-1.138-1.136V1.138a1.138
 1.138 0 012.276 0v21.726c0 .627-.509 1.136-1.138
 1.136m-7.4366-3.1599a1.137 1.137 0 01-1.138-1.136V4.2979a1.138 1.138
 0 012.276 0v15.4064c0 .628-.51 1.137-1.138 1.137m-3.7199-4.9889a1.137
 1.137 0 01-1.138-1.135V9.2857a1.138 1.138 0 012.276 0v5.4318c0
 .626-.51 1.135-1.138 1.135z" />
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
