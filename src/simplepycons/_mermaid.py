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


class MermaidIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "mermaid"

    @property
    def original_file_name(self) -> "str":
        return "mermaid.svg"

    @property
    def title(self) -> "str":
        return "Mermaid"

    @property
    def primary_color(self) -> "str":
        return "#FF3670"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Mermaid</title>
     <path d="M23.99 2.115A12.223 12.223 0 0 0 12 10.149 12.223 12.223
 0 0 0 .01 2.115a12.23 12.23 0 0 0 5.32 10.604 6.562 6.562 0 0 1 2.845
 5.423v3.754h7.65v-3.754a6.561 6.561 0 0 1 2.844-5.423 12.223 12.223 0
 0 0 5.32-10.604Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/mermaid-js/mermaid/blob/f5'''

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
