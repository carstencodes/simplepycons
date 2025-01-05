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


class InternetComputerIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "internetcomputer"

    @property
    def original_file_name(self) -> "str":
        return "internetcomputer.svg"

    @property
    def title(self) -> "str":
        return "Internet Computer"

    @property
    def primary_color(self) -> "str":
        return "#3B00B9"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Internet Computer</title>
     <path d="M18.264 6.24c-2.52 0-5.376 3.024-6.264
 3.984-.72-.792-3.696-3.984-6.264-3.984C2.568 6.24 0 8.832 0 12c0
 3.168 2.568 5.76 5.736 5.76 2.52 0 5.376-3.024 6.264-3.984.72.792
 3.696 3.984 6.264 3.984C21.432 17.76 24 15.168 24
 12c0-3.168-2.568-5.76-5.736-5.76ZM5.736 15.384A3.38 3.38 0 0 1 2.352
 12a3.395 3.395 0 0 1 3.384-3.384c1.176 0 3.24 1.8 4.68
 3.384-.408.456-3.144 3.384-4.68 3.384zm12.528 0c-1.176
 0-3.24-1.8-4.68-3.384.408-.456 3.168-3.384 4.68-3.384A3.38 3.38 0 0 1
 21.648 12c-.024 1.872-1.536 3.384-3.384 3.384z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://dfinity.frontify.com/d/pD7yZhsmpqos/i'''

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
        yield from [
            "Internet Computer Protocol",
        ]
