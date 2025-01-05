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


class HandshakeIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "handshake"

    @property
    def original_file_name(self) -> "str":
        return "handshake.svg"

    @property
    def title(self) -> "str":
        return "Handshake"

    @property
    def primary_color(self) -> "str":
        return "#D3FB52"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Handshake</title>
     <path d="M20.728 0 16.49 24h-4.583l1.87-10.532-4.743 3.893L7.856
 24H3.272L7.51 0h4.582L9.806 13.012l4.729-3.862L16.145 0h4.583z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://joinhandshake.com/career-centers/mark'''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://joinhandshake.com/career-centers/mark'''

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
