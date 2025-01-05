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


class WondershareIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "wondershare"

    @property
    def original_file_name(self) -> "str":
        return "wondershare.svg"

    @property
    def title(self) -> "str":
        return "Wondershare"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Wondershare</title>
     <path d="M16.216 17.814 7.704 9.368l.02-.02c.391.239.91.19
 1.249-.147l3.041-3.016 7.241 7.184c.397.394.402 1.029.005
 1.426l-3.044 3.019Zm-5.253-3.017-3.03 3.017L0 9.915l3.746-3.73 7.217
 7.187a1.005 1.005 0 0 1 0 1.425ZM24 9.913l-3.725 3.727L16
 9.367l.02-.021c.388.239.903.19 1.239-.146l3.014-3.015L24 9.913Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://www.wondershare.com/news/media-assets'''

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
