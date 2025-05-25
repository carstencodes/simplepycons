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


class AntennapodIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "antennapod"

    @property
    def original_file_name(self) -> "str":
        return "antennapod.svg"

    @property
    def title(self) -> "str":
        return "AntennaPod"

    @property
    def primary_color(self) -> "str":
        return "#364FF3"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>AntennaPod</title>
     <path d="M12 0A12 12 0 0 0 0 12a12 12 0 0 0 7.188
 10.98l3.339-9.459a2.118 2.118 0 1 1 2.946 0l3.339 9.46A12 12 0 0 0 24
 12 12 12 0 0 0 12 0m0 2.824a9.177 9.177 0 0 1 4.969
 16.892l-.486-1.376a7.765 7.765 0 1 0-8.967 0l-.485 1.376A9.177 9.177
 0 0 1 12 2.824m0 3.529a5.647 5.647 0 0 1 3.739
 9.879l-.521-1.478a4.235 4.235 0 1 0-6.436 0l-.522 1.478A5.647 5.647 0
 0 1 12 6.353m0 8.298-1.618 4.584a7.4 7.4 0 0 0 3.236 0zm-2.21
 6.258-.937 2.656A12 12 0 0 0 12 24a12 12 0 0 0
 3.146-.435l-.937-2.656a9.2 9.2 0 0 1-2.209.267 9.2 9.2 0 0
 1-2.21-.267" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/AntennaPod/Branding/blob/1'''

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
