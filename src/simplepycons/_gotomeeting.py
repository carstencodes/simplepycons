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


class GotomeetingIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "gotomeeting"

    @property
    def original_file_name(self) -> "str":
        return "gotomeeting.svg"

    @property
    def title(self) -> "str":
        return "GoToMeeting"

    @property
    def primary_color(self) -> "str":
        return "#F68D2E"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>GoToMeeting</title>
     <path d="M21.3 13.72a3.158 3.158 0 0 0-3.462.124.632.632 0 0
 1-.682.035l-3.137-1.81a.08.08 0 0 1 0-.137l3.12-1.8a.632.632 0 0 1
 .685.036 3.158 3.158 0 0 0 3.47.139A3.194 3.194 0 0 0 22.442
 6.1a3.158 3.158 0 0 0-5.924 1.773.633.633 0 0 1-.311.606l-3.136
 1.811a.08.08 0 0 1-.118-.068V6.6a.632.632 0 0 1 .372-.573 3.158 3.158
 0 1 0-2.64 0 .632.632 0 0 1 .373.573v3.622a.08.08 0 0
 1-.119.068L7.804 8.48a.632.632 0 0 1-.311-.605 3.157 3.157 0 1
 0-1.307 2.294.633.633 0 0 1 .687-.038l3.12 1.8a.08.08 0 0 1 0
 .137L6.854 13.88a.632.632 0 0 1-.683-.035 3.158 3.158 0 0
 0-3.461-.124 3.194 3.194 0 0 0-1.143 4.202 3.159 3.159 0 0 0
 5.924-1.792.633.633 0 0 1 .31-.61l3.137-1.81a.08.08 0 0 1
 .119.068V17.4a.632.632 0 0 1-.372.573 3.158 3.158 0 1 0 2.64 0
 .633.633 0 0 1-.373-.573v-3.621a.08.08 0 0 1 .118-.069l3.137
 1.812a.631.631 0 0 1 .31.609 3.159 3.159 0 0 0 5.924 1.792A3.194
 3.194 0 0 0 21.3 13.72Z" />
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
