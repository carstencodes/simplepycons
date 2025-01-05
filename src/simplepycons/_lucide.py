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


class LucideIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "lucide"

    @property
    def original_file_name(self) -> "str":
        return "lucide.svg"

    @property
    def title(self) -> "str":
        return "Lucide"

    @property
    def primary_color(self) -> "str":
        return "#F56565"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Lucide</title>
     <path d="M18.483 1.123a1.09 1.09 0 0 0-.752.362 1.09 1.09 0 0 0
 .088 1.54 11.956 11.956 0 0 1 4 8.946 7.62 7.62 0 0 1-7.637 7.636
 7.62 7.62 0 0 1-7.637-7.636 3.255 3.255 0 0 1 3.273-3.273c1.82 0
 3.273 1.45 3.273 3.273a1.09 1.09 0 0 0 1.09 1.09 1.09 1.09 0 0 0
 1.092-1.09c0-3-2.455-5.455-5.455-5.455s-5.454 2.455-5.454 5.455c0
 5.408 4.408 9.818 9.818 9.818 5.41 0 9.818-4.41 9.818-9.818A14.16
 14.16 0 0 0 19.272 1.4a1.09 1.09 0 0 0-.789-.277ZM9.818 2.15C4.408
 2.151 0 6.561 0 11.97a14.16 14.16 0 0 0 4.8 10.637 1.09 1.09 0 0 0
 1.54-.096 1.09 1.09 0 0 0-.095-1.54 11.957 11.957 0 0 1-4.063-9 7.62
 7.62 0 0 1 7.636-7.637 7.62 7.62 0 0 1 7.637 7.636 3.256 3.256 0 0
 1-3.273 3.273 3.256 3.256 0 0 1-3.273-3.273 1.09 1.09 0 0 0-1.09-1.09
 1.09 1.09 0 0 0-1.092 1.09c0 3 2.455 5.455 5.455 5.455s5.454-2.455
 5.454-5.455c0-5.408-4.408-9.818-9.818-9.818z" />
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
