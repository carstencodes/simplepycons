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


class CodefactorIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "codefactor"

    @property
    def original_file_name(self) -> "str":
        return "codefactor.svg"

    @property
    def title(self) -> "str":
        return "CodeFactor"

    @property
    def primary_color(self) -> "str":
        return "#F44A6A"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>CodeFactor</title>
     <path d="M5.375 2.65a2.64 2.64 0 01-2.62 2.65 2.64 2.64 0
 01-2.63-2.65A2.64 2.64 0 012.755 0a2.64 2.64 0 012.62 2.65zm0
 9.35a2.64 2.64 0 01-2.62 2.65A2.64 2.64 0 01.125 12a2.64 2.64 0
 012.63-2.65A2.64 2.64 0 015.375 12zm0 9.35A2.64 2.64 0 012.755
 24a2.64 2.64 0 01-2.63-2.65 2.64 2.64 0 012.63-2.65 2.64 2.64 0
 012.62 2.65zM11.315 0a2.64 2.64 0 00-2.61 2.65 2.64 2.64 0 002.6
 2.65h9.94a2.64 2.64 0 002.63-2.65A2.64 2.64 0 0021.255 0zm-2.61
 12a2.64 2.64 0 012.62-2.65h5.68a2.64 2.64 0 012.6 2.65 2.64 2.64 0
 01-2.6 2.65h-5.7a2.64 2.64 0 01-2.6-2.65z" />
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
