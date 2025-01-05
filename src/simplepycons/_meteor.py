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


class MeteorIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "meteor"

    @property
    def original_file_name(self) -> "str":
        return "meteor.svg"

    @property
    def title(self) -> "str":
        return "Meteor"

    @property
    def primary_color(self) -> "str":
        return "#DE4F4F"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Meteor</title>
     <path d="M0 .234l21.912 20.537s.412.575-.124
 1.151c-.535.576-1.236.083-1.236.083L0 .234zm6.508 2.058l17.01
 15.638s.413.576-.123 1.152c-.534.576-1.235.083-1.235.083L6.508
 2.292zM1.936 6.696l17.01 15.638s.412.576-.123
 1.152-1.235.082-1.235.082L1.936 6.696zm10.073-2.635l11.886
 10.927s.287.401-.087.805-.863.058-.863.058L12.009 4.061zm-8.567
 7.737l11.886 10.926s.285.4-.088.803c-.375.403-.863.059-.863.059L3.442
 11.798zm14.187-5.185l5.426
 4.955s.142.188-.044.377c-.185.188-.428.027-.428.027l-4.954-5.358v-.001zM6.178
 17.231l5.425 4.956s.144.188-.042.377-.427.026-.427.026l-4.956-5.359z"
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
