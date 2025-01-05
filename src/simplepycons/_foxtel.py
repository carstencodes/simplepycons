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


class FoxtelIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "foxtel"

    @property
    def original_file_name(self) -> "str":
        return "foxtel.svg"

    @property
    def title(self) -> "str":
        return "Foxtel"

    @property
    def primary_color(self) -> "str":
        return "#EB5205"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Foxtel</title>
     <path d="M2.867
 10.631l.341-1.024H0v4.779h1.16v-1.72h1.434l.341-1.024H1.16v-1.01zm3.03-1.085a2.454
 2.454 0 1 0-.006 4.908 2.454 2.454 0 0 0 .007-4.908zm0 3.74a1.287
 1.287 0 1 1-.007-2.574 1.287 1.287 0 0 1 .008
 2.575zm6.506-3.679h-1.297l-.812 1.304-.82-1.304H8.177l1.468
 2.335-1.536 2.444h1.297l.888-1.405.88 1.405h1.297l-1.529-2.444zm.102
 1.024h1.413v3.755h1.16V10.63h1.23V9.607h-3.16zm7.304
 0l.341-1.024h-3.208v4.779h2.867l.341-1.024h-2.046v-.915h1.432l.341-1.024h-1.773v-.792zm2.143
 2.73V9.608h-1.16v4.779h2.867L24 13.362Z" />
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
