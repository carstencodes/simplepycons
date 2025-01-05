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


class LiteralIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "literal"

    @property
    def original_file_name(self) -> "str":
        return "literal.svg"

    @property
    def title(self) -> "str":
        return "Literal"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Literal</title>
     <path d="m11.148 5.719.128-1.798 3.234.223-1.52-2.902
 1.63-.836L16.176 3.4l1.966-2.75 1.495 1.05-1.916 2.665 3.212.221-.128
 1.797-3.167-.217 1.498 2.878-1.628.836-1.578-3.017-1.99
 2.771-1.495-1.05L14.36 5.94zm-8.129 9.513L5.197 0l2.569.355-1.817
 12.708 5.978.825-.361 2.525zM20.981 21.7 4.328 24l-.36-2.524
 16.652-2.3z" />
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
