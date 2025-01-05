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


class EslintIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "eslint"

    @property
    def original_file_name(self) -> "str":
        return "eslint.svg"

    @property
    def title(self) -> "str":
        return "ESLint"

    @property
    def primary_color(self) -> "str":
        return "#4B32C3"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>ESLint</title>
     <path d="M7.257 9.132L11.816 6.5a.369.369 0 0 1 .368 0l4.559
 2.632a.369.369 0 0 1 .184.32v5.263a.37.37 0 0 1-.184.319l-4.559
 2.632a.369.369 0 0 1-.368 0l-4.559-2.632a.369.369 0 0
 1-.184-.32V9.452a.37.37 0 0 1 .184-.32M23.852
 11.53l-5.446-9.475c-.198-.343-.564-.596-.96-.596H6.555c-.396
 0-.762.253-.96.596L.149 11.509a1.127 1.127 0 0 0 0 1.117l5.447
 9.398c.197.342.563.517.959.517h10.893c.395 0
 .76-.17.959-.512l5.446-9.413a1.069 1.069 0 0 0 0-1.086m-4.51
 4.556a.4.4 0 0 1-.204.338L12.2 20.426a.395.395 0 0 1-.392
 0l-6.943-4.002a.4.4 0 0 1-.205-.338V8.08c0-.14.083-.269.204-.338L11.8
 3.74c.12-.07.272-.07.392 0l6.943 4.003a.4.4 0 0 1 .206.338z" />
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
