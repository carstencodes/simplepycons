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


class SparkfunIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "sparkfun"

    @property
    def original_file_name(self) -> "str":
        return "sparkfun.svg"

    @property
    def title(self) -> "str":
        return "SparkFun"

    @property
    def primary_color(self) -> "str":
        return "#E53525"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>SparkFun</title>
     <path d="M16.307
 5.476c-.756.134-1.975-.615-2.59-1.362-.755-.922-.66-1.647-.071-2.29.883-.978
 2.396-.6 2.396-.6s-2.772-2.432-5.658-.44c-2.571 1.77-1.833 4.183.487
 6.288 2.09 1.902.42 3.988-1.686
 3.717-1.443-.184-2.034-1.343-1.687-2.054.298-.608 1.335-.982
 1.335-.982s-1.19-.484-2.592.044c-1.259.474-2.297 1.515-2.214
 4.12V24s1.301-1.604 2.83-3.236c1.714-1.84 2.495-3.084 4.254-2.938
 3.328.205 5.735-1.273 7.371-3.645 3.141-4.563.67-9.68-1.43-10.343 0 0
 .34 1.438-.745 1.638z" />
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
