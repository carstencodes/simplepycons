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


class MoonrepoIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "moonrepo"

    @property
    def original_file_name(self) -> "str":
        return "moonrepo.svg"

    @property
    def title(self) -> "str":
        return "Moonrepo"

    @property
    def primary_color(self) -> "str":
        return "#6F53F3"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Moonrepo</title>
     <path d="M 19.514 7.342 C 19.711 7.862 19.814 8.413 19.816 8.969
 C 19.816 12.494 15.998 14.697 12.946 12.934 C 11.529 12.116 10.657
 10.605 10.657 8.969 C 10.657 5.646 14.085 3.431 17.115 4.793 C 15.26
 3.373 12.99 2.607 10.655 2.612 C 4.772 2.614 0.005 7.381 0 13.265 C
 0.002 19.148 4.772 23.918 10.655 23.92 C 16.538 23.916 21.306 19.147
 21.31 13.265 C 21.312 11.155 20.687 9.095 19.514 7.342 Z M 14.841
 4.666 C 14.841 8.191 18.657 10.395 21.709 8.632 C 23.127 7.814 24
 6.302 24 4.666 C 24 1.14 20.184 -1.061 17.13 0.699 C 15.714 1.519
 14.841 3.03 14.841 4.666" />
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
