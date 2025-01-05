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


class CbsIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "cbs"

    @property
    def original_file_name(self) -> "str":
        return "cbs.svg"

    @property
    def title(self) -> "str":
        return "CBS"

    @property
    def primary_color(self) -> "str":
        return "#033963"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>CBS</title>
     <path d="M12 24C5.314 24 .068 18.587.068 11.949.068 5.413 5.314 0
 12 0s11.932 5.413 11.932 11.949C23.932 18.587 18.686 24 12
 24zm0-5.106c5.452 0 9.36-3.473 11.109-6.945C21.875 9.294 18.172 5.106
 12 5.106c-5.452 0-9.36 3.37-11.109 6.843C2.537 15.42 6.548 18.894 12
 18.894zm0-.613c-3.497 0-6.377-2.86-6.377-6.332S8.503 5.617 12
 5.617s6.377 2.86 6.377 6.332c0 3.574-2.88 6.332-6.377 6.332Z" />
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
