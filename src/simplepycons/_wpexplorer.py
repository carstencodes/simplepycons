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


class WpexplorerIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "wpexplorer"

    @property
    def original_file_name(self) -> "str":
        return "wpexplorer.svg"

    @property
    def title(self) -> "str":
        return "WPExplorer"

    @property
    def primary_color(self) -> "str":
        return "#2563EB"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>WPExplorer</title>
     <path d="M24 12A12 12 0 1 1 12 0a12.008 12.008 0 0 1 12 12Zm-1.5
 0A10.5 10.5 0 1 0 12 22.5 10.516 10.516 0 0 0 22.5 12ZM7.542
 5.841l4.074 1.739-1.739 4.073L5.8 9.914l1.742-4.073Zm5.158 7.926
 2.185 4.406H14.2l-2.343-4.687-2.295
 4.687h-.656l2.4-5.01-1.046-.441.282-.656 3.215
 1.364-.281.67Zm-.553-5.451 3.216 1.378-1.378 3.2-3.2-1.364
 1.364-3.215Zm3.764 2.011 2.56 1.082-1.1 2.546-2.545-1.083
 1.082-2.545Z" />
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
