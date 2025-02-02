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


class CocoapodsIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "cocoapods"

    @property
    def original_file_name(self) -> "str":
        return "cocoapods.svg"

    @property
    def title(self) -> "str":
        return "CocoaPods"

    @property
    def primary_color(self) -> "str":
        return "#EE3322"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>CocoaPods</title>
     <path d="M8.812 17.176c-2.968 0-4.956-2.308-4.956-5.176 0-2.705
 1.776-5.176 4.91-5.176 2.407 0 3.856 1.445 4.207 3.357h3.95C16.479
 6.427 13.51 3.42 8.718 3.42 3.131 3.42 0 7.523 0 12c0 4.57 3.295 8.58
 8.766 8.58 4.58 0 7.549-2.822 8.18-6.272h-4.02c-.467 1.609-1.916
 2.868-4.114 2.868zM24 12.068l-3.466 8.055-2.38-1.022
 2.992-7.055-3.01-7.096 2.433-1.042Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/CocoaPods/shared_resources'''

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
