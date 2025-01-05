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


class JuliaIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "julia"

    @property
    def original_file_name(self) -> "str":
        return "julia.svg"

    @property
    def title(self) -> "str":
        return "Julia"

    @property
    def primary_color(self) -> "str":
        return "#9558B2"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Julia</title>
     <path d="M11.138 17.569a5.569 5.569 0 1 1-11.138 0 5.569 5.569 0
 1 1 11.138 0zm6.431-11.138a5.569 5.569 0 1 1-11.138 0 5.569 5.569 0 1
 1 11.138 0zM24 17.569a5.569 5.569 0 1 1-11.138 0 5.569 5.569 0 1 1
 11.138 0z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/JuliaLang/julia-logo-graph
ics/blob/b5551ca7946b4a25746c045c15fbb8806610f8d0/images/julia-dots.sv'''

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
