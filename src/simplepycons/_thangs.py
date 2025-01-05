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


class ThangsIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "thangs"

    @property
    def original_file_name(self) -> "str":
        return "thangs.svg"

    @property
    def title(self) -> "str":
        return "Thangs"

    @property
    def primary_color(self) -> "str":
        return "#FFBC00"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Thangs</title>
     <path d="M20.18 13.902a1.902 1.902 0 1 1 0-3.804 1.902 1.902 0 0
 1 0 3.804m0-5.722A3.82 3.82 0 0 0 16.36 12v3.82h3.82a3.82 3.82 0 1 0
 0-7.64m-8.656 5.722A1.907 1.907 0 0 1 9.611 12c0-1.05.857-1.902
 1.913-1.902s1.913.852 1.913 1.902c0 1.05-.857 1.902-1.913
 1.902m-7.683 0A1.907 1.907 0 0 1 1.928 12c0-1.05.857-1.902
 1.913-1.902 1.057 0 1.913.852 1.913 1.902 0 1.05-.856 1.902-1.913
 1.902m11.514-2.107-.002-.032a3.76 3.76 0 0 0-.04-.37l-.004-.019a3.693
 3.693 0 0 0-.081-.373V11a3.836 3.836 0 0 0-3.704-2.82H3.84a3.833
 3.833 0 0 0-3.794
 3.254l-.001.008c-.018.118-.03.236-.036.357l-.002.02v.016C.006 11.89 0
 11.945 0 12c0
 .07.007.137.01.206l.002.032c.008.124.021.248.041.37l.003.018a3.833
 3.833 0 0 0 3.786 3.194h11.523V12c0-.07-.006-.137-.01-.205" />
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
