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


class KeepassxcIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "keepassxc"

    @property
    def original_file_name(self) -> "str":
        return "keepassxc.svg"

    @property
    def title(self) -> "str":
        return "KeePassXC"

    @property
    def primary_color(self) -> "str":
        return "#6CAC4D"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>KeePassXC</title>
     <path d="M12 0C5.378 0 0 5.378 0 12c0 6.623 5.378 12 12 12 6.623
 0 12-5.377 12-12 0-6.622-5.377-12-12-12zm0 .791a11.203 11.203 0 0 1
 11.209 11.21A11.202 11.202 0 0 1 12 23.208 11.203 11.203 0 0 1 .791
 12 11.203 11.203 0 0 1 12.001.791zm0 1.871a9.356 9.356 0 0
 0-1.705.162A1.746 1.746 0 0 0 12 4.95a1.746 1.746 0 0 0
 1.706-2.126A9.342 9.342 0 0 0 12 2.662zM7.2 4a9.338 9.338 0 0 0-4.54
 8 9.338 9.338 0 0 0 18.677 0 9.338 9.338 0 0 0-4.54-7.998 4.888 4.888
 0 0 1-2.701 5.365l-.12 2.066 1.482 1.483-1.483
 1.482.989.989-.989.988.12 1.857L12 20.328l-2.096-2.096V9.367A4.89
 4.89 0 0 1 7.2 4zm3.4 6.543v6.99h.7v-6.99z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/keepassxreboot/keepassxc/t'''

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
