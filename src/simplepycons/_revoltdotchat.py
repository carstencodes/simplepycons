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


class RevoltdotchatIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "revoltdotchat"

    @property
    def original_file_name(self) -> "str":
        return "revoltdotchat.svg"

    @property
    def title(self) -> "str":
        return "Revolt.chat"

    @property
    def primary_color(self) -> "str":
        return "#FF4655"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Revolt.chat</title>
     <path d="M17.005 7.796c0 1.88-1.023 3.009-3.207
 3.009h-3.615v-5.95H13.8c2.183 0 3.206 1.162 3.206 2.94zM.853 0l3.5
 4.866v19.133h5.832v-9.06h1.398L16.563 24h6.583l-5.525-9.504a6.966
 6.966 0 0 0 3.879-2.532 7 7 0 0 0 1.44-4.408C22.94 3.384 20.009 0
 14.143 0h-9.79z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://app.revolt.chat/assets/badges/revolt_'''

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
        yield from [
            "revolt",
        ]
