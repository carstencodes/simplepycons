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


class AnaIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "ana"

    @property
    def original_file_name(self) -> "str":
        return "ana.svg"

    @property
    def title(self) -> "str":
        return "ANA"

    @property
    def primary_color(self) -> "str":
        return "#13448F"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>ANA</title>
     <path d="M19.11 8.975l-3.454 6.05h3.432l3.455-6.05zm3.933
 0l-3.455 6.05h.959L24 8.975zm-10.01.781H14.8l.403
 5.27h-1.31l-.025-.58a.206.206 0 0
 0-.202-.227h-1.867l.429-.757h1.21c.151 0
 .328.026.328-.202l-.202-2.37c0-.15-.126-.226-.227-.075L11.193
 15h-.882zm-9.983 0h1.74l.353 5.27h-1.31l-.026-.58a.226.226 0 0
 0-.227-.227H1.563l.429-.757h1.386c.151 0
 .328.026.328-.202l-.151-2.37c0-.15-.126-.226-.227-.075L.882
 15H0zm3.278 0h1.79l1.16 4.084c.05.126.15.101.176
 0l.756-4.084h.782l-.933
 5.27H8.244l-1.135-4.034c-.025-.101-.151-.127-.176 0l-.706
 4.033h-.832Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://www.ana.co.jp/en/eur/the-ana-experien'''

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
