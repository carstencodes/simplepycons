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


class LastpassIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "lastpass"

    @property
    def original_file_name(self) -> "str":
        return "lastpass.svg"

    @property
    def title(self) -> "str":
        return "LastPass"

    @property
    def primary_color(self) -> "str":
        return "#D32D27"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>LastPass</title>
     <path
 d="M22.629,6.857c0-0.379,0.304-0.686,0.686-0.686C23.693,6.171,24,6.483,24,6.857
 v10.286c0,0.379-0.304,0.686-0.686,0.686c-0.379,0-0.686-0.312-0.686-0.686V6.857z
 M2.057,10.286c1.136,0,2.057,0.921,2.057,2.057
 S3.193,14.4,2.057,14.4S0,13.479,0,12.343S0.921,10.286,2.057,10.286z
 M9.6,10.286c1.136,0,2.057,0.921,2.057,2.057
 S10.736,14.4,9.6,14.4s-2.057-0.921-2.057-2.057S8.464,10.286,9.6,10.286z
 M17.143,10.286c1.136,0,2.057,0.921,2.057,2.057
 S18.279,14.4,17.143,14.4s-2.057-0.921-2.057-2.057S16.007,10.286,17.143,10.286z"
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
