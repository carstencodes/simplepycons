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


class GameDeveloperIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "gamedeveloper"

    @property
    def original_file_name(self) -> "str":
        return "gamedeveloper.svg"

    @property
    def title(self) -> "str":
        return "Game Developer"

    @property
    def primary_color(self) -> "str":
        return "#E60012"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Game Developer</title>
     <path d="M23.955 11.956a.84.84 0 0 0-.837-.796H17.37V1.9c0-.019
 0-.037-.002-.055a.84.84 0 0 0-.494-.806A11.89 11.89 0 0 0 12 0a11.89
 11.89 0 0 0-8.454 3.515A11.983 11.983 0 0 0 .043 12c0 1.62.316
 3.192.94 4.672a11.928 11.928 0 0 0 2.563 3.813 11.96 11.96 0 0 0
 3.799 2.572C8.82 23.683 10.386 24 12 24c1.614 0 3.18-.317
 4.655-.943a11.905 11.905 0 0 0 3.799-2.572A11.983 11.983 0 0 0 23.957
 12c0-.014 0-.03-.002-.044Zm-4.685 7.343a10.24 10.24 0 0 1-7.272 3.022
 10.228 10.228 0 0 1-7.273-3.022A10.305 10.305 0 0 1 1.714 12a10.312
 10.312 0 0 1 6.281-9.511 10.212 10.212 0 0 1 4.003-.809 10.197 10.197
 0 0 1 3.694.688v8.792h-3.765a.84.84 0 0 0 0 1.68h3.729a3.78 3.78 0 0
 1-1.205 2.012 3.75 3.75 0 0 1-2.458.92A3.77 3.77 0 0 1 8.235 12a3.768
 3.768 0 0 1 3.758-3.772.84.84 0 0 0 0-1.68 5.385 5.385 0 0 0-3.841
 1.597A5.429 5.429 0 0 0 6.559 12c0 1.457.564 2.825 1.591 3.855a5.384
 5.384 0 0 0 3.841 1.597 5.431 5.431 0 0 0 3.555-1.329 5.46 5.46 0 0 0
 1.813-3.281h4.89a10.292 10.292 0 0 1-2.979 6.457Z" />
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
        yield from [
            "Gamasutra",
        ]
