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


class CouchbaseIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "couchbase"

    @property
    def original_file_name(self) -> "str":
        return "couchbase.svg"

    @property
    def title(self) -> "str":
        return "Couchbase"

    @property
    def primary_color(self) -> "str":
        return "#EA2328"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Couchbase</title>
     <path d="M20.111 14.104a1.467 1.458 0 0 1-1.235
 1.503c-1.422.244-4.385.398-6.875.398s-5.454-.15-6.877-.398c-.814-.14-1.235-.787-1.235-1.503V9.417a1.57
 1.56 0 0 1 1.235-1.505 15.72 15.619 0 0 1 2.156-.14.537.533 0 0 1
 .523.543v3.303c1.463 0 2.727-.086 4.201-.086 1.474 0 2.727.086
 4.196.086V8.342a.535.532 0 0 1 .494-.569h.027a15.995 15.891 0 0 1
 2.156.14 1.57 1.56 0 0 1 1.234 1.504zM12.001 0C5.373 0 0 5.374 0 12c0
 6.628 5.373 12 12 12 6.628 0 12-5.372 12-12 0-6.626-5.373-12-12-12z"
 />
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
