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


class OnePasswordIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "1password"

    @property
    def original_file_name(self) -> "str":
        return "1password.svg"

    @property
    def title(self) -> "str":
        return "1Password"

    @property
    def primary_color(self) -> "str":
        return "#3B66BC"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>1Password</title>
     <path d="M12 .007C5.373.007 0 5.376 0 11.999c0 6.624 5.373 11.994
 12 11.994S24 18.623 24 12C24 5.376 18.627.007 12 .007Zm-.895
 4.857h1.788c.484 0 .729.002.914.096a.86.86 0 0 1
 .377.377c.094.185.095.428.095.912v6.016c0 .12 0
 .182-.015.238a.427.427 0 0 1-.067.137.923.923 0 0
 1-.174.162l-.695.564c-.113.092-.17.138-.191.194a.216.216 0 0 0 0
 .15c.02.055.078.101.191.193l.695.565c.094.076.14.115.174.162.03.042.053.087.067.137a.936.936
 0 0 1 .015.238v2.746c0 .484-.001.727-.095.912a.86.86 0 0
 1-.377.377c-.185.094-.43.096-.914.096h-1.788c-.484
 0-.726-.002-.912-.096a.86.86 0 0
 1-.377-.377c-.094-.185-.095-.428-.095-.912v-6.016c0-.12
 0-.182.015-.238a.437.437 0 0 1
 .067-.139c.034-.047.08-.083.174-.16l.695-.564c.113-.092.17-.138.191-.194a.216.216
 0 0 0 0-.15c-.02-.055-.078-.101-.191-.193l-.695-.565a.92.92 0 0
 1-.174-.162.437.437 0 0 1-.067-.139.92.92 0 0
 1-.015-.236V6.25c0-.484.001-.727.095-.912a.86.86 0 0 1
 .377-.377c.186-.094.428-.096.912-.096z" />
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
