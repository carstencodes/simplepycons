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


class MaxIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "max"

    @property
    def original_file_name(self) -> "str":
        return "max.svg"

    @property
    def title(self) -> "str":
        return "Max"

    @property
    def primary_color(self) -> "str":
        return "#525252"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Max</title>
     <path d="M1.769 0A1.77 1.77 0 0 0 0 1.769V22.23A1.77 1.77 0 0 0
 1.769 24H22.23A1.77 1.77 0 0 0 24 22.231V1.77A1.77 1.77 0 0 0 22.231
 0zm12.485 3.28a4.301 4.301 0 0 1 4.3 4.302 4.301 4.301 0 0 1-1.993
 3.63 6.085 6.085 0 0 1 1.054 3.422 6.085 6.085 0 0 1-6.085 6.085
 6.085 6.085 0 0 1-6.085-6.085 6.085 6.085 0 0 1 4.66-5.916 4.301
 4.301 0 0 1-.152-1.136 4.301 4.301 0 0 1 4.301-4.301zm0 1.849a2.453
 2.453 0 0 0-2.453 2.453 2.453 2.453 0 0 0 2.453 2.453 2.453 2.453 0 0
 0 2.453-2.453 2.453 2.453 0 0 0-2.453-2.453zm-2.724 5.268a4.237 4.237
 0 0 0-4.237 4.237 4.237 4.237 0 0 0 4.237 4.237 4.237 4.237 0 0 0
 4.237-4.237 4.237 4.237 0 0 0-4.237-4.237zm.032 2.54a1.781 1.781 0 1
 1 0 3.562 1.781 1.781 0 0 1 0-3.562Z" />
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
