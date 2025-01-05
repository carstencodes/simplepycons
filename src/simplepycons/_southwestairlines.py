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


class SouthwestAirlinesIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "southwestairlines"

    @property
    def original_file_name(self) -> "str":
        return "southwestairlines.svg"

    @property
    def title(self) -> "str":
        return "Southwest Airlines"

    @property
    def primary_color(self) -> "str":
        return "#304CB2"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Southwest Airlines</title>
     <path d="M22.163 2.419C21.038 1.219 19.35.58 17.437.58c-2.062
 0-3.637.675-4.725 1.275 2.063 1.163 6.526 3.75 11.175
 7.163.075-.45.113-.938.113-1.388-.038-2.175-.675-4.012-1.837-5.212zm1.35
 8.212C18.186 6.244 15 4.031 11.55 1.97 10.612 1.406 8.775.58 6.675.58
 4.688.581 3 1.22 1.837 2.42 1.087 3.206.563 4.18.262 5.38 3 7.294
 10.462 12.656 18 18.581c2.512-2.362 4.613-5.1 5.512-7.95zM0 7.781c0
 6.15 6.487 11.85 12 15.638 1.575-1.088 3.225-2.325 4.8-3.713A736.871
 736.871 0 0 0 .15 6.131C.038 6.62 0 7.181 0 7.781Z" />
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
