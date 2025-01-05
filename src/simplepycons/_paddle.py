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


class PaddleIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "paddle"

    @property
    def original_file_name(self) -> "str":
        return "paddle.svg"

    @property
    def title(self) -> "str":
        return "Paddle"

    @property
    def primary_color(self) -> "str":
        return "#FDDD35"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Paddle</title>
     <path d="M2.363 7.904v.849a3.95 3.95 0 0 1 3.65
 2.425c.198.476.3.987.299 1.502h.791c0-1.04.416-2.037
 1.157-2.772a3.962 3.962 0 0 1 2.792-1.149V7.91a3.959 3.959 0 0
 1-3.65-2.425 3.893 3.893 0 0 1-.299-1.502h-.791c0 1.04-.416
 2.037-1.157 2.772a3.96 3.96 0 0 1-2.792 1.149M13.105
 2.51H6.312V0h6.793c4.772 0 8.532 3.735 8.532 8.314 0 4.58-3.76
 8.314-8.532 8.314H9.156V24H6.312v-9.882h6.793c3.319 0 5.688-2.352
 5.688-5.804 0-3.451-2.37-5.804-5.688-5.804" />
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
