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


class FrappeIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "frappe"

    @property
    def original_file_name(self) -> "str":
        return "frappe.svg"

    @property
    def title(self) -> "str":
        return "Frappe"

    @property
    def primary_color(self) -> "str":
        return "#0089FF"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Frappe</title>
     <path d="M2.88 0C1.29 0 0 1.29 0 2.88v18.24C0 22.71 1.29 24 2.88
 24h18.24c1.59 0 2.88-1.29 2.88-2.88V2.88C24 1.29 22.71 0 21.12
 0H2.88zM8.4 6h8.024v2.111H8.4V6zm0
 5.385h7.49v2.113h-4.93V18H8.4v-6.615z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/frappe/frappe/blob/1331fa6
f721122805d15894fa3bd9eb90dccdca2/frappe/public/images/frappe-framewor'''

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
