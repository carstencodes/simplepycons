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


class FandomIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "fandom"

    @property
    def original_file_name(self) -> "str":
        return "fandom.svg"

    @property
    def title(self) -> "str":
        return "Fandom"

    @property
    def primary_color(self) -> "str":
        return "#FA005A"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Fandom</title>
     <path d="M8.123.008a.431.431 0 00-.512.42v9.746L4.104
 6.666a.432.432 0 00-.66.064.428.428 0 00-.071.239v10.064a2.387 2.387
 0 00.701 1.694l4.565 4.57a2.4 2.4 0 001.693.703h3.34c.635 0
 1.242-.252 1.691-.701l4.565-4.572a2.394 2.394 0
 00.699-1.694V13.41a2.39 2.39 0 00-.7-1.693L8.343.125a.427.427 0
 00-.219-.117zM9.646 12.51a.719.719 0 01.508.21l1.848 1.85
 1.844-1.85a.714.714 0 011.015 0l1.32 1.321a.724.724 0
 01.212.508v1.406a.72.72 0 01-.21.508l-3.68 3.7a.72.72 0 01-1.019
 0l-3.668-3.7a.716.716 0 01-.209-.506v-1.408a.71.71 0
 01.211-.506l1.32-1.322a.713.713 0 01.508-.211Z" />
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
