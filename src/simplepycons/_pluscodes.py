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


class PlusCodesIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "pluscodes"

    @property
    def original_file_name(self) -> "str":
        return "pluscodes.svg"

    @property
    def title(self) -> "str":
        return "Plus Codes"

    @property
    def primary_color(self) -> "str":
        return "#4285F4"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Plus Codes</title>
     <path d="M12 0a2.4 2.4 0 00-2.4 2.4A2.4 2.4 0 0012 4.8a2.4 2.4 0
 002.4-2.4A2.4 2.4 0 0012 0zM9.543 9.543v4.914h4.914V9.543zM2.4
 9.6A2.4 2.4 0 000 12a2.4 2.4 0 002.4 2.4A2.4 2.4 0 004.8 12a2.4 2.4 0
 00-2.4-2.4zm19.2 0a2.4 2.4 0 00-2.4 2.4 2.4 2.4 0 002.4 2.4A2.4 2.4 0
 0024 12a2.4 2.4 0 00-2.4-2.4zM12 19.2a2.4 2.4 0 00-2.4 2.4A2.4 2.4 0
 0012 24a2.4 2.4 0 002.4-2.4 2.4 2.4 0 00-2.4-2.4z" />
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
