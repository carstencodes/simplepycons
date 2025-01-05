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


class KinopoiskIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "kinopoisk"

    @property
    def original_file_name(self) -> "str":
        return "kinopoisk.svg"

    @property
    def title(self) -> "str":
        return "Kinopoisk"

    @property
    def primary_color(self) -> "str":
        return "#FF5500"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Kinopoisk</title>
     <path d="M12.049 0C5.45 0 .104 5.373.104 12S5.45 24 12.049
 24c3.928 0 7.414-1.904 9.592-4.844l-9.803-5.174 6.256
 6.418h-3.559l-4.373-6.086V20.4h-2.89V3.6h2.89v6.095L14.535
 3.6h3.559l-6.422 6.627 9.98-5.368C19.476 1.911 15.984 0 12.05
 0zm10.924 7.133-9.994 4.027 10.917-.713a11.963 11.963 0 0
 0-.923-3.314zm-10.065 5.68 10.065
 4.054c.458-1.036.774-2.149.923-3.314l-10.988-.74z" />
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
