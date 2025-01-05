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


class InfinitiIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "infiniti"

    @property
    def original_file_name(self) -> "str":
        return "infiniti.svg"

    @property
    def title(self) -> "str":
        return "INFINITI"

    @property
    def primary_color(self) -> "str":
        return "#020B24"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>INFINITI</title>
     <path d="M1.953 11.643c0 1.51 1.83 2.69 4.601
 3.344l4.841-5.523H12l-4.19 8.06C3.25 16.744 0 14.71 0 12.233c0-3.184
 5.376-5.757 12-5.757s12 2.573 12 5.757c0 2.477-3.25 4.511-7.81
 5.293L12 9.464h.605l4.84 5.523c2.772-.654 4.601-1.834 4.601-3.344
 0-2.664-4.484-4.88-10.047-4.88-5.562 0-10.046 2.216-10.046 4.88z" />
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
