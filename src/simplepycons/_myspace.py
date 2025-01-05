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


class MyspaceIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "myspace"

    @property
    def original_file_name(self) -> "str":
        return "myspace.svg"

    @property
    def title(self) -> "str":
        return "Myspace"

    @property
    def primary_color(self) -> "str":
        return "#030303"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Myspace</title>
     <path d="M19.802 12.274A3.811 3.811 0 0023.62
 8.47c0-2.101-1.71-3.795-3.818-3.795a3.816 3.816 0 00-3.818 3.81 3.817
 3.817 0 003.818 3.811zm-8.602.705a3.43 3.43 0 003.435-3.424A3.43 3.43
 0 0011.2 6.13a3.44 3.44 0 00-3.436 3.436A3.436 3.436 0 0011.2
 13zm-7.8.635c1.71 0 3.093-1.38 3.093-3.081
 0-1.704-1.395-3.084-3.105-3.084A3.086 3.086 0 00.3 10.539c0 1.7 1.387
 3.078 3.095 3.078zm0 .705c-1.96 0-3.4 1.717-3.4 3.495v1.196c0
 .17.138.31.31.31h6.18a.31.31 0
 00.309-.31v-1.196c0-1.779-1.437-3.5-3.398-3.5zm7.8-.56c-2.18 0-3.78
 1.915-3.78 3.891v1.331c0 .188.156.344.345.344h6.87a.344.344 0
 00.342-.344V17.65c0-1.976-1.598-3.891-3.777-3.891zm8.602-.617c-2.422
 0-4.197 2.126-4.197 4.323v1.477c0 .21.172.381.382.381h7.63c.21 0
 .383-.171.383-.381v-1.477c-.001-2.197-1.776-4.323-4.198-4.323z" />
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
