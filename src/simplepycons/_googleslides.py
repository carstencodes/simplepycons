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


class GoogleSlidesIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "googleslides"

    @property
    def original_file_name(self) -> "str":
        return "googleslides.svg"

    @property
    def title(self) -> "str":
        return "Google Slides"

    @property
    def primary_color(self) -> "str":
        return "#FBBC04"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Google Slides</title>
     <path d="M16.09
 15.273H7.91v-4.637h8.18v4.637zm1.728-8.523h2.91v15.614c0 .904-.733
 1.636-1.637 1.636H4.909a1.636 1.636 0 0 1-1.636-1.636V1.636C3.273.732
 4.005 0 4.909 0h9.068v6.75h3.841zm-.363
 2.523H6.545v7.363h10.91V9.273zm-2.728-5.979V6h6.001l-6-6v3.294z" />
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
