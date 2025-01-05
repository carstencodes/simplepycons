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


class TeamcityIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "teamcity"

    @property
    def original_file_name(self) -> "str":
        return "teamcity.svg"

    @property
    def title(self) -> "str":
        return "TeamCity"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>TeamCity</title>
     <path d="m0 0v24h24v-24zm2.664
 2.964h7.48v1.832h-2.748v7.196h-1.984v-7.196h-2.748zm9.328
 18h-9v-1.5h9zm5.56391-9.21826a4.62 4.62 0 0 1 -2.03591.37426 4.556
 4.556 0 0 1 -4.628-4.616v-.024a4.584 4.584 0 0 1 4.708-4.668 4.65561
 4.65561 0 0 1 3.56 1.388l-1.264 1.456a3.33594 3.33594 0 0 0
 -2.312-1.02 2.67116 2.67116 0 0 0 -2.616 2.8v.028a2.68058 2.68058 0 0
 0 2.616 2.836 3.22606 3.22606 0 0 0 2.376-1.056l1.264 1.276a4.61947
 4.61947 0 0 1 -1.66809 1.22573z" />
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
