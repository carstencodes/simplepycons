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


class VbulletinIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "vbulletin"

    @property
    def original_file_name(self) -> "str":
        return "vbulletin.svg"

    @property
    def title(self) -> "str":
        return "vBulletin"

    @property
    def primary_color(self) -> "str":
        return "#184D66"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>vBulletin</title>
     <path d="M1.09 10.316V24h21.82V0h-2.417l-5.461
 19.613h-6.09l-3.134-9.246zm9.283-4.444l1.363 6.308L13.955
 0H1.089v5.872Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://commons.wikimedia.org/wiki/File:VBull'''

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
