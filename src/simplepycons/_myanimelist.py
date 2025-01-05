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


class MyanimelistIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "myanimelist"

    @property
    def original_file_name(self) -> "str":
        return "myanimelist.svg"

    @property
    def title(self) -> "str":
        return "MyAnimeList"

    @property
    def primary_color(self) -> "str":
        return "#2E51A2"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>MyAnimeList</title>
     <path d="M8.273 7.247v8.423l-2.103-.003v-5.216l-2.03
 2.404-1.989-2.458-.02 5.285H.001L0 7.247h2.203l1.865 2.545
 2.015-2.546 2.19.001zm8.628 2.069l.025
 6.335h-2.365l-.008-2.871h-2.8c.07.499.21 1.266.417
 1.779.155.381.298.751.583 1.128l-1.705
 1.125c-.349-.636-.622-1.337-.878-2.082a9.296 9.296 0 0
 1-.507-2.179c-.085-.75-.097-1.471.107-2.212a3.908 3.908 0 0 1
 1.161-1.866c.313-.293.749-.5 1.1-.687.351-.187.743-.264
 1.107-.359a7.405 7.405 0 0 1 1.191-.183c.398-.034 1.107-.066
 2.39-.028l.545 1.749H14.51c-.593.008-.878.001-1.341.209a2.236 2.236 0
 0 0-1.278
 1.92l2.663.033.038-1.81h2.309zm3.992-2.099v6.627l3.107.032-.43
 1.775h-4.807V7.187l2.13.03z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://myanimelist.net/forum/?topicid=157561'''

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
