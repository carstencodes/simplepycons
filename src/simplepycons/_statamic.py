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


class StatamicIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "statamic"

    @property
    def original_file_name(self) -> "str":
        return "statamic.svg"

    @property
    def title(self) -> "str":
        return "Statamic"

    @property
    def primary_color(self) -> "str":
        return "#FF269E"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Statamic</title>
     <path d="M19.78 21.639c1.754 0 2.398-.756
 2.398-2.607v-3.62c0-1.722.837-2.704 1.641-3.17.242-.145.242-.483
 0-.644-.836-.531-1.64-1.642-1.64-3.122v-3.54c0-1.996-.548-2.575-2.302-2.575H4.123c-1.754
 0-2.301.58-2.301 2.575v3.556c0 1.48-.805 2.59-1.641 3.122a.377.377 0
 0 0 0 .643c.804.451 1.64 1.433 1.64 3.17v3.605c0 1.85.645 2.607 2.399
 2.607zm-7.82-3.299c-1.883 0-3.25-.563-4.522-1.673a.891.891 0 0
 1-.29-.676.83.83 0 0 1
 .193-.563l.403-.515c.193-.242.402-.354.643-.354.274 0
 .531.112.805.29a5.331 5.331 0 0 0 2.993.884c.885 0 1.593-.37
 1.593-1.126 0-1.963-6.533-.885-6.533-5.294 0-2.366 1.93-3.685
 4.441-3.685 1.77 0 3.074.515 4.04 1.126.24.161.402.483.402.805 0
 .193-.049.37-.161.53l-.29.435c-.21.29-.45.435-.756.435-.21
 0-.435-.08-.676-.193a5.07 5.07 0 0 0-2.398-.564c-.95
 0-1.513.515-1.513 1.046 0 2.012 6.534.918 6.534 5.198 0 2.414-1.947
 3.894-4.908 3.894z" />
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
