#
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2024 Carsten Igel.
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


class SimpleAnalyticsIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "simpleanalytics"

    @property
    def original_file_name(self) -> "str":
        return "simpleanalytics.svg"

    @property
    def title(self) -> "str":
        return "Simple Analytics"

    @property
    def primary_color(self) -> "str":
        return "#FF4F64"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Simple Analytics</title>
     <path d="M1.019
 13.019h3.849V24h-3.85zm8.943-6.68h3.85V24h-3.85zM19.132
 0h3.85v24h-3.85z" />
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