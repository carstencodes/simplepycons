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


class BlackmagicDesignIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "blackmagicdesign"

    @property
    def original_file_name(self) -> "str":
        return "blackmagicdesign.svg"

    @property
    def title(self) -> "str":
        return "Blackmagic Design"

    @property
    def primary_color(self) -> "str":
        return "#FFA200"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Blackmagic Design</title>
     <path d="M10.385 0c-1.15 0-2.076.93-2.076 2.076V5.31c0 1.148.929
 2.076 2.076 2.076h3.23c1.15 0 2.076-.93 2.076-2.076V2.076A2.074 2.074
 0 0 0 13.615 0h-3.23zm0 .924h3.23c.638 0 1.155.514 1.155 1.152V5.31c0
 .638-.516 1.152-1.155 1.152h-3.23A1.152 1.152 0 0 1 9.23
 5.309V2.076c0-.638.516-1.152 1.155-1.152zm0 7.385c-1.15
 0-2.076.929-2.076 2.076v3.23c0 1.15.929 2.076 2.076 2.076h3.23c1.15 0
 2.076-.929 2.076-2.076v-3.23c0-1.15-.929-2.076-2.076-2.076h-3.23zm0
 .921h3.23c.638 0 1.155.516 1.155 1.155v3.23c0 .638-.516 1.155-1.155
 1.155h-3.23a1.154 1.154 0 0 1-1.155-1.155v-3.23c0-.638.516-1.155
 1.155-1.155zm0 7.385c-1.15 0-2.076.93-2.076 2.076v3.233c0 1.149.929
 2.076 2.076 2.076h3.23c1.15 0 2.076-.93 2.076-2.076V18.69a2.075 2.075
 0 0 0-2.076-2.076h-3.23zm0 .924h3.23c.638 0 1.155.514 1.155
 1.152v3.233c0 .638-.516 1.152-1.155 1.152h-3.23a1.152 1.152 0 0
 1-1.155-1.152V18.69c0-.638.516-1.152 1.155-1.152Z" />
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
