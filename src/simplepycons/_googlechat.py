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


class GoogleChatIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "googlechat"

    @property
    def original_file_name(self) -> "str":
        return "googlechat.svg"

    @property
    def title(self) -> "str":
        return "Google Chat"

    @property
    def primary_color(self) -> "str":
        return "#34A853"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Google Chat</title>
     <path d="M1.637 0C.733 0 0 .733 0 1.637v16.5c0 .904.733 1.636
 1.637 1.636h3.955v3.323c0 .804.97 1.207
 1.539.638l3.963-3.96h11.27c.903 0 1.636-.733 1.636-1.637V5.592L18.408
 0Zm3.955 5.592h12.816v8.59H8.455l-2.863 2.863Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://support.google.com/chat/answer/945538'''

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
