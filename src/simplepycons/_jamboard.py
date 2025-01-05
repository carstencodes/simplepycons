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


class JamboardIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "jamboard"

    @property
    def original_file_name(self) -> "str":
        return "jamboard.svg"

    @property
    def title(self) -> "str":
        return "Jamboard"

    @property
    def primary_color(self) -> "str":
        return "#F37C20"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Jamboard</title>
     <path d="M12.143 0v7.877h7.783V0zm0
 8.155v7.784h7.783V8.155zm-.28.005a7.926 7.923 0 0 0-7.789 7.917A7.926
 7.923 0 0 0 12 24a7.926 7.923 0 0 0 7.918-7.78h-8.056Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://cdn2.hubspot.net/hubfs/159104/ECS/Jam'''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://cdn2.hubspot.net/hubfs/159104/ECS/Jam'''

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
