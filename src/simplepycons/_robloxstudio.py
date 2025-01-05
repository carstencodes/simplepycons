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


class RobloxStudioIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "robloxstudio"

    @property
    def original_file_name(self) -> "str":
        return "robloxstudio.svg"

    @property
    def title(self) -> "str":
        return "Roblox Studio"

    @property
    def primary_color(self) -> "str":
        return "#00A2FF"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Roblox Studio</title>
     <path d="M 13.936 15.356 L 1.826 12.112 L 0 18.93 L 18.928 24 L
 21.608 14.01 L 14.79 12.18 L 13.936 15.356 Z M 5.072 0 L 2.394 9.992
 L 9.21 11.822 L 10.064 8.644 L 22.174 11.89 L 24 5.072 L 5.072 0 Z"
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
