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


class UnacademyIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "unacademy"

    @property
    def original_file_name(self) -> "str":
        return "unacademy.svg"

    @property
    def title(self) -> "str":
        return "Unacademy"

    @property
    def primary_color(self) -> "str":
        return "#08BD80"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Unacademy</title>
     <path d="M.715 2.188a.696.696 0
 00-.711.713H0l.002.027c-.01.306.03.658.123 1.081.905 5.546 5.875
 9.788 11.87 9.788 5.935 0 10.864-4.157
 11.84-9.622.126-.512.177-.921.162-1.273a.696.696 0
 00-.713-.714zm11.243 13.82c-2.967 0-5.432 2.079-5.92 4.81a2.287 2.287
 0 00-.08.638c0 .201.15.356.355.356h11.285a.348.348 0
 00.356-.356h.002v-.014a2.21 2.21 0
 00-.063-.54c-.453-2.774-2.938-4.894-5.935-4.894z" />
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
