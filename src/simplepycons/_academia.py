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


class AcademiaIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "academia"

    @property
    def original_file_name(self) -> "str":
        return "academia.svg"

    @property
    def title(self) -> "str":
        return "Academia"

    @property
    def primary_color(self) -> "str":
        return "#41454A"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Academia</title>
     <path d="M22.033 21.18L13.77.459H7.869l1.049 2.623L1.836
 21.18C1.574 22.098.787 22.23 0 22.361v1.18h6.82v-1.18C4.984 22.23
 3.934 21.967 4.721 20c.131-.131.656-1.574 1.311-3.41h8.393l1.18
 3.016c.131.525.262.918.262 1.311 0 1.049-.918 1.443-2.623
 1.443v1.18H24v-1.18c-.918-.13-1.705-.393-1.967-1.18zM6.82
 14.361a363.303 363.303 0 0 0 3.279-8.525l3.41 8.525H6.82z" />
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
