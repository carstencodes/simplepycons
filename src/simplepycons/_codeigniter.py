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


class CodeigniterIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "codeigniter"

    @property
    def original_file_name(self) -> "str":
        return "codeigniter.svg"

    @property
    def title(self) -> "str":
        return "CodeIgniter"

    @property
    def primary_color(self) -> "str":
        return "#EF4223"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>CodeIgniter</title>
     <path d="M11.466 0c.88 1.423-.28 3.306-1.207 4.358-.899
 1.02-1.992 1.873-2.985 2.8-1.066.996-2.091 2.044-2.967 3.213-1.753
 2.339-2.827 5.28-2.038 8.199.788 2.916 3.314 4.772 6.167
 5.429-1.44-.622-2.786-2.203-2.79-3.82-.003-1.765 1.115-3.262
 2.505-4.246-.167.632-.258 1.21.155 1.774a1.68 1.68 0 0 0
 1.696.642c1.487-.326
 1.556-1.96.674-2.914-.872-.943-1.715-2.009-1.384-3.377.167-.685.588-1.328
 1.121-1.787-.41 1.078.755 2.14 1.523 2.67 1.332.918 2.793 1.612 4.017
 2.688 1.288 1.132 2.24 2.661 2.047 4.435-.208 1.923-1.736 3.26-3.45
 3.936 3.622-.8 7.365-3.61
 7.44-7.627.093-3.032-1.903-5.717-5.158-7.384.19.48.074.697-.058.924-.55.944-2.082
 1.152-2.835.184-1.205-1.548.025-3.216.197-4.855.215-2.055-1.073-4.049-2.67-5.242z"
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
