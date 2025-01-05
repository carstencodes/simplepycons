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


class ZennIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "zenn"

    @property
    def original_file_name(self) -> "str":
        return "zenn.svg"

    @property
    def title(self) -> "str":
        return "Zenn"

    @property
    def primary_color(self) -> "str":
        return "#3EA8FF"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Zenn</title>
     <path d="M.264 23.771h4.984c.264 0
 .498-.147.645-.352L19.614.874c.176-.293-.029-.645-.381-.645h-4.72c-.235
 0-.44.117-.557.323L.03 23.361c-.088.176.029.41.234.41zM17.445
 23.419l6.479-10.408c.205-.323-.029-.733-.41-.733h-4.691c-.176
 0-.352.088-.44.235l-6.655
 10.643c-.176.264.029.616.352.616h4.779c.234-.001.468-.118.586-.353z"
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
