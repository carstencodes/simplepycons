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


class DoubanReadIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "doubanread"

    @property
    def original_file_name(self) -> "str":
        return "doubanread.svg"

    @property
    def title(self) -> "str":
        return "Douban Read"

    @property
    def primary_color(self) -> "str":
        return "#389EAC"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Douban Read</title>
     <path d="M15.328 5.553c-2.648.906-4.008 4.372-7.101 4.833C4.827
 10.833.752 7.205 0 6c0 0 .526.906 1.28 2.105C5.205 14.297 7.772
 18.224 12 18.75c5.28.68 8.146-4.535 8.826-6.64.607-1.732 1.733-1.66
 2.494-1.433l.68.227s-2.729-7.402-8.688-5.36l.016.008z" />
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
