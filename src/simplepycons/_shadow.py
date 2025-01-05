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


class ShadowIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "shadow"

    @property
    def original_file_name(self) -> "str":
        return "shadow.svg"

    @property
    def title(self) -> "str":
        return "Shadow"

    @property
    def primary_color(self) -> "str":
        return "#0A0C0D"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Shadow</title>
     <path d="M12 0C5.3727 0 0 5.3727 0 12c0 3.5145 1.511 6.6754
 3.9181 8.8702a4.457 4.457 0 01-.1998-1.3238c0-2.4597 1.9938-4.4535
 4.4536-4.4535 2.4596 0 4.4535 1.9938 4.4535 4.4535 0 1.9565-1.262
 3.6171-3.016 4.2153C10.382 23.9178 11.1815 24 12 24c6.6273 0
 12-5.3727 12-12S18.6273 0 12 0Z" />
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
