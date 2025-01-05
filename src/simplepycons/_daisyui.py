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


class DaisyuiIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "daisyui"

    @property
    def original_file_name(self) -> "str":
        return "daisyui.svg"

    @property
    def title(self) -> "str":
        return "DaisyUI"

    @property
    def primary_color(self) -> "str":
        return "#1AD1A5"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>DaisyUI</title>
     <path d="M12 0C7.828.001 4.396 3.433 4.395 7.605c.001 4.172 3.433
 7.604 7.605 7.605 4.172-.001 7.604-3.433 7.605-7.605C19.604 3.433
 16.172.001 12 0Zm0 .286c4.016 0 7.32 3.304 7.32 7.32-.001 4.015-3.305
 7.318-7.32 7.318-4.015 0-7.319-3.304-7.32-7.319 0-4.016 3.304-7.32
 7.32-7.32zm0 4.04a3.294 3.294 0 0 0-3.279 3.279v.001A3.296 3.296 0 0
 0 12 10.884a3.294 3.294 0 0 0 3.279-3.279A3.294 3.294 0 0 0 12
 4.326ZM8.34 16.681h-.008a3.67 3.67 0 0 0-3.652 3.652v.015A3.67 3.67 0
 0 0 8.332 24h7.336a3.67 3.67 0 0 0 3.652-3.652v-.016a3.67 3.67 0 0
 0-3.652-3.652h-.008Z" />
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
