#
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2026 Carsten Igel.
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


class TyIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "ty"

    @property
    def original_file_name(self) -> "str":
        return "ty.svg"

    @property
    def title(self) -> "str":
        return "ty"

    @property
    def primary_color(self) -> "str":
        return "#46EBE1"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>ty</title>
     <path d="M24 3.84H13.92V0h-12v3.84H0v9.12h1.92v7.147A3.893 3.893
 0 0 0 5.813 24H24v-9.12H13.92v-1.92h6.187A3.893 3.893 0 0 0 24
 9.067Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://docs.astral.sh/ty/assets/logo-letter.'''

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
