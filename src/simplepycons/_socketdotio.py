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


class SocketdotioIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "socketdotio"

    @property
    def original_file_name(self) -> "str":
        return "socketdotio.svg"

    @property
    def title(self) -> "str":
        return "Socket.io"

    @property
    def primary_color(self) -> "str":
        return "#010101"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Socket.io</title>
     <path d="M11.9362.0137a12.1694 12.1694 0 00-2.9748.378C4.2816
 1.5547.5678 5.7944.0918 10.6012c-.59 4.5488 1.7079 9.2856 5.6437
 11.6345 3.8608 2.4179 9.0926 2.3199 12.8734-.223 3.3969-2.206
 5.5118-6.2277
 5.3858-10.2845-.058-4.0159-2.31-7.9167-5.7588-9.9796C16.354.5876
 14.1431.0047 11.9362.0137zm-.063 1.696c4.9448-.007 9.7886 3.8137
 10.2815 8.9245.945 5.6597-3.7528 11.4125-9.4875
 11.5795-5.4538.544-10.7245-4.0798-10.8795-9.5566-.407-4.4338
 2.5159-8.8346 6.6977-10.2995a9.1126 9.1126 0 013.3878-.647zm5.0908
 3.2248c-2.6869 2.0849-5.2598 4.3078-7.8886 6.4567 1.2029.017
 2.4118.016 3.6208.01 1.41-2.165 2.8589-4.3008 4.2678-6.4667zm-5.6647
 7.6536c-1.41 2.166-2.86 4.3088-4.2699 6.4737 2.693-2.0799
 5.2548-4.3198 7.9017-6.4557a255.4132 255.4132 0 00-3.6318-.018z" />
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
