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


class FSharpIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "fsharp"

    @property
    def original_file_name(self) -> "str":
        return "fsharp.svg"

    @property
    def title(self) -> "str":
        return "F#"

    @property
    def primary_color(self) -> "str":
        return "#378BBA"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>F#</title>
     <path d="M0 12 11.39.61v5.695L5.695 12l5.695 5.695v5.695L0
 12zm7.322 0 4.068-4.068v8.136L7.322 12zM24 12 12.203.61v5.695L17.898
 12l-5.695 5.695v5.695L24 12z" />
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
        yield from [
            "F sharp",
        ]
