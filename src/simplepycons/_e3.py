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


class EThreeIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "e3"

    @property
    def original_file_name(self) -> "str":
        return "e3.svg"

    @property
    def title(self) -> "str":
        return "E3"

    @property
    def primary_color(self) -> "str":
        return "#E73D2F"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>E3</title>
     <path d="M11.0676
 16.5185H4.7723v-2.6738h6.2615v-3.757H4.7723v-2.64h6.2615V3.691H0v16.6184h14.1476c0-.0339-2.7754-.7108-3.08-3.7908zm10.12-6.3969c1.8954
 1.2862 2.8769 2.5385 2.8092 5.1108-.0677 2.6738-2.7754 5.043-5.72
 5.043-2.0984 0-4.7723-.9477-5.7876-3.7569l3.4861-1.5569c.4738.88
 1.1508 1.557 2.2 1.557 1.1507 0 1.9969-.88
 2.0984-1.997.0339-.2708-.1353-2.2338-2.0984-2.3015l-2.2-.237
 2.8092-4.5353h-6.3292v-3.757h11.5415z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://commons.wikimedia.org/wiki/File:E3_Lo'''

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
        yield from [
            "Electronic Entertainment Expo",
        ]
