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


class UnocssIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "unocss"

    @property
    def original_file_name(self) -> "str":
        return "unocss.svg"

    @property
    def title(self) -> "str":
        return "UnoCSS"

    @property
    def primary_color(self) -> "str":
        return "#333333"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>UnoCSS</title>
     <path d="M12.8602 18.3991c0-3.0761 2.4938-5.5699 5.5699-5.5699S24
 15.323 24 18.3991c0 3.0762-2.4938 5.5699-5.5699
 5.5699s-5.5699-2.4937-5.5699-5.5699ZM12.8602 5.6009c0-3.0762
 2.4938-5.57 5.5699-5.57S24 2.5248 24 5.601v5.0129a.557.557 0 0
 1-.557.5569H13.4172a.557.557 0 0 1-.557-.5569v-5.013ZM11.1398
 18.3991c0 3.0762-2.4937 5.5699-5.5699 5.5699C2.4937 23.969 0 21.4753
 0 18.3991v-5.0129a.557.557 0 0 1 .557-.557h10.0258a.557.557 0 0 1
 .557.557v5.0129Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/unocss/unocss/blob/fc2ed5b'''

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
