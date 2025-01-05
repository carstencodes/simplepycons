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


class MeilisearchIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "meilisearch"

    @property
    def original_file_name(self) -> "str":
        return "meilisearch.svg"

    @property
    def title(self) -> "str":
        return "Meilisearch"

    @property
    def primary_color(self) -> "str":
        return "#FF5CAA"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Meilisearch</title>
     <path d="m6.505 18.998 4.434-11.345a4.168 4.168 0 0 1
 3.882-2.651h2.674l-4.434 11.345a4.169 4.169 0 0 1-3.883
 2.651H6.505Zm6.505 0 4.434-11.345a4.169 4.169 0 0 1
 3.883-2.651H24l-4.434 11.345a4.168 4.168 0 0 1-3.882
 2.651H13.01Zm-13.01 0L4.434 7.653a4.168 4.168 0 0 1
 3.882-2.651h2.674L6.556 16.347a4.169 4.169 0 0 1-3.883 2.651H0Z" />
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
