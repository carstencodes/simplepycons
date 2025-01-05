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


class NetcupIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "netcup"

    @property
    def original_file_name(self) -> "str":
        return "netcup.svg"

    @property
    def title(self) -> "str":
        return "netcup"

    @property
    def primary_color(self) -> "str":
        return "#056473"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>netcup</title>
     <path d="M5.25 0A5.239 5.239 0 0 0 0 5.25v13.5A5.239 5.239 0 0 0
 5.25 24h13.5A5.239 5.239 0 0 0 24 18.75V5.25A5.239 5.239 0 0 0 18.75
 0H5.25zm-.045 5.102h9.482c1.745 0 2.631.907 2.631
 2.753v8.352h1.477v2.691h-4.666V8.58c0-.514-.298-.785-.889-.785H9.873v11.103H6.682V7.795H5.205V5.102z"
 />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://www.netcup.eu/ueber-netcup/werbemitte'''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://www.netcup.de/static/assets/images/fa'''

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
