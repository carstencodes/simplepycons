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


class MoscowMetroIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "moscowmetro"

    @property
    def original_file_name(self) -> "str":
        return "moscowmetro.svg"

    @property
    def title(self) -> "str":
        return "Moscow Metro"

    @property
    def primary_color(self) -> "str":
        return "#D9232E"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Moscow Metro</title>
     <path d="M16.603 11.85l-2.481-6.26-2.092 3.66-2.092-3.66-2.481
 6.262H6.74v.941h3.736v-.941h-.553l.538-1.555 1.569 2.57
 1.569-2.57.538 1.555h-.553v.941h3.751v-.941zm5.335-1.912A9.933 9.933
 0 0 0 12 0C6.516 0 2.062 4.453 2.062 9.938c0 2.75 1.121 5.23 2.914
 7.023a.804.804 0 0 0 1.375-.568.825.825 0 0 0-.239-.582 8.303 8.303 0
 0 1-2.42-5.873c0-4.588 3.72-8.324 8.308-8.324 4.588 0 8.324 3.736
 8.324 8.324a8.289 8.289 0 0 1-2.436 5.888l-7.024 7.023L12
 24l7.039-7.039a9.891 9.891 0 0 0 2.899-7.023Z" />
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
