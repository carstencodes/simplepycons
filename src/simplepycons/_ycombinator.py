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


class YCombinatorIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "ycombinator"

    @property
    def original_file_name(self) -> "str":
        return "ycombinator.svg"

    @property
    def title(self) -> "str":
        return "Y Combinator"

    @property
    def primary_color(self) -> "str":
        return "#F0652F"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Y Combinator</title>
     <path d="M0 24V0h24v24H0zM6.951 5.896l4.112
 7.708v5.064h1.583v-4.972l4.148-7.799h-1.749l-2.457
 4.875c-.372.745-.688 1.434-.688 1.434s-.297-.708-.651-1.434L8.831
 5.896h-1.88z" />
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
