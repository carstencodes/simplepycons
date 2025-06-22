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


class MyshowsIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "myshows"

    @property
    def original_file_name(self) -> "str":
        return "myshows.svg"

    @property
    def title(self) -> "str":
        return "MyShows"

    @property
    def primary_color(self) -> "str":
        return "#CC0000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>MyShows</title>
     <path d="M5.94
 1.897c-.375.189-.81.117-1.14-.213-.421-.42-.421-1.01 0-1.431a1.14
 1.14 0 0 1 1.432 0c.33.33.401.764.213 1.139l3.323 3.324.032.033a3.247
 3.247 0 0 1 2.242-.875c.857 0 1.615.316
 2.189.843v-.001l3.297-3.225c-.256-.395-.203-.879.156-1.238.421-.337
 1.095-.337 1.432 0 .42.42.42 1.01 0
 1.431-.297.297-.676.384-1.022.264L14.821 5.22a.524.524 0 0
 1-.093.076c.327.482.539 1.06.598
 1.692H8.842c0-.635.185-1.217.505-1.701a.48.48 0 0 1-.084-.067zM4.883
 24C2.442 24 .421 21.979.421 19.537v-7.242c0-2.442 2.021-4.463
 4.463-4.463h14.232c2.442 0 4.463 2.02 4.463 4.463v7.242c0 2.442-2.021
 4.463-4.463 4.463ZM3.032 13.137v5.642c0 1.347 1.094 2.526 2.526
 2.526h12.968c1.348 0 2.527-1.094
 2.527-2.526v-5.642c0-1.348-1.095-2.526-2.527-2.526H5.558c-1.432
 0-2.526 1.094-2.526 2.526z" />
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
