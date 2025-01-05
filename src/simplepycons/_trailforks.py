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


class TrailforksIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "trailforks"

    @property
    def original_file_name(self) -> "str":
        return "trailforks.svg"

    @property
    def title(self) -> "str":
        return "Trailforks"

    @property
    def primary_color(self) -> "str":
        return "#FFCD00"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Trailforks</title>
     <path d="M12 1.608 0 22.392h24zm-1.292 5.698h2.584v5.885l2.664
 1.917v5.587h-2.204V16.05L12 14.788l-1.752
 1.262v4.645H8.044v-5.587l2.664-1.917z" />
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
