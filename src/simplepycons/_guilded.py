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


class GuildedIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "guilded"

    @property
    def original_file_name(self) -> "str":
        return "guilded.svg"

    @property
    def title(self) -> "str":
        return "Guilded"

    @property
    def primary_color(self) -> "str":
        return "#F5C400"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Guilded</title>
     <path d="M5.297 6.255s.02 2.846 1.481 5.79c1.502 2.834 3.572
 4.654 5.28 5.38 1.765-.826 3.47-2.258
 4.4-3.8h-4.845c-1.253-1.04-2.24-2.763-2.466-4.755H23.36c-.701
 3.203-2.188 6.116-3.605 7.971a17.108 17.108 0 01-7.686
 5.659h-.045c-5.098-2.031-7.84-5.23-9.65-8.84C1.214 11.347 0 7.147 0
 1.5h24a34.23 34.23 0 01-.32 4.755z" />
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
