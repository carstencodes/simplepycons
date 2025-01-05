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


class SorianaIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "soriana"

    @property
    def original_file_name(self) -> "str":
        return "soriana.svg"

    @property
    def title(self) -> "str":
        return "Soriana"

    @property
    def primary_color(self) -> "str":
        return "#D52B1E"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Soriana</title>
     <path d="M18.994 3.2c-1.16 0-2.772.494-3.94
 2.104-.223.314-.39.664-.494 1.034a4.27 4.27 0 0 0 .678 3.692c.6.812
 1.368 1.42 2.044 1.96.332.26 1.034.926 1.26 1.208.34.422.596.674.902
 1.606.186.564.212 1.308.12 1.73C21.684 14.384 24 11.594 24
 8.56c0-3.486-2.498-5.36-5.006-5.36M15.05
 14.986c-.886-1.204-1.908-1.936-2.754-2.706-.368-.336-.772-.584-1.07-.88-1.434-1.424-2.102-3.18-1.764-5.34.268-1.692
 1.108-2.806 2.124-3.622a7.098 7.098 0 0 0-4.278-1.372C3.274 1.066-.1
 4.31.002 8.306c.184 7.22 9.224 13.37 12.948 14.628 1.992-1.02
 3.05-2.928 3.05-4.884 0-1.426-.612-2.6-.95-3.064" />
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
