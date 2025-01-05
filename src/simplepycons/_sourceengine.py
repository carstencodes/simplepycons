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


class SourceEngineIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "sourceengine"

    @property
    def original_file_name(self) -> "str":
        return "sourceengine.svg"

    @property
    def title(self) -> "str":
        return "Source Engine"

    @property
    def primary_color(self) -> "str":
        return "#F79A10"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Source Engine</title>
     <path d="M19.865.716h-.26L7.64.784a12.76 12.76 0 0 0-7.01
 1.69l.002.001A1.211 1.211 0 0 0 1.21 4.75c.35 0
 .662-.148.883-.383a10.321 10.321 0 0 1 8.818-.462c5.275 2.165 7.805
 8.22 5.64 13.495a10.283 10.283 0 0 1-2.495 3.613l.01.013a1.21 1.21 0
 1 0 1.63 1.69 12.638 12.638 0 0 0 3.04-4.419c.05-.118 4.952-12.06
 4.964-12.093A3.992 3.992 0 0 0
 21.522.996c-.55-.226-1.064-.278-1.657-.28zM6.067 6.851c-2.635
 0-5.342.807-5.342 3.941 0 2.16 1.946 2.85 3.893 3.277 2.422.522
 3.823.878 3.823 1.9 0 1.187-1.235 1.567-2.208 1.567-1.33
 0-2.564-.594-2.588-2.066H.44c.143 3.252 2.92 4.32 5.77 4.32 2.801 0
 5.603-1.044 5.603-4.273
 0-2.28-1.923-2.992-3.894-3.443-1.923-.45-3.823-.617-3.823-1.828
 0-.997 1.116-1.14 1.877-1.14 1.21 0 2.207.357 2.302
 1.662h3.205c-.26-3.015-2.73-3.917-5.413-3.917z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://developer.valvesoftware.com/favicon.i'''

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
