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


class SpringCreatorsIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "spring_creators"

    @property
    def original_file_name(self) -> "str":
        return "spring_creators.svg"

    @property
    def title(self) -> "str":
        return "Spring"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Spring</title>
     <path d="M8.563 24c-1.839
 0-4.435-.537-7.028-2.87l2.035-2.262c3.636 3.273 7.425 1.98
 8.595.888.078-.079.156-.153.234-.23-3.83-.373-6.629-3.086-6.822-3.277-2.933-2.889-3.6-6.808-1.512-8.93s6.015-1.522
 8.95 1.357c.257.246 3.116 3.052 3.677 6.605a6.776 6.776 0
 002.727-5.426 6.62 6.62 0
 00-1.995-4.791c-1.334-1.303-3.222-2.02-5.306-2.02V0c2.88 0 5.519
 1.024 7.43 2.882 1.881 1.83 2.917 4.304 2.917 6.973a9.831 9.831 0
 01-6.116 9.086c-.416 1.1-1.12 2.117-2.106 3.04-.97.905-2.865
 1.908-5.28 2.01-.13.007-.262.009-.4.009zM7.283 9.077c-.425
 0-.79.115-1.046.375-.749.762-.275 2.904 1.48 4.633l.008.009c.025.024
 2.771 2.687 6.025
 2.414v-.005c.015-2.873-2.808-5.597-2.837-5.625l-.02-.019C9.85 9.832
 8.37 9.077 7.283 9.077Z" />
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


class SpringIcon1(SpringCreatorsIcon):
    """SpringIcon1 is an alternative implementation name for SpringCreatorsIcon. 
          It is deprecated and may be removed in future versions."""
    def __init__(self, *args, **kwargs) -> "None":
        import warnings
        warnings.warn("The usage of 'SpringIcon1' is discouraged and may be removed in future major versions. Use 'SpringCreatorsIcon' instead.", DeprecationWarning)
        super().__init__(*args, **kwargs)

