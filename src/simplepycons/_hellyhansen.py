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


class HellyHansenIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "hellyhansen"

    @property
    def original_file_name(self) -> "str":
        return "hellyhansen.svg"

    @property
    def title(self) -> "str":
        return "Helly Hansen"

    @property
    def primary_color(self) -> "str":
        return "#DA2128"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Helly Hansen</title>
     <path d="M22.912 5.945a1.089 1.089 0 10-.002 2.178 1.089 1.089 0
 00.002-2.178zm.012.242a.85.85 0 110 1.7.85.85 0
 010-1.7zm-.332.375v.952h.18v-.352h.171l.184.352h.207l-.213-.385c.046-.017.19-.067.19-.28
 0-.166-.12-.287-.323-.287h-.396zm.18.157h.167c.124 0 .184.057.184.144
 0 .089-.065.143-.156.143h-.196v-.287zM0
 7.039v11.016h3.684v-3.78h3.523v3.78h1.42l2.15-11.016H7.221v3.854H3.695V7.039H0zm12.127
 0L9.988
 18.055h3.545V14.2h3.524v3.854h3.697V7.039H17.07v3.78h-3.525v-3.78h-1.418Z"
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
