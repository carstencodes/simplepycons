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


class SnowpackIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "snowpack"

    @property
    def original_file_name(self) -> "str":
        return "snowpack.svg"

    @property
    def title(self) -> "str":
        return "Snowpack"

    @property
    def primary_color(self) -> "str":
        return "#2E5E82"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Snowpack</title>
     <path d="M23.8094 19.7512l-10.8-16.7999a1.2002 1.2002 0 00-2.0189
 0L.1906 19.7512a1.2 1.2 0 00-.0439 1.224 1.2002 1.2002 0
 001.0534.6247H22.8c.4391 0 .843-.2396 1.0534-.6251a1.1994 1.1994 0
 00-.044-1.2236zM12 5.8193L15.202 10.8H12l-2.4 2.4-1.4272-1.4272z" />
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
