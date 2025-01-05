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


class DoubanIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "douban"

    @property
    def original_file_name(self) -> "str":
        return "douban.svg"

    @property
    def title(self) -> "str":
        return "Douban"

    @property
    def primary_color(self) -> "str":
        return "#2D963D"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Douban</title>
     <path d="M.51 3.06h22.98V.755H.51V3.06Zm20.976
 2.537v9.608h-2.137l-1.669
 5.76H24v2.28H0v-2.28h6.32l-1.67-5.76H2.515V5.597h18.972Zm-5.066
 9.608H7.58l1.67 5.76h5.501l1.67-5.76ZM18.367
 7.9H5.634v5.025h12.733V7.9Z" />
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
