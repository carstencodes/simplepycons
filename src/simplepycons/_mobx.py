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


class MobxIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "mobx"

    @property
    def original_file_name(self) -> "str":
        return "mobx.svg"

    @property
    def title(self) -> "str":
        return "MobX"

    @property
    def primary_color(self) -> "str":
        return "#FF9955"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>MobX</title>
     <path d="M1.402 0C.625 0 0 .625 0 1.402v21.196C0 23.375.625 24
 1.402 24h21.196c.777 0 1.402-.625 1.402-1.402V1.402C24 .625 23.375 0
 22.598 0zm2.882
 5.465h3.038v13.068H4.284v-.986h1.863V6.45H4.284zm12.394
 0h3.038v.985h-1.863v11.098h1.863v.986h-3.038zm-7.856
 3.55h1.35c.108.441.234.914.378 1.418.153.495.31.99.472
 1.485.171.486.342.958.513 1.417.171.46.333.869.486
 1.229.153-.36.315-.77.486-1.229.171-.459.338-.931.5-1.417.17-.495.328-.99.472-1.485.153-.504.284-.977.392-1.418h1.296a34.295
 34.295 0 0 1-1.242 3.78 56.44 56.44 0 0 1-1.364 3.24h-1.134a63.191
 63.191 0 0 1-1.377-3.24 36.226 36.226 0 0 1-1.228-3.78Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/mobxjs/mobx/blob/248e25e37'''

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
