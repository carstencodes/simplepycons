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


class DunkedIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "dunked"

    @property
    def original_file_name(self) -> "str":
        return "dunked.svg"

    @property
    def title(self) -> "str":
        return "Dunked"

    @property
    def primary_color(self) -> "str":
        return "#2DA9D7"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Dunked</title>
     <path d="M13.799 0v19.8599A4.2002 4.2002 0 0018.0003
 24h4.2002V4.1411A4.2002 4.2002 0 0017.9992 0H13.798zM6.2983
 15.0014a4.5008 4.5008 0 00-4.4988 4.3906v.2224a4.5008 4.5008 0
 008.9986 0v-.2154a4.5008 4.5008 0 00-4.4998-4.3986z" />
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
