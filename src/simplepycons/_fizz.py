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


class FizzIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "fizz"

    @property
    def original_file_name(self) -> "str":
        return "fizz.svg"

    @property
    def title(self) -> "str":
        return "Fizz"

    @property
    def primary_color(self) -> "str":
        return "#00D672"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Fizz</title>
     <path d="M5.822
 17.813h3.274v-7.228H5.822Zm4.298-7.228v2.841h2.107l-2.243
 4.387h6.779v-2.824h-2.24l2.24-4.399h-6.644v-.005zm13.88
 0h-6.762v2.841h2.241l-2.24 4.387h6.633v-2.824H21.76ZM6.633
 6.966l-1.23 2.736a1.587 1.587 0 0 0-.955-.324c-.56 0-1.012.363-1.012
 1.125v.038H5.13v2.858H3.43v4.414H0v-7.804c0-2.292 1.737-3.822
 3.895-3.822 1.056 0 2.023.351 2.738.779z" />
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
