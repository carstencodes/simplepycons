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


class ServerFaultIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "serverfault"

    @property
    def original_file_name(self) -> "str":
        return "serverfault.svg"

    @property
    def title(self) -> "str":
        return "Server Fault"

    @property
    def primary_color(self) -> "str":
        return "#E7282D"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Server Fault</title>
     <path d="M24
 18.185v2.274h-4.89v-2.274H24zm-24-.106h11.505v2.274H0zm12.89
 0h4.89v2.274h-4.89zm6.221-3.607H24v2.274h-4.89l.001-2.274zM0
 14.367h11.505v2.274H0v-2.274zm12.89
 0h4.89v2.274h-4.89v-2.274zm6.221-3.346H24v2.273h-4.89l.001-2.273zM0
 10.916h11.505v2.271H0v-2.271zm12.89
 0h4.89v2.271h-4.89v-2.271zm6.22-3.609H24v2.279h-4.89V7.307zM0
 7.206h11.505V9.48H0V7.201zm12.89
 0h4.89V9.48h-4.89V7.201zm6.221-3.556H24v2.276h-4.89v-2.28l.001.004zM0
 3.541h11.505v2.274H0V3.541zm12.89 0h4.89v2.274h-4.89V3.541z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://stackoverflow.com/legal/trademark-gui'''
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
