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


class DowndetectorIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "downdetector"

    @property
    def original_file_name(self) -> "str":
        return "downdetector.svg"

    @property
    def title(self) -> "str":
        return "Downdetector"

    @property
    def primary_color(self) -> "str":
        return "#FF160A"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Downdetector</title>
     <path d="M12 0C5.49 0 .257 5.362.257 12v12H12c6.51 0 11.743-5.362
 11.743-12S18.51 0 12 0Zm0 3.51c.543 0 1.086.065
 1.66.192.383.128.639.383.639.766l-.638 10.085c0
 .255-.256.511-.512.511-.766.128-1.533.128-2.171 0-.383
 0-.639-.256-.639-.51L9.701 4.467c0-.383.256-.638.638-.766A7.583 7.583
 0 0 1 12 3.51Zm.065 12.99c.447 0 .892.031 1.339.095.255 0
 .384.256.384.384.127.894.127 1.786 0 2.807 0
 .256-.257.384-.384.384a9.427 9.427 0 0 1-2.68 0c-.256
 0-.384-.256-.384-.384-.128-.893-.128-1.786 0-2.807
 0-.255.256-.384.383-.384a9.478 9.478 0 0 1 1.342-.095z" />
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
