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


class NebulaIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "nebula"

    @property
    def original_file_name(self) -> "str":
        return "nebula.svg"

    @property
    def title(self) -> "str":
        return "Nebula"

    @property
    def primary_color(self) -> "str":
        return "#2CADFE"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Nebula</title>
     <path d="M7.417 9.307 0 14.693h9.167L12
 23.413l2.833-8.72H24s-3.915-2.84-7.417-5.386l2.834-8.72L12
 5.976C8.499 3.438 4.583.588 4.583.588z" />
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
