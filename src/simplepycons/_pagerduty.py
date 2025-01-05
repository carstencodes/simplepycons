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


class PagerdutyIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "pagerduty"

    @property
    def original_file_name(self) -> "str":
        return "pagerduty.svg"

    @property
    def title(self) -> "str":
        return "PagerDuty"

    @property
    def primary_color(self) -> "str":
        return "#06AC38"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>PagerDuty</title>
     <path d="M16.965 1.18C15.085.164 13.769 0 10.683
 0H3.73v14.55h6.926c2.743 0 4.8-.164 6.61-1.37 1.975-1.303 3.004-3.484
 3.004-6.007 0-2.716-1.262-4.896-3.305-5.994zm-5.5
 10.326h-4.21V3.113l3.977-.027c3.62-.028 5.43 1.234 5.43 4.128 0
 3.113-2.248 4.292-5.197 4.292zM3.73 17.61h3.525V24H3.73Z" />
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
