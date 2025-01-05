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


class ElavonIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "elavon"

    @property
    def original_file_name(self) -> "str":
        return "elavon.svg"

    @property
    def title(self) -> "str":
        return "Elavon"

    @property
    def primary_color(self) -> "str":
        return "#0C2074"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Elavon</title>
     <path d="M12.028 12.248c-.38.9-.752 1.867-1.123 2.908a62.992
 62.992 0 00-1.016 3.13h.355a48.858 48.858 0
 011.76-4.79c.222-.513.446-.992.669-1.463-.215.066-.43.132-.645.215zm7.32-5.717c-.389-1.148-.959-1.735-1.694-1.735h-.008c-1.347
 0-3.024 1.983-4.693 5.403.29-.107.579-.206.86-.306 1.164-1.957
 2.271-3.114 3.073-3.114h.074c.446.041.777.47.967 1.28.495 2.082-.05
 6.163-1.264 10.467.933.058 1.751.29 2.437.678.933-5.362
 1.098-10.17.248-12.673zM18.1
 10.422c0-.429.85.132-.033-1.47-4.378.371-10.525 3.18-16.217
 7.765-.644.52-1.263 1.041-1.85 1.57h.363c.108-.083.207-.174.314-.265
 5.99-4.816 12.533-7.616 16.977-7.616.149 0
 .297.008.446.016zm2.255-1.397c.072.629.11 1.26.116 1.893a4.01 4.01 0
 011.33.893c.81.826 1.174 1.956 1.092 3.369-.058.958-.324 2.008-.77
 3.115h.24c.967-1.76 1.536-3.412
 1.627-4.85.075-1.355-.28-2.436-1.049-3.22-.627-.645-1.52-1.026-2.586-1.2Z"
 />
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
