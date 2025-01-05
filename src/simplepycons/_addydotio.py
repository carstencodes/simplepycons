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


class AddydotioIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "addydotio"

    @property
    def original_file_name(self) -> "str":
        return "addydotio.svg"

    @property
    def title(self) -> "str":
        return "addy.io"

    @property
    def primary_color(self) -> "str":
        return "#19216C"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>addy.io</title>
     <path d="M18 6.81V6c0-.305-.033-.605-.075-.9C17.489 2.217 15 0 12
 0S6.51 2.217 6.075 5.1A5.733 5.733 0 0 0 6 6v.81A5.987 5.987 0 0 0 3
 12v6a6 6 0 0 0 6 6h6c0-1.655-1.345-3-3-3H9c-1.655
 0-3-1.345-3-3v-6c0-1.655 1.345-3 3-3h6c1.655 0 3 1.345 3 3v1.5a3 3 0
 0 1-1.5 2.597V12c0-.83-.67-1.5-1.5-1.5H9c-.83 0-1.5.67-1.5 1.5v6c0
 .83.67 1.5 1.5 1.5h6c1.055 0 2.04-.272 2.902-.75A5.996 5.996 0 0 0 21
 13.5V12a5.987 5.987 0 0 0-3-5.19Zm-4.5 9.69h-3v-3h3zM9
 6c0-.548.15-1.06.408-1.5A2.998 2.998 0 0 1 12 3c1.106 0 2.077.605
 2.592 1.5.258.44.408.952.408 1.5Z" />
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
