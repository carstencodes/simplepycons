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


class CssIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "css"

    @property
    def original_file_name(self) -> "str":
        return "css.svg"

    @property
    def title(self) -> "str":
        return "CSS"

    @property
    def primary_color(self) -> "str":
        return "#663399"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>CSS</title>
     <path d="M0 0v20.16A3.84 3.84 0 0 0 3.84 24h16.32A3.84 3.84 0 0 0
 24 20.16V3.84A3.84 3.84 0 0 0 20.16 0Zm14.256 13.08c1.56 0 2.28 1.08
 2.304
 2.64h-1.608c.024-.288-.048-.6-.144-.84-.096-.192-.288-.264-.552-.264-.456
 0-.696.264-.696.84-.024.576.288.888.768 1.08.72.288 1.608.744 1.92
 1.296q.432.648.432 1.656c0 1.608-.912 2.592-2.496 2.592-1.656
 0-2.4-1.032-2.424-2.688h1.68c0 .792.264 1.176.792 1.176.264 0
 .456-.072.552-.24.192-.312.24-1.176-.048-1.512-.312-.408-.912-.6-1.32-.816q-.828-.396-1.224-.936c-.24-.36-.36-.888-.36-1.536
 0-1.44.936-2.472 2.424-2.448m5.4 0c1.584 0 2.304 1.08 2.328
 2.64h-1.608c0-.288-.048-.6-.168-.84-.096-.192-.264-.264-.528-.264-.48
 0-.72.264-.72.84s.288.888.792 1.08c.696.288 1.608.744 1.92
 1.296.264.432.408.984.408 1.656.024 1.608-.888 2.592-2.472 2.592-1.68
 0-2.424-1.056-2.448-2.688h1.68c0 .744.264 1.176.792 1.176.264 0
 .456-.072.552-.24.216-.312.264-1.176-.048-1.512-.288-.408-.888-.6-1.32-.816-.552-.264-.96-.576-1.2-.936s-.36-.888-.36-1.536c-.024-1.44.912-2.472
 2.4-2.448m-11.031.018c.711-.006 1.419.198 1.839.63.432.432.672
 1.128.648
 1.992H9.336c.024-.456-.096-.792-.432-.96-.312-.144-.768-.048-.888.24-.12.264-.192.576-.168.864v3.504c0
 .744.264 1.128.768 1.128a.65.65 0 0 0
 .552-.264c.168-.24.192-.552.168-.84h1.776c.096 1.632-.984 2.712-2.568
 2.688-1.536
 0-2.496-.864-2.472-2.472v-4.032c0-.816.24-1.44.696-1.848.432-.408
 1.146-.624 1.857-.63" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/CSS-Next/logo.css/blob/bac'''

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
