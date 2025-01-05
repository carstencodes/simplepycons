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


class SwiftIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "swift"

    @property
    def original_file_name(self) -> "str":
        return "swift.svg"

    @property
    def title(self) -> "str":
        return "Swift"

    @property
    def primary_color(self) -> "str":
        return "#F05138"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Swift</title>
     <path d="M7.508 0c-.287 0-.573
 0-.86.002-.241.002-.483.003-.724.01-.132.003-.263.009-.395.015A9.154
 9.154 0 0 0 4.348.15 5.492 5.492 0 0 0 2.85.645 5.04 5.04 0 0 0 .645
 2.848c-.245.48-.4.972-.495 1.5-.093.52-.122 1.05-.136 1.576a35.2 35.2
 0 0 0-.012.724C0 6.935 0 7.221 0 7.508v8.984c0 .287 0
 .575.002.862.002.24.005.481.012.722.014.526.043 1.057.136
 1.576.095.528.25 1.02.495 1.5a5.03 5.03 0 0 0 2.205
 2.203c.48.244.97.4 1.498.495.52.093 1.05.124
 1.576.138.241.007.483.009.724.01.287.002.573.002.86.002h8.984c.287 0
 .573 0 .86-.002.241-.001.483-.003.724-.01a10.523 10.523 0 0 0
 1.578-.138 5.322 5.322 0 0 0 1.498-.495 5.035 5.035 0 0 0
 2.203-2.203c.245-.48.4-.972.495-1.5.093-.52.124-1.05.138-1.576.007-.241.009-.481.01-.722.002-.287.002-.575.002-.862V7.508c0-.287
 0-.573-.002-.86a33.662 33.662 0 0 0-.01-.724 10.5 10.5 0 0
 0-.138-1.576 5.328 5.328 0 0 0-.495-1.5A5.039 5.039 0 0 0 21.152.645
 5.32 5.32 0 0 0 19.654.15a10.493 10.493 0 0 0-1.578-.138 34.98 34.98
 0 0 0-.722-.01C17.067 0 16.779 0 16.492 0H7.508zm6.035 3.41c4.114
 2.47 6.545 7.162 5.549
 11.131-.024.093-.05.181-.076.272l.002.001c2.062 2.538 1.5 5.258 1.236
 4.745-1.072-2.086-3.066-1.568-4.088-1.043a6.803 6.803 0 0
 1-.281.158l-.02.012-.002.002c-2.115 1.123-4.957
 1.205-7.812-.022a12.568 12.568 0 0 1-5.64-4.838c.649.48 1.35.902
 2.097 1.252 3.019 1.414 6.051 1.311 8.197-.002C9.651 12.73 7.101 9.67
 5.146 7.191a10.628 10.628 0 0 1-1.005-1.384c2.34 2.142 6.038 4.83
 7.365 5.576C8.69 8.408 6.208 4.743 6.324 4.86c4.436 4.47 8.528 6.996
 8.528
 6.996.154.085.27.154.36.213.085-.215.16-.437.224-.668.708-2.588-.09-5.548-1.893-7.992z"
 />
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
