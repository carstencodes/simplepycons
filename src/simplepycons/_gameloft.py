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


class GameloftIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "gameloft"

    @property
    def original_file_name(self) -> "str":
        return "gameloft.svg"

    @property
    def title(self) -> "str":
        return "Gameloft"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Gameloft</title>
     <path d="M.841 18.938c.494.86 1.247 1.262 2.192 1.368 3.394.387
 13.519.176 13.534.176 2.402 0 4.33-1.1
 4.852-3.372.133-.579.238-2.54.117-4.619-.126-2.16-1.11-3.587-4.048-3.787-3.901-.264-9.42-.14-11.651.09-1.193.124-1.887.939-1.872
 2.05.036 2.647.065 3.054.093 3.197 1.185.17 1.17.18
 1.206.116.21-.385.596-.642 1.032-.688.503-.066.124-.046
 10.598-.205.41 0 .653.185.729.588.086.522.102 1.054.047
 1.58-.034.45-.404 1.166-1.08 1.175-.015
 0-7.503.035-11.076-.13-1.08-.05-2.263-1.114-2.263-3.094 0-.841
 0-3.548.07-4.39A2.235 2.235 0 0 1 5.174 6.96c1.333-.242 13.753-.095
 14.542.085 2.241.513 2.43 3.198 2.437 3.255.21 1.543.23 3.283.211
 4.855-.046 3.548-1.371 4.327-1.814 4.84-.133.154.039.225.3.415
 1.115-.209 2.708-1.427
 3.02-4.011.12-.999.213-3.283.02-7.382-.125-2.661-1.243-4.954-4.952-5.376-3.217-.366-10.3-.074-13.482
 0C-.097 3.767.008 6.937.006 8.229c-.021 8.174-.014 9.233.836 10.709Z"
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
