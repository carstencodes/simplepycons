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


class UdacityIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "udacity"

    @property
    def original_file_name(self) -> "str":
        return "udacity.svg"

    @property
    def title(self) -> "str":
        return "Udacity"

    @property
    def primary_color(self) -> "str":
        return "#02B3E4"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Udacity</title>
     <path d="M8 0L0 4.8v9.6C0 20.8 4.8 24 8.8 24c1.348 0 2.786-.362
 4.1-1.088l6.303-3.633C21.687 18.155 24 15.64 24 11.2V.8L22.4 0 16
 4v10.4c0 1.6-.3 2.898-.785
 3.948-2.002-.257-5.615-1.597-5.615-7.15V.802zm0 1.76v9.44c0 5.342
 3.346 7.9 6.313 8.597-1.618 1.99-4.025 2.603-5.512 2.603-2.4
 0-7.2-1.6-7.2-8V5.6zm14.4.04v9.4c0 5.45-3.482 6.84-5.504
 7.132.446-1.14.704-2.45.704-3.932V4.8z" />
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
