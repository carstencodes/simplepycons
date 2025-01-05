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


class DtsIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "dts"

    @property
    def original_file_name(self) -> "str":
        return "dts.svg"

    @property
    def title(self) -> "str":
        return "DTS"

    @property
    def primary_color(self) -> "str":
        return "#F98B2B"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>DTS</title>
     <path d="m23.556 14.346-1.194-1.173a.841.841 0 0 1
 .604-1.445h.59a.346.346 0 0 0 .349-.343v-.636H18.97a1.492 1.492 0 0
 0-1.507 1.477v.003c0 .396.16.775.444 1.05l1.201 1.18a.841.841 0 0
 1-.604 1.446h-1.849a1.306 1.306 0 0
 1-1.317-1.294v-2.876h1.135a.346.346 0 0 0
 .35-.343v-.636h-1.485V7.587l-3.866
 1.66v1.494h-1.87V7.123h-2.87a.986.986 0 0 0-.997.98v2.638H3.67C1.514
 10.741 0 11.893 0 13.81c0 1.71 1.776 3.068 3.676 3.068h4.615a1.306
 1.306 0 0 0 1.318-1.294v-3.855h1.863v2.503c0 1.423.874 2.646 2.65
 2.646h8.371A1.492 1.492 0 0 0 24 15.4v-.003a1.444 1.444 0 0
 0-.444-1.051zM5.729 15.683a.217.217 0 0 1-.219.214h-.13c-1.34
 0-1.835-.908-1.85-2.088.015-1.216.525-2.088 1.85-2.088h.349v3.962z"
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
