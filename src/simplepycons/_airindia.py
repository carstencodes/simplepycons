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


class AirIndiaIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "airindia"

    @property
    def original_file_name(self) -> "str":
        return "airindia.svg"

    @property
    def title(self) -> "str":
        return "Air India"

    @property
    def primary_color(self) -> "str":
        return "#DA0E29"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Air India</title>
     <path d="M8.483.001C6.247.043 4.102 1.018 2.092
 2.898c.141-.065-.545.44-1.637 1.676.013.006-.009.017-.013.025 0 0
 .014.037.14-.064.75-.61 3.198-2.893 9.86.101a276.52 276.52 0 0 0 6.42
 2.78s1.027 3.236 2.207 6.637c2.398 6.89-.087 9.135-.76
 9.82-.102.114-.064.127-.064.127a16.746 16.746 0 0 0
 2.385-2.08c1.624-1.637 2.588-3.428
 2.855-5.344.254-1.878-.203-3.5-.584-4.566-.266-.75-.481-1.346-.672-1.88-.862-2.423-1.028-2.867-1.625-5.29l-.203-.8c-.023-.003.009-.016.014-.025l-.787-.254c-2.386-.774-2.804-.964-5.165-2.017-.52-.229-1.103-.496-1.826-.813-.85-.368-2.146-.875-3.707-.926a8.027
 8.027 0 0 0-.447-.004Z" />
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
