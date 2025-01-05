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


class BitwigIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "bitwig"

    @property
    def original_file_name(self) -> "str":
        return "bitwig.svg"

    @property
    def title(self) -> "str":
        return "Bitwig"

    @property
    def primary_color(self) -> "str":
        return "#FF5A00"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Bitwig</title>
     <path d="M4.15 7.782a1.59 1.59 0 1 1 3.181 0 1.59 1.59 0 0
 1-3.181 0zm5.741 1.591a1.59 1.59 0 1 0 0-3.181 1.59 1.59 0 0 0 0
 3.181zm4.218 0a1.59 1.59 0 1 0 0-3.181 1.59 1.59 0 0 0 0 3.181zm4.15
 0a1.59 1.59 0 1 0 0-3.181 1.59 1.59 0 0 0 0 3.181zM5.741 10.409a1.59
 1.59 0 1 0 0 3.181 1.59 1.59 0 0 0 0-3.181zm8.368 0a1.59 1.59 0 1 0 0
 3.181 1.59 1.59 0 0 0 0-3.181zm4.15 0a1.59 1.59 0 1 0 0 3.181 1.59
 1.59 0 0 0 0-3.181zm4.15 3.182a1.59 1.59 0 1 0 0-3.181 1.59 1.59 0 0
 0 0 3.181zM1.591 10.409a1.591 1.591 0 1 0 0 3.182 1.591 1.591 0 0 0
 0-3.182zm4.15 4.218a1.59 1.59 0 1 0 0 3.181 1.59 1.59 0 0 0
 0-3.181zm12.518 0a1.59 1.59 0 1 0 0 3.181 1.59 1.59 0 0 0
 0-3.181zm4.15 0a1.59 1.59 0 1 0 0 3.181 1.59 1.59 0 0 0
 0-3.181zm-20.818 0a1.59 1.59 0 1 0 0 3.181 1.59 1.59 0 0 0
 0-3.181m8.3-4.218a1.591 1.591 0 1 0 0 3.182 1.591 1.591 0 0 0
 0-3.182Z" />
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
