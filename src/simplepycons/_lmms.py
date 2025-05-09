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


class LmmsIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "lmms"

    @property
    def original_file_name(self) -> "str":
        return "lmms.svg"

    @property
    def title(self) -> "str":
        return "LMMS"

    @property
    def primary_color(self) -> "str":
        return "#10B146"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>LMMS</title>
     <path d="M1.714 0A1.71 1.71 0 000 1.714v20.572C0 23.236.765 24
 1.714 24h20.572A1.71 1.71 0 0024 22.286V1.714A1.71 1.71 0 0022.286
 0zM12 3l9 5.143v10.286l-3 1.714-3-1.714V15l3-1.714V9.857L12 6.43 6
 9.857v3.429L9 15v3.429l-3 1.714-3-1.714V8.143Z" />
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
