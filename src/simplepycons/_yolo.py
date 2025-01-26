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


class YoloIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "yolo"

    @property
    def original_file_name(self) -> "str":
        return "yolo.svg"

    @property
    def title(self) -> "str":
        return "YOLO"

    @property
    def primary_color(self) -> "str":
        return "#111F68"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>YOLO</title>
     <path d="M18.25 0c-3.05 0-5.52 2.477-5.52 5.523 0 3.842-3.125
 6.967-6.972 6.967-1.506 0-2.894-.46-4.03-1.26 1.105 1.98 2.765 3.6
 4.759 4.67v2.51c0 3.04 2.428 5.56 5.463 5.59 3.07 0 5.58-2.46
 5.58-5.52V15.9c3.64-1.96 6.16-5.8 6.23-10.208v-.165C23.76 2.477 21.28
 0 18.25 0ZM5.758.0002C2.715.0002.2399 2.477.2399 5.523c0 3.044 2.4751
 5.517 5.5181 5.517 3.044 0 5.512-2.473 5.512-5.517
 0-3.046-2.468-5.5228-5.512-5.5228Z" />
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
