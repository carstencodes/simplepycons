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


class UnderArmourIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "underarmour"

    @property
    def original_file_name(self) -> "str":
        return "underarmour.svg"

    @property
    def title(self) -> "str":
        return "Under Armour"

    @property
    def primary_color(self) -> "str":
        return "#1D1D1D"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Under Armour</title>
     <path d="M15.954
 12c-.089.066-.195.142-.324.233-.826.585-2.023.985-3.58.985h-.104c-1.556
 0-2.755-.4-3.58-.985A36.43 36.43 0 018.042
 12c.09-.067.196-.143.324-.234.825-.584 2.024-.985
 3.58-.985h.104c1.557 0 2.756.401 3.58.985.129.09.235.167.325.234M24
 7.181s-.709-.541-2.95-1.365c-1.968-.721-3.452-.883-3.452-.883l.006
 4.243c0 .598-.162 1.143-.618
 1.765-1.672-.61-3.254-.985-4.981-.985-1.728
 0-3.308.375-4.98.985-.457-.619-.62-1.168-.62-1.765l.007-4.243s-1.494.16-3.463.883C.709
 6.642 0 7.181 0 7.181c.093 1.926 1.78 3.638 4.435 4.82C1.777 13.18.09
 14.887 0 16.818c0 0 .709.54 2.949 1.365 1.968.721 3.453.883
 3.453.883l-.007-4.244c0-.597.164-1.143.619-1.764 1.672.61 3.252.983
 4.98.983 1.727 0 3.309-.374 4.98-.983.457.62.62 1.167.62 1.764l-.006
 4.244s1.484-.16 3.452-.883c2.241-.826 2.95-1.365
 2.95-1.365-.093-1.927-1.78-3.64-4.435-4.819 2.657-1.182 4.343-2.888
 4.435-4.82" />
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
