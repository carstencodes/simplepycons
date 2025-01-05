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


class WikiquoteIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "wikiquote"

    @property
    def original_file_name(self) -> "str":
        return "wikiquote.svg"

    @property
    def title(self) -> "str":
        return "Wikiquote"

    @property
    def primary_color(self) -> "str":
        return "#006699"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Wikiquote</title>
     <path d="M10.152 12a4.037 4.037 0 1 1-8.075 0 4.037 4.037 0 0 1
 8.075 0zM17.292.822c-.286-.287-.581-.56-.885-.822l-1.528 1.527C17.872
 4.036 19.778 7.8 19.778 12s-1.906 7.964-4.899 10.473L16.407
 24c.304-.262.6-.535.886-.822A15.705 15.705 0 0 0 21.923
 12c0-4.223-1.644-8.192-4.63-11.178zM13.508 2.9L12.03 4.377a9.642
 9.642 0 0 1 0 15.246l1.477 1.477a11.712 11.712 0 0 0 0-18.2zm-2.735
 2.735L9.349 7.057c1.61 1.057 2.675 2.878 2.675 4.943s-1.065
 3.886-2.675 4.943l1.423 1.422A7.884 7.884 0 0 0 14.005 12a7.884 7.884
 0 0 0-3.233-6.365z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://commons.wikimedia.org/wiki/File:Wikiq'''

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
