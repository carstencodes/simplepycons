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


class NugetIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "nuget"

    @property
    def original_file_name(self) -> "str":
        return "nuget.svg"

    @property
    def title(self) -> "str":
        return "NuGet"

    @property
    def primary_color(self) -> "str":
        return "#004880"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>NuGet</title>
     <path d="M1.998.342a1.997 1.997 0 1 0 0 3.995 1.997 1.997 0 0 0
 0-3.995zm9.18 4.34a6.156 6.156 0 0 0-6.153 6.155v6.667c0 3.4 2.756
 6.154 6.154 6.154h6.667c3.4 0 6.154-2.755 6.154-6.154v-6.667a6.154
 6.154 0 0 0-6.154-6.155zm-1.477 2.8a2.496 2.496 0 1 1 0 4.993 2.496
 2.496 0 0 1 0-4.993zm7.968 6.16a3.996 3.996 0 1 1-.002 7.992 3.996
 3.996 0 0 1 .002-7.992z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/NuGet/Media/blob/89f7c8724'''

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
