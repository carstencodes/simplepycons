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


class NortonIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "norton"

    @property
    def original_file_name(self) -> "str":
        return "norton.svg"

    @property
    def title(self) -> "str":
        return "Norton"

    @property
    def primary_color(self) -> "str":
        return "#FFE01A"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Norton</title>
     <path d="M23.978 12c0 6.617-5.373 12-11.978 12C5.395 24 .022
 18.617.022 12S5.395 0 12 0c1.826 0 3.557.41 5.107 1.146l-1.99
 2.567A8.787 8.787 0 0 0 12 3.145c-4.657 0-8.484 3.627-8.815
 8.21a9.595 9.595 0 0 0-.023.645c0 4.883 3.964 8.855 8.838 8.855 4.874
 0 8.838-3.972 8.838-8.855
 0-.652-.07-1.29-.205-1.902l2.309-2.979A11.948 11.948 0 0 1 23.978
 12m-2.442-7.253L19.518 7.35l-7.082 9.14-5.778-5.175L8.75 8.97l3.27
 2.928L17.38 4.98l1.924-2.484a12.08 12.08 0 0 1 2.231 2.25" />
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
