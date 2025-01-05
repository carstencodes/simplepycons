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


class AlgoliaIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "algolia"

    @property
    def original_file_name(self) -> "str":
        return "algolia.svg"

    @property
    def title(self) -> "str":
        return "Algolia"

    @property
    def primary_color(self) -> "str":
        return "#003DFF"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Algolia</title>
     <path d="M12 0C5.445 0 .103 5.285.01 11.817c-.097 6.634 5.285
 12.131 11.92 12.17a11.91 11.91 0 0 0 5.775-1.443.281.281 0 0 0
 .052-.457l-1.122-.994a.79.79 0 0 0-.833-.14 9.693 9.693 0 0
 1-3.923.77c-5.36-.067-9.692-4.527-9.607-9.888.084-5.293 4.417-9.573
 9.73-9.573h9.73v17.296l-5.522-4.907a.407.407 0 0 0-.596.063 4.52 4.52
 0 0 1-3.934 1.793 4.538 4.538 0 0 1-4.192-4.168 4.53 4.53 0 0 1
 4.512-4.872 4.532 4.532 0 0 1 4.509
 4.126c.018.205.11.397.265.533l1.438 1.275a.28.28 0 0 0 .462-.158 6.82
 6.82 0 0 0
 .099-1.725c-.232-3.376-2.966-6.092-6.345-6.3-3.873-.24-7.11
 2.79-7.214 6.588-.1 3.7 2.933 6.892 6.634 6.974a6.75 6.75 0 0 0
 4.136-1.294l7.212 6.394a.48.48 0 0 0 .797-.36V.456A.456.456 0 0 0
 23.54 0Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://algolia.frontify.com/d/1AZwVNcFZiu7/s'''

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
