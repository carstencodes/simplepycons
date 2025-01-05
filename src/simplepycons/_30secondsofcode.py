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


class ThirtySecondsOfCodeIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "30secondsofcode"

    @property
    def original_file_name(self) -> "str":
        return "30secondsofcode.svg"

    @property
    def title(self) -> "str":
        return "30 seconds of code"

    @property
    def primary_color(self) -> "str":
        return "#5395FD"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>30 seconds of code</title>
     <path d="M13.895 12c0 .734-.593 1.328-1.324 1.328h-.58a6.666
 6.666 0 0 1-.389 5.09 6.633 6.633 0 0 1-2.22 2.508 6.6 6.6 0 0
 1-9.028-1.619l-.044-.06c-.47-.563-.397-1.4.163-1.872a1.32 1.32 0 0 1
 1.864.164l.158.207a3.972 3.972 0 0 0 3.523 1.63 3.96 3.96 0 0 0
 3.226-2.163A3.997 3.997 0 0 0 7.771 12 3.977 3.977 0 0 0 9.45
 9.927a3.997 3.997 0 0 0-1.537-4.644 3.96 3.96 0 0
 0-5.417.971l-.158.208a1.32 1.32 0 0 1-1.864.163A1.332 1.332 0 0 1 .31
 4.754l.044-.061a6.622 6.622 0 0 1 2.583-2.128 6.595 6.595 0 0 1
 6.446.51 6.634 6.634 0 0 1 2.22 2.506 6.662 6.662 0 0 1 .389
 5.09h.58c.73 0 1.323.595 1.323 1.329Zm-.067 5.21a8.28 8.28 0 0
 1-1.196 2.811 6.628 6.628 0 0 0 4.717 1.964A6.654 6.654 0 0 0 24
 15.328V8.672a6.654 6.654 0 0 0-6.651-6.657c-1.844 0-3.513.75-4.717
 1.964a8.28 8.28 0 0 1 1.196 2.81 3.99 3.99 0 0 1 7.511
 1.883v6.656a3.992 3.992 0 0 1-7.51 1.883Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/Chalarangelo/30-seconds-of
-code/blob/44c0ba94857a7796026c6795c47e964126876d5a/logo/logo-resource'''

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
