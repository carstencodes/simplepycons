#
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2024 Carsten Igel.
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


class ThanosIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "thanos"

    @property
    def original_file_name(self) -> "str":
        return "thanos.svg"

    @property
    def title(self) -> "str":
        return "Thanos"

    @property
    def primary_color(self) -> "str":
        return "#6D41FF"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Thanos</title>
     <path d="M0 0v24h16.998A7.002 7.002 0 0 0 24 16.998V0Zm18.707
 15.129h.896v.895h-.896zm-.281-3.857h1.455v1.456h-1.455Zm-.224-3.801h1.903v1.905h-1.903Zm-3.073
 11.234h.895v.896h-.896zm-.28-3.902h1.456v1.457h-1.456zm-.224-3.755h1.906v1.904h-1.904Zm.224-1.897V7.696h1.456V9.15Zm-6.874
 9.554h.896v.896h-.896Zm-.28-3.856h1.456v1.454H7.695Zm.28-2.401v-.896h.896v.896zm-.28-4.752h1.456V9.15H7.695ZM4.4
 18.706h.897v.895h-.897Zm0-3.577h.897v.895h-.897Zm-.28-3.857h1.455v1.456H4.12Zm-.224-3.801h1.904v1.905H3.895Zm-.837-4.413H20.94v3.577h-7.153v14.307h-3.576V6.635H3.058Z"
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