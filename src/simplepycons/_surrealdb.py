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


class SurrealdbIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "surrealdb"

    @property
    def original_file_name(self) -> "str":
        return "surrealdb.svg"

    @property
    def title(self) -> "str":
        return "SurrealDB"

    @property
    def primary_color(self) -> "str":
        return "#FF00A0"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>SurrealDB</title>
     <path d="m12 6.314 5.714 3.165v-1.27L12 5.054c-.85.47-4.957
 2.74-5.714 3.157.703.39 8.085 4.467 12.572 6.946v1.264L12
 20.209c-1.71-.943-5.15-2.844-6.858-3.79v-3.788L12
 16.42l1.144-.632-9.146-5.05v6.316L12 21.472l8-4.42v-2.526L8.57
 8.21Zm-8.002.632v2.528l11.428 6.316-3.428
 1.896-5.714-3.165v1.27l5.714 3.156c.85-.47 4.957-2.74
 5.714-3.157-.703-.39-8.083-4.467-12.57-6.948V7.578L12 3.789c1.707.945
 5.148 2.846 6.858 3.789v3.789L12 7.577l-1.144.633L20 13.263V6.946L12
 2.526c-.791.438-7.416 4.1-8.002 4.42zM12 0 1.713 5.685v12.63L12
 24l10.287-5.682V5.685Zm9.14 17.683L12 22.736l-9.143-5.053V6.317L12
 1.264l9.143 5.053z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/surrealdb/surrealdb/blob/b'''

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
