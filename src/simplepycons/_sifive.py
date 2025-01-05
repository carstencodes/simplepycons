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


class SifiveIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "sifive"

    @property
    def original_file_name(self) -> "str":
        return "sifive.svg"

    @property
    def title(self) -> "str":
        return "SiFive"

    @property
    def primary_color(self) -> "str":
        return "#252323"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>SiFive</title>
     <path d="M2.9056 12.4076 6.0245 2.737h11.9511l1.2129
 3.7623H8.6317l-.6751 2.1342h11.92l1.792 5.5583L12
 21.319l-9.1888-6.7771h6.2049l2.9565 2.1805
 5.8505-4.3125-14.9175-.0023zM19.4166.4426H4.5835L0 14.7306l12 8.8268
 12-8.8298L19.4165.4427z" />
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
