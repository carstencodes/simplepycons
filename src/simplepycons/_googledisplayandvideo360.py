#
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2024 Carsten Igel.
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


class GoogleDisplayandVideoThreeHundredAndSixtyIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "googledisplayandvideo360"

    @property
    def original_file_name(self) -> "str":
        return "googledisplayandvideo360.svg"

    @property
    def title(self) -> "str":
        return "Google Display & Video 360"

    @property
    def primary_color(self) -> "str":
        return "#34A853"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Google Display &amp; Video 360</title>
     <path d="M4.421.01a2.947 2.947 0 0 0-2.828 1.52 2.967 2.967 0 0 0
 1.094 4.076l10.6 6.064 4.79-2.672a3.546 3.546 0 0 1
 1.811-.443L5.701.424A2.947 2.947 0 0 0 4.42.01ZM1.164
 4.768v14.484a3.474 3.474 0 0 1 2.972-1.687 3.47 3.47 0 0 1 2.961
 1.672l.004-10.53L2.44 6.04a3.433 3.433 0 0 1-1.275-1.271Zm18.42
 4.289a3.08 3.08 0 0 0-1.264.379L7.6 15.414c.003 1.873-.011 3.745.003
 5.617 0 .4-.072.988-.396 1.606l12.548-7.227 1.487-.83a2.978 2.978 0 0
 0 1.463-3.511 3.08 3.08 0 0 0-3.121-2.012ZM4.136 18.065A2.967 2.967 0
 1 0 4.134 24a2.967 2.967 0 0 0 .002-5.935z" />
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