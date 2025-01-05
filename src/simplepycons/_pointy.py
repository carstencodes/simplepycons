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


class PointyIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "pointy"

    @property
    def original_file_name(self) -> "str":
        return "pointy.svg"

    @property
    def title(self) -> "str":
        return "Pointy"

    @property
    def primary_color(self) -> "str":
        return "#009DE0"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Pointy</title>
     <path d="M8.076.025S4.52.234 2.833 2.751c-1.58 2.351-1.465
 5.145-1.1 8.121C2.096 13.831 2.587 24 2.587 24c.002.003 11.235-11.526
 11.23-11.506 1.75-1.805 2.408-4.468
 2.395-5.961-.037-4.274-3.461-6.815-8.136-6.508zm.777 10.774c-1.991
 0-3.604-1.632-3.604-3.645 0-2.015 1.614-3.649 3.604-3.649s3.642 1.512
 3.642 3.527c0 2.011-1.652 3.767-3.642 3.767zm2.765-3.741a1.58 1.58 0
 1 1-3.162 0 1.58 1.58 0 0 1 3.162 0zm10.879
 1.431s-2.325.158-3.644.57c-1.317.413-2.502 1.076-2.502
 1.076s.495-.852.705-2.361c.207-1.511-.14-2.652-.14-2.652l5.581
 3.367Z" />
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
