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


class FccIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "fcc"

    @property
    def original_file_name(self) -> "str":
        return "fcc.svg"

    @property
    def title(self) -> "str":
        return "FCC"

    @property
    def primary_color(self) -> "str":
        return "#1C3664"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>FCC</title>
     <path d="M21.412 17.587A7.89 7.89 0 0 1 10.268 6.414a7.867 7.867
 0 0 1 11.144 0 8 8 0 0 1 .839.996L24 6.116a10.03 10.03 0 0
 0-8.16-4.196c-5.19 0-9.458 3.942-9.996 9.002h-3.82V4.328H6.78L8.508
 1.92H0v20.16l2.024-1.488V13.08h3.82c.538 5.059 4.806 9 9.996 9A10.03
 10.03 0 0 0 24 17.884l-1.749-1.296a8 8 0 0 1-.84.999m-5.57-9.205a3.61
 3.61 0 0 1 2.97 1.572l1.752-1.296a5.77 5.77 0 0 0-4.723-2.456c-3.194
 0-5.782 2.595-5.782 5.798s2.588 5.796 5.782 5.797a5.77 5.77 0 0 0
 4.723-2.455l-1.751-1.296a3.61 3.61 0 1 1-2.972-5.664" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://apps.fcc.gov/oetcf/kdb/forms/FTSSearc'''
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
        yield from [
            "Federal Communications Commission",
        ]
