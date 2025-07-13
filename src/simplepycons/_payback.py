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


class PaybackIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "payback"

    @property
    def original_file_name(self) -> "str":
        return "payback.svg"

    @property
    def title(self) -> "str":
        return "PAYBACK"

    @property
    def primary_color(self) -> "str":
        return "#003EB0"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>PAYBACK</title>
     <path d="M16.1796 11.4765c-2.0161 0-3.6576-1.6401-3.6576-3.6548
 0-2.0148 1.6401-3.6562 3.6576-3.6562s3.6548 1.64 3.6548 3.6562c0
 2.016-1.64 3.6548-3.6548 3.6548zm-.0014 8.3595c-2.0161
 0-3.6562-1.64-3.6562-3.6562 0-2.0161 1.64-3.6562 3.6562-3.6562 2.016
 0 3.6562 1.6401 3.6562 3.6562 0 2.0161-1.6401 3.6562-3.6562
 3.6562zm0-6.5877c-1.6168 0-2.9315 1.3148-2.9315 2.9315 0 1.6168
 1.3147 2.9315 2.9315 2.9315 1.6167 0 2.9315-1.3147 2.9315-2.9315
 0-1.6167-1.3148-2.9315-2.9315-2.9315zM7.8187 19.836c-2.0162
 0-3.6562-1.64-3.6562-3.6562 0-2.0161 1.64-3.6562 3.6562-3.6562 2.016
 0 3.6561 1.6401 3.6561 3.6562 0 2.0161-1.64 3.6562-3.6561
 3.6562zm0-6.5877c-1.6168 0-2.9316 1.3148-2.9316 2.9315 0 1.6168
 1.3148 2.9315 2.9316 2.9315 1.6167 0 2.9315-1.3147 2.9315-2.9315
 0-1.6167-1.3148-2.9315-2.9315-2.9315zm0-1.7718c-2.0162
 0-3.6562-1.6401-3.6562-3.6562 0-2.0161 1.64-3.6562 3.6562-3.6562
 2.016 0 3.6561 1.64 3.6561 3.6562 0 2.0161-1.64 3.6562-3.6561
 3.6562zm0-6.5877c-1.6168 0-2.9316 1.3148-2.9316 2.9315 0 1.6167
 1.3148 2.9315 2.9316 2.9315 1.6167 0 2.9315-1.3148 2.9315-2.9315
 0-1.6167-1.3148-2.9315-2.9315-2.9315zM3.0014 0C1.3462 0 0 1.3465 0
 3.0003V21c0 1.6537 1.3462 3 3.0014 3h17.994c1.6551 0 3.003-1.3463
 3.003-3V3.0002C23.9984 1.3465 22.6519 0 20.9954 0Z" />
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
