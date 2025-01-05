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


class BandsintownIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "bandsintown"

    @property
    def original_file_name(self) -> "str":
        return "bandsintown.svg"

    @property
    def title(self) -> "str":
        return "Bandsintown"

    @property
    def primary_color(self) -> "str":
        return "#00CEC8"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Bandsintown</title>
     <path d="M6.399
 12.8v4.8H19.2v1.6H4.799V0H0v24h24V12.8H6.399Zm4.801-8H6.399v6.4H11.2V4.8Zm6.4
 0h-4.8v6.4h4.8V4.8ZM24 0h-4.8v11.2H24V0Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://www.company.bandsintown.com/brand-ass'''

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
