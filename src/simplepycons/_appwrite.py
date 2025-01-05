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


class AppwriteIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "appwrite"

    @property
    def original_file_name(self) -> "str":
        return "appwrite.svg"

    @property
    def title(self) -> "str":
        return "Appwrite"

    @property
    def primary_color(self) -> "str":
        return "#FD366E"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Appwrite</title>
     <path d="M24 17.291v5.29H10.557A10.58 10.58 0 0 1 0
 12.715v-1.43c.048-.735.174-1.463.374-2.171C1.63 4.673 5.713 1.419
 10.557 1.419c4.844 0 8.927 3.254 10.183 7.695h-5.749a5.283 5.283 0 0
 0-4.434-2.404 5.282 5.282 0 0 0-4.434 2.404A5.23 5.23 0 0 0 5.267
 12a5.27 5.27 0 0 0 1.66 3.848 5.27 5.27 0 0 0 3.63
 1.443H24Zm0-6.734v5.291h-9.813A5.276 5.276 0 0 0 15.848
 12c0-.5-.07-.984-.199-1.443H24Z" />
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
