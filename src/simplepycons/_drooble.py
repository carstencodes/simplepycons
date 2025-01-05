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


class DroobleIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "drooble"

    @property
    def original_file_name(self) -> "str":
        return "drooble.svg"

    @property
    def title(self) -> "str":
        return "Drooble"

    @property
    def primary_color(self) -> "str":
        return "#19C4BE"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Drooble</title>
     <path d="M24 11.986a7.599 7.599 0 0 0-7-7.559v7.574a5 5 0 0 1-10
 0c0-3.604 3.707-6.022 7-4.583V.17C6.615-1.069 0 4.63 0 12c0 6.628
 5.373 12 12 12 6.628 0 12-5.372 12-12v-.014m-14 .015a2 2 0 1 0 4 0 2
 2 0 0 0-4 0m14-.015a7.599 7.599 0 0 0-7-7.559v7.574a5 5 0 0 1-10
 0c0-3.604 3.707-6.022 7-4.583V.17C6.615-1.069 0 4.63 0 12c0 6.628
 5.373 12 12 12 6.628 0 12-5.372 12-12v-.014m-14 .015a2 2 0 1 0 4 0 2
 2 0 0 0-4 0Z" />
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
