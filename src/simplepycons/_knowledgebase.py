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


class KnowledgebaseIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "knowledgebase"

    @property
    def original_file_name(self) -> "str":
        return "knowledgebase.svg"

    @property
    def title(self) -> "str":
        return "KnowledgeBase"

    @property
    def primary_color(self) -> "str":
        return "#9146FF"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>KnowledgeBase</title>
     <path d="M20.1 5.52V1.5h-.18c-3.36.15-6.15 2.31-7.83
 4.02l-.09.09-.09-.09C10.2 3.81 7.44 1.65 4.08 1.5H3.9v4.02H0v6.93c0
 1.68.06 3.36.18 4.74a5.57 5.57 0 005.19 5.1c2.13.12 4.38.21
 6.63.21s4.5-.09 6.63-.24a5.57 5.57 0
 005.19-5.1c.12-1.38.18-3.06.18-4.74v-6.9zm0 6.93c0 1.59-.06 3.15-.18
 4.41-.09.81-.75 1.47-1.56 1.5a90 90 0 01-12.72
 0c-.81-.03-1.5-.69-1.56-1.5-.12-1.26-.18-2.85-.18-4.41V5.52c2.82.12
 5.64 3.15 6.48 4.32L12 12.09l1.62-2.25c.84-1.2 3.66-4.2 6.48-4.32z"
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
