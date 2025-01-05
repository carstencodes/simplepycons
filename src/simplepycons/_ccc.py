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


class CccIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "ccc"

    @property
    def original_file_name(self) -> "str":
        return "ccc.svg"

    @property
    def title(self) -> "str":
        return "CCC"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>CCC</title>
     <path d="M12 3.4C5.814 3.4.8 7.253.8 12c0 4.75 5.014 8.6 11.2
 8.6s11.2-3.85 11.2-8.6c0-4.747-5.015-8.6-11.2-8.6M24 12c0 5.19-5.374
 9.4-12 9.4S0 17.19 0 12s5.374-9.4 12-9.4S24 6.81 24 12M10 7c-2.83
 0-5.026 2.229-5.026 5 0 2.882 2.487 4.997 5.026 4.997V15.44c-1.708
 0-3.442-1.36-3.445-3.44C6.547 9.65 8.476 8.544 10 8.544zm3.8 0c-2.83
 0-5.026 2.229-5.026 5 0 2.882 2.484 4.997 5.026 4.997V15.44c-1.705
 0-3.442-1.36-3.447-3.44-.007-2.35 1.923-3.456
 3.447-3.456zm3.8.003c-2.83 0-5.026 2.23-5.026 4.997 0 2.886 2.487 5
 5.026 5v-1.56c-1.708 0-3.442-1.358-3.448-3.44-.005-2.35 1.924-3.456
 3.448-3.456z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://www.cqc.com.cn/www/chinese/c/2018-11-'''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://www.cqc.com.cn/www/chinese/c/2018-03-'''

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
        yield from [
            "China Compulsory Certificate",
        ]
