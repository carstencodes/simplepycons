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


class CrystalIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "crystal"

    @property
    def original_file_name(self) -> "str":
        return "crystal.svg"

    @property
    def title(self) -> "str":
        return "Crystal"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Crystal</title>
     <path d="M23.964 15.266l-8.687
 8.669c-.034.035-.086.052-.121.035L3.29
 20.79c-.052-.017-.087-.052-.087-.086L.007 8.856c-.018-.053
 0-.087.035-.122L8.728.065c.035-.035.087-.052.121-.035l11.866
 3.18c.052.017.087.052.087.086l3.18
 11.848c.034.053.016.087-.018.122zm-11.64-9.433L.667 8.943c-.017
 0-.035.034-.017.052l8.53
 8.512c.017.017.052.017.052-.017l3.127-11.64c.017
 0-.018-.035-.035-.017Z" />
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
