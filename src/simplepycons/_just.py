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


class JustIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "just"

    @property
    def original_file_name(self) -> "str":
        return "just.svg"

    @property
    def title(self) -> "str":
        return "Just"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Just</title>
     <path d="M12 0A12 12 0 0 0 0 12a12 12 0 0 0 12 12 12 12 0 0 0
 12-12A12 12 0 0 0 12 0m0 2.35a3.25 3.35 0 0 1 3.25 3.35A3.25 3.35 0 0
 1 12 9.05 3.25 3.35 0 0 1 8.75 5.7 3.25 3.35 0 0 1 12 2.35m0
 12.6a3.25 3.35 0 0 1 3.25 3.35A3.25 3.35 0 0 1 12 21.65a3.25 3.35 0 0
 1-3.25-3.35A3.25 3.35 0 0 1 12 14.95" />
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
