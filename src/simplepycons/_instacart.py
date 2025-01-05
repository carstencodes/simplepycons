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


class InstacartIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "instacart"

    @property
    def original_file_name(self) -> "str":
        return "instacart.svg"

    @property
    def title(self) -> "str":
        return "Instacart"

    @property
    def primary_color(self) -> "str":
        return "#43B02A"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Instacart</title>
     <path d="M15.629 9.619c1.421 1.429 2.58 3.766 1.917 5.152-1.778
 3.715-15.04 10.226-16.169 9.1C.252 22.746 6.768 9.476 10.481
 7.697c1.388-.66 3.724.51 5.152
 1.92l-.005.014v-.012zm7.028-1.566c-.231-.855-.821-1.717-1.7-1.82-1.61-.186-4.151
 2.663-3.971 3.339.181.69 3.766 1.875
 5.1.915.691-.494.781-1.56.556-2.414l.015-.02zM17.666.158c1.198.324
 2.407 1.148 2.551 2.382.261 2.259-3.732 5.819-4.68
 5.564-.948-.251-2.618-5.284-1.269-7.162.695-.972 2.201-1.106
 3.399-.788v.004h-.001z" />
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
