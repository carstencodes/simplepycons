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


class ImmersiveTranslateIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "immersivetranslate"

    @property
    def original_file_name(self) -> "str":
        return "immersivetranslate.svg"

    @property
    def title(self) -> "str":
        return "Immersive Translate"

    @property
    def primary_color(self) -> "str":
        return "#EA4C89"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Immersive Translate</title>
     <path d="M8.607
 4.008h-1.75v1.749H3.539v5.85h3.318v2.534h1.75v-2.533h3.317V5.757H8.607Zm-1.75
 3.498H5.289V9.86h1.568Zm1.75 2.353V7.506h1.568V9.86Zm12.065
 10.133-3.68-9.229h-1.75l-3.68 9.23h1.87l.954-2.474h3.462l.954
 2.473zm-3.499-4.222-1.056-2.738-1.056 2.738zm-9.471
 4.222h2.594v-1.749H7.702a1.57 1.57 0 0
 1-1.569-1.568v-1.75h-1.75v1.75a3.32 3.32 0 0 0 3.319
 3.317m5.851-15.14v1.75h2.594c.867 0 1.569.702 1.569
 1.568v1.81h1.75V8.17a3.32 3.32 0 0 0-3.319-3.318zM0 3.75A3.75 3.75 0
 0 1 3.75 0h16.5A3.75 3.75 0 0 1 24 3.75v16.5A3.75 3.75 0 0 1 20.25
 24H3.75A3.75 3.75 0 0 1 0 20.25Z" />
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
