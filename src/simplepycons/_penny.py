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


class PennyIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "penny"

    @property
    def original_file_name(self) -> "str":
        return "penny.svg"

    @property
    def title(self) -> "str":
        return "Penny"

    @property
    def primary_color(self) -> "str":
        return "#CD1414"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Penny</title>
     <path d="M2.053 11.914h.368c.419 0
 .675-.245.718-.556.043-.27-.154-.556-.547-.556H2.24zm18.611-.638.839-1.504h1.924l-2.908
 4.399H18.56l.933-1.26-1.07-3.049-.727 4.309h-1.54l-.949-2.036-.342
 2.036h-1.54l.745-4.4h1.582l.915 1.971.334-1.97h3.37l.393
 1.504zm-7.21-1.504-.744 4.399h-1.54l-.949-2.036-.342
 2.036h-1.54l.745-4.4h1.582l.915 1.971.334-1.97h1.539zM3.036
 9.707c1.07 0 1.788.547 1.797 1.438l.23-1.373h3.49l-.188
 1.112H6.517l-.094.523h1.668l-.188 1.104H6.235l-.094.548h1.873l-.188
 1.112H4.32l.402-2.38c-.273.77-1.009 1.227-1.967 1.227h-.88l-.198
 1.153H0l.753-4.464zM24 13.345c0 .523-.445.948-.992.948-.547
 0-.992-.425-.992-.948
 0-.523.445-.948.992-.948.556.008.992.425.992.948z" />
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
