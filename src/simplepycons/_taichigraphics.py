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


class TaichiGraphicsIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "taichigraphics"

    @property
    def original_file_name(self) -> "str":
        return "taichigraphics.svg"

    @property
    def title(self) -> "str":
        return "Taichi Graphics"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Taichi Graphics</title>
     <path d="M19.343 20.672a1.94 1.94 0 0 0 1.94-1.94 1.94 1.94 0 1
 0-3.88 0 1.94 1.94 0 0 0 1.94 1.94zM9.058 12.796a6.858 6.858 0 1
 0-2.324-9.67c-.062.099-.125.198-.185.3-.06.103-.11.205-.167.31a6.858
 6.858 0 0 0 2.676 9.06zm0-.003h-4.23l-2.113 3.663 2.114
 3.667h4.229l2.116-3.667zm0 7.33L6.82 23.999h4.48Z" />
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
