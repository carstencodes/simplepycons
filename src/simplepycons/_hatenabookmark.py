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


class HatenaBookmarkIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "hatenabookmark"

    @property
    def original_file_name(self) -> "str":
        return "hatenabookmark.svg"

    @property
    def title(self) -> "str":
        return "Hatena Bookmark"

    @property
    def primary_color(self) -> "str":
        return "#00A4DE"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Hatena Bookmark</title>
     <path d="M20.47 0C22.42 0 24 1.58 24 3.53v16.94c0 1.95-1.58
 3.53-3.53 3.53H3.53C1.58 24 0 22.42 0 20.47V3.53C0 1.58 1.58 0 3.53
 0h16.94zm-3.705 14.47c-.78 0-1.41.63-1.41 1.41s.63 1.414 1.41 1.414
 1.41-.645 1.41-1.425-.63-1.41-1.41-1.41zM8.61 17.247c1.2 0 2.056-.042
 2.58-.12.526-.084.976-.222 1.32-.412.45-.232.78-.564
 1.02-.99s.36-.915.36-1.48c0-.78-.21-1.403-.63-1.87-.42-.48-.99-.734-1.74-.794.66-.18
 1.156-.45 1.456-.81.315-.344.465-.824.465-1.424
 0-.48-.103-.885-.3-1.26-.21-.36-.493-.645-.883-.87-.345-.195-.735-.315-1.215-.405-.464-.074-1.29-.12-2.474-.12H5.654v10.486H8.61zm.736-4.185c.705
 0 1.185.088 1.44.262.27.18.39.495.39.93 0
 .405-.135.69-.42.855-.27.18-.765.254-1.44.254H8.31v-2.297h1.05zm8.656.706v-7.06h-2.46v7.06H18zM8.925
 9.08c.71 0 1.185.08 1.432.24.245.16.367.435.367.83 0
 .38-.13.646-.39.804-.265.154-.747.232-1.452.232h-.57V9.08h.615z" />
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
