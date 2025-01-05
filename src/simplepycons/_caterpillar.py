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


class CaterpillarIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "caterpillar"

    @property
    def original_file_name(self) -> "str":
        return "caterpillar.svg"

    @property
    def title(self) -> "str":
        return "Caterpillar"

    @property
    def primary_color(self) -> "str":
        return "#FFCD11"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Caterpillar</title>
     <path d="M11.901 11.554l.802-4.1.798 4.1zm2.869-6.52h-4.15L8.2
 15.884l4.503-3.635 4.695 3.934zm-2.067 8.156l-7.509 6.072H19.95zM24
 5.02v2.77h-2.066v11.45h-.882l-2.436-2.04V7.79h-2.057V5.02zM6.872
 16.864c.548-.458.642-1.024.642-1.532V13.2h-2.98v2.894a.75.75 0 0
 1-.748.751c-.414
 0-.722-.336-.722-.75V7.893c0-.414.308-.75.722-.75a.75.75 0 0 1
 .749.75v2.913H7.51V7.785c0-1.67-1.092-3.044-3.75-3.047-2.728 0-3.76
 1.38-3.76 3.05v8.563c0 1.655 1.314 2.907 2.995 2.907h.922Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://commons.wikimedia.org/wiki/File:Cater'''

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
