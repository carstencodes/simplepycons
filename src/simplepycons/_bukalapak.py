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


class BukalapakIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "bukalapak"

    @property
    def original_file_name(self) -> "str":
        return "bukalapak.svg"

    @property
    def title(self) -> "str":
        return "Bukalapak"

    @property
    def primary_color(self) -> "str":
        return "#E31E52"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Bukalapak</title>
     <path d="M10.976 23.845a3.158 3.158 0 1 1-1.95-6.008 3.158 3.158
 0 0 1 1.95 6.008Zm6.554-2.883c4.047-1.315 7.315-5.981
 5.689-10.984-1.626-5.003-7.012-6.856-11.058-5.541a1.89 1.89 0 0
 0-1.252 2.249l.414 1.682a1.892 1.892 0 0 0 2.42
 1.348l.162-.053c1.861-.606 3.592.504 4.071 2.019.505 1.507-.244
 3.422-2.106 4.027l-.162.054a1.891 1.891 0 0 0-1.166 2.512l.653
 1.604a1.89 1.89 0 0 0 2.335 1.083Zm-6.962-7.982L7.841 1.752A2.3 2.3 0
 0 0 4.897.113l-2.952.959A2.3 2.3 0 0 0 .526 4.128L4.92 14.815a2.3 2.3
 0 0 0 2.841 1.318l1.285-.417a2.298 2.298 0 0 0 1.522-2.736Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://brand.bukalapak.design/brand-elements'''
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
