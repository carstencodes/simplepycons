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


class ReadmeIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "readme"

    @property
    def original_file_name(self) -> "str":
        return "readme.svg"

    @property
    def title(self) -> "str":
        return "ReadMe"

    @property
    def primary_color(self) -> "str":
        return "#018EF5"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>ReadMe</title>
     <path d="M22.0113 3.269h-5.8219a4.2894 4.2894 0 0 0-4.1854
 3.3452A4.2894 4.2894 0 0 0 7.8186 3.269h-5.818A2.0007 2.0007 0 0 0 0
 5.2697v10.2434a2.0007 2.0007 0 0 0 2.0007 2.0007h3.7372c4.2574 0
 5.5299 1.0244 6.138 3.133a.112.112 0 0 0 .1121.084h.024a.112.112 0 0
 0 .112-.084c.6122-2.1086 1.8847-3.133 6.138-3.133h3.7373A2.0007
 2.0007 0 0 0 24 15.5131V5.2697a2.0007 2.0007 0 0
 0-1.9887-2.0006Zm-11.928 11.0557a.144.144 0 0
 1-.144.144H3.2571a.144.144 0 0 1-.144-.144v-.9523a.144.144 0 0 1
 .144-.144h6.6822a.144.144 0 0 1 .144.144zm0-2.5368a.144.144 0 0
 1-.144.144H3.2571a.144.144 0 0 1-.144-.144v-.9523a.144.144 0 0 1
 .144-.144h6.6822a.144.144 0 0 1 .144.144zm0-2.5368a.144.144 0 0
 1-.144.144H3.2571a.144.144 0 0 1-.144-.144v-.9524a.144.144 0 0 1
 .144-.144h6.6822a.144.144 0 0 1 .144.144zm10.8037 5.0696a.144.144 0 0
 1-.144.144h-6.6823a.144.144 0 0 1-.144-.144v-.9523a.144.144 0 0 1
 .144-.144h6.6822a.144.144 0 0 1 .144.144zm0-2.5368a.144.144 0 0
 1-.144.144h-6.6823a.144.144 0 0 1-.144-.144v-.9523a.144.144 0 0 1
 .144-.144h6.6822a.144.144 0 0 1 .144.144zm0-2.5368a.144.144 0 0
 1-.144.144h-6.6823a.144.144 0 0 1-.144-.144v-.9484a.144.144 0 0 1
 .144-.144h6.6822a.144.144 0 0 1 .144.144v.9524z" />
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
