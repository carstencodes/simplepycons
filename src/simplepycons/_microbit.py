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


class MicrobitIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "microbit"

    @property
    def original_file_name(self) -> "str":
        return "microbit.svg"

    @property
    def title(self) -> "str":
        return "micro:bit"

    @property
    def primary_color(self) -> "str":
        return "#00ED00"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>micro:bit</title>
     <path d="M6.857 5.143A6.865 6.865 0 000 12a6.864 6.864 0 006.857
 6.857h10.287A6.863 6.863 0 0024 12c0-3.781-3.075-6.857-6.856-6.857zm0
 2.744h10.287A4.117 4.117 0 0121.257 12a4.119 4.119 0 01-4.113
 4.116H6.857A4.12 4.12 0 012.743 12a4.118 4.118 0
 014.114-4.113zm10.168 2.729a1.385 1.385 0 10.003 2.77 1.385 1.385 0
 00-.003-2.77zm-10.166 0a1.385 1.385 0 10-.003 2.771 1.385 1.385 0
 00.003-2.77Z" />
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
