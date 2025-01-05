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


class KauflandIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "kaufland"

    @property
    def original_file_name(self) -> "str":
        return "kaufland.svg"

    @property
    def title(self) -> "str":
        return "Kaufland"

    @property
    def primary_color(self) -> "str":
        return "#E10915"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Kaufland</title>
     <path d="M0 24h24V0H0zm23.008-.989H.989V.989h22.022zM3.773
 3.776h7.651v7.65H3.773zm8.801 0v7.652l7.653-7.652zm-8.801
 8.8h7.651v7.651H3.773zm8.801-.004v7.652h7.653z" />
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
