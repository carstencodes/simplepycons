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


class RenaultIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "renault"

    @property
    def original_file_name(self) -> "str":
        return "renault.svg"

    @property
    def title(self) -> "str":
        return "Renault"

    @property
    def primary_color(self) -> "str":
        return "#FFCC33"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Renault</title>
     <path d="M17.463 11.99l-4.097-7.692-.924 1.707 3.213 5.985-5.483
 10.283L4.69 11.99 11.096 0H9.27L2.882 11.99 9.269 24h1.807zm3.655
 0L14.711 0h-1.807L6.517 11.99l4.117 7.712.904-1.707-3.193-6.005
 5.463-10.263L19.29 11.99 12.904 24h1.807Z" />
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
