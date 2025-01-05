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


class ApachePulsarIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "apachepulsar"

    @property
    def original_file_name(self) -> "str":
        return "apachepulsar.svg"

    @property
    def title(self) -> "str":
        return "Apache Pulsar"

    @property
    def primary_color(self) -> "str":
        return "#188FFF"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Apache Pulsar</title>
     <path d="M24
 8.925h-5.866c-1.586-3.041-3.262-5.402-5.544-5.402-2.97 0-4.367
 2.593-5.717 5.115l-.118.22H0v1.5h3.934c1.39 0 1.673.468
 1.673.468-1.09 1.691-2.4 3.363-4.584 3.363H0v1.574h1.03c4.234 0
 6.083-3.434 7.567-6.193 1.361-2.541 2.31-4.08 3.993-4.08 1.747 0
 3.584 3.801 5.201 7.157.237.488.477.988.72 1.483-6.2.197-9.155
 1.649-11.559 2.833-1.759.866-3.147 1.94-5.433
 1.94H0v1.574h1.507c2.754 0 4.47-.85 6.295-1.751 2.53-1.243
 5.398-2.652 12.157-2.652h3.907V14.5H21.66a1.18 1.18 0 01-.972-.393
 70.83 70.83 0 01-1.133-2.321l-.511-1.047s.366-.393 1.38-.393H24Z" />
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
