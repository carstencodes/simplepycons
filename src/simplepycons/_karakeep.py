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


class KarakeepIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "karakeep"

    @property
    def original_file_name(self) -> "str":
        return "karakeep.svg"

    @property
    def title(self) -> "str":
        return "Karakeep"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Karakeep</title>
     <path d="M22.582.054H1.418C.635.054 0 .69 0 1.472v21.056c0
 .783.635 1.418 1.418 1.418h21.164c.783 0 1.418-.635
 1.418-1.418V1.472C24 .69 23.365.054 22.582.054M10.487 20.437a.37.37 0
 0 1-.37.37H3.592a.37.37 0 0 1-.37-.37V3.485a.37.37 0 0 1
 .37-.37h6.422a.37.37 0 0 1 .37.37v6.452s-.035 2.776.103 4.955zm10.188
 0a.371.371 0 0 1-.575.31l-2.975-1.945a.37.37 0 0 0-.42.01l-2.608
 1.887a.36.36 0 0 1-.345.042.37.37 0 0
 1-.159-.302V7.274c.353-.07.746-.106 1.2-.106 2.229 0 5.882 1.257
 5.882 4.81z" />
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
