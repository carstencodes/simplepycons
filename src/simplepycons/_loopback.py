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


class LoopbackIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "loopback"

    @property
    def original_file_name(self) -> "str":
        return "loopback.svg"

    @property
    def title(self) -> "str":
        return "LoopBack"

    @property
    def primary_color(self) -> "str":
        return "#3F5DFF"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>LoopBack</title>
     <path d="m6.333 18.413 2.512-1.615 3.179 1.814 3.209-1.876 2.656
 1.515-5.849 3.418-5.707-3.256ZM5.273 6.239l6.687-3.907 6.73 3.839.022
 6.755-2.654-1.513-.011-3.701-4.071-2.322-4.05 2.367.011
 3.698-.903.526-1.739 1.118-.022-6.86Zm3.608 2.463 1.913 1.089-1.906
 1.11-.007-2.199Zm4.337 5.514 2.634-1.544 3.271 1.862
 2.221-1.296-.013-2.571-1.677-.957-.01-3.054 4.355 2.485.001
 5.611-4.859 2.841-5.923-3.377Zm-13.189.661L0 9.249l4.322-2.525.009
 3.061-1.675.979.013 2.57 2.234 1.274L15.098 8.66l.009 3.062-10.189
 5.944-4.889-2.789Z" />
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
