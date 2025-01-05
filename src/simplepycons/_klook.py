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


class KlookIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "klook"

    @property
    def original_file_name(self) -> "str":
        return "klook.svg"

    @property
    def title(self) -> "str":
        return "Klook"

    @property
    def primary_color(self) -> "str":
        return "#FF5722"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Klook</title>
     <path d="M4.8 0A4.79 4.79 0 0 0 0 4.8v14.4C0 21.86 2.14 24 4.8
 24h14.4c2.66 0 4.8-2.14 4.8-4.8V4.8C24 2.14 21.86 0 19.2 0H4.8zM12
 3.449v.001c4.242 0 7.833 1.904 7.833 6.17 0 2.932-3.86 7.815-6.164
 10.164-.99 1.008-2.32 1.036-3.338
 0-2.303-2.349-6.164-7.232-6.164-10.164 0-4.162 3.476-6.171
 7.833-6.171zm3.54 2.155l-5.05 4.96 5.05 4.956a1.84 1.84 0 0 0
 0-2.634v-.001l-2.366-2.323 2.366-2.323a1.84 1.84 0 0 0
 0-2.635zm-7.349.144v9.772a1.86 1.86 0 0 0 1.868-1.852V7.602a1.86 1.86
 0 0 0-1.866-1.854h-.002z" />
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
