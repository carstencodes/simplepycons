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


class KoreaderIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "koreader"

    @property
    def original_file_name(self) -> "str":
        return "koreader.svg"

    @property
    def title(self) -> "str":
        return "KOReader"

    @property
    def primary_color(self) -> "str":
        return "#00A89C"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>KOReader</title>
     <path d="M7.8489 0v14.5581L6.1996 13.178 4.55
 14.5581V.0258c-1.3637.1773-2.427 1.3509-2.427 2.7634v18.4216c0
 1.3362.951 2.4601 2.2081 2.7279a7.9086 7.9086 0 0
 1-.2363-1.92c0-4.3601 3.5401-7.9072 7.8918-7.9072 4.3516 0 7.8915
 3.547 7.8915 7.9071a7.95 7.95 0 0 1-.0817
 1.1292c.4864-.5029.788-1.186.788-1.937V2.7892c0-1.1618-.7192-2.1625-1.7332-2.5802L12.2039
 7.323c.7334.8645 3.202 3.2692 6.3988 6.001.6706.5732 1.1863 1.0062
 1.7217 1.234-1.1597.002-2.3696-.005-2.7622
 0-2.2832.031-2.3345-.415-3.0694-1.0028-1.122-.8968-3.6824-3.4473-4.9377-4.6126-.4278-.3977-.6702-.8597-.6702-1.2922v-.352c0-.5752.2163-1.1301.6055-1.5534L14.7784
 0zm10.5979 0c1.531 0 2.784 1.2553 2.784 2.7892v18.4216c0 1.534-1.253
 2.7892-2.784 2.7892h.6461c1.531 0 2.784-1.2553
 2.784-2.7892V2.7892C21.877 1.2552 20.624 0 19.093 0zm-6.4601
 17.0838c-2.7159 0-4.9253 2.2137-4.9253 4.9348 0 .705.1508 1.3743.4177
 1.9814h9.015a4.91 4.91 0 0 0
 .4177-1.9814c0-2.721-2.2093-4.9348-4.9251-4.9348z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/koreader/koreader/blob/588'''

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
