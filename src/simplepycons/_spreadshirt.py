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


class SpreadshirtIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "spreadshirt"

    @property
    def original_file_name(self) -> "str":
        return "spreadshirt.svg"

    @property
    def title(self) -> "str":
        return "Spreadshirt"

    @property
    def primary_color(self) -> "str":
        return "#00B2A5"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Spreadshirt</title>
     <path d="M12 6.306L7.796 2.102 0 9.898l12 12 12-12-7.796-7.796zm0
 12L3.592 9.898l4.204-4.204L12 9.898l4.184-4.184 4.204 4.204" />
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
