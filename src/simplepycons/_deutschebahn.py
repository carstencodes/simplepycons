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


class DeutscheBahnIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "deutschebahn"

    @property
    def original_file_name(self) -> "str":
        return "deutschebahn.svg"

    @property
    def title(self) -> "str":
        return "Deutsche Bahn"

    @property
    def primary_color(self) -> "str":
        return "#F01414"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Deutsche Bahn</title>
     <path d="M21.6 3.6H2.4C1.08 3.6 0 4.68 0 6v12c0 1.32 1.08 2.4 2.4
 2.4h19.2c1.32 0 2.4-1.08 2.4-2.424V6c0-1.32-1.08-2.4-2.4-2.4zm.648
 14.376c.024.36-.264.672-.648.696H2.4c-.36
 0-.648-.312-.648-.672V6a.667.667 0 0 1 .624-.696H21.6c.36 0
 .648.312.648.672v12zM7.344 6.504H3.312v10.992h4.032c3.336-.024
 4.416-2.376 4.416-5.544 0-3.672-1.56-5.448-4.416-5.448zm-.456
 9.216h-.936V8.232h.528c2.376 0 2.616 1.728 2.616 3.936 0 2.424-.816
 3.552-2.208 3.552zm11.832-3.984c1.128-.336 1.896-1.368 1.92-2.568
 0-.24-.048-2.688-3.144-2.688h-4.584v10.992H16.8c1.032 0 4.248 0
 4.248-3.096 0-.744-.336-2.208-2.328-2.64zm-2.352-3.528c1.176 0
 1.656.408 1.656 1.32 0 .72-.528 1.32-1.44 1.32h-1.032v-2.64h.816zm.24
 7.512h-1.08v-2.832h1.152c1.368 0 1.704.792 1.704 1.416 0 1.416-1.344
 1.416-1.776 1.416z" />
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
