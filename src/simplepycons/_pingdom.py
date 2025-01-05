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


class PingdomIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "pingdom"

    @property
    def original_file_name(self) -> "str":
        return "pingdom.svg"

    @property
    def title(self) -> "str":
        return "Pingdom"

    @property
    def primary_color(self) -> "str":
        return "#FFF000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Pingdom</title>
     <path d="M11.96 17.804l7.959-3.396-7.049
 7.241c-.124-1.315-.432-2.61-.91-3.844v-.001zM24
 11.118c-5.101-.236-10.208.414-15.087 1.92 1.024 1.073 1.881 2.292
 2.535 3.621 4.042-2.25 9.646-5.123
 12.552-5.531v-.015.005zm-12.574.275l.207-.06c1.538-.459 3.049-1.015
 4.523-1.656 1.492-.585 2.896-1.38 4.159-2.367 1.345-1.069 2.355-2.499
 2.915-4.122.12-.267.211-.549.267-.837-2.024 2.76-10.041 3.048-10.041
 3.048l1.89-1.734C9.84 3.684 4.47 5.424 0 8.645c3.03.322 5.877 1.596
 8.139 3.634 1.086-.336 2.196-.576 3.286-.879v-.006l.001-.001z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://www.pingdom.com/resources/brand-asset'''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://www.pingdom.com/resources/brand-asset'''

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
