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


class CozeIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "coze"

    @property
    def original_file_name(self) -> "str":
        return "coze.svg"

    @property
    def title(self) -> "str":
        return "Coze"

    @property
    def primary_color(self) -> "str":
        return "#4D53E8"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Coze</title>
     <path d="M9.366 12.096a.61.61 0 0 0-.608.608v1.218a.609.609 0 1 0
 1.217 0v-1.218a.61.61 0 0 0-.609-.608m.8 3.453a.605.605 0 0 1
 0-.86.605.605 0 0 1 .859 0 1.52 1.52 0 0 0 2.149 0 .605.605 0 0 1
 .859 0 .605.605 0 0 1 0 .86 2.73 2.73 0 0 1-3.867 0m4.062-2.24a.61.61
 0 1 1 .609.609.606.606 0 0 1-.61-.609zM3.023 0A3.024 3.024 0 0 0 0
 3.023v17.954A3.024 3.024 0 0 0 3.023 24h17.954A3.024 3.024 0 0 0 24
 20.977V3.023A3.024 3.024 0 0 0 20.977 0ZM12.1 3.78h.004a6.287 6.287 0
 0 1 6.283 6.286v2.635h1.508c1.73 0 2.12 2.426.476
 2.97l-1.984.663v1.137a1.513 1.513 0 0 1-2.19
 1.353l-1.101-.549c-.052-.024-.115 0-.131.055-.892 2.785-4.835
 2.785-5.727 0a.095.095 0 0 0-.13-.055l-1.102.55a1.513 1.513 0 0
 1-2.19-1.354v-1.139l-1.984-.66c-1.647-.541-1.254-2.97.477-2.97h1.507v-2.636A6.285
 6.285 0 0 1 12.1 3.78" />
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
