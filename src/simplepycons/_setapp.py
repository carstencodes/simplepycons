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


class SetappIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "setapp"

    @property
    def original_file_name(self) -> "str":
        return "setapp.svg"

    @property
    def title(self) -> "str":
        return "Setapp"

    @property
    def primary_color(self) -> "str":
        return "#E6C3A5"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Setapp</title>
     <path d="M13.0949 8.1332a.619.619 0 0 1
 0-.874l2.7712-2.7733a.619.619 0 0 1 .877 0l2.7703 2.7722a.619.619 0 0
 1 0 .8751l-2.7703 2.7722a.619.619 0 0 1-.877 0zm-1.5331-1.5331L8.7906
 3.8299a.618.618 0 0 1 0-.877L11.5618.1815a.619.619 0 0 1 .876
 0l2.7732 2.7712a.619.619 0 0 1 0 .877L12.4378 6.6a.619.619 0 0 1-.876
 0zm0 2.1902a.619.619 0 0 1 .876 0l2.7732 2.7712a.619.619 0 0 1 0
 .877l-2.7732 2.7712a.619.619 0 0 1-.876 0l-2.7712-2.7692a.618.618 0 0
 1 0-.877zm-4.3044 2.1151L4.4862 8.1332a.619.619 0 0 1
 0-.876l2.7712-2.7713a.619.619 0 0 1 .8761 0l2.7722 2.7712a.621.621 0
 0 1 0 .8761l-2.7732 2.7722a.619.619 0 0 1-.876 0zm9.4847 2.1902
 2.7723 2.7712a.618.618 0 0 1 0 .875l-2.7703 2.7723a.619.619 0 0
 1-.876 0l-2.7732-2.7722a.621.621 0 0 1 0-.8751l2.7732-2.7722a.619.619
 0 0 1 .875 0zm-4.3043 4.3033 2.7722 2.7722a.618.618 0 0 1 0
 .876l-2.7722 2.7713a.619.619 0 0 1-.876 0l-2.7712-2.7712a.619.619 0 0
 1 0-.877l2.7712-2.7713a.619.619 0 0 1 .876 0zm-1.532-1.5321a.619.619
 0 0 1 0 .875l-2.7723 2.7733a.621.621 0 0 1-.876
 0l-2.7723-2.7722a.619.619 0 0 1 0-.8751l2.7722-2.7722a.619.619 0 0 1
 .8761 0z" />
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
