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


class MonoprixIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "monoprix"

    @property
    def original_file_name(self) -> "str":
        return "monoprix.svg"

    @property
    def title(self) -> "str":
        return "Monoprix"

    @property
    def primary_color(self) -> "str":
        return "#FB1911"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Monoprix</title>
     <path d="M21.072 8.042C21.072 3.612 16.981 0 12 0 6.991 0 2.928
 3.612 2.928 8.042S6.99 16.085 12 16.085c.282 0
 .564-.029.847-.043.62.339.747.706.761.988.142 1.608-2.44 5.08-4.303
 6.49l.254.48c.113-.028 10.723-3.47
 11.429-15.026.056-.283.07-.565.084-.875v-.043z" />
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
