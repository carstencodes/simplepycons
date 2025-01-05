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


class BitcoinSvIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "bitcoinsv"

    @property
    def original_file_name(self) -> "str":
        return "bitcoinsv.svg"

    @property
    def title(self) -> "str":
        return "Bitcoin SV"

    @property
    def primary_color(self) -> "str":
        return "#EAB300"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Bitcoin SV</title>
     <path d="M14.648 14.423l.003-.004a1.34 1.34 0 0
 1-.498.659c-.269.189-.647.338-1.188.364l-1.99.004v-2.93c.288.008
 1.565-.013 2.119.015.722.035 1.171.321 1.41.668.262.351.293.82.144
 1.224zm-2.129-3.261c.503-.024.852-.162
 1.101-.336.214-.146.375-.367.46-.611.134-.375.107-.81-.136-1.135-.223-.319-.638-.584-1.306-.616-.495-.026-1.413-.003-1.664-.01v2.709c.025.004
 1.539-.001 1.545-.001zM24 12c0 6.627-5.373 12-12 12S0 18.627 0 12
 5.373 0 12 0s12 5.373 12 12zm-6.65
 2.142c.022-1.477-1.24-2.332-1.908-2.572.715-.491 1.206-1.043
 1.206-2.085
 0-1.655-1.646-2.43-2.647-2.529-.082-.009-.31-.013-.31-.013V5.361h-1.633l.004
 1.583H10.97V5.367H9.31v1.569c-.292.007-2.049.006-2.049.006v1.401h.571c.601.016.822.362.798.677v6.041a.408.408
 0 0 1-.371.391c-.249.011-.621 0-.621 0l-.32
 1.588h1.996v1.6h1.661v-1.591h1.091v1.594h1.624v-1.588c1.899.05
 3.643-1.071 3.66-2.913z" />
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
