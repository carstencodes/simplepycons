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


class PhonepeIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "phonepe"

    @property
    def original_file_name(self) -> "str":
        return "phonepe.svg"

    @property
    def title(self) -> "str":
        return "PhonePe"

    @property
    def primary_color(self) -> "str":
        return "#5F259F"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>PhonePe</title>
     <path d="M10.206
 9.941h2.949v4.692c-.402.201-.938.268-1.34.268-1.072
 0-1.609-.536-1.609-1.743V9.941zm13.47 4.816c-1.523 6.449-7.985
 10.442-14.433 8.919C2.794 22.154-1.199 15.691.324 9.243 1.847 2.794
 8.309-1.199 14.757.324c6.449 1.523 10.442 7.985 8.919
 14.433zm-6.231-5.888a.887.887 0 0
 0-.871-.871h-1.609l-3.686-4.222c-.335-.402-.871-.536-1.407-.402l-1.274.401c-.201.067-.268.335-.134.469l4.021
 3.82H6.386c-.201 0-.335.134-.335.335v.67c0
 .469.402.871.871.871h.938v3.217c0 2.413 1.273 3.82 3.418 3.82.67 0
 1.206-.067 1.877-.335v2.145c0 .603.469 1.072 1.072
 1.072h.938a.432.432 0 0 0 .402-.402V9.874h1.542c.201 0
 .335-.134.335-.335v-.67z" />
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
