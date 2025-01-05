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


class MixpanelIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "mixpanel"

    @property
    def original_file_name(self) -> "str":
        return "mixpanel.svg"

    @property
    def title(self) -> "str":
        return "Mixpanel"

    @property
    def primary_color(self) -> "str":
        return "#7856FF"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Mixpanel</title>
     <path d="M6.967
 9.996h3.053c-.763-.477-1.048-1.145-1.431-2.384L7.443 3.366C6.919
 1.458 6.49.551 4.39.551H.004v1.145h.621c1.286 0 1.431.477 1.814
 1.908L3.44 7.326c.524 1.814 1.337 2.67 3.53 2.67h-.003Zm7.06
 0h3.053c2.194 0 2.956-.86 3.484-2.67l1.001-3.722c.382-1.431.57-1.908
 1.814-1.908H24V.551h-4.34c-2.146 0-2.576.86-3.053 2.815l-1.145
 4.246c-.384 1.286-.673 1.907-1.435 2.384Zm-4.007
 4.008h4.007V9.996H10.02v4.008ZM0 23.449h4.39c2.1 0 2.529-.907
 3.053-2.815l1.146-4.246c.383-1.239.668-1.907 1.431-2.384H6.967c-2.194
 0-3.007.86-3.531 2.67l-1.001 3.722c-.383 1.431-.524 1.907-1.814
 1.907H0v1.146Zm19.65 0h4.343v-1.146h-.622c-1.239
 0-1.431-.476-1.814-1.907l-1.001-3.722c-.524-1.814-1.286-2.67-3.483-2.67h-3.046c.762.477
 1.041 1.098 1.424 2.384l1.145 4.246c.477 1.955.907 2.815 3.054
 2.815Z" />
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
