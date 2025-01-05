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


class QuicktimeIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "quicktime"

    @property
    def original_file_name(self) -> "str":
        return "quicktime.svg"

    @property
    def title(self) -> "str":
        return "QuickTime"

    @property
    def primary_color(self) -> "str":
        return "#1C69F0"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>QuickTime</title>
     <path d="M12.002 0a11.998 12 0 106.629 22l1.98
 1.97h3.139l.25-.25v-3.15l-2-1.98A11.938 11.94 0 0024 12 11.998 12 0
 0012.002 0m0 4.2a7.799 7.8 0 016.949 11.33l-5.25-5.26a2.404 2.404 0
 10-3.4 3.4l5.27 5.26a7.759 7.76 0 01-3.57.87 7.799 7.8 0 010-15.6z"
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
