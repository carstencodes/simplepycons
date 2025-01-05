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


class SlickpicIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "slickpic"

    @property
    def original_file_name(self) -> "str":
        return "slickpic.svg"

    @property
    def title(self) -> "str":
        return "SlickPic"

    @property
    def primary_color(self) -> "str":
        return "#FF880F"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>SlickPic</title>
     <path d="M21.483 18.308L6.056 14.085l2.52-9.201L24 9.104l-2.517
 9.204zm-13.414-5.37l12.263 3.354 1.654-6.033L9.72 6.9l-1.65
 6.034v.004zM8.526 15.795l-4.891 1.311-1.625-6.045
 4.146-1.11.501-1.835L0 9.902l2.478 9.215 9.178-2.467" />
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
