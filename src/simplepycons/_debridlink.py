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


class DebridlinkIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "debridlink"

    @property
    def original_file_name(self) -> "str":
        return "debridlink.svg"

    @property
    def title(self) -> "str":
        return "Debrid-Link"

    @property
    def primary_color(self) -> "str":
        return "#264E70"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Debrid-Link</title>
     <path d="M.225 5.549 0 5.778v2.484l.253.25h2.912c3.16 0 3.252.003
 3.75.146 1.053.3 1.658 1.022 1.893 2.256.052.27.059.395.06 1.034 0
 .635-.008.766-.058 1.044-.256 1.401-.98 2.149-2.308
 2.382-.252.045-.446.05-2.14.05H2.497l-.013-2.335-.014-2.335-.222-.207H.227L0
 10.769v7.379l.253.249h2.774c1.526-.001 2.96-.013 3.184-.027
 1.906-.117 3.257-.803
 4.114-2.09.512-.77.81-1.654.98-2.905.06-.456.07-2.266.012-2.736-.141-1.158-.44-2.1-.9-2.84-.67-1.077-1.743-1.81-3.056-2.087-.708-.15-.514-.142-3.951-.153Zm12.614.002-.233.232.01
 4.94c.008 4.933.008 4.938.065 5.229.086.439.155.66.298.96.394.828.996
 1.27 2.008 1.475.206.042.581.047 4.491.055l4.267.01L24
 18.2v-2.489l-.24-.236-3.878-.013-3.878-.013-.152-.062a1.03 1.03 0 0
 1-.601-.605c-.133-.35-.13-.258-.131-4.775l-.001-4.226-.23-.23h-1.026z"
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