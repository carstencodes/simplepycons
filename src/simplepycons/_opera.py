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


class OperaIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "opera"

    @property
    def original_file_name(self) -> "str":
        return "opera.svg"

    @property
    def title(self) -> "str":
        return "Opera"

    @property
    def primary_color(self) -> "str":
        return "#FF1B2D"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Opera</title>
     <path d="M8.051 5.238c-1.328 1.566-2.186 3.883-2.246
 6.48v.564c.061 2.598.918 4.912 2.246 6.479 1.721 2.236 4.279 3.654
 7.139 3.654 1.756 0 3.4-.537 4.807-1.471C17.879 22.846 15.074 24 12
 24c-.192 0-.383-.004-.57-.014C5.064 23.689 0 18.436 0 12 0 5.371
 5.373 0 12 0h.045c3.055.012 5.84 1.166 7.953
 3.055-1.408-.93-3.051-1.471-4.81-1.471-2.858 0-5.417 1.42-7.14
 3.654h.003zM24 12c0 3.556-1.545 6.748-4.002 8.945-3.078
 1.5-5.946.451-6.896-.205 3.023-.664 5.307-4.32 5.307-8.74
 0-4.422-2.283-8.075-5.307-8.74.949-.654 3.818-1.703 6.896-.205C22.455
 5.25 24 8.445 24 12z" />
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
