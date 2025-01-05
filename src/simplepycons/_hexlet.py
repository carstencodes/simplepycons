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


class HexletIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "hexlet"

    @property
    def original_file_name(self) -> "str":
        return "hexlet.svg"

    @property
    def title(self) -> "str":
        return "Hexlet"

    @property
    def primary_color(self) -> "str":
        return "#116EF5"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Hexlet</title>
     <path d="M16.732 7.099v6.422H7.268V7.099L4.563
 6.085V24h2.705v-7.775h9.464V24h2.705V6.085l-2.705
 1.014Zm3.043-4.057L12 0 4.225 3.042 12 5.746l7.775-2.704Z" />
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
