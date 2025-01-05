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


class TomtomIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "tomtom"

    @property
    def original_file_name(self) -> "str":
        return "tomtom.svg"

    @property
    def title(self) -> "str":
        return "TomTom"

    @property
    def primary_color(self) -> "str":
        return "#DF1B12"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>TomTom</title>
     <path d="M12 12.584a4.325 4.325 0 0 1-4.32-4.32A4.325 4.325 0 0 1
 12 3.944a4.325 4.325 0 0 1 4.32 4.32 4.325 4.325 0 0 1-4.32 4.32zM12
 0C7.443 0 3.736 3.707 3.736 8.264c0 4.557 3.707 8.264 8.264 8.264
 4.557 0 8.264-3.707 8.264-8.264C20.264 3.707 16.557 0 12 0m0 24
 3.167-5.486H8.833Z" />
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
