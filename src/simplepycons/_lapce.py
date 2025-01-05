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


class LapceIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "lapce"

    @property
    def original_file_name(self) -> "str":
        return "lapce.svg"

    @property
    def title(self) -> "str":
        return "Lapce"

    @property
    def primary_color(self) -> "str":
        return "#3B82F6"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Lapce</title>
     <path d="M3.802 1.267 1.608 0v24L8 20.31v-2.535L3.802 20.2Zm4.208
 13.9V6.231L18.003 12l-7.798 4.503v2.533L22.392 12 5.806
 2.424V16.44Zm5.598-3.231L10.205 9.97v3.93Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/lapce/lapce/blob/95c4cf2d8'''

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
