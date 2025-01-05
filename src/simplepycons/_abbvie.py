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


class AbbvieIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "abbvie"

    @property
    def original_file_name(self) -> "str":
        return "abbvie.svg"

    @property
    def title(self) -> "str":
        return "Abbvie"

    @property
    def primary_color(self) -> "str":
        return "#071D49"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Abbvie</title>
     <path d="M23.186 20.17c-1.533
 0-2.14-.612-2.347-1.838l-.406-1.74c-.413.72-2.453 3.579-6.945
 3.579H8.89C1.94 20.17 0 15.467 0 12c0-3.885 2.347-8.17
 8.884-8.17h4.905c5.005 0 7.759 2.853 8.372 6.431.512 2.96 1.839 9.91
 1.839 9.91zM13.076 6.378h-3.88c-4.698 0-6.231 2.965-6.231 5.623 0
 2.653 1.533 5.618 6.236 5.618h3.875c4.904 0 6.236-3.065 6.236-5.618
 0-2.246-1.231-5.618-6.236-5.618z" />
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
