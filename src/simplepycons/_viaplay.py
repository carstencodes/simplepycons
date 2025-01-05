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


class ViaplayIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "viaplay"

    @property
    def original_file_name(self) -> "str":
        return "viaplay.svg"

    @property
    def title(self) -> "str":
        return "Viaplay"

    @property
    def primary_color(self) -> "str":
        return "#FE365F"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Viaplay</title>
     <path d="M1.2766 6.6383C.4742 8.2432 0 10.0669 0 12s.4742 3.7568
 1.2766 5.3617L12 12ZM12 0C9.0456 0 6.3465 1.0578 4.231 2.845l12.5471
 6.7477v4.8146L4.231 21.155C6.31 22.9422 9.0456 24 12 24c6.6383 0
 12-5.3617 12-12S18.6383 0 12 0Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://commons.wikimedia.org/wiki/File:Viapl'''

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
