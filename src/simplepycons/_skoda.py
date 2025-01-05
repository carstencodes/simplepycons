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


class SkodaIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "skoda"

    @property
    def original_file_name(self) -> "str":
        return "skoda.svg"

    @property
    def title(self) -> "str":
        return "ŠKODA"

    @property
    def primary_color(self) -> "str":
        return "#0E3A2F"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>ŠKODA</title>
     <path d="M12 0C5.3726 0 0 5.3726 0 12s5.3726 12 12 12 12-5.3726
 12-12S18.6274 0 12 0Zm0 22.9636C5.945 22.9636 1.0364 18.055 1.0364 12
 1.0364 5.945 5.945 1.0364 12 1.0364S22.9636 5.945 22.9636 12 18.055
 22.9636 12 22.9636Zm5.189-7.2325-.269.7263h-.984c.263-.7089
 3.5783-8.6177-2.9362-13.9819a9.5254 9.5254 0 0
 0-4.0531.4483c.2172.175 2.474 2.0276 3.5373
 4.315l-.312.084c-.5861-.6387-2.7156-2.9833-4.7448-3.7379a9.6184
 9.6184 0 0 0-2.8448 2.3597c.953.4875 3.4432 1.9748 4.3896
 3.1302-.0542.0244-.267.139-.267.139-1.736-1.3195-4.8199-2.0043-4.9775-2.0383a9.5126
 9.5126 0 0 0-1.2267 3.6098c4.7759.9613 6.0618 3.1715 6.2818
 5.6721H7.878l-1.5545-.6776a.8563.8563 0 0 0-.2524-.0531H3.1767a9.587
 9.587 0 0 0 1.9267 2.9155h1.2334c.1063 0
 .1993-.0133.2923-.0664l1.2489-.6378h9.042l.269.7264a4.8386 4.8386 0 0
 0 2.9466-1.4667 4.839 4.839 0 0 0-2.9467-1.4666zm-4.14-.5786a1.1863
 1.1863 0 0 1-.5038-1.2162 1.1862 1.1862 0 0 1 .931-.9309 1.1863
 1.1863 0 0 1 1.2161.5038c.3098.4636.2563 1.0924-.1473
 1.496-.4032.4032-1.0318.4574-1.496.1473z" />
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
