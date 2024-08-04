#
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2024 Carsten Igel.
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


class ErpnextIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "erpnext"

    @property
    def original_file_name(self) -> "str":
        return "erpnext.svg"

    @property
    def title(self) -> "str":
        return "ERPNext"

    @property
    def primary_color(self) -> "str":
        return "#0089FF"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>ERPNext</title>
     <path d="M2.88 0C1.29 0 0 1.29 0 2.88v18.24C0 22.71 1.29 24 2.88
 24h18.24c1.59 0 2.88-1.29 2.88-2.88V2.88C24 1.29 22.71 0 21.12
 0Zm5.04 5.76h8.254v2.146H7.92Zm0
 5.033h7.85v2.146h-5.233v2.954h5.703v2.146H7.92Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/frappe/erpnext/blob/924911
e74317f95a59f29e9410d4f141020a0411/erpnext/public/images/erpnext-logo.'''

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