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


class LesLibrairesIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "leslibraires"

    @property
    def original_file_name(self) -> "str":
        return "leslibraires.svg"

    @property
    def title(self) -> "str":
        return "Les libraires"

    @property
    def primary_color(self) -> "str":
        return "#CF4A0C"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Les libraires</title>
     <path d="M11.79.002a10.579 10.579 0 0 0-7.735 3.575C.18 7.958.593
 14.647 4.981 18.518a10.557 10.557 0 0 0 5.3 2.51L12.002
 24l1.717-2.971a10.56 10.56 0 0 0 6.227-3.437c3.876-4.38
 3.461-11.07-.926-14.94a10.567 10.567 0 0 0-7.23-2.65zM11.277
 7.5l.613.512-1.862 2.444c-.005.007-.048.06-.048.115 0
 .056.045.112.045.113l1.866 2.461-.615.502-2.573-2.403a.883.883 0 0
 1-.3-.667c0-.38.22-.596.304-.678zm3.265 0 .613.512-1.863
 2.444c-.005.007-.048.06-.048.115 0 .056.045.112.046.113l1.866
 2.461-.615.502-2.573-2.403a.883.883 0 0
 1-.301-.667c0-.38.222-.596.305-.678z" />
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
