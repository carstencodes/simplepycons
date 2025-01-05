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


class ApacheCouchdbIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "apachecouchdb"

    @property
    def original_file_name(self) -> "str":
        return "apachecouchdb.svg"

    @property
    def title(self) -> "str":
        return "Apache CouchDB"

    @property
    def primary_color(self) -> "str":
        return "#E42528"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Apache CouchDB</title>
     <path d="M19.5 14.625c0 .995-.524 1.482-1.5
 1.5H6c-.976-.018-1.5-.505-1.5-1.5s.524-1.482 1.5-1.5h12c.976.018
 1.5.505 1.5 1.5m-1.5 2.25H6c-.976.018-1.5.505-1.5 1.5s.524 1.482 1.5
 1.5h12c.976-.018 1.5-.505
 1.5-1.5s-.524-1.482-1.5-1.5m3.75-8.248v-.001c-.976.017-1.5.504-1.5
 1.499v8.25c0 .995.524 1.482 1.5 1.5v-.002c1.464-.052 2.25-1.514
 2.25-4.498v-3.75c0-1.99-.786-2.964-2.25-2.998m-19.5-.001C.786 8.662 0
 9.637 0 11.626v3.75c0 2.984.786 4.446 2.25 4.498v.001c.976-.017
 1.5-.504
 1.5-1.499v-8.25c0-.995-.524-1.482-1.5-1.5m19.5-.75c0-2.486-1.31-3.705-3.75-3.748v-.002H6v.002c-2.44.043-3.75
 1.262-3.75 3.748v.001c1.464.026 2.25.757 2.25 2.249s.786 2.223 2.25
 2.249v.001h10.5v-.001c1.464-.026 2.25-.757 2.25-2.249s.786-2.223
 2.25-2.249z" />
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
