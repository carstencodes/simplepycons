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


class KyoceraIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "kyocera"

    @property
    def original_file_name(self) -> "str":
        return "kyocera.svg"

    @property
    def title(self) -> "str":
        return "Kyocera"

    @property
    def primary_color(self) -> "str":
        return "#DF0522"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Kyocera</title>
     <path d="M9.677 4.645L2.323 12V4.645h7.354zm-7.354
 14.71h7.355L2.323 12v7.355zm7.354 0L17.032 12 9.677
 4.645v14.71zM21.677 0h-7.355L9.677 4.645h7.355V12l4.645-4.645V0zm-12
 19.355L14.323 24h7.355v-7.355L17.032 12v7.355H9.677z" />
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
