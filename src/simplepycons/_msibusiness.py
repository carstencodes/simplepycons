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


class MsiBusinessIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "msibusiness"

    @property
    def original_file_name(self) -> "str":
        return "msibusiness.svg"

    @property
    def title(self) -> "str":
        return "MSI Business"

    @property
    def primary_color(self) -> "str":
        return "#9A8555"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>MSI Business</title>
     <path d="m15.215 10.794 3.78
 2.416h-2.663l-3.78-2.416h2.663zM5.656 8.518l-.438 1.626-.175.65-.652
 2.416-.175.65-.437
 1.622h1.869l.437-1.622.175-.65.651-2.416.175-.65.438-1.626H5.656zm6.06
 5.342-.437 1.622h4.947l2.543-1.622h-7.053zm3.556-5.342-2.548
 1.626h7.086l.438-1.626h-4.976zm6.86 0-.438 1.626-.175.65-.651
 2.416-.175.65-.437
 1.622h1.869l.437-1.622.175-.65.651-2.416.175-.65L24
 8.518h-1.868zm-20.255 0-.438 1.626-.175.65-.651 2.416-.175.65L0
 15.482h1.869l.437-1.622.175-.65.651-2.416.175-.65.438-1.626H1.877zm7.536
 0-.438 1.626-.175.65-.651 2.416-.175.65-.437
 1.622h1.869l.437-1.622.175-.65.651-2.416.175-.65.438-1.626H9.413z" />
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
