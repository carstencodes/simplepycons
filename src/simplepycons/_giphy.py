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


class GiphyIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "giphy"

    @property
    def original_file_name(self) -> "str":
        return "giphy.svg"

    @property
    def title(self) -> "str":
        return "GIPHY"

    @property
    def primary_color(self) -> "str":
        return "#FF6666"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>GIPHY</title>
     <path d="M2.666 0v24h18.668V8.666l-2.668
 2.668v10H5.334V2.668H10L12.666 0zm10.668
 0v8h8V5.334h-2.668V2.668H16V0" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://support.giphy.com/hc/en-us/articles/3'''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://support.giphy.com/hc/en-us/articles/3'''

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
