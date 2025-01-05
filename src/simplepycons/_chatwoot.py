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


class ChatwootIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "chatwoot"

    @property
    def original_file_name(self) -> "str":
        return "chatwoot.svg"

    @property
    def title(self) -> "str":
        return "Chatwoot"

    @property
    def primary_color(self) -> "str":
        return "#1F93FF"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Chatwoot</title>
     <path d="M0 12c0 6.629 5.371 12 12 12s12-5.371 12-12S18.629 0 12
 0 0 5.371 0 12m17.008 5.29H11.44a5.57 5.57 0 0 1-5.562-5.567A5.57
 5.57 0 0 1 11.44 6.16a5.57 5.57 0 0 1 5.567 5.563Z" />
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
