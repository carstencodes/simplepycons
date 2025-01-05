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


class BytedanceIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "bytedance"

    @property
    def original_file_name(self) -> "str":
        return "bytedance.svg"

    @property
    def title(self) -> "str":
        return "ByteDance"

    @property
    def primary_color(self) -> "str":
        return "#3C8CFF"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>ByteDance</title>
     <path d="M19.8772 1.4685L24 2.5326v18.9426l-4.1228
 1.0563V1.4685zm-13.3481 9.428l4.115 1.0641v8.9786l-4.115
 1.0642v-11.107zM0 2.572l4.115 1.0642v16.7354L0 21.428V2.572zm17.4553
 5.6205v11.107l-4.1228-1.0642V9.2568l4.1228-1.0642z" />
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
