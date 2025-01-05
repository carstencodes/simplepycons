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


class RunkitIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "runkit"

    @property
    def original_file_name(self) -> "str":
        return "runkit.svg"

    @property
    def title(self) -> "str":
        return "RunKit"

    @property
    def primary_color(self) -> "str":
        return "#491757"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>RunKit</title>
     <path d="M23.97 14.797a3 3 0 01-1.47 3.02l-9 5.2a3 3 0 01-3
 0l-9-5.2a3 3 0 01-1.47-3.02l1.32-7.2a3 3 0 01.98-1.82 2.96 2.96 0
 01.49-.35l7.55-4.37a3.01 3.01 0 013.28.02l7.53
 4.35c.1.05.19.1.28.17a3 3 0 011.19 2zm-9.54-10.77l-7.72
 1.59c-.43.08-.51.64-.14.86l5.6
 3.23c.23.13.5.07.63-.19l1.58-3.6.53-1.22c.16-.35-.11-.75-.5-.67z" />
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
