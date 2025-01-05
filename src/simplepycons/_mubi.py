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


class MubiIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "mubi"

    @property
    def original_file_name(self) -> "str":
        return "mubi.svg"

    @property
    def title(self) -> "str":
        return "MUBI"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>MUBI</title>
     <path d="M3.357.033A3.357 3.357 0 0 0 0 3.39a3.357 3.357 0 0 0
 3.357 3.357A3.357 3.357 0 0 0 6.713 3.39 3.357 3.357 0 0 0
 3.357.033Zm8.643 0A3.357 3.357 0 0 0 8.645 3.39 3.357 3.357 0 0 0 12
 6.746a3.357 3.357 0 0 0 3.357-3.357A3.357 3.357 0 0 0 12 .033Zm-8.643
 8.61A3.357 3.357 0 0 0 0 12a3.357 3.357 0 0 0 3.357 3.355A3.357 3.357
 0 0 0 6.713 12a3.357 3.357 0 0 0-3.356-3.357Zm8.643 0A3.357 3.357 0 0
 0 8.645 12 3.357 3.357 0 0 0 12 15.355 3.357 3.357 0 0 0 15.357 12
 3.357 3.357 0 0 0 12 8.643zm8.643 0A3.357 3.357 0 0 0 17.287 12a3.357
 3.357 0 0 0 3.356 3.355A3.357 3.357 0 0 0 24 12a3.357 3.357 0 0
 0-3.357-3.357Zm-17.286 8.61A3.357 3.357 0 0 0 0 20.612a3.357 3.357 0
 0 0 3.357 3.356 3.357 3.357 0 0 0 3.356-3.356 3.357 3.357 0 0
 0-3.356-3.357Zm8.643 0a3.357 3.357 0 0 0-3.355 3.358A3.357 3.357 0 0
 0 12 23.967a3.357 3.357 0 0 0 3.357-3.356A3.357 3.357 0 0 0 12
 17.254z" />
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
