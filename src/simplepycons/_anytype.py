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


class AnytypeIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "anytype"

    @property
    def original_file_name(self) -> "str":
        return "anytype.svg"

    @property
    def title(self) -> "str":
        return "Anytype"

    @property
    def primary_color(self) -> "str":
        return "#FF6A7B"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Anytype</title>
     <path d="M5.333 0h13.334A5.322 5.322 0 0 1 24 5.333v13.334A5.322
 5.322 0 0 1 18.667 24H5.333A5.322 5.322 0 0 1 0 18.667V5.333A5.322
 5.322 0 0 1 5.333 0Zm10.334 7.667v-3H6.344v3zm0 0v11.666h3V7.667ZM9.5
 19.333a4.833 4.833 0 1 0 0-9.666 4.833 4.833 0 0 0 0 9.666z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/anyproto/anytype-ts/blob/5'''

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
