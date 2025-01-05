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


class MarkdownIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "markdown"

    @property
    def original_file_name(self) -> "str":
        return "markdown.svg"

    @property
    def title(self) -> "str":
        return "Markdown"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Markdown</title>
     <path d="M22.27 19.385H1.73A1.73 1.73 0 010 17.655V6.345a1.73
 1.73 0 011.73-1.73h20.54A1.73 1.73 0 0124 6.345v11.308a1.73 1.73 0
 01-1.73 1.731zM5.769 15.923v-4.5l2.308 2.885
 2.307-2.885v4.5h2.308V8.078h-2.308l-2.307
 2.885-2.308-2.885H3.46v7.847zM21.232
 12h-2.309V8.077h-2.307V12h-2.308l3.461 4.039z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/dcurtis/markdown-mark/tree'''

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
