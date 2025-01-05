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


class StoryblokIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "storyblok"

    @property
    def original_file_name(self) -> "str":
        return "storyblok.svg"

    @property
    def title(self) -> "str":
        return "Storyblok"

    @property
    def primary_color(self) -> "str":
        return "#09B3AF"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Storyblok</title>
     <path d="M13.953 11.462H9.088v2.34h4.748c.281 0
 .538-.118.749-.305.187-.187.304-.468.304-.819a1.404 1.404 0 0
 0-.257-.842c-.188-.234-.398-.374-.679-.374zm.164-2.83c.21-.14.304-.445.304-.843
 0-.35-.094-.608-.257-.771a.935.935 0 0
 0-.608-.234H9.088v2.105h4.374c.234 0 .468-.117.655-.257zM21.251
 0H2.89c-.585 0-1.053.468-1.053 1.03v18.385c0 .562.468.912
 1.03.912H5.58V24l3.368-3.65h12.304c.562 0
 .913-.35.913-.935V1.053c0-.562-.351-1.03-.936-1.03zm-3.087 14.9a2.827
 2.827 0 0 1-1.006
 1.03c-.445.28-.936.538-1.497.655-.562.14-1.17.257-1.801.257H5.579v-13.1h9.403c.468
 0 .866.094 1.24.305.351.187.679.444.936.748.524.64.806 1.443.795 2.27
 0 .608-.164 1.192-.468 1.754a2.924 2.924 0 0 1-1.403 1.263c.748.21
 1.333.585 1.778 1.123.42.561.631 1.286.631 2.199 0 .584-.117
 1.076-.35 1.497z" />
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
