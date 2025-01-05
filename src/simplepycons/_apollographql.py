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


class ApolloGraphqlIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "apollographql"

    @property
    def original_file_name(self) -> "str":
        return "apollographql.svg"

    @property
    def title(self) -> "str":
        return "Apollo GraphQL"

    @property
    def primary_color(self) -> "str":
        return "#311C87"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Apollo GraphQL</title>
     <path d="M12,0C5.372,0 0,5.373 0,12 0,18.628 5.372,24 12,24
 18.627,24 24,18.628 24,12A12.014,12.014 0 0 0 23.527,8.657 0.6,0.6 0
 0 0 22.4,9.066H22.398C22.663,10.009 22.8,10.994 22.8,12A10.73,10.73 0
 0 1 19.637,19.637 10.729,10.729 0 0 1 12,22.8 10.73,10.73 0 0 1
 4.363,19.637 10.728,10.728 0 0 1 1.2,12 10.73,10.73 0 0 1 4.363,4.363
 10.728,10.728 0 0 1 12,1.2C14.576,1.2 17.013,2.096
 18.958,3.74A1.466,1.466 0 1 0 19.82,2.9 11.953,11.953 0 0 0
 12,0ZM10.56,5.88
 6.36,16.782H8.99L9.677,14.934H13.646L12.927,12.892H10.314L12.014,8.201
 15.038,16.781H17.669L13.47,5.88Z" />
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
