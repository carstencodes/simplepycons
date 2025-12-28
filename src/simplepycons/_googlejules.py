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


class GoogleJulesIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "googlejules"

    @property
    def original_file_name(self) -> "str":
        return "googlejules.svg"

    @property
    def title(self) -> "str":
        return "Google Jules"

    @property
    def primary_color(self) -> "str":
        return "#715CD7"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Google Jules</title>
     <path d="M4.2 24q-1.26 0-2.13-.87T1.2 21v-.6q0-.51.345-.855T2.4
 19.2t.855.345.345.855v.6q0 .24.18.42t.42.18.42-.18.18-.42V7.2q0-3
 2.1-5.1T12 0t5.1 2.1 2.1 5.1V21q0
 .24.18.42t.42.18.42-.18.18-.42v-.6q0-.51.345-.855t.855-.345.855.345.345.855v.6q0
 1.26-.87 2.13T19.8 24t-2.13-.87T16.8 21v-5.4h-1.62v4.8q0
 .51-.345.855t-.855.345-.855-.345-.345-.855v-4.8h-1.59v4.8q0
 .51-.345.855t-.855.345-.855-.345-.345-.855v-4.8H7.2V21q0 1.26-.87
 2.13T4.2 24m4.2-11.4q.54 0
 .87-.45t.33-1.05-.33-1.05-.87-.45-.87.45-.33 1.05.33 1.05.87.45m7.2
 0q.54 0 .87-.45t.33-1.05-.33-1.05-.87-.45-.87.45-.33 1.05.33
 1.05.87.45" />
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
