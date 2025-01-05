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


class DashIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "dash"

    @property
    def original_file_name(self) -> "str":
        return "dash.svg"

    @property
    def title(self) -> "str":
        return "Dash"

    @property
    def primary_color(self) -> "str":
        return "#008DE4"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Dash</title>
     <path d="M3.21 9.967C.922 9.967.595 11.457.38 12.36.093 13.538 0
 14.02 0 14.02h8.947c2.29 0 2.617-1.492
 2.832-2.394.285-1.178.379-1.66.379-1.66zM15.72 2.26H6.982L6.26
 6.307l7.884.01c3.885 0 5.03 1.41 4.997 3.748-.019 1.196-.537
 3.225-.762 3.884-.598 1.753-1.827 3.749-6.435 3.744l-7.666-.004-.725
 4.052h8.718c3.075 0 4.38-.36 5.767-.995 3.071-1.426 4.9-4.455
 5.633-8.41C24.76 6.448 23.403 2.26 15.72 2.26z" />
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
