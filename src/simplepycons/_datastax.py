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


class DatastaxIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "datastax"

    @property
    def original_file_name(self) -> "str":
        return "datastax.svg"

    @property
    def title(self) -> "str":
        return "DataStax"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>DataStax</title>
     <path d="M10.863 8.818v6.364l-2.181 1.683H0v-9.73h8.682l2.181
 1.683Zm-9.18
 6.366h7.498V8.818H1.683v6.366Zm13.243-6.296v2.26h6.919L24
 12.793v2.318l-2.155
 1.646h-8.153v-1.646h8.645v-2.318h-6.919l-2.155-1.645v-2.26l2.155-1.645h7.939v1.645h-8.431Z"
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
        return '''https://docs.datastax.com/en/astra/astra-db-v'''

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
