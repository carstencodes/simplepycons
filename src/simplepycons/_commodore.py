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


class CommodoreIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "commodore"

    @property
    def original_file_name(self) -> "str":
        return "commodore.svg"

    @property
    def title(self) -> "str":
        return "Commodore"

    @property
    def primary_color(self) -> "str":
        return "#1E2A4E"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Commodore</title>
     <path d="M11.202.798C5.016.798 0 5.814 0 12s5.016 11.202 11.202
 11.202c1.094 0 2.153-.157 3.154-.45v-5.335a6.27 6.27 0 1 1
 0-10.839v-5.33c-1-.293-2.057-.45-3.154-.45Zm3.375 6.343v4.304h5.27L24
 7.14Zm-.037 5.377v4.304h9.423l-4.156-4.304z" />
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
