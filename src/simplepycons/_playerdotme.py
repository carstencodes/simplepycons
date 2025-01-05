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


class PlayerdotmeIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "playerdotme"

    @property
    def original_file_name(self) -> "str":
        return "playerdotme.svg"

    @property
    def title(self) -> "str":
        return "Player.me"

    @property
    def primary_color(self) -> "str":
        return "#C0379A"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Player.me</title>
     <path d="M11.981 0a8.957 8.957 0 0 0-8.956 8.957v.363C3.283
 15.828 10.082 24 10.082
 24V13.205c-1.638-.747-2.756-2.369-2.756-4.253a4.66 4.66 0 1 1 6.152
 4.416l-.033.01v4.427c4.296-.713 7.531-4.401 7.531-8.845A8.959 8.959 0
 0 0 12.017.001h-.038.002z" />
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
