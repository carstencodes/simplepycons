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


class QwantIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "qwant"

    @property
    def original_file_name(self) -> "str":
        return "qwant.svg"

    @property
    def title(self) -> "str":
        return "Qwant"

    @property
    def primary_color(self) -> "str":
        return "#5C97FF"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Qwant</title>
     <path d="M11.39 0c5.322 0 9.652 4.46 9.652 9.944 0 5.358-4.132
 9.738-9.285 9.938l-.235.006h9.488L22.262
 24h-9.62l-1.253-4.11c-5.321-.001-9.65-4.462-9.65-9.946S6.067 0 11.388
 0zm0 3.364c-3.522 0-6.387 2.952-6.387 6.58 0 3.63 2.865 6.58 6.387
 6.58 3.522 0 6.387-2.95 6.387-6.58 0-3.628-2.865-6.58-6.387-6.58z" />
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
