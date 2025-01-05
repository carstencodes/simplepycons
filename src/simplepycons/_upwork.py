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


class UpworkIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "upwork"

    @property
    def original_file_name(self) -> "str":
        return "upwork.svg"

    @property
    def title(self) -> "str":
        return "Upwork"

    @property
    def primary_color(self) -> "str":
        return "#6FDA44"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Upwork</title>
     <path d="M18.561 13.158c-1.102
 0-2.135-.467-3.074-1.227l.228-1.076.008-.042c.207-1.143.849-3.06
 2.839-3.06 1.492 0 2.703 1.212 2.703 2.703-.001 1.489-1.212
 2.702-2.704 2.702zm0-8.14c-2.539 0-4.51 1.649-5.31
 4.366-1.22-1.834-2.148-4.036-2.687-5.892H7.828v7.112c-.002
 1.406-1.141 2.546-2.547
 2.548-1.405-.002-2.543-1.143-2.545-2.548V3.492H0v7.112c0 2.914 2.37
 5.303 5.281 5.303 2.913 0 5.283-2.389 5.283-5.303v-1.19c.529 1.107
 1.182 2.229 1.974 3.221l-1.673 7.873h2.797l1.213-5.71c1.063.679 2.285
 1.109 3.686 1.109 3 0 5.439-2.452 5.439-5.45
 0-3-2.439-5.439-5.439-5.439z" />
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
