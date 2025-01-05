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


class VoxIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "vox"

    @property
    def original_file_name(self) -> "str":
        return "vox.svg"

    @property
    def title(self) -> "str":
        return "VOX"

    @property
    def primary_color(self) -> "str":
        return "#DA074A"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>VOX</title>
     <path d="M0 8.198l4.182 7.604h2.442L8.15 13.07a4.276 4.276 0 0 1
 2.054-4.872H7.112l-1.677 3.216-1.706-3.216zm14.342 0a4.24 4.24 0 0 1
 1.923 2.206c.784 2.081-.098 4.415-2.145 5.398h2.767l1.564-1.754 1.42
 1.754H24l-3.505-4.032 3.088-3.572H19.41l-.952 1.249-.931-1.249zm-2.09
 1.596c-.949 0-1.913.69-2.074 1.775a2.132 2.132 0 0 0 2.064
 2.483c1.268.01 2.192-1.126
 2.156-2.18-.013-1.015-.877-2.08-2.146-2.078z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://commons.wikimedia.org/wiki/File:VOX_L'''

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
