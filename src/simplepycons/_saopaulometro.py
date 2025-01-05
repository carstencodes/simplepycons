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


class SaoPauloMetroIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "saopaulometro"

    @property
    def original_file_name(self) -> "str":
        return "saopaulometro.svg"

    @property
    def title(self) -> "str":
        return "São Paulo Metro"

    @property
    def primary_color(self) -> "str":
        return "#004382"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>São Paulo Metro</title>
     <path d="M13.366 6.543l5.092 5.456-5.092 5.456V6.543zM24
 0v24H0V0h24zm-5.542 11.999l1.747-1.872L11.976 1.9l-8.227 8.228 1.747
 1.871-1.747 1.871 8.227 8.229 8.228-8.229-1.746-1.871zm-7.87
 5.455V6.543l-5.092 5.456 5.092 5.455z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://commons.wikimedia.org/wiki/File:Sao_P'''

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
