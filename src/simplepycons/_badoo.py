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


class BadooIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "badoo"

    @property
    def original_file_name(self) -> "str":
        return "badoo.svg"

    @property
    def title(self) -> "str":
        return "Badoo"

    @property
    def primary_color(self) -> "str":
        return "#783BF9"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Badoo</title>
     <path d="M17.68 2.809c3.392 0 6.32 2.788 6.32 6.228 0 6.71-6.6
 12.158-12 12.158S0 15.748 0 9.037c0-3.44 2.928-6.228 6.32-6.228 4.128
 0 5.578 3.179 5.68 3.411a6.079 6.079 0 0 1 5.67-3.411zm1.078
 6.488V9.11h-2.38v.186c0 2.352-1.97 4.276-4.378 4.276-2.417
 0-4.369-1.924-4.369-4.276V9.11H5.233v.186c0 1.766.697 3.42 1.98
 4.666a6.795 6.795 0 0 0 4.778 1.933 6.797 6.797 0 0 0 4.777-1.933
 6.488 6.488 0 0 0 1.98-4.666Z" />
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
