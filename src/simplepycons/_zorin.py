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


class ZorinIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "zorin"

    @property
    def original_file_name(self) -> "str":
        return "zorin.svg"

    @property
    def title(self) -> "str":
        return "Zorin"

    @property
    def primary_color(self) -> "str":
        return "#15A6F0"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Zorin</title>
     <path d="M4 18.944L5.995 22.4h12.01L20 18.944H4zM24 12l-2.013
 3.488H9.216l12.771-6.976L24 12zM0 12l2.013-3.488h12.771L2.013 15.488
 0 12zm4-6.944L5.995 1.6h12.01L20 5.056H4z" />
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
