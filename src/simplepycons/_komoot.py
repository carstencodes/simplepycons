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


class KomootIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "komoot"

    @property
    def original_file_name(self) -> "str":
        return "komoot.svg"

    @property
    def title(self) -> "str":
        return "Komoot"

    @property
    def primary_color(self) -> "str":
        return "#6AA127"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Komoot</title>
     <path d="M9.8 14.829l2.2-3.43 2.2 3.43 5.962 5.962A11.946 11.946
 0 0 1 12 24c-3.043 0-5.935-1.14-8.162-3.209zM0 12C0 5.385 5.385 0 12
 0c6.62 0 12 5.385 12 12 0 2.663-.855 5.175-2.469
 7.284l-6.018-6.018c.15-.412.226-.839.226-1.27A3.743 3.743 0 0 0 12
 8.257a3.743 3.743 0 0 0-3.739 3.739c0 .431.075.858.226 1.27l-6.018
 6.018A11.865 11.865 0 0 1 0 12Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://newsroom.komoot.com/media_kits/219423'''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://newsroom.komoot.com/media_kits/219423'''

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
