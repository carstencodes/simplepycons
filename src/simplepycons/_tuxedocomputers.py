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


class TuxedoComputersIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "tuxedocomputers"

    @property
    def original_file_name(self) -> "str":
        return "tuxedocomputers.svg"

    @property
    def title(self) -> "str":
        return "TUXEDO Computers"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>TUXEDO Computers</title>
     <path d="m13.958 11.13 4.597 7.444h-3.509l-2.94-4.921-4.333
 6.365L24 19.968c-.074.725-.144 1.45-.215
 2.174-12.391.052-7.537.105-19.928.105l7.192-10.223-4.06-6.666h3.497l2.386
 4.096 3.49-5.515C5.202 3.887 11.17 3.987 0 3.963L.223 1.8c12.392-.015
 7.498-.046 19.889-.046z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://www.tuxedocomputers.com/Infos/Press/C'''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://www.tuxedocomputers.com/Infos/Press/C'''

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
