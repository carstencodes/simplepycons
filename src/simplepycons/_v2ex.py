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


class VTwoExIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "v2ex"

    @property
    def original_file_name(self) -> "str":
        return "v2ex.svg"

    @property
    def title(self) -> "str":
        return "V2EX"

    @property
    def primary_color(self) -> "str":
        return "#1F1F1F"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>V2EX</title>
     <path d="M.671 1.933h13.821a1.342 1.342 0 0 1 .98.425l8.166
 8.725a1.342 1.342 0 0 1 0 1.834l-8.166 8.724a1.342 1.342 0 0
 1-.98.426H.673A.671.671 0 0 1 0
 21.395v-6.878h13.19l2.276-2.28a.336.336 0 0 0
 0-.474l-2.276-2.28H0V2.604a.671.671 0 0 1 .671-.671Z" />
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
