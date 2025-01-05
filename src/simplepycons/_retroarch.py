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


class RetroarchIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "retroarch"

    @property
    def original_file_name(self) -> "str":
        return "retroarch.svg"

    @property
    def title(self) -> "str":
        return "RetroArch"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>RetroArch</title>
     <path d="M6.84 5.76L8.4 7.68H5.28l-.72 2.88H2.64l.72-2.88H1.44L0
 13.44h3.84l-.48 1.92h3.36L4.2 18.24h2.82l2.34-2.88h5.28l2.34
 2.88h2.82l-2.52-2.88h3.36l-.48-1.92H24l-1.44-5.76h-1.92l.72
 2.88h-1.92l-.72-2.88H15.6l1.56-1.92h-2.04l-1.68 1.92h-2.88L8.88
 5.76zm.24 3.84H9v1.92H7.08zm7.925 0h1.92v1.92h-1.92Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/libretro/RetroArch/blob/b0'''

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
