#
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2026 Carsten Igel.
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


class FreecadIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "freecad"

    @property
    def original_file_name(self) -> "str":
        return "freecad.svg"

    @property
    def title(self) -> "str":
        return "FreeCAD"

    @property
    def primary_color(self) -> "str":
        return "#418FDE"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>FreeCAD</title>
     <path d="M6 0h16v7.996a.7.7 0 0 1-.288.566l-2.173 1.58a.7.7 0 0
 0-.289.565v.586c0 .224.107.434.289.566l1.895 1.377a.7.7 0 0 1
 .254.783l-.649 1.997a.7.7 0 0 1-.665.484H18.03a.7.7 0 0
 0-.566.288l-.344.474a.7.7 0 0 0-.1.627l.724 2.229a.7.7 0 0
 1-.254.782l-1.699 1.234a.7.7 0 0 1-.823 0l-1.895-1.377a.7.7 0 0
 0-.628-.099l-.556.18a.7.7 0 0 0-.45.45l-.724 2.228a.7.7 0 0
 1-.665.484H2V4zm12 8V4H6v16h4v-5h4v-4h-4V8z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://fpa.freecad.org/handbook/process/logo'''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://fpa.freecad.org/handbook/process/logo'''

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
