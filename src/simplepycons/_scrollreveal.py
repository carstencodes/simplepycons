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


class ScrollrevealIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "scrollreveal"

    @property
    def original_file_name(self) -> "str":
        return "scrollreveal.svg"

    @property
    def title(self) -> "str":
        return "ScrollReveal"

    @property
    def primary_color(self) -> "str":
        return "#FFCB36"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>ScrollReveal</title>
     <path d="M1.714 2.857A1.71 1.71 0 0 0 0 4.571v6.858c0 .95.765
 1.714 1.714 1.714a1.71 1.71 0 0 0 1.715-1.714V4.57a1.71 1.71 0 0
 0-1.715-1.714zm6.857 0a1.71 1.71 0 0 0-1.714 1.714v1.143c0 .95.765
 1.715 1.714 1.715a1.71 1.71 0 0 0 1.715-1.715V4.571A1.71 1.71 0 0 0
 8.57 2.857zm6.858 0a1.71 1.71 0 0 0-1.715 1.714V19.43c0 .95.765 1.714
 1.715 1.714a1.71 1.71 0 0 0 1.714-1.714V4.57a1.71 1.71 0 0
 0-1.714-1.714zm6.857 0a1.71 1.71 0 0 0-1.715 1.714v6.858c0 .95.765
 1.714 1.715 1.714A1.71 1.71 0 0 0 24 11.429V4.57a1.71 1.71 0 0
 0-1.714-1.714zm-13.715 8a1.71 1.71 0 0 0-1.714 1.714v6.858c0 .95.765
 1.714 1.714 1.714a1.71 1.71 0 0 0 1.715-1.714V12.57a1.71 1.71 0 0
 0-1.715-1.714zm-6.857 5.714A1.71 1.71 0 0 0 0 18.286v1.143c0 .95.765
 1.714 1.714 1.714a1.71 1.71 0 0 0 1.715-1.714v-1.143a1.71 1.71 0 0
 0-1.715-1.715zm20.572 0a1.71 1.71 0 0 0-1.715 1.715v1.143c0 .95.765
 1.714 1.715 1.714A1.71 1.71 0 0 0 24 19.429v-1.143a1.71 1.71 0 0
 0-1.714-1.715Z" />
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
