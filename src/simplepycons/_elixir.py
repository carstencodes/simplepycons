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


class ElixirIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "elixir"

    @property
    def original_file_name(self) -> "str":
        return "elixir.svg"

    @property
    def title(self) -> "str":
        return "Elixir"

    @property
    def primary_color(self) -> "str":
        return "#4B275F"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Elixir</title>
     <path d="M19.793 16.575c0 3.752-2.927 7.426-7.743 7.426-5.249
 0-7.843-3.71-7.843-8.29 0-5.21 3.892-12.952 8-15.647a.397.397 0 0 1
 .61.371 9.716 9.716 0 0 0 1.694 6.518c.522.795 1.092 1.478 1.763
 2.352.94 1.227 1.637 1.906 2.644 3.842l.015.028a7.107 7.107 0 0 1 .86
 3.4z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/elixir-lang/elixir-lang.gi'''

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
