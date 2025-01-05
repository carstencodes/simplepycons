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


class AirasiaIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "airasia"

    @property
    def original_file_name(self) -> "str":
        return "airasia.svg"

    @property
    def title(self) -> "str":
        return "AirAsia"

    @property
    def primary_color(self) -> "str":
        return "#FF0000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>AirAsia</title>
     <path d="M11.54 14.49c-1.278 0-2.264-.998-2.264-2.276
 0-1.252.98-2.27 2.264-2.27 1.232 0 2.238 1.018 2.238 2.27 0
 1.278-1.005 2.277-2.239
 2.277zm3.074-7.854l-.214.998c-.59-1.18-2.348-1.297-3.295-1.297-2.952
 0-5.527 2.841-5.527 6.746 0 3.14 1.875 5.111 4.23 5.111 1.316 0
 2.432-.304 3.353-1.4l-.24
 1.102h3.711l1.692-11.26c-1.238-.001-2.482.01-3.71 0zM12 0c6.63 0 12
 5.37 12 12s-5.37 12-12 12S0 18.63 0 12 5.37 0 12 0Z" />
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
