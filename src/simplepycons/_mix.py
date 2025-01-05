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


class MixIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "mix"

    @property
    def original_file_name(self) -> "str":
        return "mix.svg"

    @property
    def title(self) -> "str":
        return "Mix"

    @property
    def primary_color(self) -> "str":
        return "#FF8126"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Mix</title>
     <path d="M.001 0v21.61c0 1.32 1.074 2.39 2.4 2.39a2.396 2.396 0 0
 0 2.402-2.39V8.54c0 .014-.005.026-.006.04V6.364a2.395 2.395 0 0 1
 2.399-2.393 2.396 2.396 0 0 1 2.398 2.393v9.356a2.394 2.394 0 0 0
 2.398 2.393 2.394 2.394 0 0 0 2.398-2.39v-3.692a2.398 2.398 0 0 1
 2.385-2.078 2.4 2.4 0 0 1 2.41 2.389v1.214a2.397 2.397 0 0 0 2.408
 2.389 2.399 2.399 0 0 0 2.406-2.39V.006a4.61 4.61 0 0
 0-.145-.004c-1.31 0-2.558.264-3.693.74A9.449 9.449 0 0 1 23.841 0z"
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
