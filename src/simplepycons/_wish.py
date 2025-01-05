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


class WishIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "wish"

    @property
    def original_file_name(self) -> "str":
        return "wish.svg"

    @property
    def title(self) -> "str":
        return "Wish"

    @property
    def primary_color(self) -> "str":
        return "#32E476"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Wish</title>
     <path d="M18.864 19.826h-4.107l-3.227-9.393-2.28 9.39H5.143L0
 4.65h4.217l4.354 13.128c1.558-4.4 2.534-8.5 1.021-13.128H13.7ZM20.57
 4.174a15.705 15.705 0 0 1-3.425 4.171 17.095 17.095 0 0 1 3.425
 5.56A17.116 17.116 0 0 1 24 8.345a15.734 15.734 0 0 1-3.43-4.17Z" />
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
