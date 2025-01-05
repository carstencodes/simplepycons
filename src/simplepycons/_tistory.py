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


class TistoryIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "tistory"

    @property
    def original_file_name(self) -> "str":
        return "tistory.svg"

    @property
    def title(self) -> "str":
        return "Tistory"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Tistory</title>
     <path d="M0 3a3 3 0 1 0 6 0 3 3 0 0 0-6 0m9 18a3 3 0 1 0 6 0 3 3
 0 0 0-6 0m0-9a3 3 0 1 0 6 0 3 3 0 0 0-6 0m0-9a3 3 0 1 0 6 0 3 3 0 0
 0-6 0m9 0a3 3 0 1 0 6 0 3 3 0 0 0-6 0" />
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
