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


class NokiaIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "nokia"

    @property
    def original_file_name(self) -> "str":
        return "nokia.svg"

    @property
    def title(self) -> "str":
        return "Nokia"

    @property
    def primary_color(self) -> "str":
        return "#005AFF"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Nokia</title>
     <path d="M16.59 9.348v5.304h.796V9.348Zm-8.497-.09c-1.55 0-2.752
 1.127-2.752 2.742 0 1.687 1.202 2.742 2.752 2.742 1.55 0 2.754-1.055
 2.751-2.742a2.72 2.72 0 0 0-2.751-2.742ZM10.05 12c0 1.195-.876
 1.987-1.957 1.987-1.082 0-1.958-.792-1.958-1.987 0-1.174.876-1.987
 1.958-1.987 1.08 0 1.957.813 1.957 1.987zM0
 9.176v5.476h.812v-3.619l4.218 3.79v-1.135zM11.442 12l2.952
 2.652h1.184L12.622 12l2.956-2.652h-1.184ZM24
 14.652h-.875l-.64-1.175h-2.898l-.64
 1.175h-.875l1.06-1.958h2.937l-1.465-2.72.432-.798Z" />
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
