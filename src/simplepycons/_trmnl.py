#
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2026 Carsten Igel.
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


class TrmnlIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "trmnl"

    @property
    def original_file_name(self) -> "str":
        return "trmnl.svg"

    @property
    def title(self) -> "str":
        return "TRMNL"

    @property
    def primary_color(self) -> "str":
        return "#F8654B"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>TRMNL</title>
     <path d="m6.024.913 6.661 2.498-1.237
 3.299-6.661-2.498ZM16.705.097l2.2 6.766-3.35 1.09-2.2-6.766zM24
 7.942l-3.917 5.939-2.941-1.94L21.06 6Zm-1.583
 10.593-7.086.64-.317-3.509 7.086-.64zm-9.271 5.367L8.228
 18.76l2.546-2.436 4.918 5.141zm-9.976-3.9.953-7.05 3.491.472-.953
 7.05zM0 9.768l6.107-3.65L7.915 9.14l-6.107 3.65Z" />
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
