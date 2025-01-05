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


class SquareIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "square"

    @property
    def original_file_name(self) -> "str":
        return "square.svg"

    @property
    def title(self) -> "str":
        return "Square"

    @property
    def primary_color(self) -> "str":
        return "#3E4348"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Square</title>
     <path d="M4.01 0A4.01 4.01 0 000 4.01v15.98c0 2.21 1.8 4 4.01
 4.01h15.98C22.2 24 24 22.2 24 19.99V4A4.01 4.01 0 0019.99 0H4zm1.62
 4.36h12.74c.7 0 1.26.57 1.26 1.27v12.74c0 .7-.56 1.27-1.26
 1.27H5.63c-.7 0-1.26-.57-1.26-1.27V5.63a1.27 1.27 0 011.26-1.27zm3.83
 4.35a.73.73 0 00-.73.73v5.09c0 .4.32.72.72.72h5.1a.73.73 0
 00.73-.72V9.44a.73.73 0 00-.73-.73h-5.1Z" />
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
