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


class RootsBedrockIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "rootsbedrock"

    @property
    def original_file_name(self) -> "str":
        return "rootsbedrock.svg"

    @property
    def title(self) -> "str":
        return "Roots Bedrock"

    @property
    def primary_color(self) -> "str":
        return "#525DDC"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Roots Bedrock</title>
     <path d="M.4 0L0 .4v5.2l.343.343 11.314-1.886L12
 4.4V8l11.52-1.92.48-.48V.4l-.4-.4zm.08 9.92L0 10.4v3.2l.343.343L12
 12V8zM12 12v4l11.52-1.92.48-.48v-3.2l-.343-.343zM.48 17.92L0
 18.4v5.2l.4.4h23.2l.4-.4v-5.2l-.343-.343-11.314 1.886L12 19.6V16L.48
 17.92z" />
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
