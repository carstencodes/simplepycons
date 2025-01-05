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


class SwiggyIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "swiggy"

    @property
    def original_file_name(self) -> "str":
        return "swiggy.svg"

    @property
    def title(self) -> "str":
        return "Swiggy"

    @property
    def primary_color(self) -> "str":
        return "#FC8019"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Swiggy</title>
     <path d="M12.034
 24c-.376-.411-2.075-2.584-3.95-5.513-.547-.916-.901-1.63-.833-1.814.178-.48
 3.355-.743 4.333-.308.298.132.29.307.29.409 0 .44-.022 1.619-.022
 1.619a.441.441 0 1 0
 .883-.002l-.005-2.939c0-.255-.278-.319-.331-.329-.511-.002-1.548-.006-2.661-.006-2.457
 0-3.006.101-3.423-.172-.904-.591-2.383-4.577-2.417-6.819C3.849 4.964
 5.723 2.225 8.362.868A8.13 8.13 0 0 1 12.026 0c4.177 0 7.617 3.153
 8.075 7.209l.001.011c.084.981-5.321
 1.189-6.39.904-.164-.044-.206-.212-.206-.284L13.5 4.996a.442.442 0 0
 0-.884.002l.009 3.866a.33.33 0 0 0 .268.32l3.354-.001c1.79 0
 2.542.207 3.042.588.333.254.461.739.349 1.37C18.633 16.755 12.273
 23.71 12.034 24z" />
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
