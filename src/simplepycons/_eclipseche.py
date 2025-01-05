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


class EclipseCheIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "eclipseche"

    @property
    def original_file_name(self) -> "str":
        return "eclipseche.svg"

    @property
    def title(self) -> "str":
        return "Eclipse Che"

    @property
    def primary_color(self) -> "str":
        return "#525C86"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Eclipse Che</title>
     <path d="M12 0L1.604 6.021v7.452L12 7.494l3.941 2.254
 6.455-3.727zm10.396 10.527L12 16.506l-7.334-4.217-3.062 1.76v3.93L12
 24l10.396-6.021z" />
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
