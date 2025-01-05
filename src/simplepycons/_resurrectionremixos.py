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


class ResurrectionRemixOsIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "resurrectionremixos"

    @property
    def original_file_name(self) -> "str":
        return "resurrectionremixos.svg"

    @property
    def title(self) -> "str":
        return "Resurrection Remix OS"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Resurrection Remix OS</title>
     <path d="M24 3.53l-9.952.078C9.142 3.647 6.994 8.265 0
 16.345c1.569.753 3.323 1.24 4.338.119 1.703-1.883 4.275-5.48
 7.154-8.346 1.793-1.784 6.01-.865 9.95-1.23 1.351-.125 2.41-2.48
 2.558-3.359zm-.147 6.076l-7.326.044c-4.39 0-5.38 2.492-11.91 10.24
 1.194.563 3.28.84 3.763.257 1.78-2.158 2.506-3.51 5.36-6.362
 1.657-1.658 4.39-.687 7.86-1.01 1.267-.12 2.132-2.449 2.253-3.169z"
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
        return '''https://avatars.githubusercontent.com/u/49319'''

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
