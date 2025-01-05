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


class MastercardIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "mastercard"

    @property
    def original_file_name(self) -> "str":
        return "mastercard.svg"

    @property
    def title(self) -> "str":
        return "MasterCard"

    @property
    def primary_color(self) -> "str":
        return "#EB001B"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>MasterCard</title>
     <path d="M11.343 18.031c.058.049.12.098.181.146-1.177.783-2.59
 1.238-4.107 1.238C3.32 19.416 0 16.096 0 12c0-4.095 3.32-7.416
 7.416-7.416 1.518 0 2.931.456 4.105 1.238-.06.051-.12.098-.165.15C9.6
 7.489 8.595 9.688 8.595 12c0 2.311 1.001 4.51 2.748
 6.031zm5.241-13.447c-1.52 0-2.931.456-4.105
 1.238.06.051.12.098.165.15C14.4 7.489 15.405 9.688 15.405 12c0
 2.31-1.001 4.507-2.748 6.031-.058.049-.12.098-.181.146 1.177.783
 2.588 1.238 4.107 1.238C20.68 19.416 24 16.096 24
 12c0-4.094-3.32-7.416-7.416-7.416zM12
 6.174c-.096.075-.189.15-.28.231C10.156 7.764 9.169 9.765 9.169 12c0
 2.236.987 4.236 2.551
 5.595.09.08.185.158.28.232.096-.074.189-.152.28-.232 1.563-1.359
 2.551-3.359 2.551-5.595
 0-2.235-.987-4.236-2.551-5.595-.09-.08-.184-.156-.28-.231z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://brand.mastercard.com/brandcenter/mast'''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://brand.mastercard.com/brandcenter/mast'''

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
