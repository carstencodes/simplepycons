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


class TheMightyIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "themighty"

    @property
    def original_file_name(self) -> "str":
        return "themighty.svg"

    @property
    def title(self) -> "str":
        return "The Mighty"

    @property
    def primary_color(self) -> "str":
        return "#D0072A"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>The Mighty</title>
     <path d="M19.178.001h-4.432L12.05 13.988
 9.309.001H4.856c.216.219.334.634.39 1.072v21.21c0 .621-.105
 1.383-.425 1.717 1.014-.214 2.307-.416 3.414-.611V9.375l2.489
 12.375c.07.46.135 1.084-.021 1.198.847-.129 1.694-.252
 2.544-.366-.105-.16-.064-.652-.005-1.061L15.696
 9.15v13.095c1.054-.123 2.366-.24
 3.47-.349l.012-.008c-.324-.328-.43-1.1-.43-1.724V1.726c0-.627.105-1.396.43-1.726v.001z"
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
