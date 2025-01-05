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


class InfomaniakIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "infomaniak"

    @property
    def original_file_name(self) -> "str":
        return "infomaniak.svg"

    @property
    def title(self) -> "str":
        return "Infomaniak"

    @property
    def primary_color(self) -> "str":
        return "#0098FF"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Infomaniak</title>
     <path d="M2.4 0A2.395 2.395 0 0 0 0 2.4v19.2C0 22.9296 1.0704 24
 2.4 24h19.2c1.3296 0 2.4-1.0704 2.4-2.4V2.4C24 1.0704 22.9296 0 21.6
 0H10.112v11.7119l3.648-4.128h6l-4.58 4.3506 4.868
 8.1296h-5.52l-2.5938-5.0211L10.112 16.8v3.264H5.12V0Z" />
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
