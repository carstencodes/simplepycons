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


class HugoIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "hugo"

    @property
    def original_file_name(self) -> "str":
        return "hugo.svg"

    @property
    def title(self) -> "str":
        return "Hugo"

    @property
    def primary_color(self) -> "str":
        return "#FF4088"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Hugo</title>
     <path d="M11.754 0a3.998 3.998 0 00-2.049.596L3.33 4.532a4.252
 4.252 0 00-2.017 3.615v8.03c0 1.473.79 2.838 2.067 3.574l6.486
 3.733a3.88 3.88 0 003.835.018l7.043-3.966a3.817 3.817 0
 001.943-3.323V7.752a3.57 3.57 0 00-1.774-3.084L13.817.541a3.998 3.998
 0 00-2.063-.54zm.022 1.674c.413-.006.828.1 1.2.315l7.095
 4.127c.584.34.941.96.94 1.635v8.462c0 .774-.414 1.484-1.089
 1.864l-7.042 3.966a2.199 2.199 0 01-2.179-.01l-6.485-3.734a2.447
 2.447 0 01-1.228-2.123v-8.03c0-.893.461-1.72
 1.221-2.19l6.376-3.935a2.323 2.323 0 011.19-.347zm-4.7
 3.844V18.37h2.69v-5.62h4.46v5.62h2.696V5.518h-2.696v4.681h-4.46V5.518Z"
 />
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
