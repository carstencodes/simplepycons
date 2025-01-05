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


class CrunchyrollIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "crunchyroll"

    @property
    def original_file_name(self) -> "str":
        return "crunchyroll.svg"

    @property
    def title(self) -> "str":
        return "Crunchyroll"

    @property
    def primary_color(self) -> "str":
        return "#F47521"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Crunchyroll</title>
     <path d="M2.933 13.467a10.55 10.55 0 1 1
 21.067-.8V12c0-6.627-5.373-12-12-12S0 5.373 0 12s5.373 12 12
 12h.8a10.617 10.617 0 0 1-9.867-10.533zM19.2 14a3.85 3.85 0 0
 1-1.333-7.467A7.89 7.89 0 0 0 14 5.6a8.4 8.4 0 1 0 8.4 8.4 6.492
 6.492 0 0 0-.133-1.6A3.415 3.415 0 0 1 19.2 14z" />
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
