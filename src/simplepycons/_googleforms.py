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


class GoogleFormsIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "googleforms"

    @property
    def original_file_name(self) -> "str":
        return "googleforms.svg"

    @property
    def title(self) -> "str":
        return "Google Forms"

    @property
    def primary_color(self) -> "str":
        return "#7248B9"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Google Forms</title>
     <path d="M14.727 6h6l-6-6v6zm0 .727H14V0H4.91c-.905
 0-1.637.732-1.637 1.636v20.728c0 .904.732 1.636 1.636
 1.636h14.182c.904 0 1.636-.732 1.636-1.636V6.727h-6zM7.91
 17.318a.819.819 0 1 1 .001-1.638.819.819 0 0 1 0
 1.638zm0-3.273a.819.819 0 1 1 .001-1.637.819.819 0 0 1 0
 1.637zm0-3.272a.819.819 0 1 1 .001-1.638.819.819 0 0 1 0 1.638zm9
 6.409h-6.818v-1.364h6.818v1.364zm0-3.273h-6.818v-1.364h6.818v1.364zm0-3.273h-6.818V9.273h6.818v1.363z"
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
