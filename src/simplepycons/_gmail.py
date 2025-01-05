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


class GmailIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "gmail"

    @property
    def original_file_name(self) -> "str":
        return "gmail.svg"

    @property
    def title(self) -> "str":
        return "Gmail"

    @property
    def primary_color(self) -> "str":
        return "#EA4335"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Gmail</title>
     <path d="M24 5.457v13.909c0 .904-.732 1.636-1.636
 1.636h-3.819V11.73L12 16.64l-6.545-4.91v9.273H1.636A1.636 1.636 0 0 1
 0 19.366V5.457c0-2.023 2.309-3.178 3.927-1.964L5.455 4.64 12
 9.548l6.545-4.91 1.528-1.145C21.69 2.28 24 3.434 24 5.457z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://fonts.gstatic.com/s/i/productlogos/gm'''

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
