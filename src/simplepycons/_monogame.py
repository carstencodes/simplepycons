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


class MonogameIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "monogame"

    @property
    def original_file_name(self) -> "str":
        return "monogame.svg"

    @property
    def title(self) -> "str":
        return "MonoGame"

    @property
    def primary_color(self) -> "str":
        return "#E73C00"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>MonoGame</title>
     <path d="M24 10.356V7.083a7.083 7.083 0 0 0-12-5.098A7.083 7.083
 0 0 0 0 7.083v9.834A7.083 7.083 0 0 0 7.083 24h9.834a7.083 7.083 0 0
 0 7.07-7.51H24v-4.332H9.834v4.332h9.834v.427a2.751 2.751 0 0 1-2.751
 2.751H7.083a2.751 2.751 0 0 1-2.751-2.751V7.083a2.751 2.751 0 1 1
 5.502 0v3.273h4.332V7.083a2.751 2.751 0 1 1 5.502 0v3.273z" />
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
