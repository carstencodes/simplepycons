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


class GoogleAdmobIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "googleadmob"

    @property
    def original_file_name(self) -> "str":
        return "googleadmob.svg"

    @property
    def title(self) -> "str":
        return "Google AdMob"

    @property
    def primary_color(self) -> "str":
        return "#EA4335"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Google AdMob</title>
     <path d="M11.46.033h-.052A11.993 11.993 0 0 0 0 11.922v.052c0
 7.475 6.563 11.928 11.447 11.928h.17a3.086 3.086 0 0 0
 3.125-3.047c0-1.693-1.433-2.917-3.152-2.917h-.039a6.016 6.016 0 0
 1-5.508-6.368v-.052a6.016 6.016 0 0 1 5.573-5.509c1.719 0 3.125-1.237
 3.125-2.917A3.086 3.086 0 0 0 11.604.02h-.143zm2.031.026a3.516 3.516
 0 0 1 1.746 3.021 3.386 3.386 0 0 1-1.928 3.047c2.865.6 4.532 3.126
 4.688 5.378v7.684a3.49 3.49 0 0 1 6.003.026v-7.736A12.046 12.046 0 0
 0 13.491.045zm7.475 17.932a2.995 2.995 0 1 0 .04 0z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://commons.wikimedia.org/wiki/File:Googl'''

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
