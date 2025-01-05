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


class CommonLispIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "commonlisp"

    @property
    def original_file_name(self) -> "str":
        return "commonlisp.svg"

    @property
    def title(self) -> "str":
        return "Common Lisp"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Common Lisp</title>
     <path d="M11.445 23.987A12.001 12 0 1 1 15.005.382a12.013 12.013
 0 0 1 6.217 3.938 11.96 11.958 0 0 1 2.376 4.59c.47 1.773.53 3.642.17
 5.442a11.981 11.98 0 0 1-6.12 8.238 12.036 12.035 0 0 1-6.203
 1.397zm5.234-2.038a5.8 5.8 0 0 0 3.1-1.236c.647-.518 1.446-1.436
 2.029-2.33a11.688 11.687 0 0 0 1.847-7.41A11.68 11.678 0 0 0 19.64
 3.14 11.674 11.673 0 0 0
 11.796.304c-.232.004-.506.013-.61.02-1.636.117-3.1.506-4.48
 1.192-.26.13-.637.333-.63.34a.845.845 0 0 0 .116-.028 6.114 6.113 0 0
 1 3.78.241 6.235 6.234 0 0 1 2.68 2.036 6.075 6.074 0 0 1 1.19
 3.007c.027.238.038.84.02 1.088a6.082 6.081 0 0 1-1.236 3.27 6.615
 6.614 0 0 1-.546.625c-.507.53-.802.941-1.089 1.516a5.81 5.81 0 0
 0-.15 4.817 5.795 5.794 0 0 0 5.837
 3.521zm-3.848-5.028c.098-.192.429-.825.735-1.406.845-1.607 1.083-2.08
 1.375-2.74.768-1.73
 1.033-3.038.87-4.302-.156-1.22-.756-2.427-1.79-3.604a3.234 3.234 0 0
 1-.147-.173c0-.003.45-.005 1.002-.003l1.002.003.063.1a78.36 78.36 0 0
 1 1.257 2.133c1.817 3.212 3.136 6.344 4.212
 10.001l.098.324c.005.013-.2.016-1.003.016h-1.007l-.008-.035c-.292-1.237-.728-2.572-1.36-4.16a55.634
 55.628 0 0 0-.684-1.655c-.004 0-.014.022-.023.047l-.178.456c-.853
 2.176-1.658 3.854-2.512 5.237l-.068.11h-2.013Zm-2.985 2.255a.98.98 0
 0
 0-.073-.09c-.69-.81-1.193-1.665-1.468-2.489-.434-1.305-.385-2.615.162-4.227.316-.933.743-1.843
 1.822-3.887.514-.974.84-1.602.84-1.62
 0-.005-.39-.01-.866-.01h-.865l-.17.287c-.878 1.47-1.666 3.16-2.565
 5.504-.073.19-.11.268-.116.255a95.92 95.92 0 0 1-.72-1.736C5.203 9.61
 4.762 8.3 4.462 7.1l-.06-.239-.875-.003-.876-.003.044.148c.71 2.397
 1.5 4.524 2.427 6.532.82 1.777 1.762 3.512 3.037
 5.595l.032.054h.828c.455 0 .827-.003.827-.006z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://commons.wikimedia.org/wiki/File:Lisp_'''

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
