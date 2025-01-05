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


class FlickrIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "flickr"

    @property
    def original_file_name(self) -> "str":
        return "flickr.svg"

    @property
    def title(self) -> "str":
        return "Flickr"

    @property
    def primary_color(self) -> "str":
        return "#0063DC"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Flickr</title>
     <path d="M5.334 6.666C2.3884 6.666 0 9.055 0 12c0 2.9456 2.3884
 5.334 5.334 5.334 2.9456 0 5.332-2.3884 5.332-5.334
 0-2.945-2.3864-5.334-5.332-5.334zm13.332 0c-2.9456 0-5.332
 2.389-5.332 5.334 0 2.9456 2.3864 5.334 5.332 5.334C21.6116 17.334 24
 14.9456 24 12c0-2.945-2.3884-5.334-5.334-5.334Z" />
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
