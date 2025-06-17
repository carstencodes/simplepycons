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


class BackstageCastingIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "backstage_casting"

    @property
    def original_file_name(self) -> "str":
        return "backstage_casting.svg"

    @property
    def title(self) -> "str":
        return "Backstage"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Backstage</title>
     <path d="M10.2 0v.056a5.997 5.997 0 0 1 0 11.886v.113a5.997 5.997
 0 0 1 0 11.886v.056h12.552V0ZM1.248 0v24H9.54V0Z" />
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


class BackstageIcon1(BackstageCastingIcon):
    """BackstageIcon1 is an alternative implementation name for BackstageCastingIcon. 
          It is deprecated and may be removed in future versions."""
    def __init__(self, *args, **kwargs) -> "None":
        import warnings
        warnings.warn("The usage of 'BackstageIcon1' is discouraged and may be removed in future major versions. Use 'BackstageCastingIcon' instead.", DeprecationWarning)
        super().__init__(*args, **kwargs)

