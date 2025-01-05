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


class NsisIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "nsis"

    @property
    def original_file_name(self) -> "str":
        return "nsis.svg"

    @property
    def title(self) -> "str":
        return "NSIS"

    @property
    def primary_color(self) -> "str":
        return "#01B0F0"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>NSIS</title>
     <path d="M13.736 24H24l-5.132-4.919L13.736 24Zm-6.021-5.064 5.133
 4.918
 5.132-4.919-10.265.001Zm-6.539-5.272v9.838l5.132-4.919-1.503-1.441-3.629-3.478Zm21.648-1.626-5.132
 4.919 5.132 4.919v-9.838Zm-4.844 6.193-5.132-4.92-5.132
 4.92H17.98ZM1.696 13.165l5.132 4.92
 5.132-4.92H1.696Zm20.608-1.625H12.039l5.133 4.919 5.132-4.919ZM6.828
 7.541l-5.132 4.92H11.96l-5.132-4.92Zm-5.652 4.421
 5.132-4.919-5.132-4.919v9.838Zm21.128-1.127-5.132-4.92-5.133
 4.92h10.265Zm-6.02-5.065H6.02l5.132 4.919
 5.132-4.919Zm6.54-5.272-5.132 4.919 5.132 4.92V.498Zm-6.539
 4.567L11.152.146 6.02 5.065h10.265ZM10.264 0H0l5.132 4.919L10.264 0Z"
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
        return '''https://github.com/idleberg/nsis-logo/blob/88
5ba2fd08a6ff450c6f7cbd675563b5df728d38/src/Logo/below%2024x24/mono-fla'''

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
            "Nullsoft Scriptable Install System",
        ]
