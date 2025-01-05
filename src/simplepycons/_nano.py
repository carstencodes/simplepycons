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


class NanoIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "nano"

    @property
    def original_file_name(self) -> "str":
        return "nano.svg"

    @property
    def title(self) -> "str":
        return "Nano"

    @property
    def primary_color(self) -> "str":
        return "#4A90E2"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Nano</title>
     <path d="M22.2864 6.8576c-.9453 0-1.7135.7665-1.7135 1.7136 0
 1.2843-.4275 1.7136-1.7136 1.7136-.9453 0-1.7135.7664-1.7135 1.7135 0
 1.2843-.4276 1.7136-1.7136 1.7136-.9453 0-1.7135.7664-1.7135 1.7135 0
 .9454.7665 1.7136 1.7135 1.7136.9454 0 1.7136-.7665 1.7136-1.7136
 0-1.2843.4275-1.7135 1.7135-1.7135.9454 0 1.7136-.7665 1.7136-1.7136
 0-1.2843.4275-1.7135 1.7135-1.7135.9454 0 1.7136-.7666 1.7136-1.7136
 0-.9454-.7682-1.7136-1.7136-1.7136zm-13.717.0017c-.9453
 0-1.7135.7665-1.7135 1.7136 0 1.2843-.4275 1.7136-1.7135 1.7136-.9454
 0-1.7136.7664-1.7136 1.7135 0 .947.77 1.7135 1.7153 1.7135S6.8576
 12.9471 6.8576 12c0-1.2843.4293-1.7135 1.7136-1.7135s1.7136.4275
 1.7136 1.7135c0 .947.7698 1.7135 1.7152 1.7135.9453 0 1.7135-.7664
 1.7135-1.7135 0-.9454-.7664-1.7135-1.7169-1.7135-1.2843
 0-1.7135-.4276-1.7135-1.7136
 0-.9453-.7683-1.7136-1.7136-1.7136zm-6.8559 6.856A1.7136 1.7136 0 0 0
 0 15.4287a1.7136 1.7136 0 0 0 1.7135 1.7136 1.7136 1.7136 0 0 0
 1.7136-1.7136 1.7136 1.7136 0 0 0-1.7135-1.7136Z" />
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
