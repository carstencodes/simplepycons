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


class GoogleAssistantIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "googleassistant"

    @property
    def original_file_name(self) -> "str":
        return "googleassistant.svg"

    @property
    def title(self) -> "str":
        return "Google Assistant"

    @property
    def primary_color(self) -> "str":
        return "#4285F4"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Google Assistant</title>
     <path d="M22.365 8.729c.9 0 1.635-.735
 1.635-1.635s-.735-1.636-1.635-1.636-1.636.735-1.636 1.636.723 1.635
 1.636 1.635m-4.907 5.452a3.27 3.27 0 1 0 0-6.542 3.27 3.27 0 0 0 0
 6.542m0 8.722c2.105 0 3.816-1.711
 3.816-3.829s-1.711-3.816-3.829-3.816a3.82 3.82 0 0 0-3.816 3.816
 3.825 3.825 0 0 0 3.829 3.83M6.542 14.18a6.542 6.542 0 1 0 0-13.084
 6.542 6.542 0 1 0 0 13.084" />
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
