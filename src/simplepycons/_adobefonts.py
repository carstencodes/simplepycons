#
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2024 Carsten Igel.
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


class AdobeFontsIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "adobefonts"

    @property
    def original_file_name(self) -> "str":
        return "adobefonts.svg"

    @property
    def title(self) -> "str":
        return "Adobe Fonts"

    @property
    def primary_color(self) -> "str":
        return "#000B1D"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Adobe Fonts</title>
     <path d="M19.764.375H4.236A4.236 4.236 0 0 0 0 4.611V19.39a4.236
 4.236 0 0 0 4.236 4.236h15.528A4.236 4.236 0 0 0 24 19.389V4.61A4.236
 4.236 0 0 0 19.764.375zm-3.25 6.536c-.242
 0-.364-.181-.44-.439-.257-.97-.59-1.257-.787-1.257s-.5.364-.833
 1.12c-.417.97-.754 1.97-1.007
 2.994l1.732-.002c.11.28.01.6-.238.772H13.23c-.56 1.878-1.031
 3.688-1.592 5.46a9.676 9.676 0 0 1-1.105 2.56 3.144 3.144 0 0 1-2.484
 1.332c-.773 0-1.53-.363-1.53-1.166.036-.503.424-.91.924-.97a.46.46 0
 0 1 .424.243c.379.682.742 1.075.909 1.075.166 0
 .303-.227.575-1.211l1.988-7.322-1.43-.002a.685.685 0 0 1
 .227-.774h1.423c.257-.895.609-1.76 1.048-2.58a3.786 3.786 0 0 1
 3.272-2.195c1.136 0 1.605.545 1.605 1.242a1.144 1.144 0 0 1-.97
 1.12z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://developer.adobe.com/developer-distrib'''
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
