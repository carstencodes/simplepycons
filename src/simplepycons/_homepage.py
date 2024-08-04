#
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2024 Carsten Igel.
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


class HomepageIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "homepage"

    @property
    def original_file_name(self) -> "str":
        return "homepage.svg"

    @property
    def title(self) -> "str":
        return "Homepage"

    @property
    def primary_color(self) -> "str":
        return "#009BD5"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Homepage</title>
     <path d="M1.992.034C1.217.166.602.841.416 1.769.388 1.901.36
 21.858.388 23.895c0 .181 0 .181.923-.593.497-.416 1.328-1.128
 1.801-1.516.34-.28.626-.543.637-.576.011-.039.022-1.148.017-2.466L3.76
 16.35h1.516c.829 0 1.52.022 1.537.044.017.021.028.538.022 1.142 0
 .61.011 1.104.022 1.104.017 0
 .643-.522.725-.604.017-.017.401-.335.851-.714.923-.77.917-.764
 1.373-1.148.28-.236.34-.264.412-.203.072.066 2.878 2.421 3.592
 3.02a1239.37 1239.37 0 0 1 3.932 3.306c.003.003 2.02 1.74 2.076
 1.702.021-.01.038-3.333.038-7.38-.006-6.574.005-7.365.082-7.381.044-.011.895-.017
 1.884-.017h1.801l-.022-3.761c-.005-2.07-.033-3.817-.05-3.877-.142-.495-.51-1.022-.883-1.28-.473-.318.164-.302-10.566-.302-5.442-.005-9.99.011-10.11.033Z"
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
        return '''https://github.com/gethomepage/homepage/blob/'''

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