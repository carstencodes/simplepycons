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


class UikitIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "uikit"

    @property
    def original_file_name(self) -> "str":
        return "uikit.svg"

    @property
    def title(self) -> "str":
        return "UIkit"

    @property
    def primary_color(self) -> "str":
        return "#2396F3"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>UIkit</title>
     <path d="M17.697 3.292l-4.109 2.489 4.738 2.696v7.077l-6.365
 3.538-6.258-3.538v-5.485L1.596 7.956V18l10.219 6
 10.589-6V6.002l-4.707-2.71zm-1.904-.989L11.813 0 7.665 2.568l4.032
 2.218 4.096-2.483z" />
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
