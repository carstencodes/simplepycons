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


class FontAwesomeIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "fontawesome"

    @property
    def original_file_name(self) -> "str":
        return "fontawesome.svg"

    @property
    def title(self) -> "str":
        return "Font Awesome"

    @property
    def primary_color(self) -> "str":
        return "#538DD7"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Font Awesome</title>
     <path d="M4.3934 4.5c.6837-.4317 1.1379-1.194
 1.1379-2.0625C5.5313 1.0913 4.4398 0 3.0938 0 1.7475 0 .6563
 1.0913.6563 2.4375c0 .7805.3668 1.4753.9375
 1.9214V24h3v-3h17.5126c.6834 0 1.2373-.554 1.2373-1.2373a1.237 1.237
 0 0 0-.1066-.5027l-2.8934-6.51 2.8934-6.51a1.237 1.237 0 0 0
 .1066-.5026c0-.6834-.5539-1.2374-1.2373-1.2374Z" />
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
