#
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2026 Carsten Igel.
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


class CachyosIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "cachyos"

    @property
    def original_file_name(self) -> "str":
        return "cachyos.svg"

    @property
    def title(self) -> "str":
        return "CachyOS"

    @property
    def primary_color(self) -> "str":
        return "#00AA88"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>CachyOS</title>
     <path d="M5.301 2.646 0 11.771l5.541
 9.583h11.486l2.904-5.017H8.102l-2.56-4.429L8.067
 7.54h6.063l2.83-4.893ZM20.058 4.12a.748.748 0 0 0 0 1.496.748.748 0 0
 0 0-1.496m-1.983 4.303a1.45 1.45 0 0 0 0 2.9 1.45 1.45 0 0 0
 0-2.9m4.02 3.98a1.904 1.904 0 0 0 0 3.809 1.904 1.904 0 0 0 0-3.81"
 />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://commons.wikimedia.org/wiki/File:Cachy'''

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
