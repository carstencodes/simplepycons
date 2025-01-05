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


class MaterialDesignIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "materialdesign"

    @property
    def original_file_name(self) -> "str":
        return "materialdesign.svg"

    @property
    def title(self) -> "str":
        return "Material Design"

    @property
    def primary_color(self) -> "str":
        return "#757575"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Material Design</title>
     <path d="M12 0C5.377 0 0 5.377 0 12s5.377 12 12 12 12-5.377
 12-12S18.623 0 12 0zm0 .75c2.871 0 5.482 1.082 7.469 2.85H4.53A11.197
 11.197 0 0 1 12 .75zm-7.186 3.6h14.372L12 18.723 4.814 4.35zM3.6
 4.53V19.47A11.197 11.197 0 0 1 .75 12c0-2.87 1.082-5.481
 2.85-7.468zm16.8 0A11.197 11.197 0 0 1 23.25 12c0 2.871-1.082
 5.482-2.85 7.469V4.53zM4.35 5.1l7.275 14.55H4.35V5.1zm15.3
 0v14.55h-7.275L19.651 5.1zM4.533 20.4H19.469A11.197 11.197 0 0 1 12
 23.25a11.197 11.197 0 0 1-7.468-2.85z" />
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
