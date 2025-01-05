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


class ProtractorIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "protractor"

    @property
    def original_file_name(self) -> "str":
        return "protractor.svg"

    @property
    def title(self) -> "str":
        return "Protractor"

    @property
    def primary_color(self) -> "str":
        return "#ED163A"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Protractor</title>
     <path d="M12 0C5.37 0 0 5.372 0 12s5.371 12 12 12c6.628 0
 12-5.372 12-12S18.627 0 12 0zm-.273 3.789v1.71h.545v-1.71a9.055 9.055
 0 015.961 2.468l-1.277 1.278.386.386 1.277-1.278a9.057 9.057 0
 012.469 5.96h-1.71v.546h1.717v2.001H2.905v-2H4.62v-.546h-1.71a9.058
 9.058 0 012.469-5.96L6.658 7.92l.386-.386-1.278-1.278a9.056 9.056 0
 015.96-2.468zM12 6.965a5.912 5.912 0 00-5.913 5.912h11.824A5.91 5.91
 0 0012 6.965z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/angular/protractor/blob/4b'''

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
