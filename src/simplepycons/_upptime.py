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


class UpptimeIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "upptime"

    @property
    def original_file_name(self) -> "str":
        return "upptime.svg"

    @property
    def title(self) -> "str":
        return "Upptime"

    @property
    def primary_color(self) -> "str":
        return "#1ABC9C"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Upptime</title>
     <path d="M11.86 15.68c1.926 0 3.489 1.526 3.489 3.406 0
 1.88-1.563 3.407-3.488 3.407-1.926 0-3.489-1.526-3.489-3.407 0-1.88
 1.563-3.407 3.489-3.407ZM24 14.884 12 1.507 0 14.885l3.158 3.52L12
 8.548l8.842 9.857L24 14.885Z" />
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
