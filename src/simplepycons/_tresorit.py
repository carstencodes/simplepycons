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


class TresoritIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "tresorit"

    @property
    def original_file_name(self) -> "str":
        return "tresorit.svg"

    @property
    def title(self) -> "str":
        return "Tresorit"

    @property
    def primary_color(self) -> "str":
        return "#00A9E2"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Tresorit</title>
     <path d="M12 0 1.636 6v12L12 24l10.364-6V6zM3.818 7.258 12
 2.521l3.574 2.069-11.756 6.753zm16.364 9.484L12 21.48 3.82
 16.742V13.86l13.938-8.006 2.425 1.404z" />
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
