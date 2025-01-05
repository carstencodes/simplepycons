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


class EseaIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "esea"

    @property
    def original_file_name(self) -> "str":
        return "esea.svg"

    @property
    def title(self) -> "str":
        return "ESEA"

    @property
    def primary_color(self) -> "str":
        return "#0E9648"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>ESEA</title>
     <path d="M14.054 2.767L8.95 9.511 0 9.65l5.832 4.47L1.042
 21l8.491-4.088 5.711 4.322V14.12L24 9.796l-17.255 4.02a12.575 12.575
 0 001.589-1.955 5.475 5.475 0 00.617-1.786l5.593-.15z" />
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
