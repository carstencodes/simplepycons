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


class GrouponIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "groupon"

    @property
    def original_file_name(self) -> "str":
        return "groupon.svg"

    @property
    def title(self) -> "str":
        return "Groupon"

    @property
    def primary_color(self) -> "str":
        return "#53A318"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Groupon</title>
     <path d="M3.316 20.334C5.618 22.736 8.554 24 12.012 24c3.988 0
 7.739-1.95 9.978-5.163 1.353-1.95 2.01-4.158 2.01-6.755
 0-.484-.032-1.006-.063-1.529H10.595v4.61h6.687c-1.155 2.012-3.094
 3.12-5.27 3.12-3.229 0-6.125-2.824-6.125-6.497 0-3.315 2.699-6.069
 6.125-6.069 1.844 0 3.355.749 4.811 2.239h6.52C21.468 3.019 17.084 0
 12.083 0c-3.323 0-6.22 1.17-8.53 3.409C1.25 5.647 0 8.572 0
 11.754c-.008 3.417 1.108 6.271 3.316 8.58z" />
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
