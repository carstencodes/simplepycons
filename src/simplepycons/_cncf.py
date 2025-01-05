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


class CncfIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "cncf"

    @property
    def original_file_name(self) -> "str":
        return "cncf.svg"

    @property
    def title(self) -> "str":
        return "CNCF"

    @property
    def primary_color(self) -> "str":
        return "#231F20"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>CNCF</title>
     <path d="M0 0v24h24V0H8.004Zm3.431 3.431h4.544l.029.023 4.544
 4.544h3.03l-4.572-4.567h9.569v9.563l-.789-.782-3.784-3.79v3.03l2.271
 2.272 2.272
 2.272.029.03v4.543h-4.55l-.023-.023-2.272-2.278-2.272-2.272H8.427l3.785
 3.79.782.783H3.43v-9.563l4.573 4.567v-3.031l-4.55-4.544-.023-.023Z"
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
        return '''https://github.com/cncf/artwork/blob/d2ed716c'''

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
