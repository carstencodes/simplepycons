#
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2024 Carsten Igel.
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


class ScrutinizerCiIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "scrutinizerci"

    @property
    def original_file_name(self) -> "str":
        return "scrutinizerci.svg"

    @property
    def title(self) -> "str":
        return "Scrutinizer CI"

    @property
    def primary_color(self) -> "str":
        return "#8A9296"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Scrutinizer CI</title>
     <path d="M14.862 0L6.879.06a6.139 6.127 0 00-3.744 2.508 6.36
 6.36 0 00-1.357 2.64l-.12.553-.12.857c-.06.8-.06 1.351.12
 1.471h5.276c.06 0-.186-.246-.186-.672
 0-.738.252-.924.552-1.23.552-.426 2.945-.12 4.728-.246 2.448 0
 4.602-.06 4.848-.12 2.7-.427 5.03-2.388
 5.522-4.536.12-.547.12-1.105.06-1.165C22.398 0 21.418 0 14.86
 0zM9.194 9.007c-3.758-.015-7.47 0-7.53.06-.126.126-.06.798.06
 1.35a5.64 5.64 0 001.843 2.761 7.549 7.549 0 003.312 1.59c.366.126
 1.044.126 4.597.126 4.236 0 4.915.06 5.22.24a1.842 1.836 0
 01.372.372c.18.24.18.307.18.98 0 .671-.065.731-.185 1.043a1.47 1.47 0
 01-.426.366c-.186.12-.307.12-4.357.18-4.67 0-5.155 0-6.32.431a6.445
 6.433 0 00-2.46 1.35c-1.163 1.04-1.841 2.203-1.961
 3.428l.06.611a283.022 282.613 0 0015.404 0l.492-.12a4.543 4.537 0
 00.737-.245l.367-.18a7.735 7.723 0 003.499-4.297 8.407 8.395 0
 00-.373-6.06 8.527 8.521 0 00-2.328-2.88 6.937 6.925 0
 00-2.394-.985c-.246-.06-4.051-.106-7.81-.12z" />
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