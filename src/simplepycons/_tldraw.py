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


class TldrawIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "tldraw"

    @property
    def original_file_name(self) -> "str":
        return "tldraw.svg"

    @property
    def title(self) -> "str":
        return "tldraw"

    @property
    def primary_color(self) -> "str":
        return "#FAFAFA"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>tldraw</title>
     <path d="M21.474 0H2.526C1.131 0 0 1.18 0 2.637v18.726C0 22.819
 1.131 24 2.526 24h18.948C22.869 24 24 22.82 24 21.363V2.637C24 1.181
 22.869 0 21.474 0zm-11.01 5.388c.397-.405.888-.607 1.474-.607.57 0
 1.052.202 1.448.607.397.404.595.896.595 1.476s-.198 1.072-.595
 1.476c-.396.405-.879.607-1.448.607-.586
 0-1.077-.202-1.474-.607-.396-.404-.594-.896-.594-1.476s.198-1.072.594-1.476zm3.13
 11.49a4.887 4.887 0 0 1-2.018
 2.136c-.483.281-.879.273-1.19-.026-.292-.281-.206-.615.26-1.002.258-.193.473-.44.646-.738.172-.299.284-.607.336-.923.017-.14-.043-.21-.181-.21-.345-.018-.698-.212-1.06-.581-.362-.37-.543-.826-.543-1.37
 0-.58.198-1.073.594-1.477a2.024 2.024 0 0 1 1.5-.633c.552 0 1.034.21
 1.448.633.414.404.655.86.724 1.37.138.95-.034 1.89-.517 2.822z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://github.com/tldraw/tldraw/blob/main/TR'''
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
