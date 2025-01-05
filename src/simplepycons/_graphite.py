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


class GraphiteIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "graphite"

    @property
    def original_file_name(self) -> "str":
        return "graphite.svg"

    @property
    def title(self) -> "str":
        return "Graphite"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Graphite</title>
     <path d="m15.215 0-12 3.215-3.215 12L8.785 24l12-3.215
 3.215-12L15.215 0Zm1.958 20.966H6.827L1.655
 12l5.172-8.966h10.346L22.345 12l-5.172 8.966Zm.68-14.823L9.86 4 4.006
 9.858l2.14 8 7.995 2.141 5.853-5.857-2.14-8Z" />
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
