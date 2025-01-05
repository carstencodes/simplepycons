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


class SpineIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "spine"

    @property
    def original_file_name(self) -> "str":
        return "spine.svg"

    @property
    def title(self) -> "str":
        return "Spine"

    @property
    def primary_color(self) -> "str":
        return "#FF4000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Spine</title>
     <path d="M7.157 2.207c.066 2.004 1.454 3.117 4.221 3.55 2.345.368
 4.46.181 5.151-1.829C17.874.01 14.681.985 11.915.55S7.051-1.013 7.157
 2.207m.831 8.23c.257 1.497 1.652 2.355 3.786 2.297 2.135-.059
 3.728-.892
 3.949-2.507.409-2.988-1.946-1.832-4.08-1.774-2.136.059-4.161-.952-3.655
 1.984m2.778 6.852c.424 1.117 1.587 1.589 3.159 1.253 1.569-.335
 2.656-.856
 2.568-2.129-.159-2.357-1.713-1.616-3.283-1.279-1.571.333-3.272-.039-2.444
 2.155m1.348 5.221c.123.943.939 1.5 2.215 1.49 1.279-.011 2.248-.515
 2.412-1.525.308-1.871-1.123-1.175-2.4-1.165-1.28.01-2.47-.65-2.227
 1.2" />
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
