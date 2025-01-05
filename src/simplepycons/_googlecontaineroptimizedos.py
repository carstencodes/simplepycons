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


class GoogleContainerOptimizedOsIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "googlecontaineroptimizedos"

    @property
    def original_file_name(self) -> "str":
        return "googlecontaineroptimizedos.svg"

    @property
    def title(self) -> "str":
        return "Google Container Optimized OS"

    @property
    def primary_color(self) -> "str":
        return "#4285F4"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Google Container Optimized OS</title>
     <path d="M12 0C5.373 0 0 5.373 0 12s5.373 12 12 12 12-5.373
 12-12S18.627 0 12 0zm0 21.6a9.6 9.6 0 0 1-5.016-1.416L11.28
 17.7v-5.4L6.612 9.6v5.424l3.3 1.908-4.152 2.4A9.6 9.6 0 0 1 7.296
 3.6v4.8L12 11.136 16.68 8.4 12 5.724 8.688 7.632V2.964a9.6 9.6 0 0 1
 12.372 5.64A9.72 9.72 0 0 1 21.672 12v.084L17.352 9.6l-4.68
 2.712v5.412l4.68-2.7v-3.816l4.14 2.4A9.6 9.6 0 0 1 12 21.6z" />
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
