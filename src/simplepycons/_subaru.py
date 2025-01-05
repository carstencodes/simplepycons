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


class SubaruIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "subaru"

    @property
    def original_file_name(self) -> "str":
        return "subaru.svg"

    @property
    def title(self) -> "str":
        return "Subaru"

    @property
    def primary_color(self) -> "str":
        return "#013C74"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Subaru</title>
     <path d="M12 4.983c3.004 0 6.224.612 8.786 2.239C22.451 8.286 24
 9.9 24 12.002c0 2.456-2.097 4.242-4.106 5.287-2.391 1.238-5.216
 1.728-7.894 1.728-3.003 0-6.217-.605-8.78-2.238C1.556 15.714 0 14.101
 0 12.003 0 9.536 2.092 7.757 4.106 6.71 6.504 5.474 9.323 4.983 12
 4.983zm-.025.746c-2.793 0-5.802.523-8.225 1.983-1.524.912-3.03
 2.347-3.03 4.253 0 2.239 2.04 3.806 3.864 4.706 2.258 1.102 4.897
 1.53 7.391 1.53 2.798 0 5.809-.523 8.232-1.983 1.517-.918 3.029-2.346
 3.029-4.253
 0-2.243-2.035-3.813-3.864-4.705-2.258-1.104-4.898-1.53-7.397-1.53zm-10.54
 4.686l4.597-.784 1.384-3.003L8.794 9.63l4.596.784-4.596.792-1.378
 3.01-1.384-3.01zm10.106 2.289l2.028-.356.605-1.359.606 1.359
 2.028.356-2.028.35-.606
 1.36-.605-1.36zm4.196-3.621l2.028-.35.605-1.365.606 1.364
 2.028.35-2.028.357-.606 1.36-.606-1.36zM13.57
 15.51l2.02-.35.607-1.365.612 1.365 2.027.35-2.027.357-.612
 1.36-.606-1.36zm-6.23.491l2.028-.35.612-1.366.605 1.366
 2.028.35-2.028.357-.605
 1.359-.612-1.359zm10.196-3.353l2.022-.357.605-1.359.612 1.359
 2.028.357-2.028.35-.612 1.357-.606-1.357Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://commons.wikimedia.org/wiki/File:Subar'''

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
