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


class SpreakerIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "spreaker"

    @property
    def original_file_name(self) -> "str":
        return "spreaker.svg"

    @property
    def title(self) -> "str":
        return "Spreaker"

    @property
    def primary_color(self) -> "str":
        return "#F5C300"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Spreaker</title>
     <path d="M14.615 0l-5.64 6.54L.529 4.718l8.68 7.372-8.537 7.463
 8.411-1.984L14.843 24l.71-8.601 7.918-3.483-7.963-3.33L14.621
 0h-.006z" />
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
