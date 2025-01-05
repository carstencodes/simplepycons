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


class KdePlasmaIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "kdeplasma"

    @property
    def original_file_name(self) -> "str":
        return "kdeplasma.svg"

    @property
    def title(self) -> "str":
        return "KDE Plasma"

    @property
    def primary_color(self) -> "str":
        return "#1D99F3"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>KDE Plasma</title>
     <path d="M6 0c-.831 0-1.5.669-1.5 1.5S5.169 3 6 3s1.5-.669
 1.5-1.5S6.831 0 6 0m10.5 0-3 3L18 7.5 13.5 12l3 3 4.5-4.5 3-3zM2.25
 9A2.245 2.245 0 0 0 0 11.25a2.245 2.245 0 0 0 2.25 2.25 2.245 2.245 0
 0 0 2.25-2.25A2.245 2.245 0 0 0 2.25 9M9 18c-1.662 0-3 1.338-3
 3s1.338 3 3 3 3-1.338 3-3-1.338-3-3-3" />
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
