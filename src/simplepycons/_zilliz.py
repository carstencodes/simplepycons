#
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2026 Carsten Igel.
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


class ZillizIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "zilliz"

    @property
    def original_file_name(self) -> "str":
        return "zilliz.svg"

    @property
    def title(self) -> "str":
        return "Zilliz"

    @property
    def primary_color(self) -> "str":
        return "#2858FF"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Zilliz</title>
     <path d="M11.25 16.317V24h1.5v-9.2l3.989 6.908a11 11 0 0 0
 1.298-.752l-4.366-7.562 4.808 1.75a7 7 0 0 0
 .51-1.41l-2.701-.984H24v-1.5h-9.201l6.909-3.989a11 11 0 0
 0-.752-1.298l-7.517 4.34 1.735-4.767a7 7 0 0 0-1.408-.518L12.75
 7.81V0h-1.5v9.2L7.261 2.293a11 11 0 0 0-1.298.752l4.348
 7.53-4.78-1.739a7 7 0 0 0-.515 1.409L7.78 11.25H0v1.5h9.2l-6.908
 3.989a11 11 0 0 0 .752 1.298l7.576-4.374-1.755 4.82a7 7 0 0 0
 1.411.51z" />
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
