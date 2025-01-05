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


class AriakitIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "ariakit"

    @property
    def original_file_name(self) -> "str":
        return "ariakit.svg"

    @property
    def title(self) -> "str":
        return "Ariakit"

    @property
    def primary_color(self) -> "str":
        return "#007ACC"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Ariakit</title>
     <path d="M18 2H6C3.79 2 2 3.79 2 6v12c0 2.21 1.79 4 4 4h12c2.21 0
 4-1.79 4-4V6c0-2.21-1.79-4-4-4Zm-6 16c-3.31 0-6-2.69-6-6s2.69-6 6-6 6
 2.69 6 6-2.69 6-6 6Zm0-6a2.5 2.5 0 0 0 5 0 2.5 2.5 0 0 0-5
 0Zm6-12H6C2.69 0 0 2.69 0 6v12c0 3.31 2.69 6 6 6h12c3.31 0 6-2.69
 6-6V6c0-3.31-2.69-6-6-6Zm5 18c0 2.76-2.24 5-5 5H6c-2.76
 0-5-2.24-5-5V6c0-2.76 2.24-5 5-5h12c2.76 0 5 2.24 5 5v12ZM18 2H6C3.79
 2 2 3.79 2 6v12c0 2.21 1.79 4 4 4h12c2.21 0 4-1.79
 4-4V6c0-2.21-1.79-4-4-4Zm-6 16c-3.31 0-6-2.69-6-6s2.69-6 6-6 6 2.69 6
 6-2.69 6-6 6Zm0-6a2.5 2.5 0 0 0 5 0 2.5 2.5 0 0 0-5 0Zm2.5-2.5a2.5
 2.5 0 0 0 0 5 2.5 2.5 0 0 0 0-5ZM18 2H6C3.79 2 2 3.79 2 6v12c0 2.21
 1.79 4 4 4h12c2.21 0 4-1.79 4-4V6c0-2.21-1.79-4-4-4Zm-6 16c-3.31
 0-6-2.69-6-6s2.69-6 6-6 6 2.69 6 6-2.69 6-6 6Zm0-6a2.5 2.5 0 0 0 5 0
 2.5 2.5 0 0 0-5 0Zm2.5-2.5a2.5 2.5 0 0 0 0 5 2.5 2.5 0 0 0 0-5Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/ariakit/ariakit/blob/a7399'''

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
